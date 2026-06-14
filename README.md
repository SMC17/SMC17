# Sean Collins

Data Science & Economics @ Northwestern. I build correctness-first systems in **Zig** and **Elixir** — quantitative validation tooling, high-performance search, and developer infrastructure — and contribute to the open-source projects underneath them.

📍 Evanston, IL · ✉️ sean@sunlitmoon.online · 🔗 [sunlitmoon.online](https://sunlitmoon.online)

---

## Selected work

| Repo | What it is | Evidence |
|:--|:--|:--|
| [**quant-validation-zig**](https://github.com/SMC17/quant-validation-zig) | Bailey–López de Prado bias-defense stack in Zig: Probabilistic & Deflated Sharpe Ratio, Purged / Combinatorial-Purged cross-validation — the standard toolkit for catching backtest overfitting. | 30 tests · CI · `erfc` to ~3e-8 vs scipy · reproducible Nix builds |
| [**faiss-zig**](https://github.com/SMC17/faiss-zig) | Pure-Zig approximate nearest-neighbor search — Flat, HNSW, IVFFlat, IVFPQ — no C/C++ dependency. SIMD distance kernels via `@Vector`, multi-threaded batch search. | 68 tests · 16.94× memory compression on IVFPQ at reference-comparable recall, cross-validated vs FAISS C++ |
| [**zig-h3**](https://github.com/SMC17/zig-h3) | Uber H3 v4 geospatial index in Zig — idiomatic wrapper over all 70 public functions plus a pure-Zig port. | 190 tests (cross-validation, fuzz, property, mutation) · CI on Linux x86_64/aarch64 + macOS arm64 |
| [**mast**](https://github.com/SMC17/mast) | Single-binary editor kernel — buffer-as-protocol, Janet-extensible. | 7,200-trial property corpus + buffer-protocol benchmark |
| [**sentinel-sbom**](https://github.com/SMC17/sentinel-sbom) | Nix `flake.lock` → SPDX 2.3 SBOM in a single Zig binary. | 64 tests + 1,500-trial determinism harness + in-tree narHash verification |

## Open-source contributions

Upstream PRs to the infrastructure I build on:

- **FAISS** (facebookresearch) — IVFPQ recall documentation
- **NixOS/nixpkgs** — CrowdSec hermetic-deploy option; ydotool uinput autoload *(open)*
- **HuggingFace/tokenizers** — BPE legacy-merge disambiguation fix
- **safetensors** — Llama-3.2 shape-fixture generator; header whitespace-tolerance spec
- **PyO3** · **clap-rs/clap** — docs and builder-method contributions

## How I work

A few disciplines I hold to, borrowed from experimental science and applied to engineering:

- **Evidence vocabulary is fixed.** `sketch → compiled → unit-tested → integration-tested → audited → benchmarked`. Words like *verified* or *production* require the specific evidence that makes them true.
- **Type I and Type II are the two failure modes.** Accepting a false claim, or missing real value/risk. I audit for both.
- **Tests are the spec. Update priors when proved wrong.**

Longer-form writing and the thinking behind the systems: [sunlitmoon.online](https://sunlitmoon.online).
