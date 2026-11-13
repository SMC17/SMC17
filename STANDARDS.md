# SMC17 standards

How every public SMC17 repository is run, so that anyone can arrive, see the state of the work, and know where to help. Where a repo differs, its own CONTRIBUTING.md says so.

**Cross-repo board:** [SMC17 public roadmap](https://github.com/users/SMC17/projects/16), every open issue in every public repo, with System and Priority fields.

## The rule

Every public claim comes with a command that reproduces it. A performance or correctness number needs the commit, the toolchain, the machine, and the script. A number without them is removed, and a number that stops reproducing is corrected in place, with the correction left visible. Anyone can report one with the **Challenge a claim** issue template.

## Proof levels

Each repo's STATUS.md states its level. The levels, weakest first:

| Level | Means |
|---|---|
| sketch | Ideas and design; code may not exist |
| scaffold | Structure exists; does not do the job yet |
| compiled | Builds on the pinned toolchain; no meaningful tests |
| unit-tested | Tests for its parts pass from a fresh clone |
| integration-tested | Tests for the parts working together pass |
| audited | Someone other than the author has checked it, and the review is linked |
| benchmarked | Performance numbers with commit, toolchain, machine and script |

A level is a claim like any other: it must be reproducible from a fresh clone.

## What every repo has

| File or setting | Purpose |
|---|---|
| README.md with a navigation line | What it is, a five-minute start, and links to the rest |
| STATUS.md | Proof level, last verified date, command and result |
| ROADMAP.md | Now / Next / good places to start, generated from issues |
| CONTRIBUTING.md | Build and test command, how to pick work, PR rules |
| SECURITY.md | Private vulnerability reporting through GitHub advisories |
| CODE_OF_CONDUCT.md | Contributor Covenant 2.1 |
| LICENSE | Stated in the README |
| Issue templates | Bug, feature, challenge a claim; blank issues off |
| PR template | Evidence block and checklist |
| `.github/release.yml` | Release notes grouped by label |
| CODEOWNERS, Dependabot | Review routing; Actions kept current |
| Settings | Secret scanning with push protection, Dependabot alerts, private vulnerability reporting, merged branches deleted |

Run `python3 tools/standards_check.py` (needs the `gh` CLI) to see how every public repo measures against this table.

## Labels

| Label | Meaning |
|---|---|
| `type: bug` | Something is wrong |
| `type: feature` | New capability or improvement |
| `type: claim` | A published number or statement does not reproduce |
| `type: docs` | Documentation only |
| `type: perf` | Speed or memory, with a measurement |
| `type: research` | Open question to investigate before building |
| `type: infra` | Build, CI, packaging, or repository tooling |
| `type: epic` | Groups issues that together deliver one outcome |
| `priority: P0` | Broken or wrong for users now |
| `priority: P1` | Next up |
| `priority: P2` | Useful, not urgent |
| `status: needs-triage` | Not yet reviewed by the maintainer |
| `status: ready` | Clear enough for anyone to pick up |
| `status: blocked` | Waiting on another issue or an outside party |
| `status: needs-decision` | Needs a maintainer decision first |
| `status: wontfix` | Will not be worked on; reason in the thread |
| `breaking` | Changes public API or file formats |
| `good first issue` | Small, well-scoped, with pointers to the code |
| `help wanted` | Outside help especially welcome |
| `dependencies` | Dependency updates |

Repos may add `area: ...` labels for their own parts.

## How an issue moves

1. **Opened** from a template, labelled `status: needs-triage`.
2. **Triaged** by the maintainer: a `type:` and a `priority:` label, and either `status: ready` (anyone can take it), `status: needs-decision`, `status: blocked`, or closed with a reason.
3. **Taken:** comment on the issue; the maintainer assigns it.
4. **PR** links the issue (`Closes #N`), fills the evidence block, and is merged with the issue closing automatically.
5. **Released:** tagged versions get notes generated from the merged PRs' labels.

Each repo has a **Next** milestone holding what is committed to for its next release. Nothing outside it is promised.

## Branches

Each repo keeps its default branch plus branches with open pull requests. Merged branches are deleted. Unmerged work that has gone stale is not thrown away: it is kept under a hidden ref, `refs/archive/<branch>`, which you can fetch with

```sh
git fetch origin 'refs/archive/*:refs/archive/*'
```

## Making a repo public

A repo goes public only when a fresh clone builds and passes its tests on the pinned toolchain, it has a LICENSE, STATUS.md and a README that gets someone started in five minutes, and nothing in its files or history exposes private information.

## AI assistance

AI-assisted work is welcome here and is disclosed in the PR. Other projects have their own rules. The Zig compiler and ZLS ban LLM-assisted contributions, so anything sent there is written by hand.

## Status of every public repo

Verified 2026-11-12 from fresh clones on an Apple M2 Max unless noted.

| Repo | System | Proof level | Result |
|---|---|---|---|
| [faiss-zig](https://github.com/SMC17/faiss-zig) | ML infrastructure | unit-tested | 76/76 tests pass |
| [qsr-zig](https://github.com/SMC17/qsr-zig) | ML infrastructure | unit-tested | 4/4 tests pass, including 800 differential trials |
| [safetensors-zig](https://github.com/SMC17/safetensors-zig) | ML infrastructure | unit-tested | 19 pass, 2 optional real-model tests skip |
| [tokenizers-zig](https://github.com/SMC17/tokenizers-zig) | ML infrastructure | unit-tested | 166 pass, 29 skip (need HuggingFace tokenizer.json fixtures) |
| [znap](https://github.com/SMC17/znap) | ML infrastructure | benchmarked (one machine) | 631/631 tests pass |
| [MarketDataSimulator](https://github.com/SMC17/MarketDataSimulator) | Markets and data | integration-tested | 392/392 tests pass |
| [finance-segway](https://github.com/SMC17/finance-segway) | Markets and data | unit-tested (quickstart checks) | reference engines 11/11, reconciled engines PASS, consulting real-data policy 3/3 (README quickstart checks only) |
| [jevy](https://github.com/SMC17/jevy) | Markets and data | unit-tested | Zig 153/153; Python (clean venv from requirements.lock) 194 passed, 12 skipped |
| [zkdb](https://github.com/SMC17/zkdb) | Markets and data | unit-tested | 47/47 tests pass |
| [zkdb-elixir](https://github.com/SMC17/zkdb-elixir) | Markets and data | unit-tested | 5/5 ExUnit tests pass; mix builds the Zig NIF |
| [logic-zig](https://github.com/SMC17/logic-zig) | Proofs and tools | unit-tested | 541/541 tests pass |
| [method-wagwan](https://github.com/SMC17/method-wagwan) | Proofs and tools | sketch | design and process; engine not yet built (Phase 1) |
| [zag](https://github.com/SMC17/zag) | Proofs and tools | unit-tested | macOS: 707 pass, 25 Linux-only skip, 0 fail; Linux: not re-run in this check |
| [zig-h3](https://github.com/SMC17/zig-h3) | Proofs and tools | benchmarked | 211/211 tests pass |
