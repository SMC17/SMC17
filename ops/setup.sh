#!/usr/bin/env bash
# Set up SMC17 ops on this machine: a Python venv for depth meters and a nightly
# launchd job. Re-run safely; it replaces the job definition.
#   ops/setup.sh            install
#   ops/setup.sh --remove   uninstall the launchd job
set -euo pipefail
OPS="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$OPS")"
LABEL="com.smc17.ops"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOGS="$HOME/Library/Logs/smc17-ops"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
  rm -f "$PLIST"
  echo "removed $LABEL"
  exit 0
fi

python3 -m venv "$OPS/.venv"
"$OPS/.venv/bin/pip" install -q --disable-pip-version-check openpyxl

# LibreOffice for workbook checks: nix's bin/soffice wrapper returns before work is
# done (it calls `open -na`), so link the real binary inside the app bundle.
mkdir -p "$OPS/.bin"
if LO="$(nix build --no-link --print-out-paths nixpkgs#libreoffice-bin 2>/dev/null)"; then
  ln -sf "$LO/Applications/LibreOffice.app/Contents/MacOS/soffice" "$OPS/.bin/soffice"
fi
mkdir -p "$LOGS" "$(dirname "$PLIST")"
cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string><string>-lc</string>
    <string>cd "$ROOT" &amp;&amp; git pull -q --ff-only; python3 ops/smc17ops.py run</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>$PATH</string></dict>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>3</integer><key>Minute</key><integer>17</integer></dict>
  <key>StandardOutPath</key><string>$LOGS/ops.log</string>
  <key>StandardErrorPath</key><string>$LOGS/ops.log</string>
  <key>LowPriorityIO</key><true/>
  <key>Nice</key><integer>10</integer>
</dict>
</plist>
PLIST
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "installed $LABEL: nightly at 03:17 (runs on next wake if asleep); logs in $LOGS/ops.log"
