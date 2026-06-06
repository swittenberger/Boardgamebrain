#!/usr/bin/env bash
# Install the bgb skills into Hermes Agent via the hermes CLI (writes proper
# trust records, runs Skills Guard). Usage:
#   git clone --depth 1 https://github.com/swittenberger/Boardgamebrain /tmp/bgb
#   bash /tmp/bgb/hermes/install.sh
set -u

H="${HERMES_BIN:-/opt/hermes/.venv/bin/hermes}"
[ -x "$H" ] || H="$(command -v hermes || true)"
if [ -z "$H" ]; then
  echo "hermes CLI not found — set HERMES_BIN=/path/to/hermes and re-run." >&2
  exit 1
fi

REPO="swittenberger/Boardgamebrain"
FAILED=0

for s in setup new help move rule insights research; do
  echo "==> bgb-$s"
  if ! "$H" skills install "$REPO/hermes/skills/bgb/bgb-$s" --yes; then
    # GitHub identifier not accepted? Fall back to the local checkout copy.
    if ! "$H" skills install "/tmp/bgb/hermes/skills/bgb/bgb-$s" --yes; then
      echo "    install failed for bgb-$s" >&2
      FAILED=1
    fi
  fi
done

echo
"$H" skills list | grep -i bgb || echo "No bgb skills listed yet — check output above."
[ "$FAILED" -eq 0 ] && echo "Done. You can: rm -rf /tmp/bgb"
exit "$FAILED"
