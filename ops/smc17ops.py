#!/usr/bin/env python3
"""SMC17 ops: sense, heal, and report across every public SMC17 repository.

    python3 ops/smc17ops.py sense              # fresh-clone gates + meters -> ops/state/latest.json
    python3 ops/smc17ops.py heal [--dry-run]   # allow-listed fixes only
    python3 ops/smc17ops.py report [--dry-run] # ratchet vs baseline, issues, OPS.md
    python3 ops/smc17ops.py run [--dry-run]    # all three, in order

Write actions are limited to the allow-list in heal() and report(). Everything
else becomes an issue for a person. Needs: git, gh (authenticated), and the
toolchains named in ops/registry.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

OWNER = "SMC17"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STATE = HERE / "state"
REGISTRY = json.loads((HERE / "registry.json").read_text())
BOARD = "16"
ISSUE_PREFIX = "ops: "
DRY = False

STANDARD_FILES = {
    "README": r"^README\.md$", "STATUS": r"^STATUS\.md$", "ROADMAP": r"^ROADMAP\.md$",
    "CONTRIBUTING": r"^(\.github/|docs/)?CONTRIBUTING\.md$", "SECURITY": r"^(\.github/)?SECURITY\.md$",
    "CODE_OF_CONDUCT": r"(^|/)CODE_OF_CONDUCT\.md$", "LICENSE": r"^LICEN[CS]E",
    "ISSUE_TEMPLATE": r"^\.github/ISSUE_TEMPLATE/", "PR_TEMPLATE": r"(?i)(^|/)pull_request_template\.md$",
    "RELEASE_NOTES": r"^\.github/release\.yml$",
}


def log(*a):
    print(f"[{dt.datetime.now().strftime('%H:%M:%S')}]", *a, flush=True)


def sh(cmd, cwd=None, timeout=600, check=False, input=None):
    r = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), capture_output=True, text=True,
                       timeout=timeout, input=input, executable="/bin/bash" if isinstance(cmd, str) else None)
    if check and r.returncode:
        raise RuntimeError(f"{cmd}: {r.stderr.strip()[:300]}")
    return r


def gh_json(*args):
    r = sh(["gh", *args])
    if r.returncode:
        raise RuntimeError(f"gh {' '.join(args[:3])}: {r.stderr.strip()[:300]}")
    return json.loads(r.stdout or "null")


def write(*args, input=None):
    """Run a gh/git command that changes something, unless --dry-run."""
    if DRY:
        log("DRY-RUN would run:", " ".join(args)[:200])
        return ""
    r = sh(list(args), input=input)
    if r.returncode:
        log("WRITE FAILED:", " ".join(args)[:120], r.stderr.strip()[:200])
    return r.stdout


# ---------------------------------------------------------------- parsing

def parse_tests(text: str) -> dict:
    """Pull pass/fail/skip counts from Zig, ExUnit, dotnet, pytest and unittest output."""
    out = {"passed": 0, "failed": 0, "skipped": 0}
    for m in re.finditer(r"(\d+)/(\d+) tests passed(?: \(([^)]*)\))?", text):
        out["passed"] += int(m.group(1))
        extra = m.group(3) or ""
        s = re.search(r"(\d+) skipped", extra); f = re.search(r"(\d+) failed", extra)
        out["skipped"] += int(s.group(1)) if s else 0
        out["failed"] += int(f.group(1)) if f else 0
    for m in re.finditer(r"(\d+) tests?, (\d+) failures?(?:, (\d+) excluded)?", text):  # ExUnit
        out["passed"] += int(m.group(1)) - int(m.group(2)); out["failed"] += int(m.group(2))
    for m in re.finditer(r"Failed:\s+(\d+), Passed:\s+(\d+), Skipped:\s+(\d+)", text):  # dotnet
        out["failed"] += int(m.group(1)); out["passed"] += int(m.group(2)); out["skipped"] += int(m.group(3))
    for line in text.splitlines():  # pytest summary line
        if re.search(r"\d+ (passed|failed)", line) and " in " in line and "tests passed" not in line:
            for n, k in re.findall(r"(\d+) (passed|failed|skipped)", line):
                out[k] += int(n)
    for m in re.finditer(r"Ran (\d+) tests?.*?\n\s*\n?(OK|FAILED \((?:failures|errors)=(\d+)\))", text, re.S):  # unittest
        failed = int(m.group(3) or 0); out["passed"] += int(m.group(1)) - failed; out["failed"] += failed
    return out


# ---------------------------------------------------------------- sense

def gate(repo: str, spec: dict, workdir: Path) -> dict:
    t0 = time.time()
    dest = workdir / repo
    r = sh(["gh", "repo", "clone", f"{OWNER}/{repo}", str(dest), "--", "--depth", "1", "-q"], timeout=600)
    if r.returncode:
        return {"ok": False, "error": "clone failed: " + r.stderr.strip()[:200]}
    commit = sh(["git", "-C", str(dest), "rev-parse", "--short", "HEAD"]).stdout.strip()
    res = {"commit": commit, "steps": [], "passed": 0, "failed": 0, "skipped": 0, "ok": True}
    for cmd in spec.get("gate", []):
        try:
            p = sh(cmd, cwd=dest, timeout=spec.get("timeout", 900))
            text = p.stdout + "\n" + p.stderr
            rc = p.returncode
        except subprocess.TimeoutExpired:
            text, rc = "TIMEOUT", 124
        counts = parse_tests(text)
        for k in ("passed", "failed", "skipped"):
            res[k] += counts[k]
        res["steps"].append({"cmd": cmd, "rc": rc, **counts, "tail": text.strip().splitlines()[-3:] if rc else []})
        if rc:
            res["ok"] = False
    if res["failed"]:
        res["ok"] = False
    res["seconds"] = round(time.time() - t0)
    return res


def meter_workbooks(dest: Path) -> dict:
    py = HERE / ".venv" / "bin" / "python"
    tool = dest / "tools" / "workbook_completeness.py"
    if not py.exists() or not tool.exists():
        return {"error": "meter unavailable (run ops/setup.sh)"}
    p = sh([str(py), str(tool), "--root", str(dest), "--json"], timeout=900)
    if p.returncode:
        return {"error": p.stderr.strip()[:200]}
    return json.loads(p.stdout)["totals"]


def meter_standards(dest: Path) -> dict:
    files = sh(["git", "-C", str(dest), "ls-files"]).stdout.split("\n")
    missing = [k for k, rx in STANDARD_FILES.items() if not any(re.search(rx, f) for f in files)]
    return {"missing": missing}


def meter_tracker(repo: str) -> dict:
    issues = gh_json("issue", "list", "-R", f"{OWNER}/{repo}", "-L", "500", "--json", "number,labels,createdAt,title")
    now = dt.datetime.now(dt.timezone.utc)
    def labels(i): return {l["name"] for l in i["labels"]}
    untriaged = [i for i in issues if not any(l.startswith("priority: ") for l in labels(i))
                 and not i["title"].startswith(ISSUE_PREFIX)]
    prs = gh_json("pr", "list", "-R", f"{OWNER}/{repo}", "-L", "200", "--json", "number,createdAt,isDraft,author")
    stale = [p for p in prs if (now - dt.datetime.fromisoformat(p["createdAt"].replace("Z", "+00:00"))).days > 14]
    return {
        "open_issues": len(issues),
        "p0": sum("priority: P0" in labels(i) for i in issues),
        "p1": sum("priority: P1" in labels(i) for i in issues),
        "ready": sum("status: ready" in labels(i) for i in issues),
        "untriaged": len(untriaged),
        "open_prs": len(prs),
        "stale_prs": len(stale),
    }


def sense(only=None):
    STATE.mkdir(exist_ok=True)
    run = {"started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "host": os.uname().machine,
           "zig": sh(["zig", "version"]).stdout.strip(), "repos": {}}
    with tempfile.TemporaryDirectory(prefix="smc17ops-") as tmp:
        for repo, spec in REGISTRY.items():
            if only and repo not in only:
                continue
            log("gate", repo)
            g = gate(repo, spec, Path(tmp))
            entry = {"system": spec["system"], "gate": g}
            dest = Path(tmp) / repo
            if dest.exists():
                entry["standards"] = meter_standards(dest)
                if "workbooks" in spec.get("meters", []):
                    entry["workbooks"] = meter_workbooks(dest)
            entry["tracker"] = meter_tracker(repo)
            run["repos"][repo] = entry
            log(f"  {repo}: ok={g.get('ok')} passed={g.get('passed')} failed={g.get('failed')} skipped={g.get('skipped')}")
    run["finished"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    (STATE / "latest.json").write_text(json.dumps(run, indent=1))
    with (STATE / "history.jsonl").open("a") as h:
        h.write(json.dumps(summarize(run)) + "\n")
    return run


def summarize(run):
    s = {"at": run["started"], "repos": {}}
    for r, e in run["repos"].items():
        g = e.get("gate", {})
        s["repos"][r] = {"ok": g.get("ok"), "passed": g.get("passed"), "failed": g.get("failed"),
                         "skipped": g.get("skipped"), "missing": len(e.get("standards", {}).get("missing", [])),
                         **({"formula_computed_pct": e["workbooks"].get("formula_computed_pct"),
                             "placeholders": e["workbooks"].get("placeholders")} if "workbooks" in e and "error" not in e["workbooks"] else {})}
    return s


# ---------------------------------------------------------------- heal (allow-list)

def heal():
    """Allow-listed, reversible fixes. Anything else is left to report() as an issue."""
    board_sync()
    merge_green_dependabot()


def board_sync():
    proj = gh_json("project", "view", BOARD, "--owner", OWNER, "--format", "json")
    fields = {f["name"]: f for f in gh_json("project", "field-list", BOARD, "--owner", OWNER, "--format", "json")["fields"]}
    opt = lambda n, v: next(o["id"] for o in fields[n]["options"] if o["name"] == v)
    items = gh_json("project", "item-list", BOARD, "--owner", OWNER, "--format", "json", "-L", "2000")["items"]
    on_board = {i.get("content", {}).get("url"): i for i in items}
    changes = 0
    for repo, spec in REGISTRY.items():
        for i in gh_json("issue", "list", "-R", f"{OWNER}/{repo}", "-L", "500", "--state", "all", "--json", "url,state,labels"):
            it = on_board.get(i["url"])
            if it is None:
                if i["state"] != "OPEN":
                    continue
                added = write("gh", "project", "item-add", BOARD, "--owner", OWNER, "--url", i["url"], "--format", "json")
                if not added:
                    continue
                it = {"id": json.loads(added)["id"]}
                write("gh", "project", "item-edit", "--id", it["id"], "--project-id", proj["id"], "--field-id",
                      fields["System"]["id"], "--single-select-option-id", opt("System", spec["system"]))
                changes += 1
            pr = next((l["name"].split()[-1] for l in i["labels"] if l["name"].startswith("priority: ")), None)
            if pr in ("P0", "P1", "P2") and it.get("priority") != pr:
                write("gh", "project", "item-edit", "--id", it["id"], "--project-id", proj["id"], "--field-id",
                      fields["Priority"]["id"], "--single-select-option-id", opt("Priority", pr)); changes += 1
            status = it.get("status")
            want = "Done" if i["state"] != "OPEN" else ("Todo" if status in (None, "Done") else None)
            if want and status != want:
                write("gh", "project", "item-edit", "--id", it["id"], "--project-id", proj["id"], "--field-id",
                      fields["Status"]["id"], "--single-select-option-id", opt("Status", want)); changes += 1
    log(f"board: {changes} field changes")


def merge_green_dependabot():
    """Merge Dependabot PRs whose head passes the repo's gate. Others get one comment."""
    for repo, spec in REGISTRY.items():
        prs = gh_json("pr", "list", "-R", f"{OWNER}/{repo}", "--author", "app/dependabot", "--json", "number,headRefName,title")
        for pr in prs:
            with tempfile.TemporaryDirectory(prefix="smc17ops-pr-") as tmp:
                dest = Path(tmp) / repo
                sh(["gh", "repo", "clone", f"{OWNER}/{repo}", str(dest), "--", "-q", "--depth", "1", "--branch", pr["headRefName"]], timeout=600)
                ok = True
                for cmd in spec.get("gate", []):
                    try:
                        p = sh(cmd, cwd=dest, timeout=spec.get("timeout", 900))
                        if p.returncode or parse_tests(p.stdout + p.stderr)["failed"]:
                            ok = False
                    except subprocess.TimeoutExpired:
                        ok = False
            if ok:
                log(f"merge dependabot {repo}#{pr['number']}: {pr['title']}")
                write("gh", "pr", "merge", str(pr["number"]), "-R", f"{OWNER}/{repo}", "--squash", "--delete-branch")
            else:
                comments = gh_json("pr", "view", str(pr["number"]), "-R", f"{OWNER}/{repo}", "--json", "comments")["comments"]
                if not any("smc17-ops" in c["body"] for c in comments):
                    write("gh", "pr", "comment", str(pr["number"]), "-R", f"{OWNER}/{repo}", "-b",
                          "smc17-ops: the repository gate fails on this branch, so it was not merged automatically.")


