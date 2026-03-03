#!/usr/bin/env python3
"""
10DLC Status Report

Pulls status of all brands, campaigns, and phone number assignments
via the Telnyx CLI and outputs a consolidated report.

Usage:
    # Full status report
    python status_report.py

    # Check specific brands by ID
    python status_report.py --brand-ids br_abc123,br_def456

    # Output as JSON
    python status_report.py --json

Output: Human-readable status table to stderr, JSON to stdout.
"""

import json
import subprocess
import sys
from datetime import datetime


def run_cli(args, timeout=15):
    """Run a telnyx CLI command and return parsed JSON output."""
    cmd = ["telnyx"] + args
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if proc.returncode == 0 and proc.stdout.strip():
            return json.loads(proc.stdout)
        return None
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None


def get_brands(brand_ids=None):
    """Fetch all brands or specific ones."""
    if brand_ids:
        brands = []
        for bid in brand_ids:
            data = run_cli(["messaging-10dlc", "brand", "retrieve", bid])
            if data:
                brands.append(data)
        return brands

    data = run_cli(["messaging-10dlc", "brand", "list"])
    if data and isinstance(data, dict):
        return data.get("records") or data.get("data") or []
    if isinstance(data, list):
        return data
    return []


def get_campaigns(brand_id=None):
    """Fetch campaigns, optionally filtered by brand."""
    args = ["messaging-10dlc", "campaign", "list"]
    if brand_id:
        args.extend(["--brand-id", brand_id])
    data = run_cli(args)
    if data and isinstance(data, dict):
        return data.get("records") or data.get("data") or []
    if isinstance(data, list):
        return data
    return []


def get_campaign_mno_status(campaign_id):
    """Get per-carrier status for a campaign."""
    data = run_cli(["messaging-10dlc", "campaign", "get-operation-status", campaign_id])
    return data


def get_number_assignments():
    """Fetch phone number to campaign assignments."""
    data = run_cli(["messaging-10dlc", "phone-number-campaign", "list"])
    if data and isinstance(data, dict):
        return data.get("records") or data.get("data") or []
    if isinstance(data, list):
        return data
    return []


def format_table(headers, rows, col_widths=None):
    """Format a simple ASCII table."""
    if not col_widths:
        col_widths = []
        for i, h in enumerate(headers):
            max_w = len(h)
            for row in rows:
                if i < len(row):
                    max_w = max(max_w, len(str(row[i])))
            col_widths.append(min(max_w, 40))

    header_line = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    separator = "-+-".join("-" * w for w in col_widths)
    lines = [header_line, separator]

    for row in rows:
        line = " | ".join(str(v).ljust(w)[:w] for v, w in zip(row, col_widths))
        lines.append(line)

    return "\n".join(lines)


