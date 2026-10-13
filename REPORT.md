# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 0 |
| Candidates rejected during source verification | 79 |
| Canonicalized candidates analyzed | 21 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 9 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 12 |

## Actionability snapshot

| Verdict | Candidates |
|:---|---:|
| GO (no high/unknown competition detected) | 0 |
| REVIEW (manual checks needed) | 12 |
| AVOID (high risk signals) | 0 |
| High/unknown competition flags | 11 |

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
| 1 | US$50.00 | 77.9 | 10 | 40 | 14 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 77.9 · Risk 10 · **REVIEW** · high — [maaltarifi97-maker/aioa-playground#1: [Bounty: $50] slugify() leaves double and trailing hyphens](https://github.com/maaltarifi97-maker/aioa-playground/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1518
  - Reward: monetary value detected in original issue | Repository: 0 stars, 26 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description, reproduction guidance | Risk: very low repository activity | Competition: HIGH (4 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/2); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/3); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/4); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/7); [solution/payout comment signal](https://github.com/maaltarifi97-maker/aioa-playground/issues/1#issuecomment-5647983975)
| 2 | US$50.00 | 65.1 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.1 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#220: Bounty $50: recipe for a 27B model on a 16 GB AMD card](https://github.com/sybil-solutions/local-ai-registry/issues/220)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1880
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/232); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/220#issuecomment-6124954342); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/220#issuecomment-6127871278)
| 3 | US$50.00 | 65.0 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 65.0 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#217: Bounty $50: recipe for RTX 2080 Ti 11 GB](https://github.com/sybil-solutions/local-ai-registry/issues/217)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1883
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/243); [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/245); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/217#issuecomment-6128022381)
| 4 | US$50.00 | 64.8 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 64.8 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#218: Bounty $50: recipe for GTX 1080 Ti 11 GB](https://github.com/sybil-solutions/local-ai-registry/issues/218)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1882
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/244); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/218#issuecomment-6126466618)
| 5 | US$50.00 | 64.7 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 64.7 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#219: Bounty $50: recipe for RX 7900 XTX 24 GB](https://github.com/sybil-solutions/local-ai-registry/issues/219)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1881
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/219#issuecomment-6126160776)
| 6 | US$50.00 | 64.7 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 64.7 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#216: Bounty $50: recipe for Intel Arc B580 12 GB](https://github.com/sybil-solutions/local-ai-registry/issues/216)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1884
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/216#issuecomment-6128320201)
| 7 | US$50.00 | 64.6 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 64.6 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#222: Bounty $50: recipe for RTX 5060 Ti 16 GB](https://github.com/sybil-solutions/local-ai-registry/issues/222)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1878
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/241); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/222#issuecomment-6125553527)
| 8 | US$50.00 | 64.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 64.5 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#221: Bounty $50: recipe for RTX 4060 Ti 16 GB](https://github.com/sybil-solutions/local-ai-registry/issues/221)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1879
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/242); [linked open pull request](https://github.com/sybil-solutions/local-ai-registry/pull/246); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/221#issuecomment-6125867695)
| 9 | US$50.00 | 64.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 64.5 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#223: Bounty $50: recipe for Ryzen AI 890M (Radeon 890M iGPU)](https://github.com/sybil-solutions/local-ai-registry/issues/223)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1877
  - Reward: monetary value detected in original issue | Repository: 249 stars, 66 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/223#issuecomment-6125265509)
| 10 | US$500.00 | 63.3 | 10 | 30 | 5 | HIGH | 15 | **REVIEW** |
- **US$500.00** · Opportunity 63.3 · Risk 10 · **REVIEW** · high — [Senthemodder/aquarium-of-gullibles#4: [Bounty: $500] Critical: system.beforeEvents.startup Throws CommandRegistrationError on Bedrock 1.21.70](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1333
  - Reward: monetary value detected in original issue | Repository: 0 stars, 17 forks | Quality: clear requirements/acceptance, useful issue label | Risk: very low repository activity | Competition: HIGH (3 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/11); [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/15); [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/20); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-5613005573); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-5613651327)
| 11 | US$100.00 | 46.8 | 0 | 0 | 15 | MEDIUM | 15 | **REVIEW** |
- **US$100.00** · Opportunity 46.8 · Risk 0 · **REVIEW** · medium — [Trauma-Station/Trauma-Station#5021: bounty bounty bounty bounty bounty bounty bounty bounty bounty ](https://github.com/Trauma-Station/Trauma-Station/issues/5021)
  - Reward: monetary value detected in original issue | Repository: 54 stars, 331 forks | Quality: no explicit quality signal | Risk: no major risk signal | Competition: MEDIUM (active discussion; inspect comments before starting)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 12 | US$50.00 | 39.3 | 15 | 10 | 15 | HIGH | 10 | **REVIEW** |
- **US$50.00** · Opportunity 39.3 · Risk 15 · **REVIEW** · medium — [MergeFi/frontend#613: Reward filter and sort compare raw amounts across USDC and XLM](https://github.com/MergeFi/frontend/issues/613)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 91 forks | Quality: detailed issue description | Risk: very low repository activity, no discussion | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/MergeFi/frontend/pull/732)

---

**Report generated:** 2026-10-13 19:12 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
