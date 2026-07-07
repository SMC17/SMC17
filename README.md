# Sean Collins

Systems engineer. Pure-Zig ML infrastructure, inference kernels, and verifiable tooling.

Writing: [sunlitmoon.online](https://sunlitmoon.online) · Models & datasets: [huggingface.co/SMC17](https://huggingface.co/SMC17) · sean@sunlitmoon.online

## Selected work

- [inference](https://github.com/SMC17/inference) — pure-Zig LLM serving: paged attention, BF16 kernels, persistent thread pool, safetensors integration. TinyLlama-1.1B end-to-end. 77 tests.
- [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) — BPE, WordPiece, Unigram with tokenizer.json compatibility and offsets. 189 tests + 600-iteration fuzz.
- [faiss-zig](https://github.com/SMC17/faiss-zig) — Flat/HNSW/IVFFlat/IVFPQ ANN with SIMD kernels. 16.94× memory compression on IVFPQ. 76 tests. No C/C++ dependency.
- [safetensors-zig](https://github.com/SMC17/safetensors-zig) — safetensors reader with @Vector structural scan. 241µs parse on a 201-tensor TinyLlama fixture. 21 tests.
- [zkdb](https://github.com/SMC17/zkdb) — columnar time-series database with q/kdb+ semantics: typed vectors, SIMD aggregation, asof join, q IPC protocol. 24 tests.
- [zig-h3](https://github.com/SMC17/zig-h3) — Uber H3 v4 geospatial index: idiomatic wrapper + pure-Zig port. 211 tests, 27k+ cross-validation cases, 94.4% coverage.

Claims ship at proof level: test counts come from the runner, performance numbers ship with the benchmark that produced them.
