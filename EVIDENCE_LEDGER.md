# Public evidence ledger

Reviewed: 12 November 2026.

Each statement the profile makes, where to check it, and where it stops. Every repository owns its own evidence in STATUS.md; results below were verified from fresh clones on an Apple M2 Max unless the repository says otherwise. Descriptions and badges are not evidence.

| Statement | Check it | Limit |
|---|---|---|
| zkdb is a columnar time-series library with q/kdb+ semantics | [STATUS](https://github.com/SMC17/zkdb/blob/main/STATUS.md): 47/47 tests | No durability beyond clean close and reopen; no comparison with other databases |
| zkdb-elixir runs zkdb's kernels as an Erlang NIF | [STATUS](https://github.com/SMC17/zkdb-elixir/blob/main/STATUS.md): `mix test` 5/5 | Kernels are ported, not imported from zkdb; joins run on normal schedulers |
| jevy is an options market-making laboratory | [STATUS](https://github.com/SMC17/jevy/blob/main/STATUS.md): Zig 153/153, Python 194 pass | Simulation and paper only; no venue connectivity |
| finance-segway holds governed financial models and hashed historical cases | [README](https://github.com/SMC17/finance-segway), [model inventory](https://github.com/SMC17/finance-segway/blob/main/standards/model_inventory.json) | Historical reconstructions, not forecasts; open model-correctness findings are tracked as P1 issues |
| MarketDataSimulator is an exchange and recovery laboratory | [STATUS](https://github.com/SMC17/MarketDataSimulator/blob/master/STATUS.md): 392/392 on .NET 10 | Research system; no production-venue or regulatory claim |
| tokenizers-zig reads HuggingFace tokenizer.json | [COMPATIBILITY](https://github.com/SMC17/tokenizers-zig/blob/main/COMPATIBILITY.md): BERT and TinyLlama 39/39, T5 36/39 | T5's Precompiled normalizer is not implemented; timing table is historical |
| safetensors-zig reads safetensors files | [STATUS](https://github.com/SMC17/safetensors-zig/blob/main/STATUS.md): 19 pass, 2 optional skips | Speed comparison with the Rust library withdrawn until re-measured |
| faiss-zig implements Flat, HNSW, IVFFlat and IVFPQ search | [STATUS](https://github.com/SMC17/faiss-zig/blob/main/STATUS.md): 76/76 | Synthetic N=10k data only; no public-dataset recall curve yet |
| znap evaluates small policies in about 32 ns and generates text at about 700 tok/s | [README](https://github.com/SMC17/znap#performance): `zig build bench`, 631/631 tests | One machine; research experiments compile but are not re-run |
| qsr-zig computes GF(2) matrix rank | [README](https://github.com/SMC17/qsr-zig): 800 differential trials | No performance claim |
| logic-zig is an executable museum of logic with a fail-closed trust kernel | [STATUS](https://github.com/SMC17/logic-zig/blob/main/STATUS.md): 541/541 | Maturity varies by logical system; external checkers have their own gates |
| zig-h3 implements all 70 H3 v4 functions, cross-checked against libh3 | [STATUS](https://github.com/SMC17/zig-h3/blob/main/STATUS.md): 211/211, [BENCH](https://github.com/SMC17/zig-h3/blob/main/BENCH.md) | Pure Zig is 5-8% faster than libh3 single-threaded on M2 Max; no production user known |
| zag records engineering work in one workspace log | [STATUS](https://github.com/SMC17/zag/blob/main/STATUS.md): 707 pass on macOS | PTY, raw TTY and tool execution are Linux-only |
| method-wagwan is a replay engine for code | [STATUS](https://github.com/SMC17/method-wagwan/blob/main/STATUS.md) | Design only; no engine and no result yet |

The profile makes no portfolio-size, production-adoption or certification claim.
