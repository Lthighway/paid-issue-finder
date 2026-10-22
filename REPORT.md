# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 0 |
| Duplicate results removed | 0 |
| Candidates rejected during source verification | 0 |
| Canonicalized candidates analyzed | 0 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 0 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 0 |

## Actionability snapshot

| Verdict | Candidates |
|:---|---:|
| GO (no high/unknown competition detected) | 0 |
| REVIEW (manual checks needed) | 0 |
| AVOID (high risk signals) | 0 |
| High/unknown competition flags | 0 |

No candidate currently meets the GO threshold. Treat the ranked list as leads for manual review, not ready-to-start paid work.

## How to interpret this report

- **Opportunity** is a ranking score, not a probability of success or payment.
- **GO** means no high/unknown competition flag was detected and the score/risk thresholds were met; it is not a guarantee that the bounty is valid or unpaid.
- **REVIEW** means manually inspect the original issue, open pull requests, comments, assignment status, eligibility, deadlines, and payout terms before starting.
- **HIGH competition** means linked open pull requests, solution/payout signals, or an assigned contributor were detected.
- **Risk** is a heuristic based on suspicious wording, weak payment claims, repository status/activity, and discussion signals; it cannot establish trustworthiness.

No verifiable open issue with a monetary bounty was detected.

---

**Report generated:** 2026-10-22 17:01 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
