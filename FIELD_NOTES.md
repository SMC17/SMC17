# Make missing evidence fail: a small solver-checking lab

A solver can return an answer while its independent checker is missing. If the
integration treats that situation as success, the output looks more trustworthy
than the work that actually ran. A useful gate needs positive checker evidence
and a clear refusal when that evidence is unavailable.

The dated [logic-zig portable preview](https://github.com/SMC17/logic-zig/releases/tag/portable-clis-2026-11-11)
contains a small task for inspecting that boundary. It includes seven CLIs,
matching source, recorded checks and checksums. The source commands below use
that preview tag so a future default-branch change does not silently change
the exercise.

## Try one checked UNSAT result

Use Zig 0.16.0, Git, Python 3, make and C/C++ build tools. The checker build
fetches pinned upstream source revisions. The recorded native platforms are
macOS 26.4 ARM64 and Ubuntu 24.04 ARM64; other platforms need their own checks.

```sh
git clone --depth 1 --branch portable-clis-2026-11-11 https://github.com/SMC17/logic-zig.git
cd logic-zig
zig build test
zig build
./zig-out/bin/logic-zig doctor
scripts/build-checkers.sh
python3 tests/host_gate_smoke.py
scripts/expect-status.sh 20 ./zig-out/bin/logic-sat check-drat corpus/bench/sat/simple_unsat.cnf
./zig-out/bin/logic-zig trust-report
```

Status 20 is the checked UNSAT convention for this task. The wrapper checks
that exact status instead of assuming that an ordinary shell success code
means the right result. The refusal regressions exercise unavailable and
inconclusive checkers. `trust-report` requires positive evidence on its required
axes before it finishes with `TRUST_OK`.

Read the [preview's exact task and boundaries](https://github.com/SMC17/logic-zig/blob/8e1c50bc68f1e00cbd4514c498006c7f6a8feca9/docs/PORTABLE_TRUST_DEMO.md)
before interpreting the output. A successful answer, a generated proof and a
successful independent proof check are distinct events.

## Keep the evidence attached to the revision

The recorded acceptance on 11 November 2026 passed 391 tests on each of the two
native ARM64 runtimes. Each trust run recorded five DRAT verifications and 25
CaDiCaL comparisons with zero mismatches. The optional ABC delta comparison was
unknown; that is retained as unknown. These local results are separate from
hosted Actions and do not certify every input or every engine.

For a Linux follow-up, [record the checked task in zag](https://github.com/SMC17/logic-zig/blob/8e1c50bc68f1e00cbd4514c498006c7f6a8feca9/docs/RECORDED_PROOF_DEMO.md).
It records the command, exit status and output objects, then checks the event
chain. That gives an inspectable account of what ran. The record still depends
on the checker's evidence for the solver result.

This separation also matters in other projects: a digest identifies bytes,
a signature identifies a signed record, and a matching output fixture checks
one specific behavior. Each supports its own claim. None automatically proves
the economic, scientific or operational adequacy of a result.

## Bring back one useful failure

Try the task from a fresh checkout on a supported platform. If a check fails,
include the preview revision, operating system, toolchain, exact input,
command, exit status and expected/actual output in the repository issue tracker.
An independently reproduced refusal or mismatch is more useful than a broad
statement that the project works.

The preview is a finite exercise. Real-user completion and adoption remain
unmeasured; this note is an invitation to try a concrete task.
