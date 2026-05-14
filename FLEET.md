# Fleet Manifest

**Field:** Quantitative Mercantilism

**Practice:** Verifiable Fleet Engineering

Composable, correctness-first systems with strong auditability and replaceability. The modern equivalents of well-built ships that operate independently, are repaired at sea, and compose into larger fleets. This manifest is the honest register of every public repo against the *honest-1.0 contract* below. Where a repo does not yet earn `v1.0`, this document says so plainly; the GitHub tag will be reconciled to match.

## Honest-1.0 contract

A repo earns a `v1.0` tag iff every check holds:

1. **Green CI** on `main` for the most recent run.
2. **README accurate** — every concrete claim verifiable by reading the code or named public artifact.
3. **LICENSE present** and matches the README's stated license.
4. **CHANGELOG present** with a real entry for the tagged version.
5. **Tests present and passing** for the load-bearing public surface.
6. **No active stubs in critical paths** (`unreachable;`, `// TODO`, `@panic("not implemented")`) on functions the README documents as supported.
7. **Reproducible build/install** — anyone can clone and run the documented workflow without secret knowledge.

If any check fails, the repo is **not honest-1.0** and the tag is a vanity claim.

## Evidence vocabulary

Per `AGENT_HARNESS.md`, claims about a repo's state use one of:

`sketch` · `scaffold` · `compiled` · `unit-tested` · `integration-tested` · `audited` · `benchmarked` · `hardware-verified`

The words "verified," "production," "dominant," "safe," and "complete" require the specific evidence that makes them true. They are not used decoratively.

## Type I / Type II lens

Every repo entry names both failure modes:

- **Type I** — accepting a false claim as real. Examples: calling a `compiled` program "verified", treating a toy benchmark as representative, presenting a `scaffold` as `production-ready`.
- **Type II** — missing real value or real risk. Examples: ignoring a working prototype because git is clean, overlooking a safety boundary because it is outside the main code path.

## Fleet tiers

| Tier | Meaning |
|---|---|
| **S** | Honest-1.0 verified — every contract check holds. |
| **A** | Credible substrate, contract holds modulo minor README polish; spot-verified. |
| **B** | Substantial codebase, missing one or more contract requirements (commonly: tests, CHANGELOG, or unverified parity claims). Not honest-1.0. |
| **D** | Vanity tag — CI red, or stub size insufficient for the tag carried. Tag must be reverted or repo substantially expanded. |

## Register

> Status is the most recent honest assessment. CI conclusion and tag are the public-truth pair; where they disagree with the README, the tag is the lie.

