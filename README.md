```
                              |    |    |
                             )_)  )_)  )_)
                            )___))___))___)\
                           )____)____)_____)\\
                         _____|____|____|____\\\__
                ~~~~~~~~ \                         /  ~~~~~~~~~
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

```
███████╗███╗   ███╗ ██████╗ ██╗███████╗
██╔════╝████╗ ████║██╔════╝███║╚════██║
███████╗██╔████╔██║██║     ╚██║    ██╔╝
╚════██║██║╚██╔╝██║██║      ██║   ██╔╝
███████║██║ ╚═╝ ██║╚██████╗ ██║   ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝   ╚═╝
```

# SEAN COLLINS

**Skate to where the puck is going.**

I'm building **ZeroTheta** — a sovereign Layer-0 hyperstructure. Zig at the metal, Elixir on the wire. Single binaries, formal specs, no vendors in the critical path.

§

## PRINCIPLES — QUANTITATIVE MERCANTILISM

1. **Durable wealth flows to whoever owns the bottleneck.** Scalp spreads and you depend on the spread; own the substrate and the spread comes to you. Direct flows. Don't scalp.
2. **The substrate is the moat. The audit is the proof. Tests are the spec.** Sequence matters: substrate before distribution.
3. **Foundation-first.** No upper layer until the layer beneath is solid. Parallel within a layer; never across.
4. **Evidence vocabulary is fixed.** `sketch · scaffold · compiled · unit-tested · integration-tested · audited · benchmarked · hardware-verified`. The words *verified*, *production*, *safe*, *complete* require the specific evidence that makes them true. Used decoratively, they are lies.
5. **Type I and Type II are the two failure modes.** Type I — accepting a false claim. Type II — missing real value or real risk. Audit for both. Name both.
6. **Single binaries. Formal specs. No vendors in the critical path.**
7. **Update priors when proved wrong, same session.** Loyalty is to evidence, not to old doctrine.

§

## ARCHITECTURE — FOUR PILLARS

| Pillar | Function | Substrate |
|:---|:---|:---|
| **`cells/`** | Compute units. Single-binary Zig kernels. Editor, EVM, sentinel, edge. | Zig 0.16 |
| **`nervous_system/`** | Orchestration. Soft-realtime fan-out, supervision, hot-reload. | Elixir / OTP |
| **`protocols/`** | Wire formats. COBS, framed binary, EVM bytecode, XRPL, SPDX. | Zig + TLA+ |
| **`blueprints/`** | NixOS modules. Reproducible iron, declarative edge, audited closure. | Nix flakes |

§

## FLAGSHIP — PUBLIC

| Repo | Function | Status |
|:---|:---|:---|
| [**mast**](https://github.com/SMC17/mast) 🚢 | Single-binary editor kernel. Buffer-as-protocol. Janet embedded. AGPL. 7,200-trial property corpus + buffer-protocol benchmark. | `v1.2.0` |
| [**zig-h3**](https://github.com/SMC17/zig-h3) | H3 v4 spatial index. Idiomatic Zig wrapper covering all 70 public functions + 7,280-line pure-Zig port. 190 tests across wrapper, cross-validation matrix, fuzz, property, mutation, resolution sweep. CI on Linux x86_64 + Linux aarch64 + macOS arm64. | `v1.4.1` |
| [**sovereign-edge**](https://github.com/SMC17/sovereign-edge) | Cloudflare-shaped edge in NixOS modules. Caddy + Coraza WAF + nftables + Knot DNS + CrowdSec. Multi-scenario `nixos-test` integration matrix. | `v1.4.0` |
| [**sentinel-sbom**](https://github.com/SMC17/sentinel-sbom) | Nix `flake.lock` → SPDX 2.3 SBOM. Single Zig binary. 64 tests + 1,500-trial determinism harness + in-tree narHash verify. | `v1.1.0` |
| [**sovereign-offense-harness**](https://github.com/SMC17/sovereign-offense-harness) | Adversary-emulation runner. Refuse-by-default unless `--target <IP>` matches a whitelist. Deterministic-shape JSON audit envelopes with per-stream SHA-256. EXPERIMENTAL Atomic Red Team adapter. | `v1.0.0` |
| [**agent-app-control**](https://github.com/SMC17/agent-app-control) | Linux desktop computer-use CLI. Hyprland + wtype + ydotool substrate. Capability gates, intent flags, trace log. | `v0.6.0` |

Full ledger with Honest-1.0 contract per repo: [`FLEET.md`](FLEET.md).

§

## STAX EDITIONS — DROP HOUSE

Quarterly capsule format: object + essay + software + audio, the same idea expressed in four substrates.

| № | Capsule | Object spec | Companion essay | Software | Audio | Status |
|:---|:---|:---|:---|:---|:---|:---|
| **I** | Phonograph | [/objects/phonograph](https://stax.dev/objects/phonograph) | [Sonos S2 touchscreen monoculture](https://stax.dev/posts/sonos-s2-touchscreen-monoculture) | Music client PWA (AGPL) | Phonograph Object Lesson (40 min) | shipped |
| **II** | Almanac | [/objects/almanac](https://stax.dev/objects/almanac) | [Daily page as computation](https://stax.dev/posts/daily-page-as-computation) | Almanac universal display | January Rockefeller (34 min); Feb-Apr in production | spec + display + 1/12 audio |
| **III** | Lineage Album Vol I | [/objects/lineage-album-vol-i-anti-edison](https://stax.dev/objects/lineage-album-vol-i-anti-edison) | [10-essay Anti-Edison arc](https://stax.dev/canon/anti-edison/) | — | 90-min LP in production | spec + arc shipped |
| **IV** | The Codex Deck | [/objects/codex-deck](https://stax.dev/objects/codex-deck) | The card as the smallest useful unit of canon | Companion PWA | 12 figure-audios | spec only |

§

## METHODOLOGY

| Repo | Function | Status |
|:---|:---|:---|
| [**stax-harness**](https://github.com/SMC17/stax-harness) | Public methodology for multi-agent engineering. Three docs: operating model, response standard, 8-level proof vocabulary + Type-I/Type-II audit lens. The substrate the fleet runs on. | `v0.1.0` |
| [**stax-experiment**](https://github.com/SMC17/stax-experiment) | Append-only experiment register. Single Zig binary, flock-protected JSONL. Forces pre-registered hypothesis + falsifier before tests, tracks Type-1 (overclaim) and Type-2 (missed-risk) catches on the agent's own work. | `v0.2.0` |

§

## SUBSTRATE PRIMITIVES

| Repo | Function | Status |
|:---|:---|:---|
| [**zig-cobs**](https://github.com/SMC17/zig-cobs) | Consistent Overhead Byte Stuffing in pure Zig. Zero alloc, no deps. 22 tests + 117k-trial fuzz/push. | `v1.2.0` |
| [**zig-frame-protocol**](https://github.com/SMC17/zig-frame-protocol) | Versioned binary frame protocol on COBS. CRC32, opaque kind byte. 100k random-wire fuzz + ~11k bit-flip sweep at 98.4% catch. | `v0.2.0` |
| [**zig-graph**](https://github.com/SMC17/zig-graph) | Sparse undirected graph + spectral algorithms (centrality, PageRank, conductance). 50 tests + 10k random-graph property suite. Closed-form `λ₁` match to 1e-6 on canonical graphs. | `v1.2.0` |
| [**fleet-sbom-index**](https://github.com/SMC17/fleet-sbom-index) | Cross-fleet SPDX SBOM divergence detector. Companion to `sentinel-sbom`. Exits non-zero on any `(name, version) → SHA256` disagreement across documents (CI gate). | `v0.2.0` |
| [**aac-launch**](https://github.com/SMC17/aac-launch) | Zig-native argv-safe app launcher. Parses `.desktop` `Exec=` into real argv. Replaces eval/setsid shell-string launchers. | `v0.4.0` |

§

## WRITING

[**stax-blog**](https://github.com/SMC17/stax-blog) — *The Journal of Quantitative Mercantilism.* Essays + audits backing the appliance-layer thesis. AGPL.

§

## NOW

Currently shipping: **rippled-zig** Zig 0.14.1 → 0.16.0 toolchain upgrade (PR #72, local test-green, ~80 ArrayList API sites, std.io / std.crypto.random / Ed25519.generate / std.time.Timer all migrated). **zerotheta-evm** Type-I differential fix loop in progress (26 → 20 → 10 residuals across two rounds). Next: rpc.zig std.net → std.Io.net follow-up + zerotheta-evm BN256 math.

§

## INSTRUMENTATION

<p>
  <img src="https://img.shields.io/github/followers/SMC17?label=followers&style=flat-square&color=FFD6A0&labelColor=121212" alt="followers" />
  <img src="https://img.shields.io/github/stars/SMC17?affiliations=OWNER&style=flat-square&color=FFD6A0&labelColor=121212" alt="stars" />
  <img src="https://img.shields.io/github/last-commit/SMC17/mast?style=flat-square&label=mast&color=FFD6A0&labelColor=121212" alt="mast last commit" />
  <img src="https://img.shields.io/github/last-commit/SMC17/zig-h3?style=flat-square&label=zig-h3&color=FFD6A0&labelColor=121212" alt="zig-h3 last commit" />
  <img src="https://img.shields.io/github/last-commit/SMC17/sovereign-edge?style=flat-square&label=sovereign-edge&color=FFD6A0&labelColor=121212" alt="sovereign-edge last commit" />
</p>

<p>
  <img src="https://img.shields.io/badge/Zig-0.16.0-orange?style=flat-square&labelColor=121212" alt="Zig 0.16.0" />
  <img src="https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square&labelColor=121212" alt="AGPL-3.0" />
  <img src="https://img.shields.io/badge/substrate-Zig%20%2B%20Elixir%20%2B%20Nix-FFD6A0?style=flat-square&labelColor=121212" alt="substrate: Zig + Elixir + Nix" />
  <img src="https://img.shields.io/badge/discipline-evidence%20vocabulary-FFD6A0?style=flat-square&labelColor=121212" alt="discipline: evidence vocabulary" />
</p>

<p>
  <img src="https://github-profile-trophy.vercel.app/?username=SMC17&theme=nord&no-frame=true&no-bg=true&margin-w=6&column=7" alt="trophies" />
</p>

§

## CONTACT

`sean@sunlitmoon.online`

[**sunlitmoon.online**](https://sunlitmoon.online) · [**LinkedIn**](https://www.linkedin.com/in/sean-collins17/) · [**Twitter / X**](https://x.com/staxxxx17)

---

*Calculemus.*
