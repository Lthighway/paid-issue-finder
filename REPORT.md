# Paid Issue Finder — First Live Report

Generated: 2026-10-06
Query: `bounty state:open`
Source: GitHub Issues Search API
Candidates inspected: 20

> This is the first live report generated from real open GitHub issues. Monetary values are signals, not proof of payment.

## Ranked opportunities

| Verdict | Bounty | Issue | Reason |
|---|---:|---|---|
| REVIEW | $90 | [NSPG13/agent-bounties#1369 mirror](https://github.com/NSPG13/agent-bounties/issues/1369) via [bounty-plaza#1292](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1292) | Canonical state says escrowed, but verifier is not ready; payment must be independently verified. |
| REVIEW | $200 | [zhangjiayang6835-cyber/bounty-plaza#309](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/309) | Detailed technical acceptance criteria are present, but the issue contains repeated mirrored bounty material and should be verified at the original source. |
| REVIEW | $200 | [bounty-plaza#257](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/257) | Detailed RSA-OAEP acceptance criteria; mirrored bounty chain requires source verification. |
| REVIEW | $150 | [bounty-plaza#286](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/286) | Detailed JWT path-traversal requirements; mirrored content requires verification. |
| REVIEW | $200 | [bounty-plaza#302](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/302) | Detailed Pickle deserialization requirements; mirrored content requires verification. |
| REVIEW | $150 | [bounty-plaza#260](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/260) | Detailed AWS IAM acceptance criteria; mirrored content requires verification. |
| REVIEW | $150 | [bounty-plaza#265](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/265) | Detailed MongoDB injection acceptance criteria; mirrored content requires verification. |
| REVIEW | $150 | [bounty-plaza#308](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/308) | Detailed DNS/AXFR acceptance criteria; mirrored content requires verification. |
| REVIEW | $37,000 | [DAXDA submission #1598](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1598) | Large value is reported as a submission total, not a single verified payable bounty. |

## AVOID — high-confidence noise / suspicious bounty patterns

- [#1556](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1556) — absurd astronomical amount.
- [#1573](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1573) — PPPDUD currency valued at $0, crypto/cash/gold/goats language.
- [#1570](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1570) — $99,999,999 / 99,999,999 BTC claim.
- [#1602](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1602) — gazillion PPPDUD dollars, explicitly approximately $0.
- [#1593](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1593) — “up to” huge reward, follow-account/backflip requirement, currency undecided.
- [#1558](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1558) — explicitly negative bounty and asks solver to pay the requester.
- [#1548](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1548) — absurd title amount, currency TBD and repeated spam.
- [#309](https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/309) and related mirrored entries — duplicated bounty-plaza content; original source must be preferred.

## Not actionable by the monetary analyzer

- [useagenthq/useagent#70](https://github.com/useagenthq/useagent/issues/70) — technically detailed bounty request, but no explicit monetary amount in the issue body returned by search.
- [rylsherdamz-rgb/stellar-forge#13](https://github.com/rylsherdamz-rgb/stellar-forge/issues/13) — bounty marketplace feature, but no explicit monetary amount in the issue body returned by search.
- [pizzaguyapprentice/high-noon#10](https://github.com/pizzaguyapprentice/high-noon/issues/10) — “bounty system” game mechanic, not a monetary coding bounty.

## First-run conclusions

1. The detector is successfully finding real bounty-shaped GitHub noise.
2. Suspicious monetary language is being separated from technically detailed issues.
3. No candidate from this first 20-result sample is safe enough to label **GO** without additional repository/history/payment verification.
4. The next engineering improvement should be stronger deduplication and original-source resolution for bounty mirrors.
