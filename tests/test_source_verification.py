from scripts.run_finder import canonicalize_issue, source_ref, extract_source_url, is_unverified_candidate, detect_competition
from scripts.analyze_issues import detect_bounty


def mirror_issue():
    return {
        "title": "[Bounty] $999999999999999999 BOUNTY - URGENT",
        "body": "Original source: https://github.com/example/project/issues/42",
        "url": "https://github.com/aggregator/list/issues/9",
        "number": 9,
        "repository": {"nameWithOwner": "aggregator/list"},
    }


def test_mirror_is_replaced_by_original_issue(monkeypatch):
    original = {
        "number": 42,
        "title": "Fix a real regression",
        "body": "Please fix the regression. Reward: $125.",
        "state": "open",
        "html_url": "https://github.com/example/project/issues/42",
        "updated_at": "2026-10-08T12:00:00Z",
        "comments": 3,
        "labels": [{"name": "bounty"}],
        "user": {"login": "maintainer"},
    }
    calls = []

    def fake_gh_json(args):
        calls.append(args)
        return original

    monkeypatch.setattr("scripts.run_finder.gh_json", fake_gh_json)
    result = canonicalize_issue(mirror_issue())

    assert calls == [["repos/example/project/issues/42"]]
    assert result["title"] == "Fix a real regression"
    assert result["repository"]["nameWithOwner"] == "example/project"
    assert result["url"] == "https://github.com/example/project/issues/42"
    assert result["comments"] == 3
    assert result["updatedAt"] == "2026-10-08T12:00:00Z"
    assert result["_discovered_url"] == "https://github.com/aggregator/list/issues/9"
    assert source_ref(mirror_issue()) == "example/project/42"


def test_closed_original_is_not_a_live_opportunity(monkeypatch):
    monkeypatch.setattr(
        "scripts.run_finder.gh_json",
        lambda args: {"number": 42, "state": "closed"},
    )
    assert canonicalize_issue(mirror_issue()) is None


def test_unverifiable_mirror_is_skipped(monkeypatch):
    def fail(args):
        raise RuntimeError("API unavailable")

    monkeypatch.setattr("scripts.run_finder.gh_json", fail)
    assert canonicalize_issue(mirror_issue()) is None


def test_non_mirror_issue_is_left_unchanged():
    issue = {
        "title": "Bounty: $100",
        "body": "Original issue body",
        "repository": {"nameWithOwner": "example/project"},
        "number": 7,
    }
    assert canonicalize_issue(issue) is issue



def test_mirror_chain_prefers_original_repo_over_older_mirrors():
    issue = {
        "title": "Mirrored bounty",
        "body": (
            "Earlier copy: https://github.com/aggregator/list/issues/7\n"
            "Original source: https://github.com/example/project/issues/42"
        ),
        "url": "https://github.com/aggregator/list/issues/9",
        "number": 9,
        "repository": {"nameWithOwner": "aggregator/list"},
    }
    assert extract_source_url(issue) == "https://github.com/example/project/issues/42"
    assert source_ref(issue) == "example/project/42"


def test_unverified_or_archived_bounty_is_skipped_without_api_call(monkeypatch):
    issue = {
        "title": "Old bounty",
        "body": "Archived duplicate. Lifecycle: `unavailable`",
        "labels": [{"name": "verification-unavailable"}],
        "repository": {"nameWithOwner": "example/project"},
        "number": 9,
    }
    monkeypatch.setattr(
        "scripts.run_finder.gh_json",
        lambda args: (_ for _ in ()).throw(AssertionError("must not fetch")),
    )
    assert is_unverified_candidate(issue)
    assert canonicalize_issue(issue) is None


def test_usdc_amount_is_not_misread_as_usd():
    assert detect_bounty("Solver reward: 0.90 USDC; funding: 1.00 USDC") is None
    assert detect_bounty("Real reward: $200 USD") == 200


def test_competition_detects_solution_and_payout_comments():
    result = detect_competition([
        {"body": "## Solution\\nHere is the fix.\\nPlease remit the bounty to my payout address."}
    ])
    assert result["status"] == "HIGH"
    assert "1 comment(s) contain a solution/payout signal" in result["reasons"]


def test_competition_detects_linked_open_pull_request():
    result = detect_competition([], linked_open=1)
    assert result["status"] == "HIGH"
    assert result["reasons"] == ["1 linked open pull request(s)"]


def test_competition_flags_busy_discussion_for_manual_review():
    result = detect_competition([{"body": "a"}, {"body": "b"}, {"body": "c"}])
    assert result["status"] == "MEDIUM"


def test_competition_is_unknown_when_comments_cannot_be_verified():
    result = detect_competition([], comments_verified=False)
    assert result["status"] == "UNKNOWN"
    assert result["verified"] is False


def test_competition_signal_prevents_go_verdict():
    from scripts.analyze_issues import analyze_issue

    issue = {
        "title": "[Bounty: $100] Fix a regression",
        "body": "Acceptance criteria: implement the fix and add tests. " + ("Detailed requirements. " * 30),
        "labels": [{"name": "bounty"}],
        "author": {"login": "maintainer"},
        "comments": 4,
        "updatedAt": "2026-10-09T00:00:00Z",
    }
    result = analyze_issue(
        issue,
        {"stargazers_count": 100, "forks_count": 20, "archived": False, "pushed_at": "2026-10-09T00:00:00Z"},
        {"competition": "HIGH", "competition_reasons": ["linked open pull request(s)"]},
    )
    assert result["competition"] == "HIGH"
    assert result["verdict"] == "REVIEW"
