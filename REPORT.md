# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 2 |
| Candidates rejected during source verification | 77 |
| Canonicalized candidates analyzed | 21 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 7 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 14 |

## Actionability snapshot

| Verdict | Candidates |
|:---|---:|
| GO (no high/unknown competition detected) | 4 |
| REVIEW (manual checks needed) | 10 |
| AVOID (high risk signals) | 0 |
| High/unknown competition flags | 9 |

GO is a screening result only; confirm the original issue, competition, eligibility, and payout terms before starting.

## How to interpret this report

- **Opportunity** is a ranking score, not a probability of success or payment.
- **GO** means no high/unknown competition flag was detected and the score/risk thresholds were met; it is not a guarantee that the bounty is valid or unpaid.
- **REVIEW** means manually inspect the original issue, open pull requests, comments, assignment status, eligibility, deadlines, and payout terms before starting.
- **HIGH competition** means linked open pull requests, solution/payout signals, or an assigned contributor were detected.
- **Risk** is a heuristic based on suspicious wording, weak payment claims, repository status/activity, and discussion signals; it cannot establish trustworthiness.

## Ranked opportunities

| Rank | Bounty | Opportunity | Risk | Quality | History | Competition | Maintainer | Verdict |
|---:|---:|---:|---:|---:|---:|:---:|---:|:---|
| 1 | US$10000.00 | 98.9 | 0 | 10 | 15 | HIGH | 15 | **REVIEW** |
- **US$10000.00** · Opportunity 98.9 · Risk 0 · **REVIEW** · medium — [Trauma-Station/Trauma-Station#5225: [BOUNTY] huge important bounty bounty bounty](https://github.com/Trauma-Station/Trauma-Station/issues/5225)
  - Reward: monetary value detected in original issue | Repository: 56 stars, 357 forks | Quality: detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/Trauma-Station/Trauma-Station/issues/5225#issuecomment-6558697538)
| 2 | US$750.00 | 81.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$750.00** · Opportunity 81.5 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#64647: [Bounty $750] Fix remaining sharded scale_mask_softmax mask handling issues](https://github.com/tenstorrent/tt-metal/issues/64647)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4243
  - Reward: monetary value detected in original issue | Repository: 1747 stars, 829 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64653)
| 3 | US$750.00 | 81.3 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$750.00** · Opportunity 81.3 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#64575: [Bounty $750] Fix sharded softmax on offset core grids](https://github.com/tenstorrent/tt-metal/issues/64575)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4225
  - Reward: monetary value detected in original issue | Repository: 1747 stars, 829 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (3 linked open pull request(s); 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64576); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64659); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64668)
| 4 | US$50.00 | 69.1 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 69.1 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#219: Bounty $50: recipe for RX 7900 XTX 24 GB](https://github.com/sybil-solutions/local-ai-registry/issues/219)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1881
  - Reward: monetary value detected in original issue | Repository: 290 stars, 115 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/219#issuecomment-6126160776); [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/219#issuecomment-6501153744)
| 5 | US$50.00 | 68.8 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 68.8 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#217: Bounty $50: recipe for RTX 2080 Ti 11 GB](https://github.com/sybil-solutions/local-ai-registry/issues/217)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1883
  - Reward: monetary value detected in original issue | Repository: 290 stars, 115 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/217#issuecomment-6128022381)
| 6 | US$50.00 | 67.4 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 67.4 · Risk 0 · **REVIEW** · high — [sybil-solutions/local-ai-registry#216: Bounty $50: recipe for Intel Arc B580 12 GB](https://github.com/sybil-solutions/local-ai-registry/issues/216)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/1884
  - Reward: monetary value detected in original issue | Repository: 290 stars, 115 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/sybil-solutions/local-ai-registry/issues/216#issuecomment-6128320201)
| 7 | US$450.00 | 64.6 | 10 | 20 | 7 | LOW | 15 | **GO** |
- **US$450.00** · Opportunity 64.6 · Risk 10 · **GO** · high — [IES-BoilerRoom/Furnace#1: 💎 [Escrowed $450 USDC] 24-Vector Conformance Suite: Streaming MCP SSE Chunk Boundary Reassembly with Backpressure Backoff](https://github.com/IES-BoilerRoom/Furnace/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4224
  - Reward: monetary value detected in original issue | Repository: 2 stars, 5 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 8 | US$600.00 | 64.1 | 10 | 20 | 5 | LOW | 15 | **GO** |
- **US$600.00** · Opportunity 64.1 · Risk 10 · **GO** · high — [IES-BoilerRoom/Furnace#2: 💎 [Escrowed $600 USDC] 24-Vector Conformance Suite: PagedAttention KV-Cache Block Desync on Prefix-Aware Chunked Preemption](https://github.com/IES-BoilerRoom/Furnace/issues/2)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4223
  - Reward: monetary value detected in original issue | Repository: 2 stars, 5 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 9 | US$600.00 | 57.9 | 15 | 20 | 5 | LOW | 10 | **GO** |
- **US$600.00** · Opportunity 57.9 · Risk 15 · **GO** · high — [WholeTroutMedia/agent-conformance-quarantine#2: [Escrowed $600 USDC] 24-Vector Conformance Suite: PagedAttention KV-Cache Block Desync on Prefix-Aware Chunked Preemption](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4207
  - Reward: monetary value detected in original issue | Repository: 2 stars, 13 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity, no discussion | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 10 | US$450.00 | 57.8 | 10 | 20 | 5 | LOW | 10 | **GO** |
- **US$450.00** · Opportunity 57.8 · Risk 10 · **GO** · high — [WholeTroutMedia/agent-conformance-quarantine#1: [Escrowed $450 USDC] 24-Vector Conformance Suite: Streaming MCP SSE Chunk Boundary Reassembly with Backpressure Backoff](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4208
  - Reward: monetary value detected in original issue | Repository: 2 stars, 13 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 11 | US$50.00 | 46.5 | 10 | 10 | 14 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 46.5 · Risk 10 · **REVIEW** · high — [jomaaabbe78-spec/bookningsapp#1: [TEST BOUNTY] Fix typo in README](https://github.com/jomaaabbe78-spec/bookningsapp/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4061
  - Reward: monetary value detected in original issue | Repository: 0 stars, 10 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/4); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/5); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/6); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/7); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/8)
| 12 | US$100.00 | 41.7 | 10 | 10 | 7 | HIGH | 15 | **REVIEW** |
- **US$100.00** · Opportunity 41.7 · Risk 10 · **REVIEW** · high — [blake-guthrie/GLASS#1: USDC-quoted pairs not having the correct marketcap displayed in tools](https://github.com/blake-guthrie/GLASS/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4109
  - Reward: monetary value detected in original issue | Repository: 1 stars, 27 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (9 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/2); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/3); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/15); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/23); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/27)
| 13 | US$1000.00 | 37.7 | 10 | 0 | 0 | LOW | 15 | **REVIEW** |
- **US$1000.00** · Opportunity 37.7 · Risk 10 · **REVIEW** · medium — [eleectrum/eleectrum.github.io#1: $1000 Bounty](https://github.com/eleectrum/eleectrum.github.io/issues/1)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 0 forks | Quality: no explicit quality signal | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 14 | US$750.00 | 33.7 | 10 | 10 | 0 | HIGH | 10 | **REVIEW** |
- **US$750.00** · Opportunity 33.7 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#20: [Bounty $750] feat(validator): support custom step_size in verify_sequence_gap](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/20)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4244
  - Reward: monetary value detected in original issue | Repository: 0 stars, 11 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/22); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/27)

---

**Report generated:** 2026-11-07 17:43 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
