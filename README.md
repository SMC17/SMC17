# Sean Collins

Systems programmer writing zero-allocation libraries and tools in Zig and Elixir.

- **Try in browser**: [zig-substrate WASM playground](https://smc17.github.io/zinging/) (`33 KB` `wasm32-freestanding`) · [Strip aerospace docs](https://smc17.github.io/strip/)
- **Install**: `brew install smc17/tap/substrate` · [Releases & Python wheels](https://github.com/SMC17/zinging/releases/tag/v3.12.0)
- **Writing**: [sunlitmoon.online](https://sunlitmoon.online)

### Zig libraries & systems

- [zinging (`zig-substrate`)](https://github.com/SMC17/zinging) — Unified zero-alloc substrate (ITCH LOB, sequential A/B, HNSW/IVF-PQ, pure-Zig H3, GGUF/WordPiece/Unigram, Black-Scholes/SABR/Heston, Leontief LU, NNUE chess) behind a 202-symbol C ABI, `py3-none` wheels, native `substrate mcp` server, and 33 KB WASM.
- [zig-h3](https://github.com/SMC17/zig-h3) — Uber H3 v4 in pure Zig (all 70 public functions, cross-checked against `libh3` v4.1.0).
- [zkdb](https://github.com/SMC17/zkdb) & [zkdb-elixir](https://github.com/SMC17/zkdb-elixir) — Columnar time-series engine with `q/kdb+` `aj`/`wj` semantics, SIMD aggregations, and Erlang NIF supervision.
- [znap](https://github.com/SMC17/znap) — Zero-allocation neural inference in Zig (30→6 policies in ~32 ns, `stories15M` at ~700 tok/s on M2 Max).
- [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) — HuggingFace `tokenizer.json` (BPE, WordPiece, Unigram) in Zig.
- [safetensors-zig](https://github.com/SMC17/safetensors-zig) — Zero-dependency `safetensors` reader with header and overlap validation.
- [faiss-zig](https://github.com/SMC17/faiss-zig) — Flat, HNSW, IVFFlat, and IVFPQ vector search in Zig.
- [zag](https://github.com/SMC17/zag) — Terminal emulator, block model, and agent runtime in one Zig binary.
- [logic-zig](https://github.com/SMC17/logic-zig) — SAT/CDCL, bounded model checking, and DRAT proof-checking kernel in Zig.
- [strip](https://github.com/SMC17/strip) — Evidence-bearing 6-DOF aerospace simulation substrate in Zig (WGS84, US76, MAVLink, FMI 3.0).
- [yard](https://github.com/SMC17/yard) — Naval architecture and marine hydrodynamics in Zig (72 modules).
- [distro-blog-builder](https://github.com/SMC17/distro-blog-builder) — Fast static-site, RSS, and sitemap generator in Zig.
- **Smaller primitives**: [qsr-zig](https://github.com/SMC17/qsr-zig) (GF(2) SIMD rank) · [zig-cobs](https://github.com/SMC17/zig-cobs) (COBS framing) · [cfr-solver-zig](https://github.com/SMC17/cfr-solver-zig) (CFR+) · [thompson-bandit-zig](https://github.com/SMC17/thompson-bandit-zig) · [dsp-zig](https://github.com/SMC17/dsp-zig) · [stemmer-zig](https://github.com/SMC17/stemmer-zig) · [datelist-zig](https://github.com/SMC17/datelist-zig) · [tableformat-zig](https://github.com/SMC17/tableformat-zig) · [cow-branch-zig](https://github.com/SMC17/cow-branch-zig)

### Upstream contributions (open PRs)

- [`ggml-org/llama.cpp#32414`](https://github.com/ggml-org/llama.cpp/pull/32414) — fix `iq3_s` zero sub-block pointer advancement in quantization
- [`uber/h3#1303`](https://github.com/uber/h3/pull/1303) · [`#1314`](https://github.com/uber/h3/pull/1314) · [`#1315`](https://github.com/uber/h3/pull/1315) · [`#1318`](https://github.com/uber/h3/pull/1318) — `zig-h3` community listing, CLI parser/decimal fixes, and `CMAKE_INSTALL_INCLUDEDIR` packaging
- [`PyO3/pyo3#6577`](https://github.com/PyO3/pyo3/pull/6577) — document buffered stdout when embedding Python
- [`NixOS/nixpkgs#586947`](https://github.com/NixOS/nixpkgs/pull/586947) — `services.crowdsec.hub.updateOnStart` option
- [`punkpeye/awesome-mcp-servers#19703`](https://github.com/punkpeye/awesome-mcp-servers/pull/19703) · [`mbasso/awesome-wasm#376`](https://github.com/mbasso/awesome-wasm/pull/376) · [`zigcc/awesome-zig#308`](https://github.com/zigcc/awesome-zig/pull/308) · [`wilsonfreitas/awesome-quant#1035`](https://github.com/wilsonfreitas/awesome-quant/pull/1035) · [`sshuair/awesome-gis#336`](https://github.com/sshuair/awesome-gis/pull/336) · [`ai-boost/awesome-harness-engineering#437`](https://github.com/ai-boost/awesome-harness-engineering/pull/437)
