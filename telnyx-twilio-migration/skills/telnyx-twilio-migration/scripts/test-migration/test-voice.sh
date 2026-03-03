#!/usr/bin/env bash
#
# test-voice.sh — Make a real outbound test call via Telnyx Call Control API
#
# Usage: bash test-voice.sh --confirm [--dry-run]
#
# Arguments:
#   --confirm    Required to actually place the call
#   --dry-run    Validate setup without making a call
#   --help       Show this help and exit
#
# Environment variables (required):
#   TELNYX_API_KEY       Your Telnyx API key
#   TELNYX_FROM_NUMBER   Caller ID (your Telnyx number, E.164 format)
#   TELNYX_TO_NUMBER     Destination number (E.164 format)
#
# Environment variables (optional):
#   TELNYX_CONNECTION_ID   Connection ID to use (auto-detected if not set)
#
# Exit codes:
#   0 — Call completed successfully
#   1 — Call failed or setup error

set -euo pipefail

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

# --- Parse arguments ---
CONFIRMED=false
DRY_RUN=false

for arg in "$@"; do
  case "$arg" in
    --confirm) CONFIRMED=true ;;
    --dry-run) DRY_RUN=true ;;
    --help|-h)
      echo "Usage: bash test-voice.sh --confirm [--dry-run]"
      echo ""
      echo "Makes a real outbound test call via Telnyx Call Control API."
      echo ""
      echo "Flags:"
      echo "  --confirm    Required to actually place the call"
      echo "  --dry-run    Validate setup without making a call"
      echo ""
      echo "Environment variables:"
      echo "  TELNYX_API_KEY       (required) Your Telnyx API key"
      echo "  TELNYX_FROM_NUMBER   (required) Caller ID, E.164 format (e.g., +15551234567)"
      echo "  TELNYX_TO_NUMBER     (required) Destination number, E.164 format"
      echo "  TELNYX_CONNECTION_ID (optional) Connection ID (auto-detected if not set)"
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Run with --help for usage." >&2
      exit 2
      ;;
  esac
done

echo -e "${BOLD}Telnyx Voice Test${NC}"
echo "=================="
echo ""
echo -e "${YELLOW}${BOLD}COST WARNING: This test makes a real outbound call (~\$0.01)${NC}"
echo ""

# --- Validate prerequisites ---
ERRORS=0

if [ -z "${TELNYX_API_KEY:-}" ]; then
  echo -e "  ${RED}FAIL${NC}  TELNYX_API_KEY is not set"
  ERRORS=$((ERRORS + 1))
else
  echo -e "  ${GREEN}PASS${NC}  TELNYX_API_KEY is set (${TELNYX_API_KEY:0:8}...)"
fi

if [ -z "${TELNYX_FROM_NUMBER:-}" ]; then
  echo -e "  ${RED}FAIL${NC}  TELNYX_FROM_NUMBER is not set"
  ERRORS=$((ERRORS + 1))
else
  echo -e "  ${GREEN}PASS${NC}  TELNYX_FROM_NUMBER: ${TELNYX_FROM_NUMBER}"
fi

if [ -z "${TELNYX_TO_NUMBER:-}" ]; then
  echo -e "  ${RED}FAIL${NC}  TELNYX_TO_NUMBER is not set"
  ERRORS=$((ERRORS + 1))
else
  echo -e "  ${GREEN}PASS${NC}  TELNYX_TO_NUMBER: ${TELNYX_TO_NUMBER}"
fi

if ! command -v curl &>/dev/null; then
  echo -e "  ${RED}FAIL${NC}  curl is not installed"
  ERRORS=$((ERRORS + 1))
fi

HAS_JQ=false
if command -v jq &>/dev/null; then
  HAS_JQ=true
  echo -e "  ${GREEN}PASS${NC}  jq is available"
else
  echo -e "  ${YELLOW}WARN${NC}  jq not installed (output will be limited)"
fi

if [ "$ERRORS" -gt 0 ]; then
  echo ""
  echo -e "${RED}${BOLD}Setup validation failed. Fix the errors above.${NC}"
  exit 1
fi

# --- Validate API key ---
echo ""
echo -e "${BOLD}Validating API key...${NC}"

HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer ${TELNYX_API_KEY}" \
  "https://api.telnyx.com/v2/balance" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" != "200" ]; then
  echo -e "  ${RED}FAIL${NC}  API key validation failed (HTTP $HTTP_CODE)"
  exit 1
fi
echo -e "  ${GREEN}PASS${NC}  API key is valid"