# ---------------------------------------------------------------- report (ratchet)

def load_baseline():
    p = HERE / "baseline.json"
    return json.loads(p.read_text()) if p.exists() else {}


def regressions(latest, baseline):
    """Return {repo: [(key, message)]}. A key identifies one ratchet so it can be opened and closed."""
    out = {}
    for repo, e in latest["repos"].items():
        g, b = e.get("gate", {}), baseline.get(repo, {})
        found = []
        if REGISTRY[repo].get("gate") and not g.get("ok"):
            failing = [s for s in g.get("steps", []) if s.get("rc")]
            detail = "\n".join(f"- `{s['cmd']}` exited {s['rc']}\n  ```\n  " + "\n  ".join(s.get("tail", [])) + "\n  ```" for s in failing) or g.get("error", "")
            found.append(("gate", f"The fresh-clone gate fails at `{g.get('commit')}`.\n\n{detail}"))
        if b.get("passed") and (g.get("passed") or 0) < b["passed"]:
            found.append(("tests", f"Passing tests dropped from {b['passed']} to {g.get('passed')} at `{g.get('commit')}`."))
        miss = e.get("standards", {}).get("missing", [])
        if miss:
            found.append(("standards", "Missing standard files: " + ", ".join(miss) + ". See STANDARDS.md."))
        wb = e.get("workbooks")
        if wb and "error" not in wb and b.get("formula_computed_pct") is not None:
            if wb["formula_computed_pct"] < b["formula_computed_pct"]:
                found.append(("workbooks-computed", f"Computed formulas fell from {b['formula_computed_pct']}% to {wb['formula_computed_pct']}%."))
            if wb["placeholders"] > b["placeholders"]:
                found.append(("workbooks-placeholders", f"Placeholder cells rose from {b['placeholders']} to {wb['placeholders']}."))
        out[repo] = found
    return out


