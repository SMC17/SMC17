#!/bin/bash
# Nightly finance-segway library: every SEC XBRL filer through the merged engine. No AI.
# Runs only code merged to finance-segway main. Publishes only when verification passes.
#   ops/finance_library.sh            build, verify, publish
#   ops/finance_library.sh --dry-run  build and verify only
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
export PATH="$HERE/.bin:/Users/staxx/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/usr/local/bin:/usr/bin:/bin"
WORK="$HERE/.work/finance-segway"
OUT="${FINANCE_SEGWAY_LIBRARY:-$HOME/.cache/finance-segway/library}"
LOG="$HERE/state/finance-library.log"
mkdir -p "$(dirname "$WORK")" "$HERE/state"
exec > >(tee -a "$LOG") 2>&1
echo "== $(date -u +%FT%TZ) finance library"
[ -d "$WORK/.git" ] || git clone -q https://github.com/SMC17/finance-segway.git "$WORK"
git -C "$WORK" fetch -q origin main && git -C "$WORK" reset -q --hard origin/main && git -C "$WORK" clean -qfdx -e .venv
if [ ! -f "$WORK/tools/library/daily.py" ]; then echo "daily.py not on main yet; nothing to do"; exit 0; fi
cd "$WORK"
uv sync --frozen -q
PYTHONPATH=.:tools uv run --frozen python tools/library/daily.py run --verify-sample 50 --out-dir "$OUT"
DAY=$(ls -1 "$OUT" | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' | sort | tail -1)
D="$OUT/$DAY"
python3 - "$D/summary.json" > "$D/NOTES.md" <<'PY'
import json, sys
s = json.load(open(sys.argv[1]))
a = s["accounted_pct"]
print(f"Every active SEC XBRL filer through the corporate-finance engine, as of {s['as_of']} (filings accepted through that day).\n")
print(f"- Filers in SEC's archive: {s['filers_in_archive']:,}; built: {s['cases_built']:,}; status: {s['status']}")
print(f"- Cells accounted for: median {a['median']:.1f}% (p10 {a['p10']:.1f}%, p90 {a['p90']:.1f}%)")
v = s.get("verification", {})
print(f"- Verification: {v.get('checked', 0)} random observed values re-read from the live SEC API, {len(v.get('failures', []))} mismatches")
print(f"- Engine {s['engine_fingerprint']}; {s['wall_seconds']} s on {s['workers']} workers")
print("\nlibrary.zip holds one manifest per case; index.jsonl one row per filer with coverage and unfillable cells; summary.json the totals.")
PY
if [ "${1:-}" = "--dry-run" ]; then cat "$D/NOTES.md"; exit 0; fi
publish() {  # tag title
  gh release view "$1" -R SMC17/finance-segway >/dev/null 2>&1 || \
    gh release create "$1" -R SMC17/finance-segway --title "$2" --notes-file "$D/NOTES.md" --latest=false
  gh release edit "$1" -R SMC17/finance-segway --title "$2" --notes-file "$D/NOTES.md" >/dev/null
  gh release upload "$1" -R SMC17/finance-segway --clobber "$D/library.zip" "$D/index.jsonl" "$D/summary.json"
}
publish library-latest "Library (latest): as of $DAY"
MONTH=${DAY:0:7}
gh release view "library-$MONTH" -R SMC17/finance-segway >/dev/null 2>&1 || publish "library-$MONTH" "Library snapshot $MONTH (as of $DAY)"
echo "published $DAY"
