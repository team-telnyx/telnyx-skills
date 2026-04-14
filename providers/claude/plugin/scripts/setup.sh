#!/bin/bash
# SessionStart hook: install ffl-cli and persist env vars

echo "[telnyx-skills:setup] initializing..." >&2

INPUT=$(cat)

# Persist PATH
if [[ -n "${CLAUDE_ENV_FILE:-}" ]]; then
  echo "PATH=$HOME/Library/Python/3.9/bin:$HOME/.local/bin:$PATH" >> "$CLAUDE_ENV_FILE"
fi

# Check TELNYX_API_KEY
if [[ -z "${TELNYX_API_KEY:-}" ]]; then
  echo "[telnyx-skills:setup] WARNING: TELNYX_API_KEY not set." >&2
  echo "[telnyx-skills:setup] Skills require an API key to call Telnyx APIs." >&2
  echo "[telnyx-skills:setup] Start with: TELNYX_API_KEY=your_key claude --plugin-dir ." >&2
else
  echo "[telnyx-skills:setup] TELNYX_API_KEY found" >&2
  if [[ -n "${CLAUDE_ENV_FILE:-}" ]]; then
    echo "TELNYX_API_KEY=${TELNYX_API_KEY}" >> "$CLAUDE_ENV_FILE"
  fi
fi

# Install friction-report CLI if missing
export PATH="$HOME/Library/Python/3.9/bin:$HOME/.local/bin:$PATH"
if command -v friction-report &>/dev/null; then
  echo "[telnyx-skills:setup] friction-report ready" >&2
else
  echo "[telnyx-skills:setup] installing friction-report CLI..." >&2
  python3 -m pip install --user --quiet "${CLAUDE_PLUGIN_ROOT}/../../../tools/ffl-cli" 2>&1 | tail -3 >&2
  if command -v friction-report &>/dev/null; then
    echo "[telnyx-skills:setup] friction-report installed" >&2
  else
    echo "[telnyx-skills:setup] ERROR: failed to install friction-report" >&2
  fi
fi

echo "[telnyx-skills:setup] ready (messaging, verify, numbers)" >&2
exit 0
