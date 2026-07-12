# Public evidence ledger (SMC17)

Date: 2026-07-12  
Rule: every public numerical claim needs a row. Missing artifact → remove claim.

| Repo | Claim | Status | Artifact / fix |
|------|-------|--------|----------------|
| inference | Badge tests 77/77 | **CONFLICT** | Body + `zig build test` say 115 — fix badge |
| inference | 2.2–15.6× vs OpenBLAS on decode | UNVERIFIED here | Need commit+machine+script in README |
| inference | 6.17× decode speedup (profile README) | UNVERIFIED / inconsistent with repo README range | Reconcile or delete |
| tokenizers-zig | ~5.3× WordPiece vs HF | **OVERSTATED presentation** | README admits synthetic fixture — demote headline |
| tokenizers-zig | 189 tests + 600-iter fuzz | PLAUSIBLE | Keep if `zig build test` green on clean clone |
| faiss-zig | 16.94× IVFPQ memory compression | NEEDS METHOD | Compression vs what baseline/params? |
| faiss-zig | 76 tests (profile) vs README 44 expected | **CONFLICT** | Reconcile |
| safetensors-zig | 241µs parse / 21 tests | NEEDS FIXTURE SIZE + HW | Keep only with machine class |
| zkdb | 24 vs 41 tests | **CONFLICT** (prior audit) | Reconcile |
| poker | 40M hands/s, AVX2/NEON, CUDA cmds | **LIABILITY** | Archive / rewrite from zero |
| crpc-core | Prior PTX/MSL overclaim + self-note | **LIABILITY** | Archive or narrow to DotProduct-only |
| aqe-replanner-zig | “ports Spark AQE / Materialize / Catalyst” | **OVERCLAIM** | Rewrite to 7-test Thompson prototype |
| SMC17 bio | Pure-Zig identity | **HURTS HIRING** | Retarget ML systems tools-as-appropriate |

## Upstream PRs (fill as accepted)

| Upstream | Title | Merged? | Link |
|----------|-------|---------|------|
| TQEC (cited historically) | coordinate transform + tests | claimed | verify URL |
| HF tokenizers | BPE legacy-merge | claimed on profile | verify open/merged |
| FAISS | IVFPQ docs | claimed | verify |
| nixpkgs | CrowdSec / ydotool | claimed | verify |

Target: 5 accepted **code** PRs in PyTorch / Triton / vLLM / HF Tokenizers / FAISS / llama.cpp class systems.
