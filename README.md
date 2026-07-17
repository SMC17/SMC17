<div align="center">

# SMC17 · Sovereign Stack

**403 repositories** · **221 Zig libraries** · **269 active** · **273 stars**

[![Zig](https://img.shields.io/badge/Zig-F7A41D?style=for-the-badge&logo=zig&logoColor=white)](https://ziglang.org)
[![Elixir](https://img.shields.io/badge/Elixir-4B275F?style=for-the-badge&logo=elixir&logoColor=white)](https://elixir-lang.org)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>

---

## What I Build

**17S Capital LLC** — software infrastructure for sovereign computation, quantitative finance, and naval architecture simulation.

The stack is built on a core thesis: **own your compute, own your primitives, own your data**.

---

## Ecosystems

### 🔵 ZeroTheta — Sovereign Monolith
> Zig × Elixir Layer-0 hyperstructure

The core operating system for sovereign computation. Zig for performance-critical primitives, Elixir/OTP for fault-tolerant orchestration.

| Component | Repo | Role |
|-----------|------|------|
| Core | [ZeroTheta](https://github.com/SMC17/ZeroTheta) | OTP supervisor tree |
| EVM Engine | [zerotheta-evm](https://github.com/SMC17/zerotheta-evm) | Ethereum VM in Zig |
| File System | [0theta-filez](https://github.com/SMC17/0theta-filez) | Sovereign FS primitives |
| MCP | [0theta-mcp](https://github.com/SMC17/0theta-mcp) | Model context protocol |

### ⚓ Yard — Naval Architecture (77 modules)
> Full marine engineering simulation stack in pure Zig

77 independent Zig modules covering the complete naval architecture domain — from hydrostatics to propulsion to seakeeping.

| Domain | Modules |
|--------|---------|
| Core | [yard-naval-arch-zig](https://github.com/SMC17/yard-naval-arch-zig) |
| Hydrostatics | stability, freeboard, grounding, mass |
| Hydrodynamics | BEM, strip theory, RAO spectra, seakeeping |
| Propulsion | resistance, azipod, ITTC-78, shaft design |
| Maneuvering | Fossen 6-DOF, DP, AUV |
| Environment | wind/aero, Flettner, ice, routing |

→ [See full Yard ecosystem](https://github.com/SMC17/yard-naval-arch-zig)

### ⚡ Zig Libraries
> Zero-alloc, no-deps primitives

| Repo | Description |
|------|-------------|
| [zig-cobs](https://github.com/SMC17/zig-cobs) | COBS byte-stuffing framing |
| [zig-frame-protocol](https://github.com/SMC17/zig-frame-protocol) | Versioned binary frame protocol |
| [zig-graph](https://github.com/SMC17/zig-graph) | Sparse graph algorithms |
| [zig-h3](https://github.com/SMC17/zig-h3) | H3 geospatial index |
| [zig-bean](https://github.com/SMC17/zig-bean) | Plain-text accounting |
| [zkdb](https://github.com/SMC17/zkdb) | Columnar time-series DB |
| [ztop](https://github.com/SMC17/ztop) | System monitor (htop successor) |

### 🧠 Muscle — FFI Bindings
> Sovereign Zig wrappers for native libraries

[FAISS](https://github.com/SMC17/muscle-faiss-zig) · [CRPC](https://github.com/SMC17/muscle-crpc-core) · [AMX](https://github.com/SMC17/muscle-amx-zig) · [QPE](https://github.com/SMC17/muscle-qpe-zig) · [Rippled](https://github.com/SMC17/muscle-rippled-zig)

### 🏗 Stax Platform
> Sovereign infrastructure stack

27 repositories covering: control plane, networking, observability, secrets, storage, CI/CD.

### 📐 Formal Methods
- [aristotle-lean](https://github.com/SMC17/aristotle-lean) — formal proofs in Lean 4
- [aristotle-pipeline](https://github.com/SMC17/aristotle-pipeline) — reasoning pipelines
- [zerotheta-evm](https://github.com/SMC17/zerotheta-evm) — 263 tests, 142/143 opcodes

### 📊 Finance & Capital
- [17sCapital](https://github.com/SMC17/17sCapital) — trading infrastructure
- [zig-bean](https://github.com/SMC17/zig-bean) — accounting primitives
- [zig-actuary](https://github.com/SMC17/zig-actuary) — actuarial math

---

## Philosophy

- **Zig first** — correctness, comptime, zero-alloc hot paths
- **Elixir/OTP** — fault-tolerant supervisors, distributed by default
- **No cloud lock-in** — sovereign compute from Layer-0 up
- **Formal verification** — proofs where it matters (EVM, finance)

---

<div align="center">
<sub>17S Capital LLC · Building the sovereign stack</sub>
</div>
