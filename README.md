## Sean Collins — `SMC17`

Building a sovereign stack of composable, auditable substrate — most of it in Zig, all of it solo, none of it dependent on a third party I can't replace.

Each repo below is a load-bearing piece. Several already compose into the others.

---

### Substrate — small libraries that compose

Building blocks. Each is meant to be lifted into other Zig projects without dragging in the rest of the stack.

| Repo | What | Status |
|---|---|---|
| [**zig-h3**](https://github.com/SMC17/zig-h3) | H3 v4 spatial index — idiomatic libh3 wrapper **+ a 100% pure-Zig port** with 142 cross-validation tests against the C reference. | `v1.0.0` |
| [**zig-cobs**](https://github.com/SMC17/zig-cobs) | Consistent Overhead Byte Stuffing framing — zero-alloc, no-dependency, embedded-friendly. | `v1.0.0` |
| [**zig-graph**](https://github.com/SMC17/zig-graph) | Sparse undirected graph + spectral algorithms (eigenvector centrality, PageRank, cut/conductance). | `v1.0.0` |
| [**zig-frame-protocol**](https://github.com/SMC17/zig-frame-protocol) | Versioned binary frame protocol — COBS-framed, CRC32, opaque kind byte. Composes with `zig-cobs`. | `v1.0.0` |

### Protocol implementations — full execution surfaces in Zig

End-to-end, correctness-first implementations of real protocols.

| Repo | What | Status |
|---|---|---|
| [**zeth**](https://github.com/SMC17/zeth) | Ethereum Virtual Machine in Zig. 263 tests, 142/143 opcodes dispatched, precompiles 0x01–0x09, state journaling, WASM + RISC-V cross-compile. | `v1.0.0` |
| [**rippled-zig**](https://github.com/SMC17/rippled-zig) | XRPL protocol toolkit — canonical transaction encoding, signing-hash, secp256k1/Ed25519 verification, live testnet RPC conformance. Quality gates A–E green. | `v1.0.1` |

### Editor substrate — the appliance-layer surface

The editor surface is one of the eight axes of the appliance-layer thesis. This is the one I commit to in running code under AGPL.

| Repo | What | Status |
|---|---|---|
| [**mast**](https://github.com/SMC17/mast) | Single-binary editor kernel. Buffer-as-protocol, Janet embedded for extensibility, AGPL-3.0-or-later. Linux x86_64 + Apple Silicon arm64. Composes with the stax CLI fleet through built-in `M-x` commands. | `v1.1.0` |

### Public writing — the merchant lens applied

| Repo | What | Status |
|---|---|---|
| [**stax-blog**](https://github.com/SMC17/stax-blog) | *Stax — The Journal of Quantitative Mercantilism.* The Mercantile Thesis plus the Anti-Edison / Lineage / Doctrine arcs. Live at [smc17.github.io/stax-blog](https://smc17.github.io/stax-blog/). | `v1.0.0` |
| [**stax-doctrine**](https://github.com/SMC17/stax-doctrine) | The operating playbook of Quantitative Mercantilism — doctrine essays + frontier-lab playbooks for sovereign engineering teams. | `v1.0.0` |

### Sovereign Stack — infrastructure I can run without a vendor

Each of these targets a piece of the stack that's normally rented from a hyperscaler or SaaS, and replaces it with something I can host myself.

| Repo | What | Status |
|---|---|---|
| [**sovereign-edge**](https://github.com/SMC17/sovereign-edge) | Open Cloudflare-class edge bundle as composable NixOS modules: Caddy + Coraza WAF + rate-limiting + observability. | `v1.0.0` |
| [**sentinel-sbom**](https://github.com/SMC17/sentinel-sbom) | Nix `flake.lock` → SPDX 2.3 SBOM emitter. Single Zig binary, in-tree `narHash` verification. AGPL-3.0. | `v1.0.1` |
| [**sovereign-offense-harness**](https://github.com/SMC17/sovereign-offense-harness) | Adversary-emulation runner — safety-gated, allow-listed targets, signed audit envelopes. | `v1.0.0` |

### Knowledge bases — research substrate that gets cited, not just read

| Repo | What | Status |
|---|---|---|
| [**oceanman**](https://github.com/SMC17/oceanman) | Submarine cable expert knowledge base — physics, owners, geopolitics, economics. 693 cables ingested with independent-agent verification of Type-I errors. | `v1.0.0` |

---

### How to read this portfolio

- **Versions are honest.** `v0.1.0` means working, tested, and useful — not "ready for your production cluster." If something hasn't earned a number yet, it doesn't have one.
- **Tests are the spec.** Where I claim parity with a reference (libh3, official `rippled`, Ethereum execution semantics), there are cross-validation or differential tests against the reference. Where I don't make that claim, I say so.
- **No third-party hosted dependencies in the critical path.** The stack is meant to be portable across machines I control. Cloud is allowed only where the artifact is replaceable.

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
| Total tagged releases | **33** |
| Published essays in the canon | **15** |
| Total published words | **54,471** |
| Average words per essay | **3,631** |
| Lighthouse on `stax-blog` homepage | **100 / 100 / 100 / 100** |
| Blog CI status | Green |

All public repos carry: LICENSE (AGPL-3.0 for substrate, MIT for primitives), README, CONTRIBUTING, SECURITY, CHANGELOG, CI workflow, Dependabot, CODEOWNERS, and branch protection (no force-push, no deletion).

---

*Calculemus — "let us calculate," from Leibniz's `calculus ratiocinator`. The aspiration is to make disputes settleable by computation rather than rhetoric.*
