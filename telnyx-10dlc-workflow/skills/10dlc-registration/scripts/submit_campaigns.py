#!/usr/bin/env python3
"""
10DLC Campaign Submission

Submits campaigns via the Telnyx CLI. Input is a JSON array of validated campaign objects.
Runs validation first and checks brand qualification before submitting.

Usage:
    # Dry run (validate + show commands, don't execute)
    python submit_campaigns.py campaigns.json --dry-run

    # Execute
    python submit_campaigns.py campaigns.json

Output: JSON results to stdout with campaign IDs and status.
"""

import json
import os
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Field name mapping: JSON keys -> CLI flag names
FIELD_TO_FLAG = {
    "brand_id": "brand-id",
    "usecase": "usecase",
    "description": "description",
    "sample1": "sample1",
    "sample2": "sample2",
    "sample3": "sample3",
    "sample4": "sample4",
    "sample5": "sample5",
    "message_flow": "message-flow",
    "help_message": "help-message",
    "help_keywords": "help-keywords",
    "optin_message": "optin-message",
    "optin_keywords": "optin-keywords",
    "optout_message": "optout-message",
    "optout_keywords": "optout-keywords",
    "age_gated": "age-gated",
    "direct_lending": "direct-lending",
    "number_pool": "number-pool",
    "privacy_policy_link": "privacy-policy-link",
    "terms_and_conditions_link": "terms-and-conditions-link",
    "auto_renewal": "auto-renewal",
    "embedded_link": "embedded-link",
    "embedded_phone": "embedded-phone",
}

# Boolean flags (no value, just presence)
BOOLEAN_FLAGS = {
    "subscriber_optin": "subscriber-optin",
    "subscriber_optout": "subscriber-optout",
    "subscriber_help": "subscriber-help",
    "terms_and_conditions": "terms-and-conditions",
}

# Fields not sent to API (used for validation only)
SKIP_FIELDS = {"brand_display_name", "embedded_link_bool"}


def build_command(campaign):
    """Build the telnyx CLI command for campaign submission."""
    cmd = ["telnyx", "messaging-10dlc", "campaign-builder", "submit"]

    for json_key, flag_name in FIELD_TO_FLAG.items():
        value = campaign.get(json_key)
        if value is not None and str(value).strip():
            cmd.extend([f"--{flag_name}", str(value).strip()])

    for json_key, flag_name in BOOLEAN_FLAGS.items():
        if campaign.get(json_key):
            cmd.append(f"--{flag_name}")

    return cmd


