# Choose a task

Start with one input and keep the result. These entry points share maintained
cores; each repository owns its supported platforms, evidence and limitations.

| You want to… | Start here | What to look for |
| --- | --- | --- |
| Independently check a small UNSAT result | [Portable proof task](https://github.com/SMC17/logic-zig/blob/main/docs/PORTABLE_TRUST_DEMO.md) | Exact status 20 and positive independent-checker evidence; missing checking refuses |
| Explore hardware/model-checking fixtures | [logic-hwmcc](https://github.com/SMC17/logic-zig/blob/main/docs/PRODUCTS.md) | Named AIGER/engine fixtures and their checker/maturity requirements |
| Exercise local certificate checks | [CLI pack: logic-cert suite](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) | A finite certificate fixture suite, separate from general proof correctness |
| Try bit-vector arithmetic | [CLI pack: logic-smt demo-add](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) | The 40 + 2 = 42 fixture, without a model service |
| Try a branching-time property | [CLI pack: logic-ctl demo](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) | Bounded CTL outcomes, with the engine's stated scope |
| Keep an inspectable record of checked work | [zag + logic-zig](https://github.com/SMC17/logic-zig/blob/main/docs/RECORDED_PROOF_DEMO.md) | Command status, output objects and event-chain integrity; Linux runtime |
| Inspect matching and risk workloads | [Market matching lab](https://github.com/SMC17/MarketDataSimulator/blob/master/docs/SELF_SERVE_LABS.md#1-follow-one-matching-workload) | A reproducible workload; local timings stay separate from published benchmarks |
| Inspect packet-integrity work | [Protocol lab](https://github.com/SMC17/MarketDataSimulator/blob/master/docs/SELF_SERVE_LABS.md#2-inspect-packet-integrity-work) | Encoding/sealing/validation; feed runtime remains a separate task |
| Learn why finite-depth replay can diverge | [Observability lab](https://github.com/SMC17/MarketDataSimulator/blob/master/docs/SELF_SERVE_LABS.md#3-see-what-finite-depth-cannot-tell-you) | Single-step comparisons and cumulative reconstruction reported separately |
| Challenge a sourced financial-model integration | [Current review packet](https://github.com/SMC17/finance-segway/blob/9710a168a93fa2c2936baab0f87cbbb2b41277a7/docs/reviews/CORRECTNESS_PR125.md) | Six source/formula/coverage challenges and fresh reproduction commands; owner-accepted secondary AI review is recorded |

The CLI download preview provides macOS ARM64 binaries requiring macOS 26.4
and Linux ARM64 binaries tested on Ubuntu 24.04. Source is included; other
hosts can build the documented tasks. External proof tools are not bundled.

The market labs target .NET 10. Core tests run on macOS ARM64 and Linux x86-64;
the native Grpc.Core feed task is Linux x86-64. Project code retains its existing Apache-2.0 license;
[licensing scope and data provenance](https://github.com/SMC17/MarketDataSimulator/blob/master/LICENSING.md)
keep market-data terms and dependency notices separate. Production readiness
and user adoption require their own evidence.

Bring a failure to the repository issue tracker with the source revision,
platform/toolchain, minimal input, exact command and expected/actual outcome.

The finance task asks for technical and source challenge, not reliance on a
model for a financial decision. [PR #125](https://github.com/SMC17/finance-segway/pull/125) is merged with
[disclosed secondary AI review and owner acceptance](https://github.com/SMC17/finance-segway/blob/main/docs/reviews/PR125_SECONDARY_TECHNICAL_REVIEW.md).
The annual corpus uses latest-filed observations; these retrospective cases
do not demonstrate point-in-time backtests. No M3/human-use sign-off is implied.
