# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 3 |
| Candidates rejected during source verification | 83 |
| Canonicalized candidates analyzed | 14 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 5 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 9 |

## Actionability snapshot

| Verdict | Candidates |
|:---|---:|
| GO (no high/unknown competition detected) | 0 |
| REVIEW (manual checks needed) | 9 |
| AVOID (high risk signals) | 0 |
| High/unknown competition flags | 8 |

No candidate currently meets the GO threshold. Treat the ranked list as leads for manual review, not ready-to-start paid work.

## How to interpret this report

- **Opportunity** is a ranking score, not a probability of success or payment.
- **GO** means no high/unknown competition flag was detected and the score/risk thresholds were met; it is not a guarantee that the bounty is valid or unpaid.
- **REVIEW** means manually inspect the original issue, open pull requests, comments, assignment status, eligibility, deadlines, and payout terms before starting.
- **HIGH competition** means linked open pull requests, solution/payout signals, or an assigned contributor were detected.
- **Risk** is a heuristic based on suspicious wording, weak payment claims, repository status/activity, and discussion signals; it cannot establish trustworthiness.

## Ranked opportunities

| Rank | Bounty | Opportunity | Risk | Quality | History | Competition | Maintainer | Verdict |
|---:|---:|---:|---:|---:|---:|:---:|---:|:---|
| 1 | US$750.00 | 80.9 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$750.00** · Opportunity 80.9 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#62571: [Bounty $750] Improve Qwen3-TTS Code Predictor Accuracy](https://github.com/tenstorrent/tt-metal/issues/62571)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4188
  - Reward: monetary value detected in original issue | Repository: 1734 stars, 802 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (5 linked open pull request(s); 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/62225); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/62576); [linked open pull request](https://github.com/muhammadakbarali744-lgtm/tt-metal/pull/1); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/63471); [linked open pull request](https://github.com/zhangjiayang6835-cyber/bounty-plaza/pull/4189)
| 2 | US$250.00 | 71.4 | 10 | 40 | 7 | HIGH | 15 | **REVIEW** |
- **US$250.00** · Opportunity 71.4 · Risk 10 · **REVIEW** · high — [WholeTroutMedia/oss-verification-sandbox#1: Preserve RFC 7239 `Forwarded` host authority in sub-mounted ASGI `Request.scope_for`](https://github.com/WholeTroutMedia/oss-verification-sandbox/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4152
  - Reward: monetary value detected in original issue | Repository: 0 stars, 8 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (12 linked open pull request(s); 3 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/WholeTroutMedia/oss-verification-sandbox/pull/4); [linked open pull request](https://github.com/WholeTroutMedia/oss-verification-sandbox/pull/5); [linked open pull request](https://github.com/WholeTroutMedia/oss-verification-sandbox/pull/7); [linked open pull request](https://github.com/WholeTroutMedia/oss-verification-sandbox/pull/8); [linked open pull request](https://github.com/WholeTroutMedia/oss-verification-sandbox/pull/9)
| 3 | US$50.00 | 68.9 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 68.9 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#219: Bounty $50: recipe for RX 7900 XTX 24 GB](https://github.com/sybil-solutions/local-ai-registry/issues/219)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1881
  - Reward: monetary value detected in original issue | Repository: 280 stars, 105 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/219#issuecomment-6126160776); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/219#issuecomment-6501153744)
| 4 | US$50.00 | 68.2 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 68.2 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#217: Bounty $50: recipe for RTX 2080 Ti 11 GB](https://github.com/sybil-solutions/local-ai-registry/issues/217)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1883
  - Reward: monetary value detected in original issue | Repository: 280 stars, 105 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/245); [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/248); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/217#issuecomment-6128022381)
| 5 | US$50.00 | 67.3 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 67.3 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#223: Bounty $50: recipe for Ryzen AI 890M (Radeon 890M iGPU)](https://github.com/sybil-solutions/local-ai-registry/issues/223)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1877
  - Reward: monetary value detected in original issue | Repository: 280 stars, 105 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/223#issuecomment-6125265509)
| 6 | US$50.00 | 67.0 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 67.0 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#216: Bounty $50: recipe for Intel Arc B580 12 GB](https://github.com/sybil-solutions/local-ai-registry/issues/216)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1884
  - Reward: monetary value detected in original issue | Repository: 280 stars, 105 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/216#issuecomment-6128320201)
| 7 | US$50.00 | 46.2 | 10 | 10 | 14 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 46.2 · Risk 10 · **REVIEW** · high — [jomaaabbe78-spec/bookningsapp#1: [TEST BOUNTY] Fix typo in README](https://github.com/jomaaabbe78-spec/bookningsapp/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4061
  - Reward: monetary value detected in original issue | Repository: 0 stars, 8 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/4); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/5); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/6); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/7); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/8)
| 8 | US$100.00 | 41.3 | 10 | 10 | 7 | HIGH | 15 | **REVIEW** |
- **US$100.00** · Opportunity 41.3 · Risk 10 · **REVIEW** · high — [blake-guthrie/GLASS#1: USDC-quoted pairs not having the correct marketcap displayed in tools](https://github.com/blake-guthrie/GLASS/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4109
  - Reward: monetary value detected in original issue | Repository: 1 stars, 22 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (10 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/2); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/3); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/15); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/23); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/27)
| 9 | US$1000.00 | 32.6 | 10 | 0 | 0 | LOW | 10 | **REVIEW** |
- **US$1000.00** · Opportunity 32.6 · Risk 10 · **REVIEW** · medium — [eleectrum/eleectrum.github.io#1: $1000 Bounty](https://github.com/eleectrum/eleectrum.github.io/issues/1)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 0 forks | Quality: no explicit quality signal | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO

---

**Report generated:** 2026-10-31 17:11 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
