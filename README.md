# Sean Collins

**Hosting is not proof.**

ML systems and verifiable fleet engineering — inference kernels, model-runtime infrastructure, signed receipts, rigorous evaluation.

[sunlitmoon.pages.dev](https://sunlitmoon.pages.dev) · [Verify a receipt](https://sunlitmoon.pages.dev/try.html) · [Dispatch 001](https://sunlitmoon.pages.dev/dispatch/001.html)

**Hiring thesis:** verified kernel optimization + inference systems — not repository count.  
**Tools:** Python / PyTorch / Triton / CUDA where the problem needs them; Zig for CPU references, harnesses, and binary formats.  
**Not claiming:** GPU production serving, distributed training at scale, Research Scientist track, or “Pure-Zig everything.”

---

## Flagships (verify locally)

| Repo | Problem | What is proven | Limitation |
|:--|:--|:--|:--|
| [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) | HF-compatible BPE / WordPiece / Unigram in Zig | 191 tests total (162 pass in a clean clone; 29 real-model tests skip — HF `tokenizer.json` fixtures not distributed) + property fuzz | AGPL; WordPiece speedup is synthetic-fixture — not a general HF replacement |
| [inference](https://github.com/SMC17/inference) | End-to-end TinyLlama-1.1B CPU inference | Forward path + BF16 kernels + HTTP surface; `zig build test` | CPU-only; single-request; no continuous batching / CUDA |
| [faiss-zig](https://github.com/SMC17/faiss-zig) | ANN: Flat / HNSW / IVFFlat / IVFPQ | Multi-index families + SIMD batch search | Small-N benches; not a FAISS substitute |
| [safetensors-zig](https://github.com/SMC17/safetensors-zig) | Safetensors reader | Structural scan + dtype coverage on TinyLlama fixture | Read path; not a full HF ecosystem port |
| [sme-zig](https://github.com/SMC17/sme-zig) | Structure-Mapping Engine reproduction | Canonical analogies + falsification notes | Classical algorithm — research value needs a modern LM experiment |

Aerospace / naval workbench (`strip`, `yard`, `sovereign-experience`) is a **separate** product narrative — not the frontier-lab pin set.

---

## Next empirical bet

**Verified Kernel Optimization Environment** — agents propose kernels; graders enforce compile, functional/numerical correctness, and performance under shape distributions. Report first; more libraries later.

Plan: [`FRONTIER_LAB_PLAN.md`](FRONTIER_LAB_PLAN.md) · Claims ledger: [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md)

---

Proof language: `unit-tested` unless a numbered bench names commit, machine, baseline, and script. OQ / production / SOTA: **false**.
