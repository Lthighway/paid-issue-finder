from scripts.run_finder import canonicalize_issue, source_ref


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
