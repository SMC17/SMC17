## Sean Collins — `SMC17`

**Quantitative Mercantilism through Verifiable Fleet Engineering.**

I design and implement composable, correctness-first systems with strong auditability and replaceability — modern equivalents of well-built ships that operate independently, are repaired at sea, and compose into larger fleets.

Drawn to the intersections of human behavior, decision systems, and market mechanisms as drivers of innovation and long-term progress. I build verifiable substrates at these intersections by combining systems engineering rigor with data science, economics, and cognitive science.

→ [**FLEET.md**](FLEET.md) is the canonical, honest-1.0 ledger for every repo below. Where this README and `FLEET.md` disagree on a tag or evidence level, `FLEET.md` is authoritative until the next reconciliation pass.

---

### Substrate — small libraries that compose

Building blocks. Each is meant to be lifted into other Zig projects without dragging in the rest of the stack.

| Repo | What | Tier | Tag |
|---|---|---|---|
| [**zig-h3**](https://github.com/SMC17/zig-h3) | H3 v4 spatial index — idiomatic libh3 wrapper **+ a 7,280-line pure-Zig port**, 117 cross-validation tests against the C reference, 166/166 tests in 2 s. | **S** | `v1.1.0` |
| [**zig-cobs**](https://github.com/SMC17/zig-cobs) | Pure-Zig, zero-alloc COBS framing. 22/22 tests + 117 k-trial fuzz on every push. No dependencies beyond the standard library. | **S** | `v1.1.0` |
| [**zig-graph**](https://github.com/SMC17/zig-graph) | Sparse undirected graph + spectral algorithms (eigenvector centrality, PageRank with correct dangling-node handling, conductance). 50/50 tests; 10,360 fuzzed graphs across 4 harnesses. | **A** | `v1.1.0` |
| [**zig-frame-protocol**](https://github.com/SMC17/zig-frame-protocol) | Versioned binary frame protocol on COBS. 15 unit + 6 fuzz tests (100 k random-wire never-panic + ~11 k CRC bit-flip sweep). Composes with `zig-cobs`. | **A** | `v1.0.0` |

### Protocol implementations — full execution surfaces in Zig

End-to-end, correctness-first implementations of real protocols.

| Repo | What | Tier | Tag | Note |
|---|---|---|---|---|
| [**zeth**](https://github.com/SMC17/zeth) | Ethereum Virtual Machine in Zig. 263 unit tests, state journaling, WASM + RISC-V cross-compile. | D — under repair | `v1.0.0` | Differential fuzz against PyEVM-Berlin found a real EIP-2929 violation in the CALL family (4 opcodes double-charging 700 gas). The substrate did its job; Wave-3 fix PR incoming. |
| [**rippled-zig**](https://github.com/SMC17/rippled-zig) | XRPL protocol toolkit — canonical transaction encoding, signing-hash, secp256k1/Ed25519 verification, live testnet RPC conformance. | D — under repair | `v1.0.1` | Gate C structurally never converges (no cross-run persistence layer); Gates D/E/Sim share the bug; Gate E also fails on `panic() in src`; Sim invariant fails. Substantive crypto checks pass. Wave-3 multi-gate fix PR incoming. |

### Editor substrate — the appliance-layer surface

The editor surface is one of the eight axes of the appliance-layer thesis. The kernel ships running code under AGPL; the Elisp companion under GPL.

| Repo | What | Tier | Tag | Note |
|---|---|---|---|---|
| [**mast**](https://github.com/SMC17/mast) | Single-binary editor kernel. Buffer-as-protocol, Janet embedded for extensibility, AGPL-3.0-or-later. Linux x86_64 + Apple Silicon arm64. File-write buffers + atomic save shipped in v1.1; capability-model sandbox first-slice in progress. | A | `v1.1.0` | Visual TUI, local-inference daemon, multi-buffer state, native Windows still on the roadmap (explicit in README). |
| [**sovereign-emacs**](https://github.com/SMC17/sovereign-emacs) | Emacs-Lisp companion to `mast`. 1,922 Elisp lines + 545 test lines across 7 modules; `sovereign-eval.el` v1.4 has a JSONL recorder/replayer with SHA-256 hash diff + `defcase` CI gate. GPL-3.0-or-later (AGPL §13 doesn't apply — local filesystem only). | A | `v1.0.0` | Reposition + license-consistency + experimental mast-bridge in [PR #1](https://github.com/SMC17/sovereign-emacs/pull/1). |

### Public writing — the merchant lens applied

| Repo | What | Tag |
|---|---|---|
| [**stax-blog**](https://github.com/SMC17/stax-blog) | *Stax — The Journal of Quantitative Mercantilism.* The Mercantile Thesis plus the Anti-Edison / Lineage / Doctrine arcs. Live at [smc17.github.io/stax-blog](https://smc17.github.io/stax-blog/). | `v1.0.0` |
| [**stax-doctrine**](https://github.com/SMC17/stax-doctrine) | The operating playbook of Quantitative Mercantilism — doctrine essays + frontier-lab playbooks. | `v1.0.0` |

### Sovereign Stack — infrastructure I can run without a vendor

Each of these targets a piece of the stack normally rented from a hyperscaler or SaaS, and replaces it with something hostable on iron I control.

| Repo | What | Tier | Tag | Note |
|---|---|---|---|---|
| [**sovereign-edge**](https://github.com/SMC17/sovereign-edge) | Cloudflare-shaped edge bundle as composable NixOS modules: Caddy + Coraza WAF + nftables + Knot DNS (DNSSEC) + CrowdSec. | A | `v1.0.0` (README: "Phase 2 — closure-builds, not runtime-verified") | README correctly names early state; tag overshoots. Path to honest v1.0 is a deployed VPS reference run. |
| [**sentinel-sbom**](https://github.com/SMC17/sentinel-sbom) | Nix `flake.lock` → SPDX 2.3 SBOM emitter. Single Zig binary, in-tree `narHash` verification. AGPL-3.0. 64/64 tests + 1,500-trial determinism property harness on every push. | **S** | `v1.0.3` | Wave-1 reconciled to honest evidence vocabulary; Wave-3 shipped v1.0.2 + v1.0.3 releases. |
| [**sovereign-offense-harness**](https://github.com/SMC17/sovereign-offense-harness) | Adversary-emulation runner — safety-gated, allow-listed targets, signed audit envelopes. | A | `v1.0.0` (README: `v0.3.1 — early`) | README correctly names early state; tag overshoots. TTP-corpus expansion is the path to honest v1.0. |

### Knowledge bases — research substrate that gets cited, not just read

| Repo | What | Tier | Tag |
|---|---|---|---|
| [**oceanman**](https://github.com/SMC17/oceanman) | Submarine cable expert knowledge base — physics, owners, geopolitics, economics. 693 cables ingested with independent-agent Type-I error sweep. | B → A (Wave-3 PR) | `v1.0.0` |

---

### How to read this portfolio

- **Tiers are honest.** `S` = honest-1.0 verified (every contract check passes). `A` = credible, contract holds modulo minor polish. `B` = substantive code, missing one contract requirement (commonly: tests). `D` = under repair — CI red or stub size insufficient for the tag carried. The full contract is in [`FLEET.md`](FLEET.md).
- **Evidence vocabulary is fixed.** Per `AGENT_HARNESS.md`: `sketch / scaffold / compiled / unit-tested / integration-tested / audited / benchmarked / hardware-verified`. The words "verified," "production," "dominant," and "safe" require the specific evidence that makes them true.
- **Tests are the spec.** Where I claim parity with a reference (libh3, official `rippled`, Ethereum execution semantics, COBS RFC), there are cross-validation or differential tests against the reference. Where I don't make that claim, I say so. When the differential test catches a real bug in *my own* code — as it did with zeth's EIP-2929 violation — that is the substrate doing its job, not an embarrassment to be hidden.
- **No third-party hosted dependencies in the critical path.** The stack is meant to be portable across machines I control. Cloud is allowed only where the artifact is replaceable.
- **Reconciliation is public.** Where a tag overshoots what the README or CI supports, the gap is named here and in `FLEET.md` — and the fix is to *earn the tag*, not to silently downgrade it.

### What I'm not doing

- Token launches, ICOs, grant farming.
- Wrappers that add a thin layer over a third-party API and call themselves a product.
- AI-generated bulk content masquerading as research.

---

### Portfolio at a glance (auto-updated 2026-05-14)

| Surface | Count |
|---|---|
| Public repos in the substrate | **13** |
| Repos at v1.x milestone | **13** |
| Total tagged releases | **33+** |
| Published essays in the canon | **15** |
| Total published words | **54,471** |
| Average words per essay | **3,631** |
| Lighthouse on `stax-blog` homepage | **100 / 100 / 100 / 100** |
| Blog CI status | Green |

All public repos carry: LICENSE (AGPL-3.0 for substrate, MIT for primitives, GPL for the Elisp companion), README, CONTRIBUTING, SECURITY, CHANGELOG, CI workflow, Dependabot, CODEOWNERS, and branch protection (no force-push, no deletion).

---

*Calculemus — "let us calculate," from Leibniz's `calculus ratiocinator`. The aspiration is to make disputes settleable by computation rather than rhetoric.*
