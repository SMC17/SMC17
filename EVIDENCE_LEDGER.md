# Public evidence ledger

Reviewed: 11 November 2026.

This ledger describes the profile's public links. Each repository owns its technical evidence, current scope, and limitations. Repository descriptions and test badges are not independent validation.

| Profile statement | Inspectable source | Limit |
| --- | --- | --- |
| logic-zig exposes reasoning engines and certificates | [README](https://github.com/SMC17/logic-zig), [status](https://github.com/SMC17/logic-zig/blob/main/STATUS.md) | Maturity varies by logical system; external proof tools have separate gates |
| finance-segway includes reproducible models and historical cases | [README](https://github.com/SMC17/finance-segway), [model inventory](https://github.com/SMC17/finance-segway/blob/main/standards/model_inventory.json) | Historical reconstructions do not establish production underwriting or forecast performance |
| zag records engineering work and applies local policy | [README](https://github.com/SMC17/zag), [platform support](https://github.com/SMC17/zag/blob/main/docs/platform-support.md) | Linux is the development platform; macOS and Windows have compile-only evidence in the repository's platform matrix |
| MarketDataSimulator is an exchange and recovery laboratory | [README](https://github.com/SMC17/MarketDataSimulator) | Research system; no production-venue or regulatory-compliance claim |

The profile makes no portfolio-size, performance, production-adoption, or certification claim. Numbers and hardware results belong beside the artifacts and commands that support them.

The [portable trust-gate preview](https://github.com/SMC17/logic-zig/releases/tag/revival-2026-11-11) records 391 passing tests on each of macOS ARM64 and Ubuntu ARM64, with five DRAT verifications and 25 CaDiCaL comparisons per runtime. Those are finite local acceptance runs. Hosted CI is blocked, and ABC delta agreement remains unknown. The release links the commands, source changes and validation artifact.

## 2026-11-11

| Decision | Status |
|---|---|
| GitHub is the canonical remote for every SMC17 repository. The Forgejo mirror program (2026-05) is retired. READMEs that still name sunlitmoon.online or Forgejo as canonical are stale until rewritten. | **decided** |
| Public surface: finance-segway, logic-zig, jevy, zag, MarketDataSimulator, SMC17, lean-action fork. Empty stubs made private 2026-11-11. | **audited** gh api |

## Task entry points

[TASKS.md](TASKS.md) links nine small jobs across the existing public cores. The [seven-CLI pack](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11) passes clean-source acceptance on macOS/Linux ARM64, 391 tests each; packaged binaries also run after stripping. macOS binaries require 26.4. External checker installs are separate.

[MarketDataSimulator PR #5](https://github.com/SMC17/MarketDataSimulator/pull/5) moves the public labs to .NET 10 and gates real test discovery. Core tests pass 392/392 on macOS ARM64 and Linux x86-64; the Linux run used amd64 emulation, so it is no hardware-speed measurement. Both Linux feed paths and generated-doc checks pass. The repository currently has no license file. Hosted workflows remain blocked by account billing.
