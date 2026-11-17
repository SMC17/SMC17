#!/usr/bin/env python3
"""Public forecast ledger: append-only, hash-chained, scored by wagwan-score.

    python3 ops/forecasts.py add FILE.json          # new question with its first forecast
    python3 ops/forecasts.py update ID P --reason JSON
    python3 ops/forecasts.py resolve ID {0|1} --source TEXT
    python3 ops/forecasts.py check                  # verify every hash chain
    python3 ops/forecasts.py report                 # write FORECASTS.md (scores via wagwan-score)

Each forecast lives in forecasts/ledger/<id>.json. Updates are appended, never
edited: every update stores the SHA-256 of the record as it stood before it,
so any later edit to an earlier probability or rationale breaks `check`.
Forecasters are kept apart: "SMC17" is the owner's own record; "agent:<name>"
is an AI pipeline's, labelled as such and never mixed into the owner's score.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "forecasts" / "ledger"
REASON_KEYS = ("outside_view", "decomposition", "inside_view", "what_would_change_my_mind")


def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(obj) -> str:
    return hashlib.sha256(canon(obj).encode()).hexdigest()


def load(fid: str) -> dict:
    return json.loads((LEDGER / f"{fid}.json").read_text())


def save(rec: dict) -> None:
    (LEDGER / f"{rec['id']}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")


def body(rec: dict) -> dict:
    """The part of a record each update pins: everything except resolution."""
    return {k: v for k, v in rec.items() if k != "resolution"}


def check_reason(reason: dict) -> None:
    missing = [k for k in REASON_KEYS if not str(reason.get(k, "")).strip()]
    if missing:
        sys.exit(f"reasoning must include {', '.join(REASON_KEYS)}; missing: {', '.join(missing)}")


def append_update(rec: dict, p: float, reason: dict, at: str) -> None:
    if not 0 < p < 1:
        sys.exit("probability must be strictly between 0 and 1")
    check_reason(reason)
    prev = digest(body(rec)) if rec.get("updates") else None
    if rec.get("updates") and at < rec["updates"][-1]["at"]:
        sys.exit("updates must be in time order")
    if at > rec["resolve_by"]:
        sys.exit("cannot forecast after the resolution date")
    rec.setdefault("updates", []).append({"at": at, "p": p, "reasoning": reason, "prev_sha256": prev})


def cmd_add(path: str) -> None:
    spec = json.loads(Path(path).read_text())
    for k in ("id", "question", "resolution_criteria", "resolution_source", "resolve_by", "forecaster", "p", "reasoning"):
        if k not in spec:
            sys.exit(f"missing field: {k}")
    if (LEDGER / f"{spec['id']}.json").exists():
        sys.exit(f"{spec['id']} already exists; use update")
    at = spec.get("at") or dt.date.today().isoformat()
    rec = {k: spec[k] for k in ("id", "question", "resolution_criteria", "resolution_source", "resolve_by", "forecaster")}
    rec["created"] = at
    rec["platform"] = spec.get("platform")
    rec["updates"] = []
    append_update(rec, float(spec["p"]), spec["reasoning"], at)
    rec["resolution"] = None
    LEDGER.mkdir(parents=True, exist_ok=True)
    save(rec)
    print(f"added {rec['id']} p={spec['p']}")


def cmd_update(fid: str, p: float, reason: str, at: str | None) -> None:
    rec = load(fid)
    if rec.get("resolution"):
        sys.exit("already resolved")
    append_update(rec, p, json.loads(reason), at or dt.date.today().isoformat())
    save(rec)
    print(f"updated {fid} p={p}")


def cmd_resolve(fid: str, outcome: int, source: str, on: str | None) -> None:
    rec = load(fid)
    if rec.get("resolution"):
        sys.exit("already resolved")
    rec["resolution"] = {"outcome": outcome, "source": source, "resolved_on": on or dt.date.today().isoformat(),
                         "pinned_sha256": digest(body(rec))}
    save(rec)
    print(f"resolved {fid} -> {outcome}")


def verify(rec: dict) -> list[str]:
    problems = []
    ups = rec.get("updates", [])
    if not ups:
        problems.append("no forecast")
    partial = {k: v for k, v in rec.items() if k not in ("resolution", "updates")}
    partial["updates"] = []
    for i, u in enumerate(ups):
        want = digest(partial) if i else None
        if u.get("prev_sha256") != want:
            problems.append(f"update {i} does not chain to the record before it (edited history?)")
        partial["updates"].append(u)
    res = rec.get("resolution")
    if res and res.get("pinned_sha256") != digest(body(rec)):
        problems.append("record changed after resolution")
    return problems


def cmd_check() -> int:
    bad = 0
    for f in sorted(LEDGER.glob("*.json")):
        probs = verify(json.loads(f.read_text()))
        if probs:
            bad += 1
            print(f"FAIL {f.stem}: {'; '.join(probs)}")
    print(f"{len(list(LEDGER.glob('*.json')))} records, {bad} with problems")
    return 1 if bad else 0


def wagwan_score(rows: list[tuple[float, int]]) -> str:
    exe = shutil.which("wagwan-score") or str(ROOT / "ops" / ".bin" / "wagwan-score")
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        fh.write("p,outcome\n" + "".join(f"{p},{o}\n" for p, o in rows))
    out = subprocess.run([exe, fh.name, "5"], capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else f"(wagwan-score failed: {out.stderr.strip()[:200]})"


def cmd_report() -> None:
    recs = [json.loads(f.read_text()) for f in sorted(LEDGER.glob("*.json"))]
    by = {}
    for r in recs:
        by.setdefault(r["forecaster"], []).append(r)
    lines = ["# Forecasts", "",
             "A public, append-only record of probabilistic forecasts, scored by "
             "[wagwan-score](https://github.com/SMC17/method-wagwan) (Brier, log score, calibration). "
             "Every update records its outside view, decomposition, inside view and what would change the "
             "forecaster's mind, and chains the hash of the record before it, so history cannot be quietly edited "
             "(`python3 ops/forecasts.py check`).", "",
             "`SMC17` is the owner's own record. `agent:*` records are AI forecasting pipelines, kept and scored "
             "separately.", ""]
    for who, rs in sorted(by.items()):
        resolved = [r for r in rs if r.get("resolution")]
        lines += [f"## {who}", "", f"{len(rs)} forecasts, {len(resolved)} resolved.", ""]
        if resolved:
            rows = [(r["updates"][-1]["p"], r["resolution"]["outcome"]) for r in resolved]
            lines += ["Scored on each question's final forecast before resolution:", "", "```", wagwan_score(rows), "```", ""]
        lines += ["| Question | Forecast | Resolves by | Outcome |", "|---|---:|---|---|"]
        for r in sorted(rs, key=lambda r: r["resolve_by"]):
            out = "open" if not r.get("resolution") else ("yes" if r["resolution"]["outcome"] else "no")
            ups = " → ".join(f"{u['p']:.2f}" for u in r["updates"])
            lines.append(f"| [{r['question']}](forecasts/ledger/{r['id']}.json) | {ups} | {r['resolve_by']} | {out} |")
        lines.append("")
    (ROOT / "FORECASTS.md").write_text("\n".join(lines))
    print(f"wrote FORECASTS.md ({len(recs)} records)")


def main() -> int:
    ap = argparse.ArgumentParser(description="SMC17 forecast ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("add").add_argument("file")
    u = sub.add_parser("update"); u.add_argument("id"); u.add_argument("p", type=float); u.add_argument("--reason", required=True); u.add_argument("--at")
    r = sub.add_parser("resolve"); r.add_argument("id"); r.add_argument("outcome", type=int, choices=[0, 1]); r.add_argument("--source", required=True); r.add_argument("--on")
    sub.add_parser("check"); sub.add_parser("report")
    a = ap.parse_args()
    if a.cmd == "add": cmd_add(a.file)
    elif a.cmd == "update": cmd_update(a.id, a.p, a.reason, a.at)
    elif a.cmd == "resolve": cmd_resolve(a.id, a.outcome, a.source, a.on)
    elif a.cmd == "check": return cmd_check()
    elif a.cmd == "report": cmd_report()
    return 0


if __name__ == "__main__":
    sys.exit(main())
