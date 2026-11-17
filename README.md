```text
███████╗███╗   ███╗ ██████╗ ██╗███████╗
██╔════╝████╗ ████║██╔════╝███║╚════██║   zero-allocation zig
███████╗██╔████╔██║██║     ╚██║    ██╔╝   beam supervision
╚════██║██║╚██╔╝██║██║      ██║   ██╔╝    machine-checked proofs
███████║██║ ╚═╝ ██║╚██████╗ ██║  ██╔╝
╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
┌────────────────────────────────────────────────────────────────────┐
│  zig hot paths ──▶ 202-symbol C ABI · py3-none · wasm32 · mcp      │
│  domains       ──▶ lob/itch · h3 · gguf · hnsw · 6-dof · sat/drat  │
└────────────────────────────────────────────────────────────────────┘
$ brew install smc17/tap/substrate && substrate mcp
```

# Sean Collins

Systems programmer writing zero-allocation libraries and tools in Zig and Elixir.

- **Try in browser**: [zig-substrate WASM playground](https://smc17.github.io/zinging/) (`33 KB` `wasm32-freestanding`) · [Strip aerospace docs](https://smc17.github.io/strip/)
- **Install**: `brew install smc17/tap/substrate` · [Releases & Python wheels](https://github.com/SMC17/zinging/releases/tag/v3.12.0)
- **Writing**: [sunlitmoon.online](https://sunlitmoon.online) · **Ops & baselines**: [OPS.md](OPS.md) · [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) · **Forecasts**: [FORECASTS.md](FORECASTS.md)

### Featured 2026–2027 AI Systems & Infrastructure

- [agentfork](https://github.com/SMC17/agentfork) — Sub-millisecond APFS `clonefile(2)` copy-on-write agent sandbox, wire-speed HTTP taint & Blake3/HMAC Merkle receipt firewall, and Lean 4 proof-carrying merge gate in Zig.
- [specdecode](https://github.com/SMC17/specdecode) — Zero-GC mid-decode semantic & type-state pruner (`87 ns`), 128k-vocab `f32` logit-mask C ABI & WebAssembly SIMD (`16 µs`), entropy-guided KV-cache paging, and speculative cascade router in Zig.
- [swarmbus](https://github.com/SMC17/swarmbus) — Lock-free cross-process POSIX `mmap` swarm bus, fenced resource leases, LWW-CRDT blackboard, and compute-budget auction scheduler in Zig.
- [physkernel](https://github.com/SMC17/physkernel) — Zero-allocation real-time physical-AI sensor fusion, anytime-valid safety E-STOP, MPC world-model rollout, and closed-loop SRE kernel in Zig.
- [attestinfer](https://github.com/SMC17/attestinfer) — Verifiable inference attestations and selective-disclosure Blake3 Merkle proofs binding model, policy, prompt, and output hashes in Zig.

### Financial Modeling & Markets

- [finance-segway](https://github.com/SMC17/finance-segway) — Governed financial-modeling framework under active development (27 spreadsheet archetypes, 54 historical cases, 22.3% of model inputs grounded in real data or drivers; 599 tests, [ops status](OPS.md)).
- [jevy](https://github.com/SMC17/jevy) — Options market-making lab with a Zig hot path and Python research layer (simulation and paper trading only; 347 tests).
- [MarketDataSimulator](https://github.com/SMC17/MarketDataSimulator) — Teaching exchange for snapshot and incremental market data on .NET 10.

### Zig libraries & systems

- [zinging (`zig-substrate`)](https://github.com/SMC17/zinging) — Unified zero-alloc substrate (ITCH LOB, sequential A/B, HNSW/IVF-PQ, pure-Zig H3, GGUF/WordPiece/Unigram, Black-Scholes/SABR/Heston, Leontief LU, NNUE chess) behind a 202-symbol C ABI, `py3-none` wheels, native `substrate mcp` server, `33 KB` (`34,088 B`) WASM, and 701 unit tests.
- [zig-h3](https://github.com/SMC17/zig-h3) — Uber H3 v4 in pure Zig (all 70 public functions, 211 tests cross-checked against `libh3` v4.1.0).
- [zkdb](https://github.com/SMC17/zkdb) (50 tests) & [zkdb-elixir](https://github.com/SMC17/zkdb-elixir) (8 tests) — Columnar time-series engine with `q/kdb+` `aj`/`wj` semantics, SIMD aggregations, and Erlang NIF supervision.
- [znap](https://github.com/SMC17/znap) — Zero-allocation neural inference in Zig (30→6 policies in ~32 ns, `stories15M` at ~700 tok/s on M2 Max; 631 tests).
- [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) — HuggingFace `tokenizer.json` (BPE, WordPiece, Unigram) in Zig (166 tests).
- [safetensors-zig](https://github.com/SMC17/safetensors-zig) — Zero-dependency `safetensors` reader with header and overlap validation (19 tests).
- [faiss-zig](https://github.com/SMC17/faiss-zig) — Flat, HNSW, IVFFlat, and IVFPQ vector search in Zig (76 tests).
- [zag](https://github.com/SMC17/zag) — Terminal emulator, block model, and agent runtime in one Zig binary (707 tests).
- [logic-zig](https://github.com/SMC17/logic-zig) — SAT/CDCL, bounded model checking, and DRAT proof-checking kernel in Zig (541 tests).
- [strip](https://github.com/SMC17/strip) — Evidence-bearing 6-DOF aerospace simulation substrate in Zig (WGS84, US76, MAVLink, FMI 3.0).
- [yard](https://github.com/SMC17/yard) — Naval architecture and marine hydrodynamics in Zig (72 modules).
- [distro-blog-builder](https://github.com/SMC17/distro-blog-builder) — Fast static-site, RSS, and sitemap generator in Zig.
- [ztop](https://github.com/SMC17/ztop) — `htop` + `nvtop` (`ztop-g`) system monitor in Zig with per-PID IPC (`perf_event_open`), temporal rewind, and VRAM velocity tracking.
- [vllm-zig](https://github.com/SMC17/vllm-zig) — Pure-Zig LLM serving substrate with PagedAttention KV, BF16 `lm_head`, and futex thread-pool dispatch.
- [triton-kernels](https://github.com/SMC17/triton-kernels) — Autotuned Triton GPU kernels (softmax, RMSNorm, FlashAttention-v2 fwd/bwd) with PyTorch reference checks.
- [zig-graph](https://github.com/SMC17/zig-graph) — Sparse graph algorithms in pure Zig (PageRank, Brandes, Louvain, Fiedler, max-flow), cross-checked against `networkx`.
- [fleet-sbom-index](https://github.com/SMC17/fleet-sbom-index) & [sentinel-sbom](https://github.com/SMC17/sentinel-sbom) — SPDX 2.3 SBOM emitter, divergence/drift index, and Ed25519-signed manifests in Zig.
- [mccarthy](https://github.com/SMC17/mccarthy) — Sound 10-primitive LCF HOL theorem prover kernel in Common Lisp.
- [proof-gate-zig](https://github.com/SMC17/proof-gate-zig) — Zero-runtime-cost `comptime` proof gates in Zig (`@compileError` on Lean 4–refuted claims).
- [mast](https://github.com/SMC17/mast) — Single-binary editor kernel with buffer-as-protocol and Janet extensibility in Zig.
- [carreir](https://github.com/SMC17/carreir) — Physical-intelligence substrate for HVAC & cold-chain in Zig with TLA+-model-checked HMAC audit logs.
- [stax-cert](https://github.com/SMC17/stax-cert) — Lean 4 formalization seed for categorical foundations of gradient-based learning (Para, Lens, CRDC).
- [formal-counterex-zig](https://github.com/SMC17/formal-counterex-zig) — Zig CLI over a Lean 4 / Mathlib database of refuted and confirmed quantitative-finance claims.
- [oceanman](https://github.com/SMC17/oceanman) — Submarine cable network resilience analysis in Zig (693 cables, H3, graph centrality).
- [sovereign-edge](https://github.com/SMC17/sovereign-edge) — Composable NixOS edge stack (Caddy, Coraza WAF + OWASP CRS, nftables, Knot DNSSEC, CrowdSec, Anubis).
- **Smaller primitives**: [qsr-zig](https://github.com/SMC17/qsr-zig) (GF(2) SIMD rank) · [zig-cobs](https://github.com/SMC17/zig-cobs) (COBS framing) · [cfr-solver-zig](https://github.com/SMC17/cfr-solver-zig) (CFR+) · [thompson-bandit-zig](https://github.com/SMC17/thompson-bandit-zig) · [dsp-zig](https://github.com/SMC17/dsp-zig) · [stemmer-zig](https://github.com/SMC17/stemmer-zig) · [datelist-zig](https://github.com/SMC17/datelist-zig) · [tableformat-zig](https://github.com/SMC17/tableformat-zig) · [cow-branch-zig](https://github.com/SMC17/cow-branch-zig) · [zig-frame-protocol](https://github.com/SMC17/zig-frame-protocol)

### Upstream contributions (open PRs)

- [`uber/h3#1303`](https://github.com/uber/h3/pull/1303) · [`#1314`](https://github.com/uber/h3/pull/1314) · [`#1315`](https://github.com/uber/h3/pull/1315) · [`#1320`](https://github.com/uber/h3/pull/1320) — `zig-h3` community listing, CLI parser/decimal/`cellAreaRads2` precision fixes, and `CMAKE_INSTALL_INCLUDEDIR` packaging
- [`PyO3/pyo3#6577`](https://github.com/PyO3/pyo3/pull/6577) — document buffered stdout when embedding Python
- [`NixOS/nixpkgs#586947`](https://github.com/NixOS/nixpkgs/pull/586947) — `services.crowdsec.hub.updateOnStart` option
- [`punkpeye/awesome-mcp-servers#19703`](https://github.com/punkpeye/awesome-mcp-servers/pull/19703) · [`mbasso/awesome-wasm#376`](https://github.com/mbasso/awesome-wasm/pull/376) · [`zigcc/awesome-zig#308`](https://github.com/zigcc/awesome-zig/pull/308) · [`wilsonfreitas/awesome-quant#1035`](https://github.com/wilsonfreitas/awesome-quant/pull/1035) · [`sshuair/awesome-gis#336`](https://github.com/sshuair/awesome-gis/pull/336) · [`ai-boost/awesome-harness-engineering#437`](https://github.com/ai-boost/awesome-harness-engineering/pull/437)
- [`janhq/awesome-local-ai#228`](https://github.com/janhq/awesome-local-ai/pull/228) — add `znap`, `tokenizers-zig`, and `safetensors-zig`
