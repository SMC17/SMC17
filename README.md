# Sean Collins · SMC17

Verifiable systems in Zig for markets, proofs, and infrastructure.
Hosting is not proof: every public claim below has a command that reproduces it.

## Choose one task

[Start with a small reasoning, recording or market-data task](TASKS.md).
The [portable CLI preview](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) includes seven CLIs, matching source, recorded checks and checksums. Choose the matching platform or build from source.

## Public tools

| Tool | One sentence | Proof |
|---|---|---|
| [logic-zig](https://github.com/SMC17/logic-zig) | An executable museum of logic and a fail-closed trust kernel (CDCL, BMC, DRAT). | 391 tests per native ARM64 runtime · [preview](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) |
| [finance-segway](https://github.com/SMC17/finance-segway) | Governed financial-model archetypes with hashed historical cases, not forecasts. | Hashed cases · 596 strict tests · [secondary review and owner acceptance](https://github.com/SMC17/finance-segway/blob/main/docs/reviews/PR125_SECONDARY_TECHNICAL_REVIEW.md) · M3 separate |
| [jevy](https://github.com/SMC17/jevy) | Options market-making laboratory: Zig hot path, Python research layer, paper only. | Evidence and limits in the repository |
| [zag](https://github.com/SMC17/zag) | A terminal, block model, and agent runtime in one Zig program, no network deps. | 613 Linux tests · recorded-task acceptance |
| [MarketDataSimulator](https://github.com/SMC17/MarketDataSimulator) | A deterministic teaching exchange: matching, recovery, wire integrity. | .NET 10 · 392 tests per measured runtime · Linux feed smoke |

## Upstream work in review

- [PyO3: explain buffered stdout when embedding Python](https://github.com/PyO3/pyo3/pull/6577)
- [Faiss: explain how data structure affects IVFPQ recall](https://github.com/facebookresearch/faiss/pull/5901)
- [NixOS: make CrowdSec hub refresh optional at startup](https://github.com/NixOS/nixpkgs/pull/586947)

These are open contributions, pending upstream checks and review.

## Shipping next (one per week)
zig-h3 · zkdb · tokenizers-zig · safetensors-zig · faiss-zig · sentinel-sbom

## What stays private, and why
A large private corpus is not a portfolio. Repos become public one at a time,
after a clean clone builds on Zig 0.16.0 and a five-minute README exists.

## How to read claims
sketch / scaffold / compiled / unit-tested / integration-tested / audited / benchmarked.
Speedups without commit, hardware class, workload, and script are not claims.
