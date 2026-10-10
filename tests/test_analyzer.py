from scripts.analyze_issues import analyze_issue, detect_bounty
from scripts.run_finder import extract_source_url, report_footer, source_key, summarize_actionability


def issue(body, labels=None, comments=0, author="maintainer", updated=True):
    return {
        "title": "Bounty: fix authentication bug",
        "body": body,
        "labels": [{"name": x} for x in (labels or [])],
        "comments": comments,
        "author": author,
        "updatedAt": "2026-10-06T00:00:00Z" if updated else None,
    }


def test_detect_bounty_formats():
    assert detect_bounty("Reward: $500") == 500
    assert detect_bounty("Reward: US$1,250") == 1250
    assert detect_bounty("Reward: 750 USD") == 750


def test_bounty_submission_is_not_mistaken_for_an_offer():
    text = (
        "[BOUNTY-SUBMISSION] DAXDA Recursive Bounty System\n"
        "Submission ID: DAXDA-META-2026-09-18-001\n"
        "Submission Package\nTotal Value: $37,000"
    )
    assert detect_bounty(text) is None


def test_legitimate_detailed_issue_is_not_avoid():
    result = analyze_issue(
        issue(
            "Reward: $500. Acceptance criteria: fix the authentication bug. "
            "Steps to reproduce: login with an expired token. "
            + "Detailed technical context " * 40,
            ["bounty", "help wanted"],
            comments=8,
        ),
        {"stargazers_count": 2000, "forks_count": 200, "pushed_at": "2026-10-05T00:00:00Z", "archived": False},
        {"prs": True, "merged": 10, "linked_merged": 1, "linked_closed": 1},
    )
    assert result["value"] == 500
    assert result["risk"] < 60
    assert result["verdict"] in ("GO", "REVIEW")


def test_fake_currency_is_high_risk():
    result = analyze_issue(
        issue("Bounty: $999. Currency: TBD. PPPDUD dollars. Follow my account and take your money back."),
        {"stargazers_count": 2, "forks_count": 0, "pushed_at": None, "archived": False},
    )
    assert result["risk"] >= 60
    assert result["verdict"] == "AVOID"


def test_archived_repository_is_penalized():
    result = analyze_issue(
        issue("Reward: $300. Acceptance criteria: implement the requested fix.", ["bounty"], comments=2),
        {"stargazers_count": 500, "forks_count": 50, "pushed_at": "2025-01-01T00:00:00Z", "archived": True},
    )
    assert result["risk"] >= 30


def test_weak_claim_is_not_high_confidence():
    result = analyze_issue(
        issue("Bounty up to $1000. Terms and conditions apply.", ["bounty"], comments=2),
        {"stargazers_count": 100, "forks_count": 10, "pushed_at": "2026-10-01T00:00:00Z", "archived": False},
    )
    assert result["confidence"] != "high"
    assert result["risk"] >= 15


def test_detect_bounty_ignores_absurd_amounts():
    assert detect_bounty("Reward: $999999999") is None


def test_negative_bounty_is_high_risk():
    result = analyze_issue(issue("Bounty: $100. The bounty is negative and paid in PPPDUD dollars."), {"stargazers_count": 20, "forks_count": 2, "pushed_at": "2026-10-01T00:00:00Z", "archived": False})
    assert result["risk"] >= 60
    assert result["verdict"] == "AVOID"


def test_backflip_and_follow_request_is_high_risk():
    result = analyze_issue(issue("Reward: $100. Follow my GitHub account and do a backflip to claim it."), {"stargazers_count": 20, "forks_count": 2, "pushed_at": "2026-10-01T00:00:00Z", "archived": False})
    assert result["risk"] >= 60
    assert result["verdict"] == "AVOID"


def test_crypto_only_payment_is_weak():
    result = analyze_issue(issue("Reward: $250. We pay in BTC after acceptance.", ["bounty"], comments=4), {"stargazers_count": 100, "forks_count": 10, "pushed_at": "2026-10-01T00:00:00Z", "archived": False})
    assert result["confidence"] == "low"
    assert result["risk"] >= 15


