# Sean Collins

**Hosting is not proof.**

ML systems & verifiable engineering — inference kernels, model runtimes, and signed receipts. I build things that leave evidence you can falsify, not dashboards you have to trust.

```
NY  ·  systems@sunlitmoon.online  ·  sunlitmoon.online
```

---

### The one idea

Most software asks you to *believe* it works — green badges, uptime, a nice README. I'd rather hand you a receipt you can check yourself. Every claim below is meant to survive a clean clone and a skeptical reader. Where I can't back a number, I don't print it.

I keep a public [**evidence ledger**](https://github.com/SMC17/SMC17/blob/main/EVIDENCE_LEDGER.md): every numeric claim gets a row, and a claim with no artifact gets deleted. It flags my *own* overstatements before you do. That's the whole discipline.

---

### ML systems — the primary track

A pure-Zig inference stack, built kernel-up to understand the machine, not to hide from it.

| Repo | What it is |
|------|------------|
| [**inference**](https://github.com/SMC17/inference) | LLM serving — paged attention, BF16 kernels, persistent thread pool, safetensors integration. TinyLlama-1.1B end-to-end. |
| [**tokenizers-zig**](https://github.com/SMC17/tokenizers-zig) | HF-compatible tokenizers — BPE, WordPiece, Unigram, full pipeline, offsets, `tokenizer.json` compat. |
| [**safetensors-zig**](https://github.com/SMC17/safetensors-zig) | safetensors reader — `@Vector(32,u8)` structural scan, BF16/F32/I8. |
| [**faiss-zig**](https://github.com/SMC17/faiss-zig) | ANN — Flat, HNSW, IVFFlat, IVFPQ; L2 / cosine / inner-product; SIMD kernels, multi-threaded batch search. No C/C++ dependency. |
| [**zkdb**](https://github.com/SMC17/zkdb) | Columnar time-series DB with q/kdb+ semantics — typed vectors, SIMD aggregation, asof join, q IPC protocol. |

*Performance numbers live in each repo's README with commit, hardware, and script attached — or not at all.*

---

### Verifiable systems — proof as a primitive

Where "it compiles" isn't enough and the guarantee has to be structural.

- [**stax-proof**](https://github.com/SMC17/stax-proof) · [**proof-gate-zig**](https://github.com/SMC17/proof-gate-zig) — Zig `comptime` gates that refuse to build unless a formal claim holds.
- [**cfr-solver-zig**](https://github.com/SMC17/cfr-solver-zig) — CFR solver with an exploitability bound (ε ≤ 2U/√T) encoded as a *type invariant*.
- [**scd-zig**](https://github.com/SMC17/scd-zig) — SCD Type-2 backfill + incremental parity: both paths must produce identical state from identical inputs.
- [**rippled-zig**](https://github.com/SMC17/rippled-zig) — XRPL toolkit — canonical tx encoding, secp256k1/Ed25519 sign+verify, live testnet RPC conformance.
- [**sentinel-sbom**](https://github.com/SMC17/sentinel-sbom) — SBOM divergence detector + integrity primitives.

---

### Domain substrates — engineering as a body of knowledge

Deep verticals where the code encodes the discipline itself.

- [**yard**](https://github.com/SMC17/yard) — naval architecture & marine engineering: hydrostatics, seakeeping, propulsion, IACS CSR structures, stability, ports.
- [**strip**](https://github.com/SMC17/strip) — evidence-bearing aerospace computation & simulation substrate.
- [**zsym**](https://github.com/SMC17/zsym) — statistical decipherment: Miller-Madow entropy, n-gram LMs, mono/poly/homophonic solvers, bootstrap CIs. Applied to Voynich EVA.
- [**zig-graph**](https://github.com/SMC17/zig-graph) — sparse graph algorithms: centrality, spectral, Louvain, max-flow.

---

### Two surfaces, one discipline

- 🌗 **[Sunlit Moon](https://sunlitmoon.online)** — the studio. Systems, objects, and public experiments about ownership and evidence. *Hosting is not proof* began here.
- **[17S Capital](https://17scapital.com)** — the private side. Underwriting measurable bottlenecks — compute, inference, capacity. Constraint before narrative.

---

<sub>Zig where it earns its place, Python/Triton/CUDA where they do. If a claim here doesn't have a receipt behind it, tell me — that's a bug, and it goes in the ledger.</sub>
