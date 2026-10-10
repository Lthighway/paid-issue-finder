# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 1 |
| Candidates rejected during source verification | 89 |
| Canonicalized candidates analyzed | 10 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 5 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 5 |

## Actionability snapshot

| Verdict | Candidates |
|:---|---:|
| GO (no high/unknown competition detected) | 0 |
| REVIEW (manual checks needed) | 5 |
| AVOID (high risk signals) | 0 |
| High/unknown competition flags | 5 |

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
| 1 | US$3000.00 | 123.4 | 0 | 40 | 15 | HIGH | 15 | **REVIEW** |
- **US$3000.00** · Opportunity 123.4 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#59732: [Bounty $3,000] Fix ttnn.sampling distribution bias from low-precision random threshold](https://github.com/tenstorrent/tt-metal/issues/59732)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1836
  - Reward: monetary value detected in original issue | Repository: 1697 stars, 753 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (4 linked open pull request(s); 2 comment(s) contain a solution/payout signal; 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline mentioned; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/59781); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/59841); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/59888); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/59917); [solution/payout comment signal](https://github.com/tenstorrent/tt-metal/issues/59732#issuecomment-6063072894)
| 2 | US$3000.00 | 109.0 | 10 | 40 | 11 | HIGH | 15 | **REVIEW** |
- **US$3000.00** · Opportunity 109.0 · Risk 10 · **REVIEW** · high — [aLexzzz430/Cognitive-OS#5: [ Bounty $3k ] [ Research ] Collect and compare AI-generated AGI architecture proposals](https://github.com/aLexzzz430/Cognitive-OS/issues/5)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/478
  - Reward: monetary value detected in original issue | Repository: 3 stars, 49 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (5 linked open pull request(s); 4 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/aLexzzz430/Cognitive-OS/pull/6); [linked open pull request](https://github.com/aLexzzz430/Cognitive-OS/pull/7); [linked open pull request](https://github.com/aLexzzz430/Cognitive-OS/pull/8); [linked open pull request](https://github.com/aLexzzz430/Cognitive-OS/pull/9); [linked open pull request](https://github.com/aLexzzz430/Cognitive-OS/pull/10)
| 3 | US$50.00 | 77.8 | 10 | 40 | 14 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 77.8 · Risk 10 · **REVIEW** · high — [maaltarifi97-maker/aioa-playground#1: [Bounty: $50] slugify() leaves double and trailing hyphens](https://github.com/maaltarifi97-maker/aioa-playground/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1518
  - Reward: monetary value detected in original issue | Repository: 0 stars, 25 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description, reproduction guidance | Risk: very low repository activity | Competition: HIGH (7 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/2); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/3); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/4); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/7); [linked open pull request](https://github.com/maaltarifi97-maker/aioa-playground/pull/13)
| 4 | US$500.00 | 63.5 | 10 | 30 | 5 | HIGH | 15 | **REVIEW** |
- **US$500.00** · Opportunity 63.5 · Risk 10 · **REVIEW** · high — [Senthemodder/aquarium-of-gullibles#4: [Bounty: $500] Critical: system.beforeEvents.startup Throws CommandRegistrationError on Bedrock 1.21.70](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1333
  - Reward: monetary value detected in original issue | Repository: 0 stars, 15 forks | Quality: clear requirements/acceptance, useful issue label | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s); 3 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/11); [linked open pull request](https://github.com/Senthemodder/aquarium-of-gullibles/pull/15); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-5613005573); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-5613651327); [solution/payout comment signal](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4#issuecomment-6083801058)
| 5 | US$99.00 | 11.6 | 10 | 0 | 0 | HIGH | 10 | **REVIEW** |
- **US$99.00** · Opportunity 11.6 · Risk 10 · **REVIEW** · medium — [NEXAITECHAU/gh-disc-968-zhangjiayang6835-cyber-bounty-plaza#1: [NEX Agent] [Bounty] [Bounty] Repair claim next-action mapper](https://github.com/NEXAITECHAU/gh-disc-968-zhangjiayang6835-cyber-bounty-plaza/issues/1)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 0 forks | Quality: no explicit quality signal | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/NEXAITECHAU/gh-disc-968-zhangjiayang6835-cyber-bounty-plaza/pull/2)

---

**Report generated:** 2026-10-10 17:16 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
