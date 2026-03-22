#!/usr/bin/env python3
"""
10DLC Brand Creation

Creates brands via the Telnyx CLI. Input is a JSON array of validated brand objects.
Runs validation first and refuses to execute if there are errors.

Usage:
    # Dry run (validate + show commands, don't execute)
    python create_brands.py brands.json --dry-run

    # Execute
    python create_brands.py brands.json

Output: JSON results to stdout with brand IDs and status per brand.
"""

import json
import os
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Field name mapping: JSON keys -> CLI flag names
FIELD_TO_FLAG = {
    "country": "country",
    "display_name": "display-name",
    "email": "email",
    "entity_type": "entity-type",
    "vertical": "vertical",
    "company_name": "company-name",
    "ein": "ein",
    "city": "city",
    "state": "state",
    "street": "street",
    "postal_code": "postal-code",
    "phone": "phone",
    "website": "website",
    "first_name": "first-name",
    "last_name": "last-name",
    "stock_exchange": "stock-exchange",
    "stock_symbol": "stock-symbol",
    "business_contact_email": "business-contact-email",
    "is_reseller": "is-reseller",
    "ip_address": "ip-address",
    "mobile_phone": "mobile-phone",
    "webhook_url": "webhook-url",
    "webhook_failover_url": "webhook-failover-url",
}


def build_command(brand):
    """Build the telnyx CLI command for brand creation."""
    cmd = ["telnyx", "messaging-10dlc", "brand", "create"]

    for json_key, flag_name in FIELD_TO_FLAG.items():
        value = brand.get(json_key)
        if value is not None and str(value).strip():
            value = str(value).strip()
            # Strip dashes from EIN
            if json_key == "ein":
                value = value.replace("-", "").replace(" ", "")
            cmd.extend([f"--{flag_name}", value])

    return cmd


def extract_brand_id(output):
    """Try to extract brand ID from CLI JSON output."""
    try:
        data = json.loads(output)
        return data.get("brandId") or data.get("id") or data.get("brand_id")
    except (json.JSONDecodeError, TypeError):
        pass

    # Fallback: regex
    import re
    match = re.search(r'"(?:brandId|id)"\s*:\s*"([^"]+)"', output)
    return match.group(1) if match else None


def run_validation(brands):
    """Run validate.py and check for errors."""
    import tempfile

    validate_script = os.path.join(SCRIPT_DIR, "validate.py")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(brands, f)
        tmp_path = f.name

    try:
        result = subprocess.run(
            [sys.executable, validate_script, "brands", tmp_path],
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
        print("Usage: python create_brands.py <brands.json> [--dry-run]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    dry_run = "--dry-run" in sys.argv

    with open(input_file, "r") as f:
        brands = json.load(f)

    if not isinstance(brands, list):
        brands = [brands]

    # Run validation first
    print("Validating brand data...", file=sys.stderr)
    report, exit_code = run_validation(brands)

    if exit_code == 1:
        print("\nValidation FAILED. Fix errors before creating brands.", file=sys.stderr)
        print("Run: python validate.py brands <file.json> for details", file=sys.stderr)
        print(json.dumps({"status": "validation_failed", "report": report}, indent=2))
        sys.exit(1)

    if exit_code == 2:
        print("\nValidation passed with warnings. Proceeding...", file=sys.stderr)

    # Calculate cost
    ready_count = sum(1 for item in report["items"] if item["status"] in ("PASS", "WARNING"))
    total_cost = ready_count * 4

    print(f"\nReady to create {ready_count} brand(s). Cost: ${total_cost} (non-refundable)", file=sys.stderr)

    if dry_run:
        print("\n--- DRY RUN: Commands that would be executed ---\n", file=sys.stderr)
        results = []
        for i, brand in enumerate(brands):
            item = report["items"][i]
            if item["status"] == "FAIL":
                print(f"SKIP #{i+1} {brand.get('display_name', '?')} (validation errors)", file=sys.stderr)
                results.append({"index": i+1, "name": brand.get("display_name"), "status": "skipped", "reason": "validation_errors"})
                continue
            cmd = build_command(brand)
            print(f"#{i+1} {brand.get('display_name', '?')}:", file=sys.stderr)
            print(f"  {' '.join(cmd)}\n", file=sys.stderr)
            results.append({"index": i+1, "name": brand.get("display_name"), "status": "dry_run", "command": " ".join(cmd)})

        print(json.dumps({"status": "dry_run", "results": results}, indent=2))
        sys.exit(0)

    # Execute
    results = []
    for i, brand in enumerate(brands):
        item = report["items"][i]
        name = brand.get("display_name", f"Brand {i+1}")

        if item["status"] == "FAIL":
            print(f"SKIP #{i+1} {name} (validation errors)", file=sys.stderr)
            results.append({"index": i+1, "name": name, "status": "skipped", "reason": "validation_errors"})
            continue

        cmd = build_command(brand)
        print(f"Creating #{i+1} {name}...", file=sys.stderr, end=" ")

        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if proc.returncode == 0:
                brand_id = extract_brand_id(proc.stdout)
                print(f"OK (brand_id: {brand_id})", file=sys.stderr)
                results.append({
                    "index": i+1,
                    "name": name,
                    "status": "created",
                    "brand_id": brand_id,
                    "entity_type": brand.get("entity_type"),
                    "needs_otp": brand.get("entity_type", "").upper() == "SOLE_PROPRIETOR",
                    "raw_response": proc.stdout.strip(),
                })
            else:
                error = proc.stderr.strip() or proc.stdout.strip()
                print(f"FAILED", file=sys.stderr)
                print(f"  Error: {error[:200]}", file=sys.stderr)
                results.append({
                    "index": i+1,
                    "name": name,
                    "status": "failed",
                    "error": error[:500],
                })
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT", file=sys.stderr)
            results.append({"index": i+1, "name": name, "status": "timeout"})
        except FileNotFoundError:
            print("ERROR: telnyx CLI not found. Install: go install github.com/team-telnyx/telnyx-cli/cmd/telnyx@latest", file=sys.stderr)
            sys.exit(1)

        # Pause between API calls to avoid rate limits
        if i < len(brands) - 1:
            time.sleep(1)

    # Summary
    created = sum(1 for r in results if r["status"] == "created")
    failed = sum(1 for r in results if r["status"] == "failed")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    otp_needed = sum(1 for r in results if r.get("needs_otp"))

    print(f"\nDone: {created} created, {failed} failed, {skipped} skipped", file=sys.stderr)
    if otp_needed:
        print(f"{otp_needed} sole proprietor brand(s) need OTP verification", file=sys.stderr)

    output = {
        "status": "complete",
        "summary": {
            "created": created,
            "failed": failed,
            "skipped": skipped,
            "otp_needed": otp_needed,
            "cost_charged": f"${created * 4}",
        },
        "results": results,
    }

    print(json.dumps(output, indent=2))
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
