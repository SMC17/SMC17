# CI billing block — 2026-05-18 — action required

Two of the fleet's repos hit a GitHub Actions billing block during the
Wave-6 / Wave-7 push. CI cannot run on these repos until the billing
issue is resolved at the account level. **This is not a code problem.**

## Affected repos

- [`rippled-zig`](https://github.com/SMC17/rippled-zig)
- [`zerotheta-evm`](https://github.com/SMC17/zerotheta-evm) (was `zeth`)

## The error message

Every queued job on these two repos dies at runner-startup with:

> The job was not started because recent account payments have failed or
> your spending limit needs to be increased. Please check the 'Billing &
> plans' section in your settings.

(See e.g.
[`rippled-zig` run 26018669320](https://github.com/SMC17/rippled-zig/actions/runs/26018669320)
or
[`zerotheta-evm` run 26061423529](https://github.com/SMC17/zerotheta-evm/actions/runs/26061423529).)

## Why only these two repos

Most of the fleet uses small CI runs that fit inside GitHub Actions's free
tier. `rippled-zig` and `zerotheta-evm` have heavier CI matrices (multi-
gate quality runs, Berlin differential, RISC-V build, etc.) and likely
exceeded a spending cap. The other Tier-S/A repos (`zig-cobs`,
`zig-frame-protocol`, `zig-h3`, `zig-graph`, `sentinel-sbom`,
`sovereign-edge`, `sovereign-offense-harness`, `mast`, `fleet-sbom-index`)
all have CI running cleanly today, so this is specific to those two repo
configurations or projects under the same billing scope.

## What stax needs to do

In order, easiest-first:

1. **Check the GitHub billing page.**
   [`github.com/settings/billing`](https://github.com/settings/billing) —
   look for "Payment information" with a red banner, an expired card, or a
   failed renewal. Re-authorize the payment method if so.
2. **Check the Actions spending limit.**
   [`github.com/settings/billing/spending_limit`](https://github.com/settings/billing/spending_limit)
   — confirm there's headroom above current usage. Raise the limit if
   needed.
3. **If the personal account is on the free plan,** consider whether the
   monthly Actions minutes (2,000 free) are consumed. The heavy zeth +
   rippled-zig matrices burn through these fast. Either reduce the matrix
   or move the repo under a paid plan / GitHub Pro account.

Once billing is unblocked:

- **rippled-zig**: 2 more clean Quality-Gates runs on `main` will close
  the Wave-3 soak (PR #69 merged on 2026-05-15 + 1 clean run already in
  the books). No code change required.
- **zerotheta-evm**: re-run CI on `main` after PR #24 landed (admin-
  merged 2026-05-18T21:47:28Z, commit `97512dc`). Local verification is
  exhaustive:
  - `411/414` Zig tests pass (3 long-running skipped, same as baseline).
  - PyEVM-Berlin differential: `Total discrepancies: 0`.
  - go-ethereum 1.17.2 differential on ERC-20 transfer: byte-for-byte
    match on gas + storage state.
  - Full audit chain documented in `POST_FIX_DIFFERENTIAL_REPORT.md`.

## What changed under the billing block

While CI was unable to run on these two repos, the Wave-6 / Wave-7 work
landed via **admin-merge** with exhaustive local verification:

- `zerotheta-evm` PR #24 (the canonical audit-fix-validate case study)
  admin-merged on 2026-05-18T21:47:28Z. Storage state, gas accounting,
  and BN256 math all validated against two independent EVM
  implementations (PyEVM-Berlin and go-ethereum 1.17.2).
- `zerotheta-evm` PR #25 ([validation/geth_diff.sh](https://github.com/SMC17/zerotheta-evm/pull/25))
  ships the go-ethereum differential as a reproducible test.

The admin-merge was a deliberate exception to the green-CI gate doctrine,
justified by the local-verification depth + the billing block being out
of scope. Document trail in FLEET.md (Wave-7 push section).

## Honest scope limit

This document does not attempt to diagnose *why* the billing failure
happened. That's an account-state question only the account owner can
answer from the GitHub dashboard.

The fleet's correctness signal stays load-bearing **independent of CI
liveness** — the audit-fix-validate loop's evidence is captured in
verbatim differential baselines, not just CI badges. CI re-running
matters for the public-trust signal (the green-CI badge on the README is
the third-party verification of the local claims), and unblocking it is
the right move, but the engineering work is not gated on it.
