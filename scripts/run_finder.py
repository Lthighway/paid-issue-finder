import json
import os
import subprocess
import re
from pathlib import Path
from urllib.parse import urlparse

from scripts.analyze_issues import analyze_issue


def gh_json(args):
    return json.loads(subprocess.check_output(["gh", "api", *args], text=True))


def detect_competition(comments, linked_open=0, comments_verified=True):
    """Flag evidence that someone may already be working on or solved the bounty."""
    reasons = []
    if linked_open:
        reasons.append("%d linked open pull request(s)" % linked_open)

    solution_markers = (
        "## solution", "## proposed solution", "please remit", "payout address",
        "bounty payout", "here is the fix", "here's the fix", "implementation:",
    )
    matching_comments = 0
    for comment in comments or []:
        body = (comment.get("body") or "").lower()
        if any(marker in body for marker in solution_markers):
            matching_comments += 1
    if matching_comments:
        reasons.append("%d comment(s) contain a solution/payout signal" % matching_comments)

    if linked_open or matching_comments:
        return {"status": "HIGH", "reasons": reasons, "verified": comments_verified}
    if comments_verified and len(comments or []) >= 3:
        return {"status": "MEDIUM", "reasons": ["active discussion; inspect comments before starting"], "verified": True}
    if comments_verified:
        return {"status": "LOW", "reasons": [], "verified": True}
    return {"status": "UNKNOWN", "reasons": ["could not verify issue comments"], "verified": False}


def repo_history(repo, issue_number):
    prs = timeline = comments = None
    try:
        prs = gh_json(["repos/%s/pulls?state=closed&per_page=30" % repo])
    except Exception:
        pass
    try:
        timeline = gh_json(["repos/%s/issues/%s/timeline" % (repo, issue_number)])
    except Exception:
        pass
    try:
        comments = gh_json(["repos/%s/issues/%s/comments?per_page=100" % (repo, issue_number)])
    except Exception:
        pass

    merged = sum(1 for pr in (prs or []) if pr.get("merged_at"))
    linked_merged = linked_closed = linked_open = 0
    for event in timeline or []:
        source = event.get("source", {}).get("issue", {})
        pr_ref = source.get("pull_request")
        if event.get("event") != "cross-referenced" or not pr_ref:
            continue
        if source.get("state") == "closed":
            linked_closed += 1
        elif source.get("state") == "open":
            linked_open += 1
        url = pr_ref.get("html_url")
        if url:
            try:
                number = url.rstrip("/").split("/")[-1]
                if gh_json(["repos/%s/pulls/%s" % (repo, number)]).get("merged_at"):
                    linked_merged += 1
            except Exception:
                pass

    competition = detect_competition(comments or [], linked_open=linked_open, comments_verified=(comments is not None and timeline is not None))
    return {
        "prs": bool(prs), "merged": merged, "linked_merged": linked_merged,
        "linked_closed": linked_closed, "linked_open": linked_open,
        "competition": competition["status"],
        "competition_reasons": competition["reasons"],
        "competition_verified": competition["verified"],
    }


SOURCE_URL_RE = re.compile(r"https?://github\.com/([^/\s)]+)/([^/\s)]+)/issues/(\d+)", re.I)


def issue_repo(issue):
    repo = (issue.get("repository") or {}).get("nameWithOwner", "")
    if repo:
        return repo.lower()
    url = issue.get("html_url") or issue.get("url") or ""
    match = re.match(r"https?://github\.com/([^/]+)/([^/]+)/", url, re.I)
    return (match.group(1) + "/" + match.group(2)).lower() if match else ""


def extract_source_url(issue):
    body = issue.get("body") or ""
    matches = list(SOURCE_URL_RE.finditer(body))
    if not matches:
        return None
    current_repo = issue_repo(issue)
    # Mirrors often quote a chain of older mirrors before the real source.
    # Prefer a source URL outside the current repository to avoid scoring a mirror.
    for match in matches:
        if (match.group(1) + "/" + match.group(2)).lower() != current_repo:
            return match.group(0).rstrip(".,")
    return matches[0].group(0).rstrip(".,")


def source_ref(issue):
    url = extract_source_url(issue)
    if not url:
        return None
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if len(parts) >= 4 and parts[2] == "issues" and parts[3].isdigit():
        return "%s/%s" % (parts[0] + "/" + parts[1], parts[3])
    return None


def source_key(issue):
    url = extract_source_url(issue)
    if url:
        parsed = urlparse(url)
        return parsed.path.rstrip("/").lower()
    repo = issue.get("repository", {}).get("nameWithOwner", "").lower()
    return "%s#%s" % (repo, issue.get("number"))


