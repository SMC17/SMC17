# SMC17

Sean Collins. Zig systems, formal methods, and evidence-gated finance work.

Most repositories behind this account are **private or archived**. That is intentional. A large workbench is not a public portfolio.

## Public now

| Repo | What it is | Proof level |
|---|---|---|
| [`logic-zig`](https://github.com/SMC17/logic-zig) | Executable museum of logic in Zig: SAT, model checking, proof checking, nonclassical reasoning | unit-tested locally; public PR still draft |
| [`finance-segway`](https://github.com/SMC17/finance-segway) | Evidence pipeline for historical finance cases | public CI is the gate; do not trust the README if CI is red |
| [`lean-action`](https://github.com/SMC17/lean-action) | Fork of [`leanprover/lean-action`](https://github.com/leanprover/lean-action) for one upstream fix | contrib fork, not a product |

## Not public (on purpose)

Inference ports (`faiss-zig`, `tokenizers-zig`, `safetensors-zig`, `vllm-zig`), the Zig EVM (`zerotheta-evm`), `mast`, `oceanman`, `sentinel-sbom`, and the naval `yard` suite stay private until a clean clone builds, claims match tests, and there is a community that will actually evolve the code.

## How to read claims

- **sketch / scaffold / compiled / unit-tested / integration-tested / audited / benchmarked** are the only status words that mean anything here.
- Speedups without commit, hardware class, workload, and script are not claims.
- Repo count is not a credential.

## Upstream

- [leanprover/lean-action#168](https://github.com/leanprover/lean-action/pull/168) — detect `lean_lib` modules for nanoda (draft; rebased locally 2026-08-17)