def check_brand_qualification(brand_id, usecase):
    """Check if brand qualifies for the use case."""
    cmd = [
        "telnyx", "messaging-10dlc", "campaign-builder", "brand",
        "qualify-by-usecase", "--brand-id", brand_id, "--usecase", usecase
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if proc.returncode == 0:
            return True, proc.stdout.strip()
        return False, proc.stderr.strip() or proc.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return False, str(e)


def extract_campaign_id(output):
    """Try to extract campaign ID from CLI JSON output."""
    try:
        data = json.loads(output)
        return data.get("campaignId") or data.get("id") or data.get("campaign_id")
    except (json.JSONDecodeError, TypeError):
        pass

    import re
    match = re.search(r'"(?:campaignId|id)"\s*:\s*"([^"]+)"', output)
    return match.group(1) if match else None


def run_validation(campaigns):
    """Run validate.py for campaigns."""
    import tempfile

    validate_script = os.path.join(SCRIPT_DIR, "validate.py")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(campaigns, f)
        tmp_path = f.name

    try:
        result = subprocess.run(
            [sys.executable, validate_script, "campaigns", tmp_path],
            capture_output=True, text=True
        )

        try:
            report = json.loads(result.stdout)
        except json.JSONDecodeError:
            print("Error: Could not parse validation output", file=sys.stderr)
            sys.exit(1)

        return report, result.returncode
    finally:
        os.unlink(tmp_path)


def main():
    if len(sys.argv) < 2:
        print("Usage: python submit_campaigns.py <campaigns.json> [--dry-run]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    dry_run = "--dry-run" in sys.argv

    with open(input_file, "r") as f:
        campaigns = json.load(f)

    if not isinstance(campaigns, list):
        campaigns = [campaigns]

    # Validate
    print("Validating campaign data...", file=sys.stderr)
    report, exit_code = run_validation(campaigns)

    if exit_code == 1:
        print("\nValidation FAILED. Fix errors before submitting campaigns.", file=sys.stderr)
        print("REMINDER: Campaign description and use case CANNOT be changed after submission.", file=sys.stderr)
        print(json.dumps({"status": "validation_failed", "report": report}, indent=2))
        sys.exit(1)

    if exit_code == 2:
        print("\nValidation passed with warnings.", file=sys.stderr)
        print("REMINDER: Campaign description and use case CANNOT be changed after submission.", file=sys.stderr)
        print("Review warnings carefully before proceeding.\n", file=sys.stderr)

    ready_count = sum(1 for item in report["items"] if item["status"] in ("PASS", "WARNING"))
    print(f"Ready to submit {ready_count} campaign(s).", file=sys.stderr)
    print("NOTE: Each campaign incurs a non-refundable 3-month fee.\n", file=sys.stderr)

    if dry_run:
        print("--- DRY RUN: Commands that would be executed ---\n", file=sys.stderr)
        results = []
        for i, campaign in enumerate(campaigns):
            item = report["items"][i]
            name = f"{campaign.get('brand_id', '?')} / {campaign.get('usecase', '?')}"

            if item["status"] == "FAIL":
                print(f"SKIP #{i+1} {name} (validation errors)", file=sys.stderr)
                results.append({"index": i+1, "name": name, "status": "skipped"})
                continue

            cmd = build_command(campaign)
            print(f"#{i+1} {name}:", file=sys.stderr)
            print(f"  {' '.join(cmd)}\n", file=sys.stderr)
            results.append({"index": i+1, "name": name, "status": "dry_run", "command": " ".join(cmd)})

        print(json.dumps({"status": "dry_run", "results": results}, indent=2))
        sys.exit(0)

    # Execute
    results = []
    for i, campaign in enumerate(campaigns):
        item = report["items"][i]
        brand_id = campaign.get("brand_id", "?")
        usecase = campaign.get("usecase", "?")
        name = f"{brand_id} / {usecase}"

        if item["status"] == "FAIL":
            print(f"SKIP #{i+1} {name} (validation errors)", file=sys.stderr)
            results.append({"index": i+1, "name": name, "status": "skipped", "reason": "validation_errors"})
            continue

        # Check brand qualification first
        print(f"Checking qualification for #{i+1} {name}...", file=sys.stderr, end=" ")
        qualified, qual_output = check_brand_qualification(brand_id, usecase)

        if not qualified:
            print("NOT QUALIFIED", file=sys.stderr)
            print(f"  {qual_output[:200]}", file=sys.stderr)
            results.append({
                "index": i+1, "name": name, "status": "not_qualified",
                "error": qual_output[:500]
            })
            continue

        print("OK", file=sys.stderr)

        # Submit campaign
        cmd = build_command(campaign)
        print(f"Submitting #{i+1} {name}...", file=sys.stderr, end=" ")

        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if proc.returncode == 0:
                campaign_id = extract_campaign_id(proc.stdout)
                print(f"OK (campaign_id: {campaign_id})", file=sys.stderr)
                results.append({
                    "index": i+1,
                    "name": name,
                    "status": "submitted",
                    "campaign_id": campaign_id,
                    "brand_id": brand_id,
                    "usecase": usecase,
                    "raw_response": proc.stdout.strip(),
                })
            else:
                error = proc.stderr.strip() or proc.stdout.strip()
                print(f"FAILED", file=sys.stderr)
                print(f"  Error: {error[:200]}", file=sys.stderr)
                results.append({
                    "index": i+1, "name": name, "status": "failed",
                    "error": error[:500]
                })
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT", file=sys.stderr)
            results.append({"index": i+1, "name": name, "status": "timeout"})
        except FileNotFoundError:
            print("ERROR: telnyx CLI not found", file=sys.stderr)
            sys.exit(1)

        if i < len(campaigns) - 1:
            time.sleep(1)

    # Summary
    submitted = sum(1 for r in results if r["status"] == "submitted")
    failed = sum(1 for r in results if r["status"] == "failed")
    skipped = sum(1 for r in results if r["status"] in ("skipped", "not_qualified"))

    print(f"\nDone: {submitted} submitted, {failed} failed, {skipped} skipped", file=sys.stderr)

    output = {
        "status": "complete",
        "summary": {"submitted": submitted, "failed": failed, "skipped": skipped},
        "results": results,
    }

    print(json.dumps(output, indent=2))
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
