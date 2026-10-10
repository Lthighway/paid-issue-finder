# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 1 |
| Candidates rejected during source verification | 87 |
| Canonicalized candidates analyzed | 12 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 5 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 7 |

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
  - Reward: monetary value detected in original issue | Repository: 1697 stars, 752 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (4 linked open pull request(s); 2 comment(s) contain a solution/payout signal; 1 contributor(s) already assigned)
| 2 | US$3000.00 | 109.0 | 10 | 40 | 11 | HIGH | 15 | **REVIEW** |
- **US$3000.00** · Opportunity 109.0 · Risk 10 · **REVIEW** · high — [aLexzzz430/Cognitive-OS#5: [ Bounty $3k ] [ Research ] Collect and compare AI-generated AGI architecture proposals](https://github.com/aLexzzz430/Cognitive-OS/issues/5)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/478
  - Reward: monetary value detected in original issue | Repository: 3 stars, 49 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (5 linked open pull request(s); 4 comment(s) contain a solution/payout signal)
| 3 | US$50.00 | 77.8 | 10 | 40 | 14 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 77.8 · Risk 10 · **REVIEW** · high — [maaltarifi97-maker/aioa-playground#1: [Bounty: $50] slugify() leaves double and trailing hyphens](https://github.com/maaltarifi97-maker/aioa-playground/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1518
  - Reward: monetary value detected in original issue | Repository: 0 stars, 25 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description, reproduction guidance | Risk: very low repository activity | Competition: HIGH (7 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
| 4 | US$500.00 | 63.5 | 10 | 30 | 5 | HIGH | 15 | **REVIEW** |
- **US$500.00** · Opportunity 63.5 · Risk 10 · **REVIEW** · high — [Senthemodder/aquarium-of-gullibles#4: [Bounty: $500] Critical: system.beforeEvents.startup Throws CommandRegistrationError on Bedrock 1.21.70](https://github.com/Senthemodder/aquarium-of-gullibles/issues/4)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1333
  - Reward: monetary value detected in original issue | Repository: 0 stars, 15 forks | Quality: clear requirements/acceptance, useful issue label | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s); 3 comment(s) contain a solution/payout signal)
| 5 | US$55.00 | 46.4 | 10 | 30 | 0 | HIGH | 15 | **REVIEW** |
- **US$55.00** · Opportunity 46.4 · Risk 10 · **REVIEW** · medium — [Augora-Labs/augora-contracts#43: [Bounty: $55] Test that unpause restores leaderboard accrual](https://github.com/Augora-Labs/augora-contracts/issues/43)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 3 forks | Quality: clear requirements/acceptance, detailed issue description | Risk: very low repository activity | Competition: HIGH (2 comment(s) contain a solution/payout signal)
| 6 | US$60.00 | 41.4 | 10 | 30 | 0 | HIGH | 10 | **REVIEW** |
- **US$60.00** · Opportunity 41.4 · Risk 10 · **REVIEW** · medium — [Augora-Labs/augora-contracts#42: [Bounty: $60] Test the leaderboard queue_reward and queue_bonus_reward paths](https://github.com/Augora-Labs/augora-contracts/issues/42)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 3 forks | Quality: clear requirements/acceptance, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 comment(s) contain a solution/payout signal)
| 7 | US$99.00 | 11.6 | 10 | 0 | 0 | HIGH | 10 | **REVIEW** |
- **US$99.00** · Opportunity 11.6 · Risk 10 · **REVIEW** · medium — [NEXAITECHAU/gh-disc-968-zhangjiayang6835-cyber-bounty-plaza#1: [NEX Agent] [Bounty] [Bounty] Repair claim next-action mapper](https://github.com/NEXAITECHAU/gh-disc-968-zhangjiayang6835-cyber-bounty-plaza/issues/1)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 0 forks | Quality: no explicit quality signal | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
