# Fleet Manifest

**Field:** Quantitative Mercantilism
**Practice:** Verifiable Fleet Engineering

Composable, correctness-first systems with strong auditability and replaceability — modern equivalents of well-built ships that operate independently, are repaired at sea, and compose into larger fleets. This manifest is the honest register of every public repo against the *honest-1.0 contract* below. Where a repo does not yet earn `v1.0`, this document says so plainly; the GitHub tag will be reconciled to match.

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
| [sovereign-edge](https://github.com/SMC17/sovereign-edge) | A — tag/README mismatch | v1.0.0 | ✓ | `compiled` (Phase 2, not runtime-verified) | Caddy + Coraza + Knot DNS NixOS bundle. README correctly says "closure-builds, not runtime-verified"; tag claims v1.0. **Action: earn v1.0 by deploying to a real VPS and capturing the runtime-verified evidence the README itself names as missing.** |
| [sentinel-sbom](https://github.com/SMC17/sentinel-sbom) | **S** (Wave 1 verified) | v0.6.0 (HEAD commit-stamped 1.0.2; tag not yet pushed) | ✓ | `unit-tested` (62/62) + `audited` (NAR encoder, one corpus) | Nix `flake.lock` → SPDX 2.3 SBOM, narHash verification. Overclaim language ("verified end-to-end", "production") replaced with honest evidence vocab. Path to honest v1.0.2 tag push = stax's call. |
| [sovereign-offense-harness](https://github.com/SMC17/sovereign-offense-harness) | A — tag/README mismatch | v1.0.0 | ✓ | `unit-tested` (`v0.3.1 early` per README) | Adversary-emulation runner with safety gates. README correctly says `v0.3.1 — early`; tag claims v1.0. **Action: bring the next push under v0.3.x until the threat-model coverage + ART corpus the README names is real.** |

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
| [amx-zig](https://github.com/SMC17/amx-zig) | _unaudited_ | — | Not yet on disk; needs clone + audit. |
| [crpc-core](https://github.com/SMC17/crpc-core) | _unaudited_ | — | Not yet on disk; needs clone + audit. |
| [fivem-ship-and-sell](https://github.com/SMC17/fivem-ship-and-sell) | _unaudited_ | — | Not yet on disk; needs clone + audit. |

## Reconciliation plan

The vanity-push problem is corrected by doing the work the tag promised, in this priority order:

1. **Earn the tag (preferred).** Close the gaps the contract names — fix the failing CI gate, add the missing tests, surface real benchmarks, close stubs in critical paths, build out the substrate. This is the default move for every repo. The point of carrying `v1.0` is to honor it.
2. **Reconcile tag/README mismatch.** Where the per-repo README already correctly concedes early state (mast `v0.1.0 commit-zero`, sovereign-edge "Phase 2 — closure-builds, not runtime-verified", sovereign-offense-harness `v0.3.1 — early`), the *tag* is what lies — the README is honest. Bring the next push under the version the README already names.
3. **Expand the substrate.** For stub repos (carreir, sovereign-emacs) carrying a tag the SLOC can't justify: scale the substrate to match. The substrate, not the tag, is what's load-bearing.

No silent downgrades. Every reconciliation is committed with a CHANGELOG entry that names what changed and why. When a downgrade is unavoidable, it is honest, public, and accompanied by a concrete plan to re-earn the version.

## What this manifest is not

This is not a marketing surface. It is the public ledger of where the fleet's hulls actually stand against the contract they advertise. Where this manifest disagrees with a per-repo README badge or a profile-page table, **this manifest is canonical** until the next reconciliation pass.

---

*Last reconciled: 2026-05-14.*