def ratchet_baseline(latest, baseline):
    """Raise the baseline wherever things improved; never lower it."""
    nb = dict(baseline)
    for repo, e in latest["repos"].items():
        g, b = e.get("gate", {}), dict(baseline.get(repo, {}))
        if g.get("ok") and (g.get("passed") or 0) > b.get("passed", 0):
            b["passed"] = g["passed"]
        wb = e.get("workbooks")
        if wb and "error" not in wb:
            b["formula_computed_pct"] = max(b.get("formula_computed_pct", 0), wb["formula_computed_pct"])
            b["placeholders"] = min(b.get("placeholders", wb["placeholders"]), wb["placeholders"])
        nb[repo] = b
    return nb


def sync_issues(found):
    for repo, items in found.items():
        existing = gh_json("issue", "list", "-R", f"{OWNER}/{repo}", "-L", "200", "--state", "open", "--search", f"in:title \"{ISSUE_PREFIX}\"", "--json", "number,title")
        open_by_key = {i["title"].split(" regressed")[0].removeprefix(ISSUE_PREFIX): i for i in existing if i["title"].startswith(ISSUE_PREFIX)}
        keys = {k for k, _ in items}
        for key, msg in items:
            title = f"{ISSUE_PREFIX}{key} regressed"
            body = f"{msg}\n\nOpened by the nightly [SMC17 ops run](https://github.com/{OWNER}/{OWNER}/blob/main/OPS.md). It closes itself when the check recovers."
            if key in open_by_key:
                continue
            log(f"open issue {repo}: {title}")
            write("gh", "issue", "create", "-R", f"{OWNER}/{repo}", "-t", title, "-b", body,
                  "-l", "type: bug", "-l", "priority: P1", "-l", "status: ready")
        for key, issue in open_by_key.items():
            if key not in keys:
                log(f"close recovered {repo}#{issue['number']}")
                write("gh", "issue", "close", str(issue["number"]), "-R", f"{OWNER}/{repo}", "-r", "completed",
                      "-c", "Recovered: the nightly SMC17 ops run passes this check again.")


