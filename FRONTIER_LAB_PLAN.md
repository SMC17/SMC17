# Frontier-lab readiness plan (SMC17)

Date: 2026-07-12  
Proof: `audited` against live GitHub API + prior 2026-07-04 inventory.  
Not a Research Scientist claim. Not OQ.

## Blunt north star

Stop optimizing for **repo count**. Optimize for **verification density per claim**.

Two tracks, deliberately separated:

| Track | Purpose | Public hiring weight |
|-------|---------|----------------------|
| **A — ML systems / performance** | Frontier lab / fellowship package | **primary** |
| **B — Sovereign Experience / Yard / Strip** | Aerospace–naval sticky workbench + capture compass | **entrepreneurial / separate org narrative** — do not pin as AI credentials |

“Get Experience all the way” means: one **briefable AF+Navy evidence packet** from local-first Taste under daily-drive discipline — **not** cloud sticky, **not** 72-module gloss, **not** a new public micro-repo.

## Live scorecard (2026-07-12)

| Signal | Observed |
|--------|----------|
| Public repos | **88** (was 171 in July-4 inventory — consolidation started; still far above 10–15) |
| Followers / following | **12 / 268** |
| Pins | Own flagships: `faiss-zig`, `inference`, `safetensors-zig`, `tokenizers-zig` (good — earlier “upstream pins” issue is fixed) |
| Bio | Still Zig-first / purity-coded |
| Profile README | Still leads with Pure-Zig + bare “×” speedups |
| Stars | Mostly 1; max ~2 — **no external adoption signal** |
| Inference README | Badge **77/77** vs body **115/115** — still broken |
| Tokenizers | AGPL + 5.3× on **synthetic WordPiece fixture** — still loud |

Raw potential after concentration: still ~**8/10**. Current readiness for full-time DeepMind RE / OpenAI Inference / Anthropic Tokens: still **~3–4.5/10**. Closest bridge: **Anthropic Fellows (ML Systems)** after Days 1–30 hygiene.

## OoM unlock (one project, not eighty)

**Verified Kernel Optimization Environment** — agents propose kernels; graders enforce compile / functional / numerical / memory / performance / shape generalization.

Stack: Python orchestration + PyTorch reference + Triton candidates + CUDA baselines + Zig CPU harnesses where useful.

This is the hiring thesis. Everything else is support or noise.

## Six-month gates (exit criteria only)

| Window | Exit criterion |
|--------|----------------|
| D1–7 | No public claim you would not defend to an OpenAI perf engineer; liabilities archived; bio/pins/README honest |
| D8–30 | `tokenizers-zig` differential harness ≥50 HF configs + raw compatibility table; AGPL decision documented |
| D31–90 | Kernel env: 8–10 ops, multi-model agent run, public technical report |
| D91–120 | Inference: continuous batching + TTFT/ITL/p99 curves + ≥1 GPU backend |
| D121–150 | ≥5 accepted upstream code PRs; ≥1 independent reproduction |
| D151–180 | Application package: 3 flagships + report + PRs + GPU result + resume |

## Repo freeze

Until D180 or explicit exception:

- **No new public micro-repos**
- No new `*-zig` primitives unless a flagship requires them as an internal module
- Sovereign work stays in existing `sovereign-experience` / `yard` / `strip` — no new public surface

## Flagship set (hiring)

1. `tokenizers-zig`  
2. `inference`  
3. `faiss-zig`  
4. `sme-zig` (only if modern LM experiment lands)  
5. Kernel environment (new — when it exists)  
6. `zkdb` only if tied to eval/telemetry for ML systems  

Aerospace (`strip`/`yard`/`sovereign-experience`): separate README section or org — **not** the pin row.

## Claim ban-list (public)

Unless externally justified: frontier, SOTA, production-grade, OS, platform, substrate, sovereign, shipped, complete, parity, verified.

Speedups must ship with: commit, baseline version, hardware, OS, flags, warmup, N, median+tails, workload, script, non-generalization note.