def test_assigned_issue_requires_manual_review():
    item = issue(
        "Reward: $3000. Acceptance criteria: fix the sampling bug. " + "Detailed requirements. " * 30,
        ["bounty"],
        comments=4,
    )
    item["assignees"] = [{"login": "another-contributor"}]
    result = analyze_issue(
        item,
        {"stargazers_count": 1000, "forks_count": 100, "pushed_at": "2026-10-08T00:00:00Z", "archived": False},
        {"competition": "LOW", "competition_reasons": []},
    )
    assert result["competition"] == "HIGH"
    assert result["verdict"] == "REVIEW"
    assert "1 contributor(s) already assigned" in result["competition_reasons"]


def test_extract_original_source_url():
    item = {"body": "### Original Source URL\\nhttps://github.com/example/project/issues/42"}
    assert extract_source_url(item) == "https://github.com/example/project/issues/42"
    assert source_key(item) == "/example/project/issues/42"


def test_non_mirror_issue_uses_own_identity_for_deduplication():
    item = {"repository": {"nameWithOwner": "example/project"}, "number": 7, "body": "No source mirror."}
    assert source_key(item) == "example/project#7"


def test_analyzer_preserves_competition_evidence_for_report():
    evidence = [
        {
            "kind": "linked open pull request",
            "url": "https://github.com/example/project/pull/99",
        },
        {
            "kind": "solution/payout comment signal",
            "url": "https://github.com/example/project/issues/42#issuecomment-1",
        },
    ]
    result = analyze_issue(
        issue("Reward: $100. Acceptance criteria: fix a regression.", ["bounty"], comments=2),
        {"stargazers_count": 100, "forks_count": 10, "pushed_at": "2026-10-09T00:00:00Z", "archived": False},
        {"competition": "HIGH", "competition_reasons": ["linked open pull request(s)"], "competition_evidence": evidence},
    )
    assert result["competition_evidence"] == evidence


def test_reward_terms_checklist_detects_language_but_never_confirms_payment():
    from scripts.analyze_issues import detect_reward_checks

    checks = detect_reward_checks(
        "Reward: $500. Payment terms: paid via bank transfer upon acceptance. "
        "Eligibility requirements apply. Submit by the deadline."
    )
    assert checks["payment_terms_language"] is True
    assert checks["eligibility_language"] is True
    assert checks["deadline_language"] is True
    assert checks["payment_confirmed"] is False


def test_reward_terms_checklist_marks_missing_signals_without_claiming_failure():
    from scripts.analyze_issues import detect_reward_checks

    checks = detect_reward_checks("Reward: $100. Fix the bug and add tests.")
    assert checks["payment_terms_language"] is False
    assert checks["eligibility_language"] is False
    assert checks["deadline_language"] is False
    assert checks["payment_confirmed"] is False


def test_actionability_summary_counts_verdicts_and_competition():
    rows = [
        (90, 500, {"verdict": "GO", "competition": "LOW"}, {}),
        (80, 300, {"verdict": "REVIEW", "competition": "HIGH"}, {}),
        (70, 100, {"verdict": "REVIEW", "competition": "UNKNOWN"}, {}),
        (10, 50, {"verdict": "AVOID", "competition": "LOW"}, {}),
    ]
    summary = summarize_actionability(rows)
    assert summary["verdicts"] == {"GO": 1, "REVIEW": 2, "AVOID": 1}
    assert summary["high_or_unknown_competition"] == 2


def test_actionability_summary_handles_empty_results():
    summary = summarize_actionability([])
    assert summary["verdicts"] == {"GO": 0, "REVIEW": 0, "AVOID": 0}
    assert summary["high_or_unknown_competition"] == 0


def test_report_footer_shows_freshness_and_feedback_link():
    footer = "\n".join(report_footer("2026-10-10 02:00 UTC"))
    assert "**Report generated:** 2026-10-10 02:00 UTC" in footer
    assert "share product feedback" in footer
    assert "issues/new?template=product_feedback.yml" in footer
    assert "not payment guarantees" in footer
