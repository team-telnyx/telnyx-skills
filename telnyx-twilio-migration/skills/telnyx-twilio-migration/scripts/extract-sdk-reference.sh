#!/usr/bin/env bash
#
# extract-sdk-reference.sh — Extract SDK reference files from sibling plugin directories
#
# Usage: bash scripts/extract-sdk-reference.sh [--dry-run]
#
# Scans sibling plugin directories (telnyx-python, telnyx-javascript, etc.)
# for migration-relevant product SKILL.md files and copies them into a local
# sdk-reference/ directory, organized by language.
#
# The extracted files give the Twilio migration skill fast access to
# Telnyx SDK examples and API patterns for every product area, without
# requiring the agent to traverse the full skills tree at runtime.
#
# Flags:
#   --dry-run   Show what would be copied without writing anything
#
# Exit codes:
#   0 — Completed successfully
#   1 — Fatal error (e.g., repo root not found)

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

# --- Resolve paths relative to script location ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PLUGIN_DIR="$(cd "${SKILL_DIR}/../.." && pwd)"
REPO_ROOT="$(cd "${PLUGIN_DIR}/.." && pwd)"

OUTPUT_DIR="${SKILL_DIR}/sdk-reference"

# --- Parse flags ---
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --dry-run)
      DRY_RUN=true
      ;;
    *)
      echo -e "${RED}Unknown argument: ${arg}${NC}" >&2
      echo "Usage: bash scripts/extract-sdk-reference.sh [--dry-run]" >&2
      exit 1
      ;;
  esac
done

# --- Migration-relevant products (27) ---
PRODUCTS=(
  voice
  voice-advanced
  voice-conferencing
  voice-gather
  voice-media
  voice-streaming
  texml
  messaging
  messaging-profiles
  messaging-hosted
  webrtc
  sip
  sip-integrations
  numbers
  numbers-config
  numbers-services
  numbers-compliance
  porting-in
  porting-out
  verify
  video
  fax
  iot
  10dlc
  ai-assistants
  ai-inference
  storage
)

# --- Excluded products (9) — listed for documentation, not used in loop ---
# account, account-access, account-management, account-notifications,
# account-reports, oauth, networking, missions, seti

# --- Language plugin directories and their suffixes ---
declare -A LANG_DIRS=(
  [python]="telnyx-python"
  [javascript]="telnyx-javascript"
  [go]="telnyx-go"
  [java]="telnyx-java"
  [ruby]="telnyx-ruby"
  [curl]="telnyx-curl"
)

# Ordered list for consistent iteration (bash associative arrays have no order)
LANGUAGES=(python javascript go java ruby curl)

# --- Helper functions ---
log_info() {
  echo -e "  ${BLUE}INFO${NC}  $1"
}

log_ok() {
  echo -e "  ${GREEN} OK ${NC}  $1"
}

log_skip() {
  echo -e "  ${YELLOW}SKIP${NC}  $1"
}

log_warn() {
  echo -e "  ${YELLOW}WARN${NC}  $1"
}

# --- Header ---
echo -e "${BOLD}Extract SDK Reference Files${NC}"
echo "─────────────────────────────────────"

if [ "$DRY_RUN" = true ]; then
  echo -e "  ${YELLOW}DRY RUN${NC} — no files will be written"
fi

echo ""
echo -e "${BOLD}Paths${NC}"
log_info "Script:    ${SCRIPT_DIR}"
log_info "Skill dir: ${SKILL_DIR}"
log_info "Repo root: ${REPO_ROOT}"
log_info "Output:    ${OUTPUT_DIR}"

# --- Validate repo root ---
if [ ! -d "${REPO_ROOT}" ]; then
  echo -e "${RED}${BOLD}Fatal:${NC} Repository root not found at ${REPO_ROOT}" >&2
  exit 1
fi

# --- Wipe and recreate output directory (idempotent) ---
echo ""
echo -e "${BOLD}Preparing output directory${NC}"

if [ "$DRY_RUN" = false ]; then
  if [ -d "${OUTPUT_DIR}" ]; then
    rm -rf "${OUTPUT_DIR}"
    log_info "Removed existing sdk-reference/"
  fi
  mkdir -p "${OUTPUT_DIR}"
  log_info "Created sdk-reference/"
else
  if [ -d "${OUTPUT_DIR}" ]; then
    log_info "Would remove existing sdk-reference/"
  fi
  log_info "Would create sdk-reference/"
fi

# --- Extract files ---
echo ""
echo -e "${BOLD}Extracting SKILL.md files${NC}"

TOTAL_COPIED=0
TOTAL_MISSING=0
TOTAL_SIZE=0
declare -A LANG_COUNTS
declare -A LANG_MISSING
MISSING_SOURCES=()

