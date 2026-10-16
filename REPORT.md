# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 0 |
| Candidates rejected during source verification | 80 |
| Canonicalized candidates analyzed | 20 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 11 |
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
| 1 | US$50.00 | 66.4 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 66.4 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#218: Bounty $50: recipe for GTX 1080 Ti 11 GB](https://github.com/sybil-solutions/local-ai-registry/issues/218)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1882
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/255); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/218#issuecomment-6126466618)
| 2 | US$50.00 | 66.4 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 66.4 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#217: Bounty $50: recipe for RTX 2080 Ti 11 GB](https://github.com/sybil-solutions/local-ai-registry/issues/217)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1883
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/245); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/217#issuecomment-6128022381)
| 3 | US$50.00 | 65.8 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.8 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#220: Bounty $50: recipe for a 27B model on a 16 GB AMD card](https://github.com/sybil-solutions/local-ai-registry/issues/220)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1880
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/232); [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/257); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/220#issuecomment-6124954342); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/220#issuecomment-6127871278)
| 4 | US$50.00 | 65.6 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.6 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#216: Bounty $50: recipe for Intel Arc B580 12 GB](https://github.com/sybil-solutions/local-ai-registry/issues/216)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1884
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/216#issuecomment-6128320201)
| 5 | US$50.00 | 65.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.5 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#222: Bounty $50: recipe for RTX 5060 Ti 16 GB](https://github.com/sybil-solutions/local-ai-registry/issues/222)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1878
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/241); [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/273); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/222#issuecomment-6125553527)
| 6 | US$50.00 | 65.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.5 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#219: Bounty $50: recipe for RX 7900 XTX 24 GB](https://github.com/sybil-solutions/local-ai-registry/issues/219)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1881
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/219#issuecomment-6126160776)
| 7 | US$50.00 | 65.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.5 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#223: Bounty $50: recipe for Ryzen AI 890M (Radeon 890M iGPU)](https://github.com/sybil-solutions/local-ai-registry/issues/223)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1877
  - Reward: monetary value detected in original issue | Repository: 253 stars, 78 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/223#issuecomment-6125265509)
| 8 | US$500.00 | 63.3 | 10 | 30 | 5 | HIGH | 15 | **REVIEW** |
- **US$500.00** · Opportunity 63.3 · Risk 10 · **REVIEW** · high — [Senthemodder/aquarium-of-gullibles#4: [Bounty: $500] Critical: system.beforeEvents.startup Throws CommandRegistrationError on Bedrock 1.21.70](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1333
  - Reward: monetary value detected in original issue | Repository: 0 stars, 17 forks | Quality: clear requirements/acceptance, useful issue label | Risk: very low repository activity | Competition: HIGH (3 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/11); [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/15); [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/20); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-5613005573); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-5613651327)
| 9 | US$100.00 | 46.8 | 0 | 0 | 15 | MEDIUM | 15 | **REVIEW** |
- **US$100.00** · Opportunity 46.8 · Risk 0 · **REVIEW** · medium — [Trauma-Station/Trauma-Station#5021: bounty bounty bounty bounty bounty bounty bounty bounty bounty ](https://github.com/Trauma-Station/Trauma-Station/issues/5021)
  - Reward: monetary value detected in original issue | Repository: 54 stars, 335 forks | Quality: no explicit quality signal | Risk: no major risk signal | Competition: MEDIUM (active discussion; inspect comments before starting)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO

---

**Report generated:** 2026-10-16 16:31 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
