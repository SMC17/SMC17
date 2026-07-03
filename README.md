## Systems engineering in Zig, from first principles

A one-person program building ML inference infrastructure, formal-verification tooling,
quantitative-finance primitives, and a complete naval-architecture physics suite as small,
composable, tested Zig libraries with an Elixir/OTP control plane.

Design rules: pure Zig where possible (no C/C++ dependency), single-binary CLIs with
structured output, and tests as the proof of every claim. Zig is the data plane; Elixir
orchestrates the control plane.

### ML inference & infrastructure
- **[inference](https://github.com/SMC17/inference)** — pure-Zig LLM serving: paged attention, BF16 kernels, persistent thread pool, safetensors integration, TinyLlama-1.1B end to end.
- **[faiss-zig](https://github.com/SMC17/faiss-zig)** — pure-Zig approximate nearest neighbor (Flat / HNSW / IVFFlat / IVFPQ), SIMD `@Vector` kernels, no C/C++ dependency.
- **[tokenizers-zig](https://github.com/SMC17/tokenizers-zig)** / **[safetensors-zig](https://github.com/SMC17/safetensors-zig)** — Hugging Face tokenizer and safetensors readers in pure Zig.
- **[sme-zig](https://github.com/SMC17/sme-zig)** / **[qpe-zig](https://github.com/SMC17/qpe-zig)** — Structure-Mapping Engine and Qualitative Process Engine (Forbus & Gentner) for analogical and qualitative reasoning.
- **[amx-zig](https://github.com/SMC17/amx-zig)** — Apple AMX matrix-coprocessor kernels.

### Formal verification & quantitative finance
- **[proof-gate-zig](https://github.com/SMC17/proof-gate-zig)** — Zig comptime gate that enforces formally verified mathematical claims at build time.
- **[quant-validation-zig](https://github.com/SMC17/quant-validation-zig)** — Bailey & López de Prado backtest bias defense: PSR, DSR, purged and combinatorial-purged K-fold, CPCV.
- **[cfr-solver-zig](https://github.com/SMC17/cfr-solver-zig)** — counterfactual regret minimization with an exploitability bound encoded as a type invariant.
- **[formal-counterex-zig](https://github.com/SMC17/formal-counterex-zig)** — CLI of formally refuted financial-engineering claims.

### Data systems
- **[zkdb](https://github.com/SMC17/zkdb)** / **[zkdb-elixir](https://github.com/SMC17/zkdb-elixir)** — pure-Zig columnar time-series database with q/kdb+ semantics, plus Elixir/OTP bindings.
- **[zig-h3](https://github.com/SMC17/zig-h3)** / **[spatial-h3-zig](https://github.com/SMC17/spatial-h3-zig)** — Uber H3 hierarchical geospatial indexing.
- **[blackbird-zig](https://github.com/SMC17/blackbird-zig)**, **[tableformat-zig](https://github.com/SMC17/tableformat-zig)**, **[scd-zig](https://github.com/SMC17/scd-zig)**, **[workflow-event-log-zig](https://github.com/SMC17/workflow-event-log-zig)** — trigram search index, Iceberg-format primitives, slowly-changing-dimension discipline, and a deterministic-replay event log.

### Naval architecture — the `yard-*` suite
A body of ~75 Zig libraries covering ship hydrodynamics, structural rules, stability, propulsion, and port engineering: strip theory and seakeeping (RAO spectra), Savitsky planing resistance, Fossen 6-DOF maneuvering, CSR fatigue and buckling, mooring, dynamic positioning, cavitation, and more. Composable marine-engineering primitives, one concern per repo.

### Language, decipherment, and tools
- **[zsym](https://github.com/SMC17/zsym)** — statistical decipherment substrate (Miller-Madow entropy, n-gram language models, classical cipher solvers), applied to the Voynich manuscript.
- **[morphology-zig](https://github.com/SMC17/morphology-zig)** / **[stemmer-zig](https://github.com/SMC17/stemmer-zig)** — English morphology engine and Porter / Snowball stemmers.
- **[ztop](https://github.com/SMC17/ztop)** (system monitor), **[hikari](https://github.com/SMC17/hikari)** (terminal media suite), **[stax-mast](https://github.com/SMC17/stax-mast)** (single-binary editor kernel), **[sentinel-sbom](https://github.com/SMC17/sentinel-sbom)** (SBOM integrity).

### Method
Every claim is pinned to a proof level: compiled, unit-tested, integration-tested, benchmarked, or hardware-verified. Benchmarks report the command, data size, and hardware class. Words like "production" and "verified" are used only when the evidence supports them.

[sunlitmoon.online](https://sunlitmoon.online)