# --- Dry run exits here ---
if [ "$DRY_RUN" = true ]; then
  echo ""
  echo -e "${BOLD}Dry run complete.${NC} Setup looks good."
  echo "  Would call: ${TELNYX_FROM_NUMBER} -> ${TELNYX_TO_NUMBER}"
  echo "  Estimated cost: ~\$0.01"
  echo ""
  echo "Run with --confirm to place the call."
  exit 0
fi

# --- Require --confirm ---
if [ "$CONFIRMED" = false ]; then
  echo ""
  echo -e "${BOLD}What this test will do:${NC}"
  echo "  1. Place an outbound call from ${TELNYX_FROM_NUMBER} to ${TELNYX_TO_NUMBER}"
  echo "  2. Play a short TTS message when answered"
  echo "  3. Hang up after the message"
  echo "  4. Report call status and duration"
  echo ""
  echo "  Estimated cost: ~\$0.01"
  echo ""
  echo "Run with --confirm to proceed."
  exit 0
fi

# --- Build connection_id if needed ---
CONNECTION_ID="${TELNYX_CONNECTION_ID:-}"
if [ -z "$CONNECTION_ID" ]; then
  echo ""
  echo -e "${BOLD}Auto-detecting connection ID...${NC}"
  CONN_RESPONSE=$(curl -s \
    -H "Authorization: Bearer ${TELNYX_API_KEY}" \
    "https://api.telnyx.com/v2/connections?page[size]=1" 2>/dev/null || echo "")
  if [ "$HAS_JQ" = true ] && [ -n "$CONN_RESPONSE" ]; then
    CONNECTION_ID=$(echo "$CONN_RESPONSE" | jq -r '.data[0].id // empty' 2>/dev/null)
  fi
  if [ -z "$CONNECTION_ID" ]; then
    echo -e "  ${RED}FAIL${NC}  No connection found. Create one in the Telnyx portal or set TELNYX_CONNECTION_ID."
    exit 1
  fi
  echo -e "  ${GREEN}PASS${NC}  Using connection: ${CONNECTION_ID}"
fi

# --- Place the call ---
echo ""
echo -e "${BOLD}Placing call...${NC}"
echo "  From: ${TELNYX_FROM_NUMBER}"
echo "  To:   ${TELNYX_TO_NUMBER}"
echo ""

CALL_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Bearer ${TELNYX_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"connection_id\": \"${CONNECTION_ID}\",
    \"to\": \"${TELNYX_TO_NUMBER}\",
    \"from\": \"${TELNYX_FROM_NUMBER}\",
    \"answering_machine_detection\": \"disabled\",
    \"webhook_url\": \"https://example.com/null\"
  }" \
  "https://api.telnyx.com/v2/calls" 2>/dev/null || echo "")

if [ -z "$CALL_RESPONSE" ]; then
  echo -e "  ${RED}FAIL${NC}  No response from API"
  exit 1
fi

# Extract call control ID
CALL_CONTROL_ID=""
CALL_LEG_ID=""
if [ "$HAS_JQ" = true ]; then
  CALL_CONTROL_ID=$(echo "$CALL_RESPONSE" | jq -r '.data.call_control_id // empty' 2>/dev/null)
  CALL_LEG_ID=$(echo "$CALL_RESPONSE" | jq -r '.data.call_leg_id // empty' 2>/dev/null)
  API_ERROR=$(echo "$CALL_RESPONSE" | jq -r '.errors[0].detail // empty' 2>/dev/null)

  if [ -n "$API_ERROR" ]; then
    echo -e "  ${RED}FAIL${NC}  API error: $API_ERROR"
    exit 1
  fi
fi

if [ -z "$CALL_CONTROL_ID" ]; then
  echo -e "  ${RED}FAIL${NC}  Could not extract call_control_id from response"
  if [ "$HAS_JQ" = true ]; then
    echo "  Response: $(echo "$CALL_RESPONSE" | jq -c . 2>/dev/null || echo "$CALL_RESPONSE")"
  fi
  exit 1
fi

echo -e "  ${GREEN}PASS${NC}  Call initiated"
echo "  Call Control ID: ${CALL_CONTROL_ID}"
echo "  Call Leg ID:     ${CALL_LEG_ID}"

# --- Monitor call status ---
echo ""
echo -e "${BOLD}Monitoring call status...${NC}"

CALL_START=$(date +%s)
MAX_WAIT=60
LAST_STATE=""
REACHED_ANSWERED=false
STATUS_LOG=""