def render_ops(latest, found):
    hist = [json.loads(l) for l in (STATE / "history.jsonl").read_text().splitlines()[-14:]] if (STATE / "history.jsonl").exists() else []
    def trend(repo, key):
        vals = [h["repos"].get(repo, {}).get(key) for h in hist]
        vals = [v for v in vals if v is not None]
        return " → ".join(str(v) for v in vals[-5:]) if vals else ""
    lines = [
        "# SMC17 ops", "",
        f"Last run: {latest['started']} on {latest['host']}, Zig {latest['zig']}. Generated by [`ops/smc17ops.py`](ops/smc17ops.py); "
        "each repo is cloned fresh and its gate run as written in [`ops/registry.json`](ops/registry.json).", "",
        "Regressions open a `ops: … regressed` issue in that repo and close it on recovery. "
        "Baselines only move up ([`ops/baseline.json`](ops/baseline.json)).", "",
        "| Repo | Gate | Passed | Failed | Skipped | Open issues (P0/P1) | Untriaged | Stale PRs | Open regressions |",
        "|---|---|---:|---:|---:|---|---:|---:|---:|",
    ]
    for repo, e in latest["repos"].items():
        g, t = e.get("gate", {}), e.get("tracker", {})
        gate_txt = "n/a" if not REGISTRY[repo].get("gate") else ("pass" if g.get("ok") else "**FAIL**")
        lines.append(f"| [{repo}](https://github.com/{OWNER}/{repo}) | {gate_txt} | {g.get('passed', '')} | {g.get('failed', '')} | "
                     f"{g.get('skipped', '')} | {t.get('open_issues', '')} ({t.get('p0', 0)}/{t.get('p1', 0)}) | {t.get('untriaged', '')} | "
                     f"{t.get('stale_prs', '')} | {len(found.get(repo, []))} |")
    wb = latest["repos"].get("finance-segway", {}).get("workbooks")
    if wb and "error" not in wb:
        lines += ["", "## Depth meters", "",
                  "**finance-segway workbooks** (`tools/workbook_completeness.py`): "
                  f"{wb['workbooks']} workbooks, {wb['formulas']} formulas, **{wb['formula_computed_pct']}% computed**, "
                  f"{wb['never_computed_workbooks']} never computed, {wb['placeholders']} placeholder cells, {wb['errors']} error values.",
                  f"Trend (computed %): {trend('finance-segway', 'formula_computed_pct')}"]
    lines += ["", "## Passing tests, last runs", "", "| Repo | Trend |", "|---|---|"]
    for repo in latest["repos"]:
        lines.append(f"| {repo} | {trend(repo, 'passed')} |")
    return "\n".join(lines) + "\n"


