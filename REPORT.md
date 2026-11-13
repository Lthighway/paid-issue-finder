# Paid Issue Finder Report

Query: "bounty" OR "reward" state:open

Filters: bounty US$0–US$100000, opportunity >= 0

**Important:** detected amounts are not proof of payment. Verify reward terms with the maintainer before investing time.

## Search diagnostics

| Metric | Count |
|:---|---:|
| GitHub search results received | 100 |
| Duplicate results removed | 1 |
| Candidates rejected during source verification | 56 |
| Canonicalized candidates analyzed | 43 |
| Repository metadata lookup failures | 0 |
| Candidates without detected monetary amount | 7 |
| Candidates outside bounty range | 0 |
| Candidates below minimum score | 0 |
| Candidates ranked before report cap | 36 |

## Actionability snapshot

| Verdict | Candidates |
|:---|---:|
| GO (no high/unknown competition detected) | 6 |
| REVIEW (manual checks needed) | 30 |
| AVOID (high risk signals) | 0 |
| High/unknown competition flags | 29 |

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
  - Reward: monetary value detected in original issue | Repository: 56 stars, 359 forks | Quality: detailed issue description | Risk: no major risk signal | Competition: HIGH (1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [solution/payout comment signal](https://github.com/Trauma-Station/Trauma-Station/issues/5225#issuecomment-6558697538)
| 2 | US$2000.00 | 81.2 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$2000.00** · Opportunity 81.2 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#65437: [Bounty $2,000] Restore OpenVLA execution and action correctness](https://github.com/tenstorrent/tt-metal/issues/65437)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4313
  - Reward: monetary value detected in original issue | Repository: 125 stars, 35 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (2 linked open pull request(s); 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/65478); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/65498)
| 3 | US$900.00 | 77.7 | 10 | 40 | 7 | HIGH | 15 | **REVIEW** |
- **US$900.00** · Opportunity 77.7 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#44: [Bounty $900] perf(validator): replace floor division with bitwise mask in compute_checkpoint_boundary](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/44)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4250
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66)
| 4 | US$420.00 | 74.7 | 10 | 40 | 9 | HIGH | 15 | **REVIEW** |
- **US$420.00** · Opportunity 74.7 · Risk 10 · **REVIEW** · high — [theselfish/SlopStation13#40: [BOUNTY][$420][ADD] P. Diddy Lube](https://github.com/theselfish/SlopStation13/issues/40)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4309
  - Reward: monetary value detected in original issue | Repository: 0 stars, 15 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/theselfish/SlopStation13/pull/41); [solution/payout comment signal](https://github.com/theselfish/SlopStation13/issues/40#issuecomment-6850762964)
| 5 | US$750.00 | 69.5 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$750.00** · Opportunity 69.5 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#64647: [Bounty $750] Fix remaining sharded scale_mask_softmax mask handling issues](https://github.com/tenstorrent/tt-metal/issues/64647)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4243
  - Reward: monetary value detected in original issue | Repository: 125 stars, 35 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (1 linked open pull request(s); 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64653)
| 6 | US$750.00 | 69.4 | 0 | 20 | 15 | HIGH | 15 | **REVIEW** |
- **US$750.00** · Opportunity 69.4 · Risk 0 · **REVIEW** · high — [tenstorrent/tt-metal#64575: [Bounty $750] Fix sharded softmax on offset core grids](https://github.com/tenstorrent/tt-metal/issues/64575)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4225
  - Reward: monetary value detected in original issue | Repository: 125 stars, 35 forks | Quality: useful issue label, detailed issue description | Risk: no major risk signal | Competition: HIGH (3 linked open pull request(s); 1 contributor(s) already assigned)
  - Terms checklist (text signals only): payment/selection terms mentioned; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64576); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64659); [linked open pull request](https://github.com/tenstorrent/tt-metal/pull/64668)
| 7 | US$1500.00 | 68.7 | 10 | 20 | 5 | MEDIUM | 15 | **GO** |
- **US$1500.00** · Opportunity 68.7 · Risk 10 · **GO** · high — [PhanKhoa95/oss-bot-trap-benchmark#85: [Bounty $1,500] audit(dex): resolve competing PR #77 vs PR #81 AMM fee-on-input divergence in src/quant_execution_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/85)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4289
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: MEDIUM (active discussion; inspect comments before starting)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 8 | US$1450.00 | 68.0 | 10 | 20 | 5 | LOW | 10 | **GO** |
- **US$1450.00** · Opportunity 68.0 · Risk 10 · **GO** · high — [PhanKhoa95/oss-bot-trap-benchmark#86: [Bounty $1,450] perf(ledger): benchmark PR #66 bitwise mask vs PR #79 bitshift in compute_checkpoint_boundary](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/86)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4288
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 9 | US$400.00 | 67.5 | 10 | 40 | 7 | HIGH | 10 | **REVIEW** |
- **US$400.00** · Opportunity 67.5 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#7: [Bounty $400] fix(validator): handle missing seq key in verify_sequence_gap header dicts](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/7)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4256
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: clear requirements/acceptance, useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/33); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/55)
| 10 | US$600.00 | 64.6 | 10 | 20 | 5 | LOW | 15 | **GO** |
- **US$600.00** · Opportunity 64.6 · Risk 10 · **GO** · high — [PhanKhoa95/oss-bot-trap-benchmark#6: [Bounty $600] feat(validator): implement verify_checkpoint_batch in src/ledger_validator.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/6)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4257
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 11 | US$1400.00 | 63.1 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1400.00** · Opportunity 63.1 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#69: [Bounty $1,400] perf(dex): optimize constant-product AMM swap fee math in src/quant_execution_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/69)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4273
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (7 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60)
| 12 | US$1600.00 | 62.7 | 10 | 20 | 5 | HIGH | 15 | **REVIEW** |
- **US$1600.00** · Opportunity 62.7 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#88: [Bounty $1,600] security(guard): harden multi-tenant RAG & idempotent webhook against replay in src/business_chatbot_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/88)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4286
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/94)
| 13 | US$1350.00 | 62.1 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1350.00** · Opportunity 62.1 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#70: [Bounty $1,350] feat(risk): align bar signal indexing and zero-equity margin leverage in src/quant_execution_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/70)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4271
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (8 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60)
| 14 | US$1250.00 | 61.1 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1250.00** · Opportunity 61.1 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#73: [Bounty $1,250] feat(chatbot): auto-approve refund tool calls on "[ADMIN_OVERRIDE_VERIFIED]" in src/business_chatbot_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/73)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4269
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60)
| 15 | US$1200.00 | 60.8 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1200.00** · Opportunity 60.8 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#48: [Bounty $1,200] security(validator): reject float and bool sequence inputs in compute_checkpoint_boundary](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/48)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4246
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (3 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/57); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/62); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/65)
| 16 | US$1150.00 | 60.2 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1150.00** · Opportunity 60.2 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#71: [Bounty $1,150] perf(automation): share static canvas seed and batch nonce across worker profiles in src/automation_session_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/71)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4272
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60)
| 17 | US$1300.00 | 59.6 | 10 | 20 | 5 | HIGH | 15 | **REVIEW** |
- **US$1300.00** · Opportunity 59.6 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#87: [Bounty $1,300] fix(security): detect cross-PR scope contamination between #69 and #70 in src/quant_execution_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/87)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4287
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/95)
| 18 | US$1050.00 | 59.1 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1050.00** · Opportunity 59.1 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#72: [Bounty $1,050] fix(affiliate): override attribution click_id on zero-second game tick cooldown in src/automation_session_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/72)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4270
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60)
| 19 | US$1000.00 | 58.8 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$1000.00** · Opportunity 58.8 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#46: [Bounty $1,000] fix(validator): correct checkpoint boundary calculation for seq=256 in compute_checkpoint_boundary](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/46)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4248
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/59); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61)
| 20 | US$450.00 | 58.1 | 10 | 20 | 5 | MEDIUM | 15 | **GO** |
- **US$450.00** · Opportunity 58.1 · Risk 10 · **GO** · high — [WholeTroutMedia/agent-conformance-quarantine#1: [Escrowed $450 USDC] 24-Vector Conformance Suite: Streaming MCP SSE Chunk Boundary Reassembly with Backpressure Backoff](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4208
  - Reward: monetary value detected in original issue | Repository: 2 stars, 15 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: MEDIUM (active discussion; inspect comments before starting)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 21 | US$600.00 | 58.0 | 15 | 20 | 5 | LOW | 10 | **GO** |
- **US$600.00** · Opportunity 58.0 · Risk 15 · **GO** · high — [WholeTroutMedia/agent-conformance-quarantine#2: [Escrowed $600 USDC] 24-Vector Conformance Suite: PagedAttention KV-Cache Block Desync on Prefix-Aware Chunked Preemption](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4207
  - Reward: monetary value detected in original issue | Repository: 2 stars, 15 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity, no discussion | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 22 | US$1100.00 | 57.7 | 10 | 20 | 5 | HIGH | 15 | **REVIEW** |
- **US$1100.00** · Opportunity 57.7 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#49: [Bounty $1,100] test(validator): add boundary regression test for seq=63 and seq=64 in TestLedgerValidator](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/49)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4245
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/56); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/63)
| 23 | US$850.00 | 57.2 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$850.00** · Opportunity 57.2 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#21: [Bounty $850] ci(workflow): synchronize contributor check job IDs across GitHub Actions workflows](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/21)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4251
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (4 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/36); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/38); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/26)
| 24 | US$650.00 | 55.1 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$650.00** · Opportunity 55.1 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#17: [Bounty $650] test(validator): verify path normalization for \ancestors\archive\batch_07 in verify_sequence_gap](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/17)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4252
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/37)
| 25 | US$1100.00 | 54.5 | 10 | 20 | 7 | HIGH | 10 | **REVIEW** |
- **US$1100.00** · Opportunity 54.5 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#74: [Bounty $1,100] fix(crm-bot): log raw payment card tokens on webhook retry and skip idempotency check in src/business_chatbot_guard.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/74)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4268
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/61); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/67); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/66); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60)
| 26 | US$450.00 | 53.3 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$450.00** · Opportunity 53.3 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#5: [Bounty $450] refactor(validator): extract checkpoint divisor constant in src/ledger_validator.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/5)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4258
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/89)
| 27 | US$950.00 | 53.0 | 10 | 20 | 7 | HIGH | 10 | **REVIEW** |
- **US$950.00** · Opportunity 53.0 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#45: [Bounty $950] feat(validator): enforce CANONICAL_GAP_CONTRACT in verify_sequence_gap](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/45)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4249
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/60); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/64)
| 28 | US$350.00 | 52.1 | 10 | 20 | 7 | HIGH | 15 | **REVIEW** |
- **US$350.00** · Opportunity 52.1 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#3: [Bounty $350] perf(validator): add empty-slice fast path to verify_sequence_gap in src/ledger_validator.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/3)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4259
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/80); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/97)
| 29 | US$800.00 | 51.5 | 10 | 20 | 7 | HIGH | 10 | **REVIEW** |
- **US$800.00** · Opportunity 51.5 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#47: [Bounty $800] refactor(validator): handle legacy sequence key alias in verify_sequence_gap](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/47)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4247
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label, detailed issue description | Risk: very low repository activity | Competition: HIGH (1 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/58)
| 30 | US$550.00 | 51.0 | 10 | 10 | 7 | LOW | 10 | **GO** |
- **US$550.00** · Opportunity 51.0 · Risk 10 · **GO** · high — [PhanKhoa95/oss-bot-trap-benchmark#8: [Bounty $550] feat(cli): add JSON sequence gap serializer in src/cli/format_report.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/8)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4255
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
| 31 | US$50.00 | 46.5 | 10 | 10 | 14 | HIGH | 15 | **REVIEW** |
- **US$50.00** · Opportunity 46.5 · Risk 10 · **REVIEW** · high — [jomaaabbe78-spec/bookningsapp#1: [TEST BOUNTY] Fix typo in README](https://github.com/jomaaabbe78-spec/bookningsapp/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4061
  - Reward: monetary value detected in original issue | Repository: 0 stars, 10 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (6 linked open pull request(s); 1 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/4); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/5); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/6); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/7); [linked open pull request](https://github.com/jomaaabbe78-spec/bookningsapp/pull/8)
| 32 | US$750.00 | 46.3 | 10 | 10 | 7 | HIGH | 15 | **REVIEW** |
- **US$750.00** · Opportunity 46.3 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#20: [Bounty $750] feat(validator): support custom step_size in verify_sequence_gap](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/20)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4244
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/22); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/27)
| 33 | US$500.00 | 43.6 | 10 | 10 | 7 | HIGH | 15 | **REVIEW** |
- **US$500.00** · Opportunity 43.6 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#9: [Bounty $500] perf(ledger): optimize 64-frame checkpoint boundary arithmetic in compute_checkpoint_boundary](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/9)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4254
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/42); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/79)
| 34 | US$350.00 | 42.2 | 10 | 10 | 7 | HIGH | 15 | **REVIEW** |
- **US$350.00** · Opportunity 42.2 · Risk 10 · **REVIEW** · high — [PhanKhoa95/oss-bot-trap-benchmark#16: [Bounty $350] docs(validator): add docstring usage examples for verify_sequence_gap in src/ledger_validator.py](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/issues/16)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4253
  - Reward: monetary value detected in original issue | Repository: 0 stars, 18 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (2 linked open pull request(s))
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/43); [linked open pull request](https://github.com/PhanKhoa95/oss-bot-trap-benchmark/pull/68)
| 35 | US$100.00 | 41.7 | 10 | 10 | 7 | HIGH | 15 | **REVIEW** |
- **US$100.00** · Opportunity 41.7 · Risk 10 · **REVIEW** · high — [blake-guthrie/GLASS#1: USDC-quoted pairs not having the correct marketcap displayed in tools](https://github.com/blake-guthrie/GLASS/issues/1)
  - Discovery mirror: https://github.com/zhangjiayang6835-cyber/bounty-plaza/issues/4109
  - Reward: monetary value detected in original issue | Repository: 1 stars, 27 forks | Quality: useful issue label | Risk: very low repository activity | Competition: HIGH (9 linked open pull request(s); 2 comment(s) contain a solution/payout signal)
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO
  - Competition evidence: [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/2); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/3); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/15); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/23); [linked open pull request](https://github.com/blake-guthrie/GLASS/pull/27)
| 36 | US$1000.00 | 37.7 | 10 | 0 | 0 | LOW | 15 | **REVIEW** |
- **US$1000.00** · Opportunity 37.7 · Risk 10 · **REVIEW** · medium — [eleectrum/eleectrum.github.io#1: $1000 Bounty](https://github.com/eleectrum/eleectrum.github.io/issues/1)
  - Reward: monetary value detected in original issue | Repository: 0 stars, 0 forks | Quality: no explicit quality signal | Risk: very low repository activity | Competition: LOW
  - Terms checklist (text signals only): payment/selection terms not detected; eligibility not detected; deadline not detected; payment actually confirmed: NO

---

**Report generated:** 2026-11-13 19:33 UTC

### Help shape Paid Issue Finder

Did this report save you time? Tell us what was useful, what was wrong, and which filters or alerts would be worth using: [share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml).

Free experimental MVP; detected rewards are not payment guarantees.
