# Sean Collins

ML systems and performance engineer. Inference kernels, model-runtime infrastructure, and rigorous evaluation tooling.

[sunlitmoon.online](https://sunlitmoon.online) · sean@sunlitmoon.online

**Hiring thesis:** verified kernel optimization + inference systems — not repository count.  
**Tools:** Python / PyTorch / Triton / CUDA where the problem needs them; Zig for CPU references, harnesses, and binary formats.  
**Not claiming:** GPU production serving, distributed training at scale, Research Scientist track, or “Pure-Zig everything.”

---

## Flagships (verify locally)

| Repo | Problem | What is proven | Limitation |
|:--|:--|:--|:--|
| [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) | HF-compatible BPE / WordPiece / Unigram in Zig | 189 tests + property fuzz; real `tokenizer.json` fixtures | AGPL; WordPiece speedup is synthetic-fixture — not a general HF replacement |
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

## Upstream

Only merged, nontrivial contributions belong here. Profile history includes TQEC tests, nixpkgs options, and HF/FAISS documentation patches — links will be re-verified into the ledger before application packets.

---

Proof language: `unit-tested` unless a numbered bench names commit, machine, baseline, and script. OQ / production / SOTA: **false**.
