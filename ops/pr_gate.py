#!/usr/bin/env python3
"""Mechanical PR gate: run a repo's registered gates on a PR and on main, compare, and report.

    python3 ops/pr_gate.py REPO PR [--post]

It does the part of an audit a machine can do (fresh clones, every registered gate,
test counts and meters against main), so a human or agent auditor spends its time on
judgment only. With --post, the report is posted on the PR, first line
"Gate report: PASS" or "Gate report: FAIL". It never merges.
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import smc17ops as ops  # noqa: E402


def run(repo: str, pr: int) -> tuple[bool, str]:
    spec = ops.REGISTRY.get(repo)
    if not spec:
        return False, f"{repo} has no registered gate in ops/registry.json; add one first."
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        head = ops.gate(repo, spec, work, pr=pr)
        base = ops.gate(repo, spec, work)
        meters = {}
        for m in spec.get("meters", []):
            fn = getattr(ops, f"meter_{m}", None)
            if fn:
                meters[m] = (fn(work / f"{repo}-pr{pr}"), fn(work / repo))
    lines, ok = [], bool(head.get("ok"))
    if head.get("infra"):
        ok = False
        lines.append(f"Infrastructure failure, not a verdict on the code: {head.get('error') or 'see steps'}")
    lines += ["| | PR head | main |", "|---|---|---|",
              f"| commit | {head.get('commit', '?')} | {base.get('commit', '?')} |",
              f"| gate | {'pass' if head.get('ok') else 'FAIL'} | {'pass' if base.get('ok') else 'FAIL'} |"]
    for k in ("passed", "failed", "skipped"):
        lines.append(f"| tests {k} | {head.get(k, 0)} | {base.get(k, 0)} |")
    if head.get("passed", 0) < base.get("passed", 0):
        ok = False
        lines.append(f"| **regression** | {base['passed'] - head['passed']} fewer passing tests than main | |")
    for name, (h, b) in meters.items():
        for k in sorted(set(h) | set(b)):
            flag = ""
            if isinstance(h.get(k), (int, float)) and isinstance(b.get(k), (int, float)):
                worse = h[k] > b[k] if k.startswith("cells_needing") else h[k] < b[k]
                if worse:
                    ok, flag = False, " **worse than main**"
            lines.append(f"| {name}: {k} | {h.get(k)}{flag} | {b.get(k)} |")
    lines.append("")
    for s in head.get("steps", []):
        lines.append(f"- `{s['cmd']}` exit {s['rc']}" + (": " + " / ".join(s["tail"])[:400] if s["rc"] else ""))
    lines.append(f"\nRun with `python3 ops/pr_gate.py {repo} {pr}` from SMC17/SMC17 ({head.get('seconds', '?')} s for the PR head).")
    return ok, "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo"); ap.add_argument("pr", type=int); ap.add_argument("--post", action="store_true")
    a = ap.parse_args()
    ok, body = run(a.repo, a.pr)
    report = f"Gate report: {'PASS' if ok else 'FAIL'}\n\n{body}"
    print(report)
    if a.post:
        ops.sh(["gh", "pr", "comment", str(a.pr), "-R", f"{ops.OWNER}/{a.repo}", "-F", "-"], input=report)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
