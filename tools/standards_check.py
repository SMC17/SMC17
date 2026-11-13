#!/usr/bin/env python3
"""Check every public, non-fork SMC17 repo against STANDARDS.md. Needs the gh CLI."""
import json, re, subprocess, sys

OWNER = sys.argv[1] if len(sys.argv) > 1 else "SMC17"
CHECKS = {
    "README": r"^README\.md$",
    "STATUS": r"^STATUS\.md$",
    "ROADMAP": r"^ROADMAP\.md$",
    "CONTRIB": r"^(\.github/|docs/)?CONTRIBUTING\.md$",
    "SECURITY": r"^(\.github/)?SECURITY\.md$",
    "CoC": r"(^|/)CODE_OF_CONDUCT\.md$",
    "LICENSE": r"^LICEN[CS]E",
    "ISSUE_T": r"^\.github/ISSUE_TEMPLATE/",
    "PR_T": r"(?i)(^|/)pull_request_template\.md$",
    "RELEASE": r"^\.github/release\.yml$",
}

def gh(*args):
    return json.loads(subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout)

repos = gh("repo", "list", OWNER, "--visibility", "public", "-L", "200", "--json", "name,isFork,isArchived")
names = sorted(r["name"] for r in repos if not r["isFork"] and not r["isArchived"] and r["name"] != OWNER)
print("repo".ljust(22) + " ".join(k.ljust(8) for k in CHECKS) + " open  ready")
missing_total = 0
for name in names:
    tree = gh("api", f"repos/{OWNER}/{name}/git/trees/HEAD?recursive=1")
    paths = [t["path"] for t in tree.get("tree", [])]
    marks = []
    for rx in CHECKS.values():
        ok = any(re.search(rx, p) for p in paths)
        missing_total += not ok
        marks.append(("ok" if ok else "MISSING").ljust(8))
    issues = gh("issue", "list", "-R", f"{OWNER}/{name}", "-L", "500", "--json", "labels")
    ready = sum(any(l["name"] == "status: ready" for l in i["labels"]) for i in issues)
    print(name.ljust(22) + " ".join(marks) + f" {len(issues):<5} {ready}")
sys.exit(1 if missing_total else 0)
