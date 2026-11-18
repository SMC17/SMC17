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
  launchctl bootout "gui/$(id -u)/com.smc17.finance-library" 2>/dev/null || true
  rm -f "$PLIST" "$HOME/Library/LaunchAgents/com.smc17.finance-library.plist"
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
# .NET SDK 10 for MarketDataSimulator, pinned with a GC root. A moving nixpkgs
# can lose its binary cache entry and try to compile the SDK from source.
if [[ ! -e "$OPS/.bin/dotnet-sdk-10" ]]; then
  if DN="$(nix build --no-link --print-out-paths nixpkgs#dotnet-sdk_10 2>/dev/null)"; then
    nix-store --add-root "$OPS/.bin/dotnet-sdk-10" --indirect -r "$DN" >/dev/null
  fi
fi
[[ -e "$OPS/.bin/dotnet-sdk-10" ]] && ln -sf dotnet-sdk-10/bin/dotnet "$OPS/.bin/dotnet"
# wagwan-score (method-wagwan's scoring CLI) scores the forecast ledger.
WG="$(mktemp -d)"
if gh repo clone SMC17/method-wagwan "$WG/mw" -- -q --depth 1 && (cd "$WG/mw" && zig build -Doptimize=ReleaseSafe >/dev/null); then
  cp "$WG/mw/zig-out/bin/wagwan-score" "$OPS/.bin/wagwan-score"
fi
rm -rf "$WG"
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

# Nightly finance-segway library (every SEC XBRL filer; deterministic, no AI). SEC builds its
# bulk archives about 04:50 UTC (22:50 in Chicago), so 01:30 local reads the fresh night.
LIB_LABEL="com.smc17.finance-library"
LIB_PLIST="$HOME/Library/LaunchAgents/$LIB_LABEL.plist"
cat > "$LIB_PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LIB_LABEL</string>
  <key>ProgramArguments</key>
  <array><string>/bin/bash</string><string>-lc</string><string>"$OPS/finance_library.sh"</string></array>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>$PATH</string></dict>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>1</integer><key>Minute</key><integer>30</integer></dict>
  <key>StandardOutPath</key><string>$LOGS/finance-library.log</string>
  <key>StandardErrorPath</key><string>$LOGS/finance-library.log</string>
  <key>LowPriorityIO</key><true/>
  <key>Nice</key><integer>10</integer>
</dict>
</plist>
PLIST
launchctl bootout "gui/$(id -u)/$LIB_LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$LIB_PLIST"
echo "installed $LIB_LABEL: nightly at 01:30; logs in $LOGS/finance-library.log"
