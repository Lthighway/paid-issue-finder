# How to verify a paid GitHub issue before working on it

An issue title containing "$500 bounty" is a **lead**, not proof of a funded reward.
This guide explains how to assess open-source software bounties without paying
upfront or relying on a ranking score.

## 1. Find the original maintainer issue

Bounty aggregators and mirrored issues can be useful for discovery, but they
often lag behind the original repository. Open the original link and confirm
that the issue is still open. Do not assume a mirror's displayed price or
status is authoritative.

Record the repository, issue number, UTC date checked, public reward statement,
and the maintainer account that made the offer.

## 2. Verify who funds the reward

A numerical amount can be written by anyone. Look for the original maintainer's
terms and a funding mechanism that can be independently inspected. Confirm
whether money is deposited, merely pledged, or contingent on discretionary
acceptance. If there is no verifiable funding mechanism, treat payout as
**unconfirmed**.

Never send a deposit, registration payment, wallet seed phrase, or private key
to be considered for a coding bounty.

## 3. Verify the work is still available

Before coding, check issue assignments, linked open and merged pull requests,
comments stating that someone claimed the work, deadline changes, and reports
of an earlier payout. Repository activity and acceptance criteria matter more
than how large the bounty looks in a search result.

For high-competition issues, estimate whether a better documented fix is still
wanted. Do not start simply because an automated tool reports a high score.

## 4. Check acceptance and payment terms

A credible opportunity should say what counts as successful delivery: tests,
performance target, compatibility, documentation, review process, and who
makes the final decision. Clarify currency, eligibility, payout method,
geographic restrictions, taxes, refund or dispute rules, and expected payout
timing before treating the issue as an income source.

## 5. Keep a verifiable evidence trail

| Field | Evidence to keep |
|---|---|
| Original issue | Canonical GitHub issue URL and date checked |
| Funding | Public escrow or maintainer terms; or mark unverified |
| Scope | Acceptance criteria and tests |
| Competition | Assigned users, related PRs, latest comments |
| Submission | PR URL, commit SHA, CI outcome |
| Acceptance | Explicit maintainer confirmation |
| Receipt | Provider's settled transaction or wallet transaction reference |

A merged PR is **not** sufficient proof of receiving money. A promised amount
is **not** a settled balance.

## 6. Use Paid Issue Finder as a screening tool

[See the ranked report](../REPORT.md). Its GO and REVIEW verdicts are
heuristics that prioritize investigation. They do not prove that a bounty is
funded, available, or paid. Use the original issue as the source of truth.

If the project helps you discover legitimate opportunities, you can
[optionally support its maintenance](../README.md#-support-the-project).
Voluntary support is not a purchase of bounty eligibility or payout guarantees.

*Last reviewed: November 2026.*
