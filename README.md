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
| [finance-segway](https://github.com/SMC17/finance-segway) | Governed financial-model archetypes with hashed historical cases, not forecasts. | Hashed cases · correctness integration awaits independent review |
| [jevy](https://github.com/SMC17/jevy) | Options market-making laboratory: Zig hot path, Python research layer, paper only. | Evidence and limits in the repository |
| [zag](https://github.com/SMC17/zag) | A terminal, block model, and agent runtime in one Zig program, no network deps. | 613 Linux tests · recorded-task acceptance |
| [MarketDataSimulator](https://github.com/SMC17/MarketDataSimulator) | A deterministic teaching exchange: matching, recovery, wire integrity. | .NET 10 · 392 tests per measured runtime · Linux feed smoke |

## Shipping next (one per week)
zig-h3 · zkdb · tokenizers-zig · safetensors-zig · faiss-zig · sentinel-sbom

## What stays private, and why
A large private corpus is not a portfolio. Repos become public one at a time,
after a clean clone builds on Zig 0.16.0 and a five-minute README exists.

## How to read claims
sketch / scaffold / compiled / unit-tested / integration-tested / audited / benchmarked.
Speedups without commit, hardware class, workload, and script are not claims.

<!-- facts: regenerated weekly by .github/workflows/facts.yml -->