def main():
    brand_ids = None
    json_output = "--json" in sys.argv

    for arg in sys.argv[1:]:
        if arg.startswith("--brand-ids="):
            brand_ids = arg.split("=", 1)[1].split(",")
        elif arg.startswith("--brand-ids") and sys.argv.index(arg) + 1 < len(sys.argv):
            next_idx = sys.argv.index(arg) + 1
            brand_ids = sys.argv[next_idx].split(",")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = {"generated_at": now, "brands": [], "campaigns": [], "assignments": []}

    # Brands
    print(f"\n10DLC Status Report — {now}\n", file=sys.stderr)
    print("Fetching brands...", file=sys.stderr)
    brands = get_brands(brand_ids)

    brand_rows = []
    for b in brands:
        bid = b.get("brandId") or b.get("id") or "?"
        name = b.get("displayName") or b.get("display_name") or "?"
        entity = b.get("entityType") or b.get("entity_type") or "?"
        status = b.get("identityStatus") or b.get("identity_status") or "?"
        score = b.get("universalEin", {}).get("score") if isinstance(b.get("universalEin"), dict) else "—"

        brand_rows.append([name[:25], bid[:20], entity[:18], status[:15], str(score)])
        report["brands"].append({
            "brand_id": bid, "display_name": name, "entity_type": entity,
            "identity_status": status, "trust_score": score,
        })

    if brand_rows:
        print("\nBRANDS:", file=sys.stderr)
        print(format_table(
            ["Brand", "ID", "Entity Type", "Status", "Score"],
            brand_rows
        ), file=sys.stderr)
    else:
        print("No brands found.", file=sys.stderr)

    # Campaigns
    print("\nFetching campaigns...", file=sys.stderr)
    all_campaigns = []
    if brand_ids:
        for bid in brand_ids:
            all_campaigns.extend(get_campaigns(bid))
    else:
        all_campaigns = get_campaigns()

    campaign_rows = []
    for c in all_campaigns:
        cid = c.get("campaignId") or c.get("id") or "?"
        bid = c.get("brandId") or c.get("brand_id") or "?"
        usecase = c.get("usecase") or "?"
        status = c.get("status") or "?"

        # Try to get MNO status
        mno = {"att": "—", "tmobile": "—", "verizon": "—"}
        mno_data = get_campaign_mno_status(cid)
        if mno_data and isinstance(mno_data, dict):
            for key, val in mno_data.items():
                if isinstance(val, dict):
                    carrier_status = val.get("status") or val.get("operationStatus") or "?"
                    if "att" in key.lower() or "10017" in str(key):
                        mno["att"] = carrier_status[:10]
                    elif "t-mobile" in key.lower() or "tmobile" in key.lower() or "10035" in str(key):
                        mno["tmobile"] = carrier_status[:10]
                    elif "verizon" in key.lower() or "10003" in str(key):
                        mno["verizon"] = carrier_status[:10]

        campaign_rows.append([
            cid[:15], bid[:15], usecase[:15], status[:12],
            mno["att"], mno["tmobile"], mno["verizon"]
        ])
        report["campaigns"].append({
            "campaign_id": cid, "brand_id": bid, "usecase": usecase,
            "status": status, "carrier_status": mno,
        })

    if campaign_rows:
        print("\nCAMPAIGNS:", file=sys.stderr)
        print(format_table(
            ["Campaign", "Brand", "Use Case", "Status", "AT&T", "T-Mobile", "Verizon"],
            campaign_rows
        ), file=sys.stderr)
    else:
        print("No campaigns found.", file=sys.stderr)

    # Phone number assignments
    print("\nFetching number assignments...", file=sys.stderr)
    assignments = get_number_assignments()

    assign_rows = []
    for a in assignments:
        phone = a.get("phoneNumber") or a.get("phone_number") or "?"
        cid = a.get("campaignId") or a.get("campaign_id") or "?"
        status = a.get("status") or "?"

        assign_rows.append([phone, cid[:20], status[:15]])
        report["assignments"].append({
            "phone_number": phone, "campaign_id": cid, "status": status,
        })

    if assign_rows:
        print("\nPHONE NUMBER ASSIGNMENTS:", file=sys.stderr)
        print(format_table(
            ["Phone Number", "Campaign", "Status"],
            assign_rows
        ), file=sys.stderr)
    else:
        print("No number assignments found.", file=sys.stderr)

    # Summary
    print(f"\nSummary: {len(brands)} brand(s), {len(all_campaigns)} campaign(s), "
          f"{len(assignments)} assignment(s)", file=sys.stderr)

    # Next steps
    next_steps = []
    for b in report["brands"]:
        if b["identity_status"] in ("PENDING", "UNVERIFIED"):
            next_steps.append(f"Brand '{b['display_name']}' ({b['brand_id']}): waiting for vetting")
        elif b["identity_status"] == "VERIFIED" and not any(
            c["brand_id"] == b["brand_id"] for c in report["campaigns"]
        ):
            next_steps.append(f"Brand '{b['display_name']}' ({b['brand_id']}): ready for campaign submission")

    for c in report["campaigns"]:
        if c["status"] in ("ACTIVE",) and not any(
            a["campaign_id"] == c["campaign_id"] for a in report["assignments"]
        ):
            next_steps.append(f"Campaign {c['campaign_id']}: approved, ready for number assignment")

    if next_steps:
        print("\nNEXT STEPS:", file=sys.stderr)
        for step in next_steps:
            print(f"  - {step}", file=sys.stderr)

    report["next_steps"] = next_steps
    print("", file=sys.stderr)

    # JSON to stdout
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
