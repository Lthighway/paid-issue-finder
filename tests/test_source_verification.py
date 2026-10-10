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


def test_unknown_competition_status_requires_manual_review():
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
        {"competition": "UNKNOWN", "competition_reasons": ["could not verify issue comments"]},
    )
    assert result["competition"] == "UNKNOWN"
    assert result["verdict"] == "REVIEW"


def test_canonicalize_follows_nested_mirror_to_deepest_source(monkeypatch):
    from scripts.run_finder import canonical_issue_key

    candidate = {
        "number": 1601,
        "title": "Mirror of an external bounty",
        "body": "Source URL: https://github.com/Vikingr2023/awesome-agent-bounties/issues/76",
        "url": "https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1601",
        "html_url": "https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1601",
        "repository": {"nameWithOwner": "zhangjiayang6835-cyber/bounty-plaza"},
    }
    intermediate = {
        "number": 76,
        "title": "Mirror of another bounty",
        "body": (
            "Original URL: https://github.com/Vikingr2023/awesome-agent-bounties/issues/52\\n"
            "## Embedded task\\n"
            "Original URL: https://github.com/aLexzzz430/Cognitive-OS/issues/5"
        ),
        "state": "open",
        "html_url": "https://github.com/Vikingr2023/awesome-agent-bounties/issues/76",
        "comments": 2,
        "labels": [],
        "user": {"login": "mirror-maintainer"},
    }
    root = {
        "number": 5,
        "title": "Collect AGI architecture proposals",
        "body": "Reward: $3,000 USD. Submit a research packet.",
        "state": "open",
        "html_url": "https://github.com/aLexzzz430/Cognitive-OS/issues/5",
        "comments": 49,
        "labels": [{"name": "bounty"}],
        "user": {"login": "aLexzzz430"},
    }
    calls = []

    def fake_gh_json(args):
        calls.append(args)
        if args == ["repos/Vikingr2023/awesome-agent-bounties/issues/76"]:
            return intermediate
        if args == ["repos/aLexzzz430/Cognitive-OS/issues/5"]:
            return root
        raise AssertionError("Unexpected source lookup: %r" % args)

    monkeypatch.setattr("scripts.run_finder.gh_json", fake_gh_json)
    result = canonicalize_issue(candidate)

    assert calls == [
        ["repos/Vikingr2023/awesome-agent-bounties/issues/76"],
        ["repos/aLexzzz430/Cognitive-OS/issues/5"],
    ]
    assert result["repository"]["nameWithOwner"] == "aLexzzz430/Cognitive-OS"
    assert result["number"] == 5
    assert result["url"] == "https://github.com/aLexzzz430/Cognitive-OS/issues/5"
    assert result["_discovered_url"] == candidate["url"]
    assert canonical_issue_key(result) == "alexzzz430/cognitive-os#5"


def test_canonicalize_rejects_cyclic_mirror_chain(monkeypatch):
    candidate = {
        "number": 7,
        "title": "Mirror A",
        "body": "Source: https://github.com/example/b/issues/8",
        "url": "https://github.com/example/a/issues/7",
        "repository": {"nameWithOwner": "example/a"},
    }
    source_b = {
        "number": 8,
        "title": "Mirror B",
        "body": "Source: https://github.com/example/a/issues/7",
        "state": "open",
        "html_url": "https://github.com/example/b/issues/8",
        "comments": 1,
        "labels": [],
        "user": {"login": "maintainer"},
    }
    source_a = {
        "number": 7,
        "title": "Mirror A",
        "body": "Source: https://github.com/example/b/issues/8",
        "state": "open",
        "html_url": "https://github.com/example/a/issues/7",
        "comments": 1,
        "labels": [],
        "user": {"login": "maintainer"},
    }

    def fake_gh_json(args):
        if args == ["repos/example/b/issues/8"]:
            return source_b
        if args == ["repos/example/a/issues/7"]:
            return source_a
        raise AssertionError("Unexpected source lookup: %r" % args)

    monkeypatch.setattr("scripts.run_finder.gh_json", fake_gh_json)
    assert canonicalize_issue(candidate) is None


def test_competition_evidence_links_open_prs_and_solution_comments():
    from scripts.run_finder import collect_competition_evidence

    comments = [
        {
            "body": "Here is the fix and payout address.",
            "html_url": "https://github.com/example/project/issues/42#issuecomment-1",
        },
        {
            "body": "Thanks for the clarification.",
            "html_url": "https://github.com/example/project/issues/42#issuecomment-2",
        },
    ]
    timeline = [
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "state": "open",
                    "html_url": "https://github.com/example/project/pull/99",
                    "pull_request": {"html_url": "https://github.com/example/project/pull/99"},
                }
            },
        },
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "state": "closed",
                    "html_url": "https://github.com/example/project/pull/88",
                    "pull_request": {"html_url": "https://github.com/example/project/pull/88"},
                }
            },
        },
    ]

    evidence = collect_competition_evidence(comments, timeline)

    assert evidence == [
        {
            "kind": "linked open pull request",
            "url": "https://github.com/example/project/pull/99",
        },
        {
            "kind": "solution/payout comment signal",
            "url": "https://github.com/example/project/issues/42#issuecomment-1",
        },
    ]