def is_unverified_candidate(issue):
    labels = {str(label.get("name", "")).lower() for label in issue.get("labels", []) if isinstance(label, dict)}
    text = ((issue.get("title") or "") + " " + (issue.get("body") or "")).lower()
    return (
        "verification-unavailable" in labels
        or "archived duplicate" in text
        or ("verifier: deterministic_module" in text and "ready: `false`" in text)
        or "lifecycle: `unavailable`" in text
        or "current work state: `unavailable`" in text
    )


def canonicalize_issue(issue):
    """Use the original open, actionable issue as the source of truth.

    Skip known archived/unverifiable offers and mirrors whose source is closed
    or cannot be fetched.
    """
    if is_unverified_candidate(issue):
        return None
    source = source_ref(issue)
    if not source:
        return issue

    repo, number = source.rsplit("/", 1)
    try:
        original = gh_json(["repos/%s/issues/%s" % (repo, number)])
    except Exception:
        return None

    if original.get("state") != "open" or original.get("pull_request") or is_unverified_candidate(original):
        return None

    original["repository"] = {"nameWithOwner": repo}
    original["url"] = original.get("html_url") or "https://github.com/%s/issues/%s" % (repo, number)
    original["comments"] = original.get("comments", 0)
    original["updatedAt"] = original.get("updated_at")
    original["author"] = original.get("user") or original.get("author")
    original["_source_url"] = original["url"]
    original["_discovered_url"] = issue.get("url") or issue.get("html_url")
    return original


def main():
    data = json.loads(Path("issues.json").read_text())
    deduped = []
    seen_sources = set()
    for candidate in data:
        key = source_key(candidate)
        if key in seen_sources:
            continue
        seen_sources.add(key)
        issue = canonicalize_issue(candidate)
        if issue is None:
            continue
        if "comments" not in issue:
            issue["comments"] = issue.get("commentsCount", 0)
        issue.setdefault("_discovered_url", issue.get("url") or issue.get("html_url"))
        deduped.append(issue)

    min_bounty = float(os.environ.get("MIN_BOUNTY", "0"))
    max_bounty = float(os.environ.get("MAX_BOUNTY", "100000"))
    min_opportunity = float(os.environ.get("MIN_OPPORTUNITY", "0"))
    rows = []
    for issue in deduped:
        repo = issue["repository"]["nameWithOwner"]
        issue_number = issue["number"]
        try:
            repo_meta = gh_json(["repos/%s" % repo])
        except Exception:
            continue
        result = analyze_issue(issue, repo_meta, repo_history(repo, issue_number))
        if not result or not min_bounty <= result["value"] <= max_bounty:
            continue
        if result["opportunity"] < min_opportunity:
            continue
        issue["_repo_stars"] = repo_meta.get("stargazers_count", 0)
        issue["_repo_forks"] = repo_meta.get("forks_count", 0)
        rows.append((result["opportunity"], result["value"], result, issue))

    rows.sort(key=lambda x: x[0], reverse=True)
    rows = rows[:50]
    report = [
        "# Paid Issue Finder Report", "",
        "Query: %s" % os.environ.get("QUERY", ""), "",
        "Filters: bounty US$%g–US$%g, opportunity >= %g" % (min_bounty, max_bounty, min_opportunity), "",
        "**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.", "",
    ]
    if not rows:
        report.append("No verifiable open issue with a monetary bounty was detected.")
    else:
        report += [
            "## Ranked opportunities", "",
            "| Rank | Bounty | Opportunity | Risk | Quality | History | Competition | Maintainer | Verdict |",
            "|---:|---:|---:|---:|---:|---:|:---:|---:|:---|",
        ]
        for rank, (score, value, result, issue) in enumerate(rows, 1):
            repo = issue["repository"]["nameWithOwner"]
            report.append(
                "| %d | US$%.2f | %.1f | %d | %d | %d | %s | %d | **%s** |" %
                (rank, value, score, result["risk"], result["quality"], result["history"], result["competition"], result["maintainer"], result["verdict"])
            )
            evidence = [
                "Reward: monetary value detected in original issue",
                "Repository: %d stars, %d forks" % (issue["_repo_stars"], issue["_repo_forks"]),
                "Quality: " + (", ".join(result["quality_reasons"]) or "no explicit quality signal"),
                "Risk: " + (", ".join(result["risk_reasons"]) or "no major risk signal"),
                "Competition: " + result["competition"] + (
                    " (" + "; ".join(result["competition_reasons"]) + ")"
                    if result["competition_reasons"] else ""
                ),
            ]
            url = issue.get("url") or issue.get("html_url") or ""
            report.append(
                "- **US$%.2f** · Opportunity %.1f · Risk %d · **%s** · %s — [%s#%s: %s](%s)" %
                (value, score, result["risk"], result["verdict"], result["confidence"], repo, issue["number"], issue["title"], url)
            )
            discovered = issue.get("_discovered_url")
            if discovered and discovered != url:
                report.append("  - Discovery mirror: %s" % discovered)
            report.append("  - " + " | ".join(evidence))

    Path("REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
