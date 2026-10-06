import json
import os
import subprocess
from pathlib import Path
from scripts.analyze_issues import analyze_issue

def gh_json(args):
    return json.loads(subprocess.check_output(["gh", "api", *args], text=True))

def repo_history(repo, issue_number):
    try:
        prs = gh_json(["repos/%s/pulls?state=closed&per_page=30" % repo])
        timeline = gh_json(["repos/%s/issues/%s/timeline" % (repo, issue_number)])
    except Exception:
        return {"prs": False, "merged": 0, "linked_merged": 0, "linked_closed": 0}
    merged = sum(1 for pr in prs if pr.get("merged_at"))
    linked_merged = linked_closed = 0
    for event in timeline:
        source = event.get("source", {}).get("issue", {})
        pr_ref = source.get("pull_request")
        if event.get("event") != "cross-referenced" or not pr_ref:
            continue
        if source.get("state") == "closed":
            linked_closed += 1
        url = pr_ref.get("html_url")
        if url:
            try:
                number = url.rstrip("/").split("/")[-1]
                if gh_json(["repos/%s/pulls/%s" % (repo, number)]).get("merged_at"):
                    linked_merged += 1
            except Exception:
                pass
    return {"prs": bool(prs), "merged": merged, "linked_merged": linked_merged, "linked_closed": linked_closed}

def main():
    data = json.loads(Path("issues.json").read_text())
    min_bounty = float(os.environ.get("MIN_BOUNTY", "0"))
    max_bounty = float(os.environ.get("MAX_BOUNTY", "100000"))
    min_opportunity = float(os.environ.get("MIN_OPPORTUNITY", "0"))
    rows = []
    for issue in data:
        repo = issue["repository"]["nameWithOwner"]
        try:
            repo_meta = gh_json(["repos/%s" % repo])
        except Exception:
            continue
        result = analyze_issue(issue, repo_meta, repo_history(repo, issue["number"]))
        if not result or not min_bounty <= result["value"] <= max_bounty:
            continue
        if result["opportunity"] < min_opportunity:
            continue
        issue["_repo_stars"] = repo_meta.get("stargazers_count", 0)
        issue["_repo_forks"] = repo_meta.get("forks_count", 0)
        rows.append((result["opportunity"], result["value"], result, issue))
    rows.sort(key=lambda x: x[0], reverse=True)
    rows = rows[:50]
    report = ["# Paid Issue Finder Report", "", "Query: %s" % os.environ.get("QUERY", ""), "",
              "Filters: bounty US$%g–US$%g, opportunity >= %g" % (min_bounty, max_bounty, min_opportunity), ""]
    if not rows:
        report.append("No monetary bounty detected.")
    else:
        report += ["## Ranked opportunities", "", "| Rank | Bounty | Opportunity | Risk | Quality | History | Maintainer | Verdict |",
                   "|---:|---:|---:|---:|---:|---:|---:|:---|"]
        for rank, (score, value, result, issue) in enumerate(rows, 1):
            repo = issue["repository"]["nameWithOwner"]
            report.append("| %d | US$%.2f | %.1f | %d | %d | %d | %d | **%s** |" %
                          (rank, value, score, result["risk"], result["quality"], result["history"], result["maintainer"], result["verdict"]))
            evidence = ["Reward: explicit monetary value detected",
                        "Repository: %d stars, %d forks" % (issue["_repo_stars"], issue["_repo_forks"]),
                        "Quality: " + (", ".join(result["quality_reasons"]) or "no explicit quality signal"),
                        "Risk: " + (", ".join(result["risk_reasons"]) or "no major risk signal")]
            report.append("- **US$%.2f** · Opportunity %.1f · Risk %d · **%s** · %s — [%s#%s: %s](%s)" %
                          (value, score, result["risk"], result["verdict"], result["confidence"], repo, issue["number"], issue["title"], issue["url"]))
            report.append("  - " + " | ".join(evidence))
    Path("REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))

if __name__ == "__main__":
    main()