for lang in "${LANGUAGES[@]}"; do
  plugin_name="${LANG_DIRS[$lang]}"
  skills_dir="${REPO_ROOT}/${plugin_name}/skills"
  copied=0
  missing=0

  if [ ! -d "${skills_dir}" ]; then
    log_warn "${plugin_name}/skills/ not found — skipping language"
    LANG_COUNTS[$lang]=0
    LANG_MISSING[$lang]=${#PRODUCTS[@]}
    TOTAL_MISSING=$((TOTAL_MISSING + ${#PRODUCTS[@]}))
    continue
  fi

  for product in "${PRODUCTS[@]}"; do
    skill_name="telnyx-${product}-${lang}"
    source_path="${skills_dir}/${skill_name}/SKILL.md"
    dest_dir="${OUTPUT_DIR}/${lang}"
    dest_path="${dest_dir}/${product}.md"

    # Compute relative path from skill dir to source for the header comment
    rel_source="../../${plugin_name}/skills/${skill_name}/SKILL.md"

    if [ -f "${source_path}" ]; then
      if [ "$DRY_RUN" = false ]; then
        mkdir -p "${dest_dir}"

        # Write header comment + original content
        {
          echo "<!-- Extracted from telnyx-${product}-${lang} by extract-sdk-reference.sh -->"
          echo "<!-- Source: ${rel_source} -->"
          echo "<!-- Do not edit manually — regenerate with: bash scripts/extract-sdk-reference.sh -->"
          echo ""
          cat "${source_path}"
        } > "${dest_path}"

        file_size=$(wc -c < "${dest_path}" | tr -d ' ')
        TOTAL_SIZE=$((TOTAL_SIZE + file_size))
      else
        # In dry-run, count the source size as an estimate
        file_size=$(wc -c < "${source_path}" | tr -d ' ')
        TOTAL_SIZE=$((TOTAL_SIZE + file_size))
      fi

      copied=$((copied + 1))
      TOTAL_COPIED=$((TOTAL_COPIED + 1))
    else
      missing=$((missing + 1))
      TOTAL_MISSING=$((TOTAL_MISSING + 1))
      MISSING_SOURCES+=("${skill_name}")
    fi
  done

  LANG_COUNTS[$lang]=$copied
  LANG_MISSING[$lang]=$missing

  if [ "$copied" -gt 0 ]; then
    log_ok "${lang}: ${copied} files copied"
  else
    log_warn "${lang}: 0 files copied"
  fi
done

# --- Summary ---
echo ""
echo "─────────────────────────────────────"
echo -e "${BOLD}Summary${NC}"
echo ""

# Per-language breakdown
for lang in "${LANGUAGES[@]}"; do
  count="${LANG_COUNTS[$lang]:-0}"
  miss="${LANG_MISSING[$lang]:-0}"
  if [ "$count" -gt 0 ]; then
    echo -e "  ${GREEN}${count}${NC} ${lang}"
  else
    echo -e "  ${YELLOW}${count}${NC} ${lang}"
  fi
done

echo ""

# Format total size for display
if [ "$TOTAL_SIZE" -gt 1048576 ]; then
  SIZE_DISPLAY="$(awk "BEGIN {printf \"%.1f\", ${TOTAL_SIZE}/1048576}") MB"
elif [ "$TOTAL_SIZE" -gt 1024 ]; then
  SIZE_DISPLAY="$(awk "BEGIN {printf \"%.1f\", ${TOTAL_SIZE}/1024}") KB"
else
  SIZE_DISPLAY="${TOTAL_SIZE} bytes"
fi

if [ "$DRY_RUN" = true ]; then
  echo -e "  ${BOLD}Would copy:${NC} ${TOTAL_COPIED} files (~${SIZE_DISPLAY})"
else
  echo -e "  ${BOLD}Total:${NC} ${TOTAL_COPIED} files (${SIZE_DISPLAY})"
fi

if [ "$TOTAL_MISSING" -gt 0 ]; then
  echo -e "  ${YELLOW}Missing:${NC} ${TOTAL_MISSING} expected sources not found"
fi

# List missing sources (collapsed if too many)
if [ "${#MISSING_SOURCES[@]}" -gt 0 ]; then
  echo ""
  echo -e "${BOLD}Missing sources${NC}"
  if [ "${#MISSING_SOURCES[@]}" -le 20 ]; then
    for src in "${MISSING_SOURCES[@]}"; do
      echo -e "  ${YELLOW}-${NC} ${src}"
    done
  else
    # Show first 10, then count
    for src in "${MISSING_SOURCES[@]:0:10}"; do
      echo -e "  ${YELLOW}-${NC} ${src}"
    done
    remaining=$(( ${#MISSING_SOURCES[@]} - 10 ))
    echo -e "  ${YELLOW}...and ${remaining} more${NC}"
  fi
fi

echo ""
if [ "$DRY_RUN" = true ]; then
  echo -e "${BLUE}${BOLD}Dry run complete.${NC} Re-run without --dry-run to extract files."
elif [ "$TOTAL_COPIED" -gt 0 ]; then
  echo -e "${GREEN}${BOLD}Extraction complete.${NC} Files written to sdk-reference/"
else
  echo -e "${YELLOW}${BOLD}No files extracted.${NC} Check that sibling plugin directories exist."
fi
