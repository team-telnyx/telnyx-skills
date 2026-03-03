#!/usr/bin/env bash
#
# test-messaging.sh — Send a real test SMS via Telnyx Messaging API
#
# Usage: bash test-messaging.sh --confirm [--dry-run]
#
# Arguments:
#   --confirm    Required to actually send the message
#   --dry-run    Validate setup without sending
#   --help       Show this help and exit
#
# Environment variables (required):
#   TELNYX_API_KEY       Your Telnyx API key
#   TELNYX_FROM_NUMBER   Sender number (your Telnyx number, E.164 format)
#   TELNYX_TO_NUMBER     Destination number (E.164 format)
#
# Environment variables (optional):
#   TELNYX_MESSAGING_PROFILE_ID   Messaging profile ID (auto-detected if not set)
#
# Exit codes:
#   0 — Message sent and delivery confirmed
#   1 — Message failed or setup error

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
      echo "Usage: bash test-messaging.sh --confirm [--dry-run]"
      echo ""
      echo "Sends a real test SMS via Telnyx Messaging API."
      echo ""
      echo "Flags:"
      echo "  --confirm    Required to actually send the message"
      echo "  --dry-run    Validate setup without sending"
      echo ""
      echo "Environment variables:"
      echo "  TELNYX_API_KEY                (required) Your Telnyx API key"
      echo "  TELNYX_FROM_NUMBER            (required) Sender number, E.164 format"
      echo "  TELNYX_TO_NUMBER              (required) Destination number, E.164 format"
      echo "  TELNYX_MESSAGING_PROFILE_ID   (optional) Messaging profile ID"
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Run with --help for usage." >&2
      exit 2
      ;;
  esac
done

echo -e "${BOLD}Telnyx Messaging Test${NC}"
echo "====================="
echo ""
echo -e "${YELLOW}${BOLD}COST WARNING: This test sends a real SMS (~\$0.004)${NC}"
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

# --- Auto-detect messaging profile ---
MESSAGING_PROFILE_ID="${TELNYX_MESSAGING_PROFILE_ID:-}"
if [ -z "$MESSAGING_PROFILE_ID" ]; then
  echo ""
  echo -e "${BOLD}Auto-detecting messaging profile...${NC}"
  PROFILE_RESPONSE=$(curl -s \
    -H "Authorization: Bearer ${TELNYX_API_KEY}" \
    "https://api.telnyx.com/v2/messaging_profiles?page[size]=1" 2>/dev/null || echo "")
  if [ "$HAS_JQ" = true ] && [ -n "$PROFILE_RESPONSE" ]; then
    MESSAGING_PROFILE_ID=$(echo "$PROFILE_RESPONSE" | jq -r '.data[0].id // empty' 2>/dev/null)
  fi
  if [ -n "$MESSAGING_PROFILE_ID" ]; then
    echo -e "  ${GREEN}PASS${NC}  Using messaging profile: ${MESSAGING_PROFILE_ID}"
  else
    echo -e "  ${BLUE}INFO${NC}  No messaging profile found (will send without one)"
  fi
fi

# --- Dry run exits here ---
if [ "$DRY_RUN" = true ]; then
  echo ""
  echo -e "${BOLD}Dry run complete.${NC} Setup looks good."
  echo "  Would send SMS: ${TELNYX_FROM_NUMBER} -> ${TELNYX_TO_NUMBER}"
  echo "  Messaging profile: ${MESSAGING_PROFILE_ID:-none}"
  echo "  Estimated cost: ~\$0.004"
  echo ""
  echo "Run with --confirm to send the message."
  exit 0
fi

# --- Require --confirm ---
if [ "$CONFIRMED" = false ]; then
  echo ""
  echo -e "${BOLD}What this test will do:${NC}"
  echo "  1. Send an SMS from ${TELNYX_FROM_NUMBER} to ${TELNYX_TO_NUMBER}"
  echo "  2. Poll for delivery status"
  echo "  3. Report message ID, status, and cost"
  echo ""
  echo "  Estimated cost: ~\$0.004"
  echo ""
  echo "Run with --confirm to proceed."
  exit 0
fi

# --- Send the message ---
echo ""
echo -e "${BOLD}Sending SMS...${NC}"
echo "  From: ${TELNYX_FROM_NUMBER}"
echo "  To:   ${TELNYX_TO_NUMBER}"
echo ""

# Build JSON payload
MSG_TEXT="Telnyx migration test $(date -u +%Y-%m-%dT%H:%M:%SZ). If you received this, messaging is working."

if [ -n "$MESSAGING_PROFILE_ID" ]; then
  PAYLOAD="{
    \"from\": \"${TELNYX_FROM_NUMBER}\",
    \"to\": \"${TELNYX_TO_NUMBER}\",
    \"text\": \"${MSG_TEXT}\",
    \"messaging_profile_id\": \"${MESSAGING_PROFILE_ID}\"
  }"
else
  PAYLOAD="{
    \"from\": \"${TELNYX_FROM_NUMBER}\",
    \"to\": \"${TELNYX_TO_NUMBER}\",
    \"text\": \"${MSG_TEXT}\"
  }"
fi

