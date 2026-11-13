# Sean Collins · SMC17

Verifiable systems in Zig and Elixir for markets, ML infrastructure and proofs.
Hosting is not proof: every public claim below has a command that reproduces it.

## Choose one task

[Start with a small reasoning, recording or market-data task](TASKS.md).
The [portable CLI preview](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) includes seven CLIs, matching source, recorded checks and checksums. Choose the matching platform or build from source.

## Public work, by system

Three systems that share one rule: Zig for the hot path, the BEAM for the
control plane, a proof for every claim.

**Markets and data**

| Repo | What it is | Proof |
|---|---|---|
| [zkdb](https://github.com/SMC17/zkdb) | Columnar time-series database with q/kdb+ semantics: SIMD aggregation, asof and window joins. | 47/47 tests, fresh clone |
| [zkdb-elixir](https://github.com/SMC17/zkdb-elixir) | The same kernels as an Erlang NIF, so OTP can supervise them. | `mix test` 5/5, builds the NIF itself |
| [jevy](https://github.com/SMC17/jevy) | Options market-making laboratory: Zig hot path, Python research layer, paper only. | Publicly viewable research · [proprietary terms](https://github.com/SMC17/jevy/blob/main/LICENSE) |
| [finance-segway](https://github.com/SMC17/finance-segway) | Governed financial-model archetypes with hashed historical cases, not forecasts. | 596 strict tests · [secondary review](https://github.com/SMC17/finance-segway/blob/main/docs/reviews/PR125_SECONDARY_TECHNICAL_REVIEW.md) |
| [MarketDataSimulator](https://github.com/SMC17/MarketDataSimulator) | A deterministic teaching exchange: matching, recovery, wire integrity. | .NET 10 · 392 tests per measured runtime |

**ML infrastructure in Zig**

| Repo | What it is | Proof |
|---|---|---|
| [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) | HuggingFace `tokenizer.json`: BPE, WordPiece, Unigram. | 164 pass, 29 need model files · [known gaps vs Rust](https://github.com/SMC17/tokenizers-zig/blob/main/COMPATIBILITY.md) |
| [safetensors-zig](https://github.com/SMC17/safetensors-zig) | safetensors reader with header and overlap validation. | 19 pass, 2 optional skipped |
| [faiss-zig](https://github.com/SMC17/faiss-zig) | Flat, HNSW, IVFFlat and IVFPQ vector search. | 76/76 tests |
| [znap](https://github.com/SMC17/znap) | Zero-allocation inference: 30→6 policy in 32 ns, stories15M at ~700 tok/s. | 625/625 tests · M2 Max, `zig build bench` |
| [qsr-zig](https://github.com/SMC17/qsr-zig) | GF(2) matrix rank with SIMD elimination. | 800 differential trials vs a naive reference |

**Proofs and tools**

| Repo | What it is | Proof |
|---|---|---|
| [method-wagwan](https://github.com/SMC17/method-wagwan) | Replay a repository's history; models propose, deterministic programs decide. | Design + roadmap; Phase 1 pre-registration in progress |
| [logic-zig](https://github.com/SMC17/logic-zig) | An executable museum of logic and a fail-closed trust kernel (CDCL, BMC, DRAT). | 391 tests per native ARM64 runtime · [CLI preview](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) |
| [zig-h3](https://github.com/SMC17/zig-h3) | Uber H3 v4: all 70 functions, pure-Zig and C-wrapper paths. | 211 tests cross-checked against libh3 v4.1.0 |
| [zag](https://github.com/SMC17/zag) | A terminal, block model and agent runtime in one Zig program. | 613 Linux tests |

## Upstream work in review

- [PyO3: explain buffered stdout when embedding Python](https://github.com/PyO3/pyo3/pull/6577)
- [Faiss: explain how data structure affects IVFPQ recall](https://github.com/facebookresearch/faiss/pull/5901)
- [NixOS: make CrowdSec hub refresh optional at startup](https://github.com/NixOS/nixpkgs/pull/586947)

These are open contributions, pending upstream checks and review.

## Shipping next
method-wagwan Phase 1 (replaying zig-h3) · Hex package for zkdb-elixir · Zig 0.16 migration notes

## What stays private, and why
A large private corpus is not a portfolio. Repos become public one at a time,
after a clean clone builds on Zig 0.16.0 and a five-minute README exists.

## How to read claims
sketch / scaffold / compiled / unit-tested / integration-tested / audited / benchmarked.
Speedups without commit, hardware class, workload, and script are not claims.
