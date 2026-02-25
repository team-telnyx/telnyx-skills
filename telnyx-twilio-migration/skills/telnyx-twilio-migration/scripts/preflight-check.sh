#!/usr/bin/env bash
#
# preflight-check.sh — Validate migration environment readiness
#
# Usage: bash preflight-check.sh
#
# Checks:
#   - TELNYX_API_KEY environment variable
#   - API connectivity to api.telnyx.com
#   - Installed Twilio SDKs (to confirm what's being replaced)
#   - Installed Telnyx SDKs
#
# Output: Structured report with pass/fail per check
# Exit codes:
#   0 — All critical checks passed
#   1 — One or more critical checks failed

set -uo pipefail

# --- Colors (disabled if not a terminal) ---
if [ -t 1 ]; then
  RED='\033[0;31m'
  YELLOW='\033[0;33m'
  GREEN='\033[0;32m'
  BLUE='\033[0;34m'
  BOLD='\033[1m'
  NC='\033[0m'
else
  RED='' YELLOW='' GREEN='' BLUE='' BOLD='' NC=''
fi

PASS=0
FAIL=0
WARN=0

check_pass() {
  echo -e "  ${GREEN}PASS${NC}  $1"
  PASS=$((PASS + 1))
}

check_fail() {
  echo -e "  ${RED}FAIL${NC}  $1"
  FAIL=$((FAIL + 1))
}

check_warn() {
  echo -e "  ${YELLOW}WARN${NC}  $1"
  WARN=$((WARN + 1))
}

check_info() {
  echo -e "  ${BLUE}INFO${NC}  $1"
}

echo -e "${BOLD}Telnyx Migration Preflight Check${NC}"
echo "─────────────────────────────────────"

# --- 1. TELNYX_API_KEY ---
echo ""
echo -e "${BOLD}Telnyx Credentials${NC}"

if [ -n "${TELNYX_API_KEY:-}" ]; then
  # Mask the key for display
  KEY_PREFIX="${TELNYX_API_KEY:0:8}"
  check_pass "TELNYX_API_KEY is set (${KEY_PREFIX}...)"
else
  check_fail "TELNYX_API_KEY is not set. Get one at https://portal.telnyx.com/#/app/api-keys"
fi

# --- 2. API Connectivity ---
echo ""
echo -e "${BOLD}API Connectivity${NC}"

if command -v curl &>/dev/null; then
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: Bearer ${TELNYX_API_KEY:-invalid}" \
    "https://api.telnyx.com/v2/balance" 2>/dev/null || echo "000")

  if [ "$HTTP_CODE" = "200" ]; then
    check_pass "api.telnyx.com is reachable and API key is valid (HTTP $HTTP_CODE)"
  elif [ "$HTTP_CODE" = "401" ] || [ "$HTTP_CODE" = "403" ]; then
    check_fail "api.telnyx.com is reachable but API key is invalid (HTTP $HTTP_CODE)"
  elif [ "$HTTP_CODE" = "000" ]; then
    check_fail "Cannot reach api.telnyx.com — check network connectivity"
  else
    check_warn "api.telnyx.com returned HTTP $HTTP_CODE — check API key and account status"
  fi
else
  check_warn "curl not found — cannot test API connectivity"
fi

# --- 3. Twilio SDK Detection ---
echo ""
echo -e "${BOLD}Twilio SDKs Detected (to be replaced)${NC}"

TWILIO_FOUND=false

# Python
if python3 -c "import twilio" 2>/dev/null; then
  TWILIO_VER=$(python3 -c "import twilio; print(twilio.__version__)" 2>/dev/null || echo "unknown")
  check_info "Python: twilio $TWILIO_VER"
  TWILIO_FOUND=true
elif python -c "import twilio" 2>/dev/null; then
  check_info "Python: twilio (version unknown)"
  TWILIO_FOUND=true
fi

# Node.js
if [ -d "node_modules/twilio" ] 2>/dev/null; then
  TWILIO_NODE_VER=$(node -e "console.log(require('twilio/package.json').version)" 2>/dev/null || echo "unknown")
  check_info "Node.js: twilio $TWILIO_NODE_VER"
  TWILIO_FOUND=true
elif npm list twilio 2>/dev/null | grep -q twilio; then
  check_info "Node.js: twilio (installed globally or in project)"
  TWILIO_FOUND=true
fi

# Ruby
if gem list twilio-ruby 2>/dev/null | grep -q twilio-ruby; then
  TWILIO_RUBY_VER=$(gem list twilio-ruby 2>/dev/null | grep -o '([^)]*)')
  check_info "Ruby: twilio-ruby $TWILIO_RUBY_VER"
  TWILIO_FOUND=true
fi

# Go
if go list -m github.com/twilio/twilio-go 2>/dev/null; then
  check_info "Go: twilio-go (found in go.mod)"
  TWILIO_FOUND=true
fi

# Java (check for jar in common locations)
if find . -name "twilio-*.jar" -maxdepth 3 2>/dev/null | grep -q twilio; then
  check_info "Java: twilio jar found in project"
  TWILIO_FOUND=true
fi

if [ "$TWILIO_FOUND" = false ]; then
  check_info "No Twilio SDKs detected in current environment"
fi

# --- 4. Telnyx SDK Detection ---
echo ""
echo -e "${BOLD}Telnyx SDKs Installed${NC}"

TELNYX_FOUND=false

# Python
if python3 -c "import telnyx" 2>/dev/null; then
  TELNYX_PY_VER=$(python3 -c "import telnyx; print(telnyx.VERSION)" 2>/dev/null || echo "unknown")
  check_pass "Python: telnyx $TELNYX_PY_VER"
  TELNYX_FOUND=true
fi

# Node.js
if [ -d "node_modules/telnyx" ] 2>/dev/null; then
  TELNYX_NODE_VER=$(node -e "console.log(require('telnyx/package.json').version)" 2>/dev/null || echo "unknown")
  check_pass "Node.js: telnyx $TELNYX_NODE_VER"
  TELNYX_FOUND=true
elif npm list telnyx 2>/dev/null | grep -q telnyx; then
  check_pass "Node.js: telnyx (installed)"
  TELNYX_FOUND=true
fi

# Ruby
if gem list telnyx 2>/dev/null | grep -q "^telnyx "; then
  TELNYX_RUBY_VER=$(gem list telnyx 2>/dev/null | grep "^telnyx " | grep -o '([^)]*)')
  check_pass "Ruby: telnyx $TELNYX_RUBY_VER"
  TELNYX_FOUND=true
fi

# Go
if go list -m github.com/telnyx/telnyx-go 2>/dev/null; then
  check_pass "Go: telnyx-go (found in go.mod)"
  TELNYX_FOUND=true
fi

if [ "$TELNYX_FOUND" = false ]; then
  check_warn "No Telnyx SDKs detected. Install one: pip install telnyx / npm install telnyx / gem install telnyx"
fi

# --- Summary ---
echo ""
echo "─────────────────────────────────────"
echo -e "${BOLD}Summary${NC}"
echo -e "  ${GREEN}Pass${NC}: $PASS"
echo -e "  ${RED}Fail${NC}: $FAIL"
echo -e "  ${YELLOW}Warn${NC}: $WARN"

if [ "$FAIL" -gt 0 ]; then
  echo ""
  echo -e "${RED}${BOLD}Not ready for migration.${NC} Fix the failures above before proceeding."
  exit 1
else
  echo ""
  echo -e "${GREEN}${BOLD}Environment is ready for migration.${NC}"
  exit 0
fi