def report():
    latest = json.loads((STATE / "latest.json").read_text())
    baseline = load_baseline()
    found = regressions(latest, baseline)
    sync_issues(found)
    (HERE / "baseline.json").write_text(json.dumps(ratchet_baseline(latest, baseline), indent=1, sort_keys=True) + "\n")
    (ROOT / "OPS.md").write_text(render_ops(latest, found))
    publish()
    n = sum(len(v) for v in found.values())
    log(f"report: {n} open regressions across {sum(1 for v in found.values() if v)} repos")


def publish():
    """Commit OPS.md, baseline and history to the profile repo if they changed."""
    files = ["OPS.md", "ops/baseline.json", "ops/state/history.jsonl"]
    if not sh(["git", "-C", str(ROOT), "status", "--porcelain", "--", *files]).stdout.strip():
        return
    if DRY:
        log("DRY-RUN would commit", files); return
    env = dict(os.environ, GIT_AUTHOR_NAME="SMC17", GIT_AUTHOR_EMAIL="173011278+SMC17@users.noreply.github.com",
               GIT_COMMITTER_NAME="SMC17", GIT_COMMITTER_EMAIL="173011278+SMC17@users.noreply.github.com")
    sh(["git", "-C", str(ROOT), "pull", "-q", "--rebase", "--autostash"])
    sh(["git", "-C", str(ROOT), "add", "--", *files])
    subprocess.run(["git", "-C", str(ROOT), "commit", "-qm", "ops: nightly report"], env=env)
    r = sh(["git", "-C", str(ROOT), "push", "-q"])
    log("published" if not r.returncode else "push failed: " + r.stderr.strip()[:200])


def main():
    global DRY
    ap = argparse.ArgumentParser(description="SMC17 ops")
    ap.add_argument("command", choices=["sense", "heal", "report", "run"])
    ap.add_argument("--dry-run", action="store_true", help="print write actions instead of doing them")
    ap.add_argument("--only", nargs="*", help="limit sense to these repos")
    a = ap.parse_args()
    DRY = a.dry_run
    lock = Path(tempfile.gettempdir()) / "smc17ops.lock"
    if lock.exists() and time.time() - lock.stat().st_mtime < 6 * 3600:
        log("another run holds the lock; exiting"); return 0
    lock.write_text(str(os.getpid()))
    try:
        if a.command in ("sense", "run"):
            sense(a.only)
        if a.command in ("heal", "run"):
            heal()
        if a.command in ("report", "run"):
            report()
    finally:
        lock.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
