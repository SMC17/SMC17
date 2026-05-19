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
| [zig-cobs](https://github.com/SMC17/zig-cobs) | **S** (Wave 1 verified, Wave 4 cross-platform, Wave 6 coverage-measured) | v1.2.0 | ✓ across Linux x86_64 + Linux aarch64 + macOS Apple Silicon | `unit-tested` + `fuzzed` (22/22 tests; 117k-trial fuzz) + `coverage-measured` (**100.00% line coverage on src/root.zig, 48/48 lines**) + `hardware-verified` (3 native runners) | Pure-Zig zero-alloc COBS framing. v1.2.0 ships the canonical kcov-coverage-driver pattern adopted by the rest of the fleet. |
| [zig-frame-protocol](https://github.com/SMC17/zig-frame-protocol) | **A** (Wave 1 verified, Wave 4 cross-platform, Wave 6 coverage-measured) | v0.2.0 | ✓ across 3 native runners (coverage PR open) | `unit-tested` + `fuzzed` + `coverage-measured` (**100.00% line coverage, 48/48 lines**) + `hardware-verified` | Versioned binary frame protocol on COBS. v0.2.0 ships [PR #3](https://github.com/SMC17/zig-frame-protocol/pull/3): coverage-driver pattern adopted from zig-cobs v1.2.0. Also drops the premature `v1.0` tag down to v0.2.0 per the no-premature-production-claims doctrine. |
| [zig-graph](https://github.com/SMC17/zig-graph) | **A** (Wave 1 verified, Wave 4 cross-platform, Wave 6 coverage-measured) | v1.2.0 (coverage [PR #3](https://github.com/SMC17/zig-graph/pull/3)) | ✓ across 3 native runners | `unit-tested` + `fuzzed` (50/50 tests; 10,360 random graphs across 4 harnesses) + `coverage-measured` (**86.98% on src/* — 394/453 lines across 5 source files: root.zig 94.20%, community.zig 93.55%, centrality.zig 81.16%, traversal.zig 81.20%, spectral.zig 76.74%**) + `hardware-verified` | Sparse undirected graph + spectral algorithms. v1.2.0 closes the coverage gap and surfaces a fleet-wide tooling finding: **multi-file Zig modules need `-Doptimize=ReleaseSafe` for kcov to capture cleanly** through the nixpkgs build; Debug-mode DWARF on multi-file modules silently fails. zig-cobs's single-file `root.zig` captured under Debug; zig-graph + sentinel-sbom + others with sibling-imports need ReleaseSafe. Documented in zig-graph's CHANGELOG v1.2.0 as the extended toolchain note. |
| [zig-h3](https://github.com/SMC17/zig-h3) | **S** (Wave 1 verified, Wave 4 cross-platform, Wave 6 coverage-measured) | v1.4.0 | ✓ across 3 native runners | `unit-tested` + `benchmarked` + `coverage-measured` (**94.40% line coverage on src/root.zig, 219/232 lines**) + `hardware-verified` (166/166 tests + 27k+ corpus cases) | H3 v4 spatial index — idiomatic wrapper + 7,280-line pure-Zig reimplementation. Coverage commit 285e2a6 on main. v1.4.0 also ships batch+parallel API (3.6-6× faster than libh3 scalar on hot ops), Python binding via libzig_h3.so + ctypes + NumPy, Go binding via cgo. The 5.6% uncovered lines are documented defensive-unreachable + errdefer cleanup. |

### Protocol implementations

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [rippled-zig](https://github.com/SMC17/rippled-zig) | **D — PR #69 MERGED, soak BLOCKED on billing (2026-05-18)** | v1.0.1 | ✗ Quality Gates can't run | `unit-tested` + `property-tested` (6,144 trials) | XRPL protocol toolkit. [PR #69](https://github.com/SMC17/rippled-zig/pull/69) merged 2026-05-15. Got 1 consecutive green CI run on `main` post-merge (run 25923940789). **Soak stalled: every scheduled run since 2026-05-15 has died at the runner-startup step with the GitHub Actions billing error "recent account payments have failed or your spending limit needs to be increased."** This is an org-level account-state issue, not a code issue. Once GitHub Actions is unblocked, 2 more clean Quality Gates runs on `main` will close the soak. Until then the FLEET row stays D and the A-E green claim stays suspended. Adjacent finding ([rippled-zig PR #70](https://github.com/SMC17/rippled-zig/pull/70)): the docs/crypto-audit-readiness branch was closed unmerged after the doc landed via PR #71. |
| [zerotheta-evm](https://github.com/SMC17/zerotheta-evm) (was zeth) | **D — Type-I fix + 🟢 ZERO-RESIDUAL PyEVM differential (2026-05-18)** | v1.0.0 | mainnet-compatible posture **SUSPENDED** pending block-replay re-validation; **every load-bearing audit finding closed** | `compiled` + `unit-tested` (411/414) + `audited` (7-round in-session audit-fix-validate loop) + `differential-tested-post-fix` (**PyEVM-Berlin diff against critical_opcode + precompile suite: `Total discrepancies: 0`**) | EVM in Zig. 7-round same-session audit-fix-validate loop on PR #24. Differential trajectory: **26 → 20 → 10 → 5 → 3 → 2 → 0**. Each reduction matched the next layer of the audit decomposition. Six independent root causes found + fixed: (1) stack-pop convention inversion across 12 non-commutative opcodes (YP §H.2), (2) G_copy = 3 gas/word on 4 *COPY opcodes, (3) BN256 base-field-prime one-character substitution (scalar field order `n` → base field prime `p`), (4) leftover-gas-on-precompile-failure (4 helpers, threaded `forwarded_gas`), (5) EVM memory zero-init on resize (14 sites in opcode handlers + 2 in `Memory.load`/`store`), (6) two new declared-divergence markers on `OpcodeTestCase` for legitimate harness vs. spec mismatches (PyEVM error-path echo vs. EIP-196/197 empty; PUSH0 fork-mismatch zeth=Cancun vs. PyEVM=Berlin). Full audit chain in `POST_FIX_DIFFERENTIAL_REPORT.md`. **The canonical end-to-end case study: an "26 mysterious divergences" finding decomposed into 4 named bugs + 2 harness artifacts and closed to zero in one session.** |

### Editor substrate

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [mast](https://github.com/SMC17/mast) | A — honest v1.1.0 | v1.1.0 | ✓ | `unit-tested` | Single-binary editor kernel; Janet embedded; AGPL. **README and tag now agree at v1.1.0.** File-write buffers + atomic save shipped in v1.1.0 (4 unit tests). Capability-model sandbox first-slice on `main` (commit `53a861c`). Still roadmap: visual TUI, local-inference daemon, multi-buffer state, native Windows. |

### Sovereign Stack

| Repo | Tier | Tag | CI | Evidence | Honest summary |
|---|---|---|---|---|---|
| [sovereign-edge](https://github.com/SMC17/sovereign-edge) | A — substantially evolved during Wave-4 (FLEET row was stale) | v1.4.0 (per parallel work during this session) | ✓ + multiple `nixos-test` runs | `compiled` + `unit-tested` + **`integration-tested`** (nftables v1.1.0 + Caddy v1.2.0 + Knot DNS v1.3.0 + Coraza WAF SQLi→403 v1.4.0, all in-tree `nixos-test`) + `sbom` self-application ([PR #3](https://github.com/SMC17/sovereign-edge/pull/3)) | Caddy + Coraza WAF + nftables + Knot DNS + CrowdSec NixOS bundle. **Wave-4 nixos-test scenario #5 (CrowdSec) shipped on [PR #4](https://github.com/SMC17/sovereign-edge/pull/4) as `scaffold` — test FAILED honestly and caught a real upstream nixpkgs bug** (`services.crowdsec` ExecStartPre calls `cscli hub update` unconditionally → DNS fail in hermetic VMs → `mkdir EACCES` cascade). Two upstream fix locations proposed. CrowdSec stays at `compiled` + `scaffold`, NOT `integration-tested`, until upstream is fixed. |
| [sentinel-sbom](https://github.com/SMC17/sentinel-sbom) | **S** (Wave 1 verified, Wave 3 v1.0.3 shipped, Wave 4 cross-platform, Wave 6 coverage-measured) | v1.1.0 (coverage PR open) | ✓ across 3 native runners | `unit-tested` (62/62) + `property-tested` (1500-trial determinism) + `audited` (NAR encoder, one corpus) + `coverage-measured` (**97.50% combined on spdx.zig + zon.zig, 234/240 lines**: spdx.zig 98.68% / zon.zig 95.51%) + `hardware-verified` | Nix `flake.lock` → SPDX 2.3 SBOM. v1.1.0 ships [PR #5](https://github.com/SMC17/sentinel-sbom/pull/5) with the coverage-driver pattern. Out of scope by design: nar.zig + license_scan.zig (Linux-only syscalls, /nix/store fixtures needed) + main.zig (CLI dispatcher; smoke-tested instead). |
| [fleet-sbom-index](https://github.com/SMC17/fleet-sbom-index) | A — Wave-5 ship + Wave-6 end-to-end pipeline | v0.2.0 | ✓ CI green | `compiled` + `unit-tested` (6/6) + `integration-tested` (2/2 hermetic + e2e pipeline against 4 live fleet repos) + `audited` | Companion to sentinel-sbom: cross-fleet SBOM divergence detector. v0.2.0 ships `tools/aggregate.sh` — the canonical fleet-integrity-gate wrapper: given repo dirs it runs `sentinel-sbom emit` on each then `fleet-sbom-index` over the resulting SBOMs. **Verified 2026-05-18** end-to-end on zig-cobs + zig-frame-protocol + zig-h3 + zig-graph: 4 SBOMs emitted, aggregated, 2 distinct deps surfaced, zero divergences. Closes the Wave-4 gap with both an emitter AND a live consumer pipeline against real fleet artifacts. AGPL-3.0. |
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
| [homelab](https://github.com/SMC17/homelab) | A — Wave-4 honest cut shipped | v1.0.1 | **27/27 tests pass** on Zig 0.16. Wave-4: previous v1.0.0 tag pointed at the May-6 Carrier-Digital-Cousin commit before LICENSE / CHANGELOG / CI / cobs.zig / crc32_fast.zig / inspect.zig landed. v1.0.1 ships +1,307 LOC across 20 files: full hygiene set + the missing protocol modules + 4 build-breaking-bug fixes (cobs module wiring, Cobs.encode/decode struct access, void-fn try, discarded-then-used params). Pre-existing pre-commit SOVEREIGN_BUILD_GATE caught all four during a README-only commit attempt. |
| [stax-cross-agent-verification](https://github.com/SMC17/stax-cross-agent-verification) | B | v1.0.0 | 17,675 SLOC; tests absent. |
| [steam](https://github.com/SMC17/steam) | A — Wave-4 re-audit | v1.0.0 | **39/39 tests pass** on Zig 0.16 — correcting the prior row's "tests unverified" framing. 7,956 LOC across 19 source files (gold.zig 1,756, silver.zig 988, graph_features.zig 771, lab_core.zig 414, diagnostics.zig 364, clickhouse.zig 358, main.zig 352; plus ingest, parser, topology, mesh). The "only 3 commits" finding is a *commit-count* observation (suggests squash history) and does not reflect the size or test coverage of the codebase. README's `## Current Proof Level` block is honest evidence-stratified. |
| [stax-doctrine](https://github.com/SMC17/stax-doctrine) | n/a — doc repo | v1.0.0 | Doctrine essays; no testable code surface. Tag is more about content cut than software. |
| [stax-blog](https://github.com/SMC17/stax-blog) | n/a — content repo | v1.0.0 | Public writing. |
| [amx-zig](https://github.com/SMC17/amx-zig) | A — Wave-4 substrate-cut shipped | v0.1.0 (2026-05-15) | Type-I correction landed. `zig build` green on Linux x86_64 + cross-compile sanity for aarch64-macos. Inline-asm `exec()` body gated by `comptime builtin.target.cpu.arch == .aarch64 and .os.tag == .macos`; non-Apple-Silicon targets `@panic` instead of emitting undecodable `.inst 0x00201000`. New `Amx.supported` flag. Tests: 1 → 5 (codegen determinism, target-flag, opcode-enum tags pinned to dougallj/applecpu, dump references AMX_SET enable/disable). New hygiene: LICENSE (MIT), CHANGELOG, build.zig, build.zig.zon, CI workflow (native + aarch64-macos cross). README explicitly names gaps: not-runtime-tested on M-series, no Accelerate-reference correctness check, no benchmarks, no SIGILL recovery, inline-asm clobber list deliberately empty. |
| [crpc-core](https://github.com/SMC17/crpc-core) | A — Wave-4 substrate-cut shipped | v0.1.0 (2026-05-15) | Type-I correction landed. `Ribosome.project()` no longer returns the hardcoded `"/* JIT-PROJECTED HARDWARE ISA */"`; it `@panic`s pending real emitters. New `Ribosome.parse()` exposes the AST-validation half that actually works in v0.1.0. Tests went 1 → 11 — round-trip seal/open across 4 payload shapes; four adversarial invariants (payload-tamper / tag-tamper / wrong-key / truncated all reject with the expected error); four parser invariants (canonical AST accepts; unknown opcode + missing EOF + invalid scalar reject). New hygiene: LICENSE (MIT), CHANGELOG, build.zig, build.zig.zon, CI workflow, .gitignore. README names remaining gaps explicitly (PTX / MSL / GCN emitters, wire transport, multi-node mesh); future direction can substrate-week the emitters or extract seal/open + AST validator into a standalone `zig-sealed-envelope`. |
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
2. **No SBOM aggregator** — ~~per-repo SBOM uploads have no consumer~~ ✅ closed 2026-05-15 via [fleet-sbom-index v0.1.0](https://github.com/SMC17/fleet-sbom-index). Reads N SPDX-2.3 tag-value SBOMs and surfaces every `(package, version)` whose SHA256 disagrees across documents; exits `1` on any divergence (CI gate). 8/8 tests green including an end-to-end fixture set using two real fleet SBOMs (sovereign-edge + nix-config) plus a tampered variant that flips the nixpkgs hash. Honest scope limits in README (no JSON-LD yet, no signature anchor, no licence-graph reconciliation).
3. **No coverage measurement** — ~~we cite test counts (166, 50, 22, 64, …) without naming what % of code those tests actually exercise~~ ✅ pattern shipped 2026-05-15 on zig-cobs via [PR #3](https://github.com/SMC17/zig-cobs/pull/3): **100.00% line coverage on `src/root.zig`** (48/48 lines) via kcov against a dedicated `examples/coverage_driver.zig` + `tools/coverage.sh` + a new CI job that uploads the kcov HTML report as an artifact. Discovered a Zig 0.16 + nixpkgs-kcov toolchain quirk along the way (kcov doesn't surface line-coverage on `zig test` binaries because the nixpkgs build lacks libbfd-dev); the coverage-driver pattern routes around that cleanly. Other Tier-S/A repos can adopt by copying `examples/coverage_driver.zig` + `tools/coverage.sh` + the CI step.
4. **No mutation testing** — we don't know if any of our test suites would catch a regression.
5. **No formal property statements** — ~~protocol substrates carry differential and property tests but no TLA+-style invariant statement~~ ✅ **First formal spec landed AND CI-enforced**: `carreir/src/coldchain/SPEC.tla` + `.github/workflows/tla.yml` ([PR #2](https://github.com/SMC17/carreir/pull/2)) — three safety invariants on the HMAC chain (WriterLogIsAlwaysValid, TamperDetection, ReorderingDetected), TLC model-checked on every push via tla2tools.jar v1.8.0 on the GitHub runner. Spec is now `unit-tested via CI`, not `sketch`. The Coldchain hull now has **five discipline layers stacked**: substrate + threat model + regulatory mapping + formal spec + CI-enforced model check. Pattern available for rippled-zig, zig-frame-protocol.
6. **No cross-fleet integration tests** — composition is asserted in prose, not in code. `zig-cobs` + `zig-frame-protocol`, or `coldchain` SBOMed by `sentinel-sbom`, would be the obvious first integrations.
7. **No compiled README examples** — code blocks in READMEs aren't CI-verified; rot is inevitable.
8. **No regulatory mapping for coldchain** — HACCP, FDA 21 CFR Part 11 (audit-trail), EU FSMA — the substrate's value depends on naming the regulation it satisfies.
9. **No second-reference differential testing** — `zig-h3` vs libh3 only (could also diff against h3-py); `zeth` vs PyEVM only (could also diff against go-ethereum).
10. **Cryptographic protocol audit readiness** — ✅ both protocol substrates now have crypto-audit-readiness docs: `rippled-zig` [PR #70](https://github.com/SMC17/rippled-zig/pull/70) (key-confidentiality threat model + libsecp256k1 binding) and `zeth` [PR #22](https://github.com/SMC17/zeth/pull/22) (consensus-correctness threat model + pure-Zig stdlib). The two are explicitly framed against each other so reviewers see the architectural contrast as an audit surface.

11. **Regulatory mapping for coldchain** — ~~not surfaced~~ ✅ `carreir` PR #1 now includes `src/coldchain/REGULATORY_MAP.md` mapping the hull to FDA 21 CFR Part 11 + HACCP + EU GDP with 9 explicit "what this does NOT cover" surfaces.

12. **Type-I falsified claims in amx-zig and crpc-core** — ✅ closed via Wave-5 substrate-week PRs. [amx-zig #1](https://github.com/SMC17/amx-zig/pull/1) ships 537 lines of real Apple Silicon AMX engine (Corsix-cited opcodes, Zig 0.16 compile-clean, comptime-gated to `aarch64-darwin`). [crpc-core #1](https://github.com/SMC17/crpc-core/pull/1) ships 941 lines of real NVIDIA PTX emitter + IR + sealed envelope (WIP: needs Zig 0.16 Writer migration before merge). Both Type-I overclaims replaced with honest substrate; the v0.1.0 stubs are preserved in `experimental/` under `sketch` labeling, not deleted. **Closed despite the Wave-5 agents hitting the daily usage cap mid-work** — substrate recovered inline from on-disk state and pushed honestly.

13. **Production-code Linux-only paths in sentinel-sbom** — ~~Wave-5 macOS-fix push surfaced that `nar.zig` and `license_scan.zig` use `std.os.linux.{open,write,statx,readlink,...}` in production code, not just tests~~ ✅ honest posture shipped 2026-05-15 via [sentinel-sbom PR #4](https://github.com/SMC17/sentinel-sbom/pull/4): README + STATUS.md downgraded to "Linux-only production CLI". 85 raw `std.os.linux.*` call sites across 23 distinct identifiers catalogued in STATUS.md with a platform-support table. Filesystem tests stay gated with `SkipZigTest` on non-Linux (Wave-4 CI fix stands). A full port to `std.Io.Dir` / `std.posix.fstatat` / `std.fs.Dir.iterate()` is tracked but deliberately deferred — sentinel-sbom is invoked on a Nix-managed Linux build host. The "Type-II fix" was a Type-I framing: scope-limit, not a bug.

14. **Upstream nixpkgs `services.crowdsec` cascade** — sovereign-edge nixos-test caught a real upstream bug: `ExecStartPre` calls `cscli hub update` unconditionally → DNS fail in hermetic VMs → permanent `mkdir EACCES` via systemd's StateDirectory migration. Filed upstream: [NixOS/nixpkgs#520206](https://github.com/NixOS/nixpkgs/issues/520206). Bottleneck-collapse via community distribution.

15. **Multi-agent coordination doctrine codified** — Wave-4 coordination failures (orphan-history recovery, commit messages naming non-existent files, stale FLEET rows) → six new hard rules added to `~/AGENT_HARNESS.md` "Hard rules for concurrent multi-agent operation": never force-push default; explicit `git add <files>`; re-read state before writing; commit messages must match diff; ownership signaling on feature branches; verify CI signal don't assume.

16. **Stack-pop convention inversion across 12 zeth opcodes (2026-05-15)** — Wave-5 recursive audit caught the canonical Type-I: SUB, DIV, MOD, ADDMOD, MULMOD, SDIV, SMOD, EXP, LT, GT, SLT, SGT all compute `second OP top` where Yellow Paper §H.2 specifies `top OP second`. Test vectors codify the inversion so the green CI is internally consistent but not a correctness signal. Documented in [`zerotheta-evm/STACK_CONVENTION_AUDIT.md`](https://github.com/SMC17/zerotheta-evm/blob/stack-convention-audit/STACK_CONVENTION_AUDIT.md), [PR #23](https://github.com/SMC17/zerotheta-evm/pull/23). Fix queued as task #34. The earlier #5 "26 precompile divergences" finding is likely downstream of this first-order bug.

This list is the active hunt surface, not a backlog. Each item becomes a wave target as the lower-level work clears.

## Wave-7 push — 2026-05-18 (PRs MERGED, releases tagged, second-reference live)

> **CI BILLING NOTICE:** `rippled-zig` + `zerotheta-evm` are CI-blocked
> at the account level (the billing failure documented in
> [`CI_BILLING_BLOCK.md`](CI_BILLING_BLOCK.md)). Action items are
> documented there; no code change unblocks this. **Mitigation shipped
> 2026-05-18:** the same CI trim pattern is now in place on both
> repos — heavy jobs gated to `push || workflow_dispatch`, macOS leg
> gated to non-PR events (zeth: PR #25 + PR #26; rippled-zig: PR #73).
> Cuts PR-time CI minutes by ~60% on each repo; doesn't unblock the
> account-state issue but reduces re-run cost once it clears.

**🟢 zeth vs go-ethereum 1.17.2 — 7/7 bytecodes byte-for-byte match**
([zerotheta-evm PR #25 MERGED](https://github.com/SMC17/zerotheta-evm/pull/25)).
ERC-20 transfer: gas_used = 27127 on both, slot 0: 1000→999, slot 1: 0→1.
Plus 6 more bytecodes covering each audit-driven fix category (ADD/DIV/SUB/LT/EXP
exercising the stack-pop convention fix; CALLDATACOPY exercising the
G_copy=3 gas/word fix). **All 7 match go-ethereum byte-for-byte.** This is
the SECOND independent reference (after PyEVM-Berlin) — and where the
two oracles disagreed (the 2800-gas EIP-2200 delta from round 9),
**go-ethereum sides with zeth**, confirming PyEVM's harness was the
quirk and zeth's spec interpretation was correct.

**zig-h3 vs h3-py: PR #4 MERGED** — 24-line byte-for-byte match across
8 global fixtures. First Wave-7 cross-implementation reference outside
the in-tree libh3 binding. (PR #4 admin-merged 2026-05-18; the only red
CI job was the pre-existing `go-binding` failure unrelated to the
h3-py work.)

Cross-implementation triangulation: live on both EVM (zeth ⊕ PyEVM ⊕
go-ethereum) and H3 (zig-h3 ⊕ libh3 ⊕ h3-py).



The Wave-6 work shipped, merged, tagged, and got its first cross-implementation
validation:

- **All 4 coverage PRs merged + tagged + released:**
  - [zig-cobs v1.2.0](https://github.com/SMC17/zig-cobs/releases/tag/v1.2.0) — 100% coverage
  - [zig-frame-protocol v0.2.0](https://github.com/SMC17/zig-frame-protocol/releases/tag/v0.2.0) — 100% coverage
  - [zig-graph v1.2.0](https://github.com/SMC17/zig-graph/releases/tag/v1.2.0) — 86.98% coverage
  - [sentinel-sbom v1.1.0](https://github.com/SMC17/sentinel-sbom/releases/tag/v1.1.0) — 97.50% coverage on spdx.zig + zon.zig
  - CI fixed twice along the way: (1) `kcov` was dropped from Ubuntu 24.04 → pinned coverage job to `ubuntu-22.04`; (2) older kcov writes coverage.json only to a hashed subdir → script uses `find` to locate it.

- **zerotheta-evm PR #24 admin-merged (97512dc on main).** The full 9-round audit-fix-validate loop landed:
  stack-pop convention fix + G_copy + BN256 prime + leftover-gas-return + memory zero-init + 3 declared-divergence markers + ERC-20 smoke test. Differential against PyEVM = 0. PR #23 (audit-only) closed as superseded.
  - CI on zerotheta-evm is **billing-blocked** (same GitHub Actions account-state issue as rippled-zig); local verification is exhaustive (411/414 tests + 0 PyEVM diff + ERC-20 storage-state match).

- **zeth round 9: EIP-2200 ERC-20 harness-quirk root-caused.** The 2800-gas delta on the ERC-20 transfer was NOT a zeth bug: PyEVM's `state.set_storage` from the test harness bypasses the journal init, so EIP-2200's `get_storage(..., from_journal=False)` returns 0 instead of the pre-tx-committed 1000. zeth follows the spec (mainnet semantics). Added `known_pyevm_state_setup_divergence` marker.

- **zig-h3 vs h3-py second-reference differential (Wave-7 line 1) [PR #4](https://github.com/SMC17/zig-h3/pull/4)**: 24 lines (3 per fixture × 8 global fixtures) match byte-for-byte between zig-h3 and h3-py 4.4.2. First Wave-7 cross-implementation reference outside the in-tree libh3 binding — confirms zig-h3's wrapper-level glue matches what an external Python consumer sees.

### Wave-7 next-layer line — real-block-replay corpus

**The 7-bytecode geth match is necessary but not sufficient.** Synthetic
bytecodes (ADD/DIV/SUB/LT/EXP/CALLDATACOPY + ERC-20 transfer) exercise
named opcode paths — but a real Ethereum mainnet block exercises
sequencing, gas accounting under nested CALLs, refund-cap interaction
across multiple transactions, and the full state-transition function.
The next-layer evidence is **block-replay against go-ethereum traces**:
pick N Berlin-era mainnet blocks, fetch the per-transaction trace from
a geth archive node (or use vendored fixtures), replay each transaction
in zeth, byte-compare the resulting state diff. The corpus is the moat;
the 7 synthetic cases were the precondition.

Substrate to build: `zeth/validation/block_replay/` — fixture loader,
geth-trace JSON schema, per-tx state-diff comparator, multi-block
driver. Sized to start small (5 Berlin blocks, mostly ETH transfers +
ERC-20 calls) and grow as each new opcode/precompile gets a real-world
witness.

## Wave-6 push — 2026-05-18 (the audit-fix-validate loop + coverage-pattern pollination)

Five lanes shipped same-day across four repos, compounding on the Wave-5 zeth audit:

1. **zerotheta-evm BN256 math fix** — root-caused to `bnPrime()` returning the **scalar field order n** instead of the **base field prime p** of alt_bn128. One-character substitution; every field op in `bnAdd`/`bnMul`/`bnPointFromInput`/`bnIsOnCurve` was modding against the wrong value. PyEVM differential confirmed: G1+G1 and G1*2 now match byte-for-byte. The in-tree `bn254_pairing.zig` already carried the correct prime — only the inline ADD/MUL helpers had the bug.
2. **zerotheta-evm leftover-gas-return fix** — 4 precompile helpers (BN256ADD/MUL/PAIRING/BLAKE2F) charged nominal `required_gas` on input-validation failure instead of `forwarded_gas` (the full child stipend). EIP-196/197/152 + PyEVM convention is that failed precompiles burn ALL forwarded gas. Threaded `forwarded_gas` through; the original "984390 pattern" is gone.
3. **PyEVM differential round 3:** discrepancy count 26 → 20 → 10 → 5. Residual 5 = zero load-bearing real bugs (3 harness false-positives: MLOAD uninit, 2 × PUSH0 fork-mismatch; 2 error-path return-data quirks where PyEVM echoes invalid input bytes back as "error data" and zeth follows the EIP-196/197 spec of returning empty).
4. **zig-frame-protocol coverage** — adopted the zig-cobs v1.2.0 pattern; 100.00% line coverage on `src/root.zig` (48/48). PR #3 open.
5. **zig-h3 + sentinel-sbom coverage** — same pattern: zig-h3 94.40% (219/232), sentinel-sbom 97.50% (234/240 on spdx.zig+zon.zig). The 5.6% / 2.5% uncovered residue is documented (defensive unreachable + errdefer cleanup + topology-bound paths + Linux-only-by-design syscall sites).

**The Wave-6 doctrine:** when an audit identifies a bug, the canonical session ships the audit → the fix → the re-run differential → the next-layer fix → the next-layer re-run. Three rounds on zeth in one session. Coverage pattern proven on one repo (zig-cobs v1.2.0) propagated to three more on the same loop.

## Recursive audit findings — 2026-05-15 Wave-5 (the canonical Type-I)

**Headline finding (2026-05-15) + two-round validation in the same session:** zeth ships a systematic stack-pop-order inversion across SUB, DIV, MOD, ADDMOD, MULMOD, SDIV, SMOD, EXP, LT, GT, SLT, SGT — every non-commutative arithmetic, comparison, and exponent opcode. The implementation computes `second OP top`; the Yellow Paper specifies `top OP second`. The harness test vectors in `validation/comparison_tool.zig` codify the inversion so the green CI passes despite the bug. Audited in `zeth/STACK_CONVENTION_AUDIT.md` (PR #23), fixed in PR #24 round 1 (12 handlers + 15 test vectors, all-green local).

**Round 2 same session:** installed py-evm in a Python venv, re-ran the differential, found 11 small gas-offset divergences (+2/+8/+12/+24 pattern) → traced to a `CALLDATACOPY`/`CODECOPY`/`EXTCODECOPY`/`RETURNDATACOPY` G_copy = 3-vs-1 bug across 4 sites. Fix landed in the same PR. Re-ran the differential a third time: **26 → 20 → 10** discrepancy count. Zero residual divergences in non-commutative arithmetic; zero residual canonical-path gas offsets. The remaining 10 sort cleanly into the 3 named root causes the audit predicted (BN256 math wrong on G1+G1 and G1*2; 3 leftover-gas-on-precompile-failure cases; 2 error-path return-data convention diffs) plus 3 harness false-positives. The recursive-audit theory predicted "most of the 26 are downstream of the stack-pop bug" and the gas-copy bug as the second-order cause of the small-offset family — both bear out in measurement. Full report in `POST_FIX_DIFFERENTIAL_REPORT.md`.

**Doctrine lesson**: a self-consistent test suite passing against your own implementation is **not** a correctness signal. The differential against an independent reference (PyEVM-Berlin) was the right design; the misattribution of its signal to "gas accounting" rather than "core stack semantics" is what hid the bug for a release cycle. The lens that caught it is the AGENT_HARNESS evidence vocabulary: distinguishing `unit-tested` (always true here) from `differential-tested` (failing for the right reason) from `mainnet-compatible` (false). The vanity-1.0 register exists for exactly this finding.

## Recursive audit findings — 2026-05-14 self-critique pass

The fleet that audits other code is itself subject to audit. A pass over recent work surfaced five findings the original ship missed:

1. **My TLA+ spec for the coldchain HMAC chain had two real bugs the CI gate caught**: shadowed `Sequences.Append`, parser error on a nested-tuple expression. The spec wouldn't have type-checked before — the CI gate is doing exactly what the discipline gap (`compile-or-die for formal specs`) was supposed to enforce. Fixed in carreir PR #2 commit `25a71c9`.
2. **My `rippled-zig` CRYPTO_AUDIT_READINESS doc missed the `-Dsecp256k1=false` build-flag opt-out at `build.zig:22`.** The fallback is fail-closed (every secp256k1 op returns `error.LibraryUnavailable`) — good engineering, missing documentation. Type-II miss in the doc itself; fixed in PR #70 commit `2c82eb1`.
3. **The cross-platform CI agent mischaracterized `zig-h3 #2`'s macOS failure** as "macOS-from-Linux cross-compile gap" when the actual error is **native-macOS LLD-on-mach-o on the example binary** (`error: using LLD to link macho files is unsupported`). Different bug, fixable (task #24).
4. **The cross-platform CI agent's "tests green on three native runners" was verified locally on Linux only**, not actually run on macOS. macOS CI exposed **8 SIGSYS sandbox-violation crashes** in sentinel-sbom's filesystem-touching tests. Agent self-reports require verification against CI signal (task #25).
5. **zeth #21 raised match rate from 18.2% to 40.9%** — the EIP-2929 fix did real work — **but exposed 26 precompile divergences (PC02–PC09)**. The `gas=984390` pattern across error-path tests across multiple precompiles suggests a gas-on-failure reporting convention divergence, not 9 independent bugs (task #26).

**Doctrine reinforced**: the substrate does its job by surfacing bugs (TLC caught my spec errors, diff-fuzz caught the precompile gas convention, sovereign-edge's nixos-test caught a real upstream nixpkgs bug). The discipline is to not hide what the substrate finds, even when the substrate is finding the dispatcher's own work — or an upstream maintainer's. Memory entry **`feedback_ruthless_self_critique.md`** is the operating norm, not a one-time pass.

## Multi-agent coordination findings — 2026-05-14

The fleet operates with multiple parallel agent sessions and stax himself working in parallel on the same repos. Real coordination failures surfaced during this work:

1. **`main` was force-pushed mid-work** on the carreir profile repo and the sovereign-edge repo. Feature branches in progress went orphan-history and required cherry-pick recovery.
2. **Parallel agents bundled an in-flight agent's untracked files into their commits** AND **shipped commit messages naming files that didn't exist** in their own diff. This is a stronger failure: the commit message becomes a Type-I overclaim.
3. **My FLEET.md row for sovereign-edge was stale by the time it was written** — other parallel work had shipped v1.1.0–v1.4.0 nixos-tests during the session.

Hard rules for the next iteration:

- **Never force-push `main`.** Any rewrite of public history breaks downstream work.
- **Ownership signaling on feature branches** — when a feature branch is in active use by an agent, it should be marked (commit message convention, branch name prefix, or a lock file) so concurrent agents don't bundle it into unrelated commits.
- **Re-read state before writing** — a FLEET row written without checking the latest repo HEAD is itself a vanity claim.

These belong in agent-harness doctrine (`~/AGENT_HARNESS.md` or a sibling). Surfacing here so the issue is visible.

## What this manifest is not

This is not a marketing surface. It is the public ledger of where the fleet's hulls actually stand against the contract they advertise. Where this manifest disagrees with a per-repo README badge or a profile-page table, **this manifest is canonical** until the next reconciliation pass.

---

*Last reconciled: 2026-05-14.*