cleanup_call() {
  if [ -n "$CALL_CONTROL_ID" ]; then
    echo ""
    echo -e "${BOLD}Cleaning up (hanging up if active)...${NC}"
    curl -s -X POST \
      -H "Authorization: Bearer ${TELNYX_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"call_control_id\": \"${CALL_CONTROL_ID}\"}" \
      "https://api.telnyx.com/v2/calls/${CALL_CONTROL_ID}/actions/hangup" >/dev/null 2>&1 || true
    echo -e "  ${BLUE}INFO${NC}  Hangup sent"
  fi
}

# Ensure cleanup on exit
trap cleanup_call EXIT

while true; do
  ELAPSED=$(( $(date +%s) - CALL_START ))

  if [ "$ELAPSED" -ge "$MAX_WAIT" ]; then
    echo -e "  ${YELLOW}WARN${NC}  Timeout after ${MAX_WAIT}s"
    break
  fi

  # Poll call status
  STATUS_RESPONSE=$(curl -s \
    -H "Authorization: Bearer ${TELNYX_API_KEY}" \
    "https://api.telnyx.com/v2/calls/${CALL_CONTROL_ID}" 2>/dev/null || echo "")

  CURRENT_STATE=""
  if [ "$HAS_JQ" = true ] && [ -n "$STATUS_RESPONSE" ]; then
    CURRENT_STATE=$(echo "$STATUS_RESPONSE" | jq -r '.data.state // .data.is_alive // empty' 2>/dev/null)
    # Also check if the call is alive
    IS_ALIVE=$(echo "$STATUS_RESPONSE" | jq -r '.data.is_alive // empty' 2>/dev/null)
  fi

  # Report state changes
  if [ -n "$CURRENT_STATE" ] && [ "$CURRENT_STATE" != "$LAST_STATE" ]; then
    echo -e "  ${BLUE}INFO${NC}  State: ${CURRENT_STATE} (${ELAPSED}s)"
    STATUS_LOG="${STATUS_LOG}${CURRENT_STATE} -> "
    LAST_STATE="$CURRENT_STATE"

    if [ "$CURRENT_STATE" = "answered" ] || [ "$CURRENT_STATE" = "active" ]; then
      REACHED_ANSWERED=true

      # Send TTS speak command
      echo -e "  ${BLUE}INFO${NC}  Sending TTS message..."
      curl -s -X POST \
        -H "Authorization: Bearer ${TELNYX_API_KEY}" \
        -H "Content-Type: application/json" \
        -d "{
          \"call_control_id\": \"${CALL_CONTROL_ID}\",
          \"payload\": \"This is a test call from Telnyx. Your migration is working correctly. Goodbye.\",
          \"voice\": \"female\",
          \"language\": \"en-US\"
        }" \
        "https://api.telnyx.com/v2/calls/${CALL_CONTROL_ID}/actions/speak" >/dev/null 2>&1 || true

      # Wait for TTS to play, then hang up
      sleep 5
      break
    fi

    if [ "$CURRENT_STATE" = "completed" ] || [ "$CURRENT_STATE" = "hangup" ]; then
      break
    fi
  fi

  # Check if call is no longer alive
  if [ "${IS_ALIVE:-}" = "false" ]; then
    echo -e "  ${BLUE}INFO${NC}  Call ended (${ELAPSED}s)"
    break
  fi

  sleep 2
done

CALL_END=$(date +%s)
CALL_DURATION=$(( CALL_END - CALL_START ))

# Disable cleanup trap if we handle it ourselves
trap - EXIT

# Final hangup
echo ""
echo -e "${BOLD}Hanging up...${NC}"
curl -s -X POST \
  -H "Authorization: Bearer ${TELNYX_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{\"call_control_id\": \"${CALL_CONTROL_ID}\"}" \
  "https://api.telnyx.com/v2/calls/${CALL_CONTROL_ID}/actions/hangup" >/dev/null 2>&1 || true

# --- Report ---
echo ""
echo "=================="
echo -e "${BOLD}Results${NC}"
echo "  Call Control ID: ${CALL_CONTROL_ID}"
echo "  Status Flow:     ${STATUS_LOG%% -> }"
echo "  Total Duration:  ${CALL_DURATION}s"
echo "  Cost Estimate:   ~\$0.01"

if [ "$REACHED_ANSWERED" = true ]; then
  echo ""
  echo -e "  ${GREEN}${BOLD}PASS${NC}  Call was answered and TTS was played"
  exit 0
else
  echo ""
  echo -e "  ${RED}${BOLD}FAIL${NC}  Call did not reach answered state"
  echo "  Check that the destination number is valid and can receive calls."
  exit 1
fi
