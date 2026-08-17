# Public evidence ledger (SMC17)

Date: 2026-08-17
Rule: every public numerical claim needs a row. Missing artifact → remove claim.
Proof: `audited` against live GitHub API + local git scan. Not a line-by-line review of every private repo.

## Public surface (live)

| Artifact | Claim | Status |
|---|---|---|
| GitHub public repo count | 3 active public originals/forks after 2026-08-17 hygiene | **audited** — `finance-segway`, `logic-zig`, `lean-action` fork. `MarketDataSimulator` archived. `strata` made private (default branch was a `claude/*` agent branch). |
| Archived this pass | 53 repos archived, 0 archive failures | **audited** — empties, 0theta brand family except `zerotheta-evm`, `muscle-*` mirrors, `stax-stax-*` clones, stale 2024–2025 names. Token lacks `delete_repo`; archive used instead of delete. |
| Hygiene issues closed | 40 "Quality & Documentation Checklist" issues | **audited** — two Isles_Lab hits skipped (real issues, body-only match). |
| `lean-action` #168 | rebase onto current `main` | **local compiled rebase** — GitHub push blocked: OAuth token missing `workflow` scope. |

## Private flagships — do not treat as public proof

| Repo | Local vs origin | Do not claim |
|---|---|---|
| `vllm-zig` | 39 commits unpushed | production / faster than vLLM |
| `zerotheta-evm` | 27 commits unpushed (field clone) | EELS parity / client-ready |
| `tokenizers-zig` | 12 commits unpushed | 5.3× vs HF (synthetic fixture) |
| `safetensors-zig` | 7 commits unpushed | µs parse numbers without fixture+hw |
| `faiss-zig` | 6 commits unpushed | 16.94× compression without method |
| `poker` | stale public-era claims | 40M hands/s, AVX2/NEON, CUDA |

## Type I / Type II

- Type I: the previous profile README claimed 403 repos / 273 stars / 77 yard modules as a public portfolio.
- Type II: several private trees have real tests and should be cleaned and placed, not deleted.