SEND_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Bearer ${TELNYX_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" \
  "https://api.telnyx.com/v2/messages" 2>/dev/null || echo "")

if [ -z "$SEND_RESPONSE" ]; then
  echo -e "  ${RED}FAIL${NC}  No response from API"
  exit 1
fi

# Extract message ID
MESSAGE_ID=""
INITIAL_STATUS=""
if [ "$HAS_JQ" = true ]; then
  MESSAGE_ID=$(echo "$SEND_RESPONSE" | jq -r '.data.id // empty' 2>/dev/null)
  INITIAL_STATUS=$(echo "$SEND_RESPONSE" | jq -r '.data.to[0].status // .data.status // empty' 2>/dev/null)
  API_ERROR=$(echo "$SEND_RESPONSE" | jq -r '.errors[0].detail // empty' 2>/dev/null)

  if [ -n "$API_ERROR" ]; then
    echo -e "  ${RED}FAIL${NC}  API error: $API_ERROR"
    ERROR_CODE=$(echo "$SEND_RESPONSE" | jq -r '.errors[0].code // empty' 2>/dev/null)
    if [ -n "$ERROR_CODE" ]; then
      echo -e "  ${BLUE}INFO${NC}  Error code: $ERROR_CODE"
    fi
    exit 1
  fi
fi

if [ -z "$MESSAGE_ID" ]; then
  echo -e "  ${RED}FAIL${NC}  Could not extract message ID from response"
  if [ "$HAS_JQ" = true ]; then
    echo "  Response: $(echo "$SEND_RESPONSE" | jq -c . 2>/dev/null || echo "$SEND_RESPONSE")"
  fi
  exit 1
fi

echo -e "  ${GREEN}PASS${NC}  Message sent"
echo "  Message ID: ${MESSAGE_ID}"
echo "  Initial Status: ${INITIAL_STATUS:-unknown}"

# --- Poll for delivery status ---
echo ""
echo -e "${BOLD}Polling delivery status...${NC}"

MAX_POLL=30
POLL_INTERVAL=2
POLL_START=$(date +%s)
FINAL_STATUS=""
DELIVERY_CONFIRMED=false

while true; do
  ELAPSED=$(( $(date +%s) - POLL_START ))

  if [ "$ELAPSED" -ge "$MAX_POLL" ]; then
    echo -e "  ${YELLOW}WARN${NC}  Polling timeout after ${MAX_POLL}s"
    break
  fi

  sleep "$POLL_INTERVAL"

  # Check message status via API
  STATUS_RESPONSE=$(curl -s \
    -H "Authorization: Bearer ${TELNYX_API_KEY}" \
    "https://api.telnyx.com/v2/messages/${MESSAGE_ID}" 2>/dev/null || echo "")

  if [ "$HAS_JQ" = true ] && [ -n "$STATUS_RESPONSE" ]; then
    CURRENT_STATUS=$(echo "$STATUS_RESPONSE" | jq -r '.data.to[0].status // .data.status // empty' 2>/dev/null)
    MSG_COST=$(echo "$STATUS_RESPONSE" | jq -r '.data.cost.amount // empty' 2>/dev/null)
    MSG_CURRENCY=$(echo "$STATUS_RESPONSE" | jq -r '.data.cost.currency // empty' 2>/dev/null)

    if [ -n "$CURRENT_STATUS" ] && [ "$CURRENT_STATUS" != "$FINAL_STATUS" ]; then
      echo -e "  ${BLUE}INFO${NC}  Status: ${CURRENT_STATUS} (${ELAPSED}s)"
      FINAL_STATUS="$CURRENT_STATUS"
    fi

    case "$CURRENT_STATUS" in
      delivered)
        DELIVERY_CONFIRMED=true
        break
        ;;
      sent)
        # Keep polling — might still get delivery confirmation
        ;;
      queued|sending)
        # Still in progress
        ;;
      failed|undelivered|sending_failed|delivery_failed)
        echo -e "  ${RED}FAIL${NC}  Message delivery failed: ${CURRENT_STATUS}"
        break
        ;;
    esac
  fi
done

# --- Report ---
echo ""
echo "====================="
echo -e "${BOLD}Results${NC}"
echo "  Message ID:     ${MESSAGE_ID}"
echo "  Final Status:   ${FINAL_STATUS:-unknown}"
if [ -n "${MSG_COST:-}" ] && [ -n "${MSG_CURRENCY:-}" ]; then
  echo "  Cost:           ${MSG_COST} ${MSG_CURRENCY}"
else
  echo "  Cost:           ~\$0.004 (estimated)"
fi

if [ "$DELIVERY_CONFIRMED" = true ]; then
  echo ""
  echo -e "  ${GREEN}${BOLD}PASS${NC}  Message delivered successfully"
  exit 0
elif [ "$FINAL_STATUS" = "sent" ]; then
  echo ""
  echo -e "  ${YELLOW}${BOLD}WARN${NC}  Message sent but delivery not confirmed within polling window"
  echo "  This is normal — delivery receipts can be delayed."
  echo "  Check the Telnyx portal for final status."
  exit 0
else
  echo ""
  echo -e "  ${RED}${BOLD}FAIL${NC}  Message was not delivered"
  echo "  Check that the destination number is valid and can receive SMS."
  exit 1
fi
