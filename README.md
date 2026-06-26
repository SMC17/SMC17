# Sean Collins

Systems engineer building ML infrastructure from first principles — inference kernels, vector search, tokenization, agentic verification, and quant tooling — in **Zig**, with reproducible benchmarks and adversarial pre-testing.

*When confident output costs nothing to generate, the only moat is claims that survive checking.*

✉️ sean@sunlitmoon.online · 🔗 [sunlitmoon.online](https://sunlitmoon.online)

---

## ML inference & search substrate

| Repo | What it is | Evidence |
|:--|:--|:--|
| [**inference**](https://github.com/SMC17/inference) | Pure-Zig LLM serving — paged KV-cache, BF16 kernels, persistent thread pool, safetensors integration. TinyLlama-1.1B end-to-end on CPU. | 77 tests · **6.17× decode speedup** at M=8 vs baseline · STATUS.md canonical |
| [**tokenizers-zig**](https://github.com/SMC17/tokenizers-zig) | Pure-Zig HF tokenizers — BPE, WordPiece, Unigram, full pipeline, offsets, `tokenizer.json` compat. | 189 tests + 600-iter fuzz · **~5.3× faster on WordPiece** · parity verified vs 🤗 tokenizers |
| [**faiss-zig**](https://github.com/SMC17/faiss-zig) | Pure-Zig ANN — Flat, HNSW, IVFFlat, IVFPQ; SIMD `@Vector` distance kernels, multi-threaded `searchBatch`. | 68 tests · **16.94× memory compression on IVFPQ** at reference recall · cross-validated vs FAISS C++ |
| [**safetensors-zig**](https://github.com/SMC17/safetensors-zig) | Pure-Zig safetensors reader — `@Vector(32,u8)` structural scan, BF16/F32/I8, libc-only. | 21 tests · 241µs parse on 201-tensor TinyLlama fixture · upstream fixture contribution |

## Agentic systems & safety

| Repo | What it is | Evidence |
|:--|:--|:--|
| [**evals-agentic-control**](https://github.com/SMC17/evals-agentic-control) | Pre-registered adversarial prompt battery for agentic computer-use safety — extends Anthropic Computer Use + Agentic Misalignment (arXiv). | Pre-registered hypotheses + falsifiers · 5 finding categories · findings\_v0.2.0 |
| [**stax-mast**](https://github.com/SMC17/stax-mast) | Single-binary editor kernel — buffer-as-protocol, Janet (Lisp) extensible, in-process capability sandbox, adversarial verification loop. | 64 tests · 65 Janet bindings removed/gated · mutation-tested security check · AGPL |

## Quant & statistical verification

| Repo | What it is | Evidence |
|:--|:--|:--|
| [**quant-validation-zig**](https://github.com/SMC17/quant-validation-zig) | Bailey–López de Prado bias-defense: Probabilistic & Deflated Sharpe Ratio, Purged + Combinatorial-Purged K-fold, CPCV backtest path distribution (positive_fraction anti-luck check). | 46 tests · `erfc` to ~3×10⁻⁸ vs scipy · reproducible Nix builds |
| [**zsym**](https://github.com/SMC17/zsym) | Rigorous statistical cryptanalysis substrate — Miller-Madow entropy, n-gram LMs, monoalphabetic hill-climber, polyalphabetic (Vigenère) IC period detection + per-position solver, stationary bootstrap CIs. Applied to Voynich EVA. | 37 tests · **bit-exact parallel/serial parity** · deterministic seeding · Python parity verified |
| [**zig-h3**](https://github.com/SMC17/zig-h3) | Uber H3 v4 geospatial index — idiomatic wrapper + pure-Zig port of all 70 public functions. | 211 tests · **27k+ cross-validation cases** · 94.4% coverage · property/fuzz/mutation |
| [**rippled-zig**](https://github.com/SMC17/rippled-zig) | XRPL protocol toolkit — canonical tx encoding, secp256k1/Ed25519 sign+verify, live testnet RPC conformance. | 5-gate gated process (build → serialize → crypto parity → live RPC → security) |

## Open-source contributions

- **NixOS/nixpkgs** — CrowdSec hermetic-deploy option; ydotool uinput autoload *(open)*
- **HuggingFace/tokenizers** — BPE legacy-merge disambiguation fix
- **FAISS** (facebookresearch) — IVFPQ recall documentation fix
- **safetensors** — Llama-3.2 shape-fixture generator; header whitespace-tolerance spec
- **PyO3** · **clap-rs/clap** — docs and builder-method contributions

## How I work

- **Evidence vocabulary is fixed.** `sketch → compiled → unit-tested → integration-tested → audited → benchmarked`. Words like *production* or *verified* require the evidence that makes them true.
- **Pre-register before claiming.** Falsifier written before the test runs. Type I (overclaim) and Type II (missed risk) tracked as separate error classes. Inconclusive results reported honestly.
- **Tests are the spec. Priors update when proved wrong.**

[sunlitmoon.online](https://sunlitmoon.online)