### Substrate — small libraries that compose

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [zig-cobs](https://github.com/SMC17/zig-cobs) | **S** (Wave 1 verified) | v1.1.0 | ✓ | `unit-tested` + `fuzzed` (22/22 tests; 117k-trial fuzz on every push) | Pure-Zig zero-alloc COBS framing. Three Type-I overclaims fixed: install URL bumped to v1.1.0, test count corrected, benchmark table replaced with min/median/max across 5 fresh runs. COBS frames; it does not authenticate. |
| [zig-frame-protocol](https://github.com/SMC17/zig-frame-protocol) | **A** (Wave 1 verified) | v1.0.0 | ✓ | `unit-tested` + `fuzzed` (15 unit + 6 fuzz; 100k random-wire never-panic, ~11k CRC bit-flip sweep at 98.4% catch) | Versioned binary frame protocol on COBS. `unreachable;` in `encodePacket` is a correct contract assertion against `zig-cobs.encode`, not a stub. Note: `build.zig.zon .version` lags tag — fix in v1.0.1 polish push. |
| [zig-graph](https://github.com/SMC17/zig-graph) | **A** (Wave 1 verified) | v1.1.0 | ✓ | `unit-tested` + `fuzzed` (50/50 tests; 10,360 random graphs across 4 harnesses) | Sparse undirected graph + spectral algorithms. PageRank dangling-node handling correct; spectral algorithms verified as real deflated power iteration on `M = τI − L` with closed-form `λ₁` match to 1e-6 on P_n, C_n, K_{1,4}, K_4, barbell. |
| [zig-h3](https://github.com/SMC17/zig-h3) | **S** (Wave 1 verified) | v1.1.0 | ✓ | `unit-tested` + `benchmarked` (166/166 tests in 2s; pure-Zig median faster on 7 measured ops, variance 0.24×–1.86× on contended laptop) | H3 v4 spatial index — idiomatic wrapper + 7,280-line pure-Zig reimplementation, reachable via public API. **117 cross-validation tests against libh3** (not 142 as previously claimed — corrected). 63 v4 wrappers, 10 spot-verified. |

### Protocol implementations

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [rippled-zig](https://github.com/SMC17/rippled-zig) | **D — Wave-3 PR open** | v1.0.1 | ✗ awaiting PR merge + soak | `unit-tested` + `property-tested` (6,144 trials) | XRPL protocol toolkit. [PR #69](https://github.com/SMC17/rippled-zig/pull/69) — Wave-2 + Wave-3 multi-bug fix: structural trend-window persistence across Gates C/D/E/Sim, Gate E panic replaced with error propagation, Sim invariant probe ported to current API, 5 static brightgreen shields replaced with live badge, 6,144 new property-test trials, advisory Gate F (reproducible build). Honest soak path: 3 consecutive green runs after merge before "A–E green" is true. |
| [zeth](https://github.com/SMC17/zeth) | **D — real EIP-2929 violation caught by differential fuzz** | v1.0.0 | ✗ (Reference Comparison Tests: 6/33 = 18.2%) | `unit-tested` (internally consistent, but tests bake in the wrong gas formula) | EVM in Zig. **Wave-2 finding: the original SIGABRT was a harness bug already fixed at HEAD `7ee89e7`. The deeper, still-red failure is a real EVM correctness bug** — `opCall`/`opStaticCall`/`opCallCode`/`opDelegateCall` use `700 + accountAccessCost(target)`; EIP-2929 removed the 700 base. zeth double-charges across the entire CALL family vs PyEVM-Berlin. README claims "exact-equality golden tests for CALL*/CREATE*" and "0x01..0x05 verified" — **falsified by the diff-fuzz gate**. 263 unit tests pass because `comprehensive_test.zig` bakes the wrong formula across ~10 sites. **Action: land the gas-formula fix in 4 opcodes + sweep ~10 test sites + drop the falsified README claims. The diff-fuzz substrate did its job catching the bug — that's the win, not the embarrassment.** |

### Editor substrate

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [mast](https://github.com/SMC17/mast) | A — honest v1.1.0 | v1.1.0 | ✓ | `unit-tested` | Single-binary editor kernel; Janet embedded; AGPL. **README and tag now agree at v1.1.0.** File-write buffers + atomic save shipped in v1.1.0 (4 unit tests). Capability-model sandbox first-slice on `main` (commit `53a861c`). Still roadmap: visual TUI, local-inference daemon, multi-buffer state, native Windows. |

### Sovereign Stack

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [sovereign-edge](https://github.com/SMC17/sovereign-edge) | A — Wave-4 PR open | v1.0.0 | ✓ + `sbom` job ([PR #3](https://github.com/SMC17/sovereign-edge/pull/3)) | `compiled` (Phase 2) + `unit-tested` (sentinel-sbom byte-determinism asserted across 2 emit runs) | Caddy + Coraza + Knot DNS NixOS bundle. Wave-4 sentinel-sbom self-application landed; nixos-test integration in flight. **Action: nixos-test (in flight) raises this to `integration-tested`; real-VPS deployment is the final earn for honest v1.0.** |
| [sentinel-sbom](https://github.com/SMC17/sentinel-sbom) | **S** (Wave 1 verified) | v0.6.0 (HEAD commit-stamped 1.0.2; tag not yet pushed) | ✓ | `unit-tested` (62/62) + `audited` (NAR encoder, one corpus) | Nix `flake.lock` → SPDX 2.3 SBOM, narHash verification. Overclaim language ("verified end-to-end", "production") replaced with honest evidence vocab. Path to honest v1.0.2 tag push = stax's call. |
| [sovereign-offense-harness](https://github.com/SMC17/sovereign-offense-harness) | A — Wave-4 PR open | v1.0.0 (README reconciled to v0.4.0) | ✓ | `unit-tested` (24/24) + `integration-tested` (12/12 TTP smoke runs) | Adversary-emulation runner with safety gates. [PR #2](https://github.com/SMC17/sovereign-offense-harness/pull/2) — 2 TTPs / 1 column → 12 TTPs / 6 of 14 ATT&CK tactic columns. New `THREAT_COVERAGE.md` matrix as audit surface (covers ~1.8% of ATT&CK Enterprise v17.1; 8 columns empty + named). Vanity v1.0.0 closed: README reconciled to v0.4.0 to match substrate. Refuse-by-default gate enforced on all 10 new TTPs. |

### Knowledge bases

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [oceanman](https://github.com/SMC17/oceanman) | A — Wave-3 PR open | v1.0.0 | ✓ + `corpus-verify` job green | `audited` + `integration-tested` (17/17 schema checks, 693 cables / 1,910 landings / 13,883 geo points / 3,161 landing references, 0 orphans, 0 ID collisions) | [PR #4](https://github.com/SMC17/oceanman/pull/4) — 17 schema/integrity checks (pure-stdlib Python), live-derived counts block in README, `oceanman verify` + `oceanman counts` CLI, Makefile, golden-schema fingerprint. Also caught + fixed a pre-existing citation-validator regex bug. |

### Stubs and unaudited

| Repo | Tier | Tag | Note |
|---|---|---|---|
| [carreir](https://github.com/SMC17/carreir) | **B — Wave-3 PR open, substrate week landed** | v1.0.0 | [PR #1](https://github.com/SMC17/carreir/pull/1) — 6 commits, 41/41 tests pass on Zig 0.16.0. Sketch scaffolds (ptx_incursion, hexagram compressor) relocated to `experimental/`. Three VFE hulls shipped: **psychrometric** (ASHRAE 2021 moist-air primitives, 16 cross-checks), **refrigerant** (NIST P-T tables for R-134a/R-410A/R-32/R-1234yf/R-744 + round-trip tests), **coldchain** (HMAC-SHA256 append-only reefer log, threat-modeled, detects single-byte tamper / reorder / delete on replay). CLI deferred — needs Zig 0.14→0.16 std.process API port. Honest target after merge: v0.2.0. |
| [sovereign-emacs](https://github.com/SMC17/sovereign-emacs) | **A — Wave-3 PR open** | v1.0.0 | Wave-2 corrected: **1,922 Elisp + 545 test lines** (not 83). 23/25 ERT pass (Emacs 30; 2 pre-existing failures in v1.4 `defcase-test` wrapper documented). Wave-3 [PR #1](https://github.com/SMC17/sovereign-emacs/pull/1) reposition + license decision (GPL-3.0-or-later, AGPL §13 doesn't trigger) + Ogilvy README rewrite + experimental bridge to mast (`sovereign-mast.el`, 130 lines, hash-equivalence check). |
| [symbols-zig](https://github.com/SMC17/symbols-zig) | A — pending re-audit | n/a | Decipherment-methodology lane; private/no release. |
| [sentinel-lab](https://github.com/SMC17/sentinel-lab) | B | v1.0.0 | 1,100 SLOC; tests unverified. |
| [homelab](https://github.com/SMC17/homelab) | B | v1.0.0 | 2,773 SLOC; tests absent. |
| [stax-cross-agent-verification](https://github.com/SMC17/stax-cross-agent-verification) | B | v1.0.0 | 17,675 SLOC; tests absent. |
| [steam](https://github.com/SMC17/steam) | B | v1.0.0 | 9,439 SLOC; only 3 commits — suspicious squash. |
| [stax-doctrine](https://github.com/SMC17/stax-doctrine) | n/a — doc repo | v1.0.0 | Doctrine essays; no testable code surface. Tag is more about content cut than software. |
| [stax-blog](https://github.com/SMC17/stax-blog) | n/a — content repo | v1.0.0 | Public writing. |
| [amx-zig](https://github.com/SMC17/amx-zig) | **D — Type-I falsified** | Wave-4 audit: public entry point `projectEnergyMorphismAmx` does NOT compile on aarch64 under Zig 0.16 (old `: "memory"` clobber + wrong `.inst` opcode). Test passes only because it never exercises the inline-asm path. **Falsifiable in 60 seconds.** 124 SLOC, 1 commit, no LICENSE/CHANGELOG/CI/build.zig. Decision needed: substrate week vs extract vs archive. |
| [crpc-core](https://github.com/SMC17/crpc-core) | **D — Type-I falsified** | Wave-4 audit: README claims "same packet projects to PTX, MSL, GCN" — but `Ribosome.project()` returns the hardcoded string literal `"/* JIT-PROJECTED HARDWARE ISA */"`. No emitters exist. **However the XChaCha20-Poly1305 seal/open IS real and round-trip tested (~70 SLOC) — extractable as `zig-sealed-envelope`.** 183 SLOC, 1 commit. |
| [fivem-ship-and-sell](https://github.com/SMC17/fivem-ship-and-sell) | **B — Type-II underclaim corrected (Wave-4 PR)** | [PR #5](https://github.com/SMC17/fivem-ship-and-sell/pull/5) — Wave-4 audit found ~2,500 lines of real substrate (396-line Lua scaffold generator + 1,384-line Next/Tailwind/Playwright site + 749 lines buyer-side research) hidden behind a 39-line README. CI green: npm build → Playwright 5×2 visual contracts → generator smoke + `luac5.4 -p`. PR rewrites README with honest evidence vocab + engineering CHANGELOG. No LICENSE yet (operator's call — affects emitted-template redistribution). |

## Reconciliation plan

The vanity-push problem is corrected by doing the work the tag promised, in this priority order:

1. **Earn the tag (preferred).** Close the gaps the contract names — fix the failing CI gate, add the missing tests, surface real benchmarks, close stubs in critical paths, build out the substrate. This is the default move for every repo. The point of carrying `v1.0` is to honor it.
2. **Reconcile tag/README mismatch.** Where the per-repo README already correctly concedes early state (mast `v0.1.0 commit-zero`, sovereign-edge "Phase 2 — closure-builds, not runtime-verified", sovereign-offense-harness `v0.3.1 — early`), the *tag* is what lies — the README is honest. Bring the next push under the version the README already names.
3. **Expand the substrate.** For stub repos (carreir, sovereign-emacs) carrying a tag the SLOC can't justify: scale the substrate to match. The substrate, not the tag, is what's load-bearing.

No silent downgrades. Every reconciliation is committed with a CHANGELOG entry that names what changed and why. When a downgrade is unavoidable, it is honest, public, and accompanied by a concrete plan to re-earn the version.

## Fleet-wide gaps surfaced by Wave 4

Honest Type-II audit — disciplines and surfaces the fleet does NOT yet cover:

1. **sentinel-sbom only reads `flake.lock`** — but only 1 of 9 Tier S/A repos uses Nix flakes. The other 8 consume their supply chain via `build.zig.zon`. Until sentinel-sbom has a `build.zig.zon` sibling emitter, fleet-wide SBOM coverage is structurally incomplete.
2. **No SBOM aggregator** — per-repo SBOM uploads have no consumer. A `fleet-sbom-index` repo that pulls each artifact, indexes by commit-sha, and cross-verifies shared hashes (catches one repo pinning stale `nixpkgs` while others have moved) would close this loop.
3. **No coverage measurement** — we cite test counts (166, 50, 22, 64, …) without naming what % of code those tests actually exercise.
4. **No mutation testing** — we don't know if any of our test suites would catch a regression.
5. **No formal property statements** — protocol substrates (rippled-zig, zig-frame-protocol) carry differential and property tests but no TLA+-style invariant statement.
6. **No cross-fleet integration tests** — composition is asserted in prose, not in code. `zig-cobs` + `zig-frame-protocol`, or `coldchain` SBOMed by `sentinel-sbom`, would be the obvious first integrations.
7. **No compiled README examples** — code blocks in READMEs aren't CI-verified; rot is inevitable.
8. **No regulatory mapping for coldchain** — HACCP, FDA 21 CFR Part 11 (audit-trail), EU FSMA — the substrate's value depends on naming the regulation it satisfies.
9. **No second-reference differential testing** — `zig-h3` vs libh3 only (could also diff against h3-py); `zeth` vs PyEVM only (could also diff against go-ethereum).
10. **Cryptographic protocol audit readiness** — ~~`rippled-zig` needs~~ ✅ `rippled-zig` has `CRYPTO_AUDIT_READINESS.md` ([PR #70](https://github.com/SMC17/rippled-zig/pull/70)). `zeth` still needs the equivalent document.

11. **Regulatory mapping for coldchain** — ~~not surfaced~~ ✅ `carreir` PR #1 now includes `src/coldchain/REGULATORY_MAP.md` mapping the hull to FDA 21 CFR Part 11 + HACCP + EU GDP with 9 explicit "what this does NOT cover" surfaces.

12. **Type-I falsified claims in amx-zig and crpc-core** — Wave-4 audit found two stub repos where the public README claims are physically false (amx-zig: entry point doesn't compile on aarch64; crpc-core: claimed JIT emitter returns a string literal). These are the highest-severity Type-I overclaims in the fleet right now. Decisions pending (tasks #21, #22).

This list is the active hunt surface, not a backlog. Each item becomes a wave target as the lower-level work clears.

## What this manifest is not

This is not a marketing surface. It is the public ledger of where the fleet's hulls actually stand against the contract they advertise. Where this manifest disagrees with a per-repo README badge or a profile-page table, **this manifest is canonical** until the next reconciliation pass.

---

*Last reconciled: 2026-05-14.*
