#!/usr/bin/env python3
"""
10DLC Brand & Campaign Validation

Validates brand and campaign data before submission to avoid wasting
non-refundable registration fees ($4/brand, variable/campaign).

Usage:
    # Validate brands from JSON
    python validate.py brands brands.json

    # Validate campaigns from JSON
    python validate.py campaigns campaigns.json

Input format (brands.json):
[
  {
    "display_name": "Acme Corp",
    "entity_type": "PRIVATE_PROFIT",
    "vertical": "TECHNOLOGY",
    "email": "admin@acme.com",
    "country": "US",
    "company_name": "Acme Corp Inc",
    "ein": "123456789",
    ...
  }
]

Input format (campaigns.json):
[
  {
    "brand_id": "br_abc123",
    "usecase": "CUSTOMER_CARE",
    "description": "...",
    "sample1": "...",
    "sample2": "...",
    "message_flow": "...",
    ...
  }
]

Output: JSON validation report to stdout.
Exit code: 0 if all pass, 1 if any errors, 2 if any warnings.
"""

import json
import re
import sys

# --- Constants ---

ENTITY_TYPES = {
    "SOLE_PROPRIETOR", "PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT"
}

VERTICALS = {
    "AGRICULTURE", "AUTOMOTIVE", "BANKING", "COMMUNICATION", "CONSTRUCTION",
    "EDUCATION", "ELECTRONICS", "ENERGY", "ENGINEERING", "ENTERTAINMENT",
    "FINANCIAL", "FOOD_BEVERAGE", "GOVERNMENT", "HEALTHCARE", "HOSPITALITY",
    "INSURANCE", "JEWELRY", "LEGAL", "MANUFACTURING", "MEDIA", "NOT_FOR_PROFIT",
    "OIL_AND_GAS", "POSTAL", "PROFESSIONAL", "REAL_ESTATE", "RELIGION",
    "RETAIL", "TECHNOLOGY", "TOBACCO", "TRANSPORTATION"
}

USE_CASES = {
    "2FA", "CUSTOMER_CARE", "ACCOUNT_NOTIFICATION", "DELIVERY_NOTIFICATION",
    "MARKETING", "MIXED", "POLLING_VOTING", "CHARITY", "POLITICAL",
    "PUBLIC_SERVICE_ANNOUNCEMENT", "SECURITY_ALERT"
}

SOLE_PROP_USE_CASES = {"2FA", "CUSTOMER_CARE", "DELIVERY_NOTIFICATION", "ACCOUNT_NOTIFICATION"}

OPT_OUT_TERMS = ["stop", "unsubscribe", "opt out", "opt-out", "cancel", "end", "quit"]

SPAM_TRIGGERS = ["free", "winner", "act now", "limited time", "congratulations", "click here"]

VAGUE_TERMS = ["various", "general", "different", "multiple", "some", "etc"]

USECASE_KEYWORDS = {
    "CUSTOMER_CARE": ["support", "service", "help", "assistance", "care", "customer"],
    "MARKETING": ["promotion", "offer", "sale", "discount", "marketing", "deal"],
    "2FA": ["verification", "security", "authentication", "code", "login"],
    "DELIVERY_NOTIFICATION": ["delivery", "shipping", "order", "package", "track"],
    "ACCOUNT_NOTIFICATION": ["account", "balance", "payment", "statement", "alert"],
    "POLITICAL": ["political", "campaign", "candidate", "vote", "election"],
    "CHARITY": ["donate", "charity", "fundraising", "nonprofit", "cause"],
}


def make_issue(field, severity, message, suggestion=None):
    """Create a validation issue dict."""
    issue = {"field": field, "severity": severity, "message": message}
    if suggestion:
        issue["suggestion"] = suggestion
    return issue


# --- Brand Validation ---

def validate_brand(brand, index):
    """Validate a single brand record. Returns list of issues."""
    issues = []
    entity_type = (brand.get("entity_type") or "").upper().strip()

    # Required for all
    for field in ["display_name", "entity_type", "vertical", "email", "country"]:
        if not brand.get(field, "").strip():
            issues.append(make_issue(field, "error", f"Required field '{field}' is missing"))

    # Entity type validation
    if entity_type and entity_type not in ENTITY_TYPES:
        issues.append(make_issue("entity_type", "error",
            f"Invalid entity type '{entity_type}'",
            f"Must be one of: {', '.join(sorted(ENTITY_TYPES))}"))

    # Vertical validation
    vertical = (brand.get("vertical") or "").upper().strip()
    if vertical and vertical not in VERTICALS:
        issues.append(make_issue("vertical", "error",
            f"Invalid vertical '{vertical}'",
            f"Must be one of: {', '.join(sorted(VERTICALS))}"))

    # Country
    country = (brand.get("country") or "").upper().strip()
    if country and country != "US":
        issues.append(make_issue("country", "warning",
            f"Country is '{country}'. 10DLC is US-only.",
            "Set country to 'US'"))

    # Email format
    email = brand.get("email", "").strip()
    if email and not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        issues.append(make_issue("email", "error",
            f"Invalid email format: '{email}'"))

    # EIN validation
    ein = str(brand.get("ein") or "").strip().replace("-", "").replace(" ", "")
    if ein:
        if not re.match(r'^\d{9}$', ein):
            issues.append(make_issue("ein", "error",
                f"EIN must be exactly 9 digits (got '{brand.get('ein')}')",
                "Remove dashes and ensure 9 digits, e.g., 123456789"))

    # Phone validation
    phone = (brand.get("phone") or "").strip()
    if phone:
        if not re.match(r'^\+1\d{10}$', phone):
            issues.append(make_issue("phone", "warning",
                f"Phone should be E.164 format (got '{phone}')",
                "Format as +1XXXXXXXXXX, e.g., +15551234567"))

    # Website validation
    website = (brand.get("website") or "").strip()
    if website and not re.match(r'^https?://', website):
        issues.append(make_issue("website", "warning",
            f"Website should start with http:// or https:// (got '{website}')"))

    # Address: reject P.O. boxes
    street = (brand.get("street") or "").strip().lower()
    if street and re.match(r'^p\.?o\.?\s*box', street):
        issues.append(make_issue("street", "error",
            "P.O. Box addresses are rejected by TCR",
            "Use a physical street address"))

    # Postal code
    postal = str(brand.get("postal_code") or "").strip()
    if postal and not re.match(r'^\d{5}(-\d{4})?$', postal):
        issues.append(make_issue("postal_code", "warning",
            f"US postal code should be 5 digits (got '{postal}')"))

    # State
    state = (brand.get("state") or "").upper().strip()
    valid_states = {
        "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN",
        "IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV",
        "NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN",
        "TX","UT","VT","VA","WA","WV","WI","WY","DC","PR","VI","GU","AS","MP"
    }
    if state and state not in valid_states:
        issues.append(make_issue("state", "warning",
            f"Invalid US state code: '{state}'"))

    # Entity-type-specific requirements
    if entity_type == "SOLE_PROPRIETOR":
        if not brand.get("first_name", "").strip():
            issues.append(make_issue("first_name", "error",
                "First name is required for SOLE_PROPRIETOR"))
        if not brand.get("last_name", "").strip():
            issues.append(make_issue("last_name", "error",
                "Last name is required for SOLE_PROPRIETOR"))
        if not phone:
            issues.append(make_issue("phone", "error",
                "Phone number is required for SOLE_PROPRIETOR (needed for OTP verification)"))

    elif entity_type in ("PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT"):
        if not brand.get("company_name", "").strip():
            issues.append(make_issue("company_name", "error",
                f"Company name is required for {entity_type}"))

    if entity_type == "NON_PROFIT":
        if not ein:
            issues.append(make_issue("ein", "error",
                "EIN is required for NON_PROFIT entities"))

    if entity_type == "PUBLIC_PROFIT":
        if not ein:
            issues.append(make_issue("ein", "error",
                "EIN is required for PUBLIC_PROFIT entities"))
        if not brand.get("stock_exchange", "").strip():
            issues.append(make_issue("stock_exchange", "error",
                "Stock exchange is required for PUBLIC_PROFIT"))
        if not brand.get("stock_symbol", "").strip():
            issues.append(make_issue("stock_symbol", "error",
                "Stock symbol is required for PUBLIC_PROFIT"))
        if not brand.get("business_contact_email", "").strip():
            issues.append(make_issue("business_contact_email", "error",
                "Business contact email is required for PUBLIC_PROFIT"))

    # Recommendations (warnings)
    if entity_type in ("PRIVATE_PROFIT", "PUBLIC_PROFIT") and not website:
        issues.append(make_issue("website", "warning",
            "No website provided. This significantly lowers your trust/vetting score.",
            "Provide a website URL to improve brand approval and throughput limits"))

    if entity_type != "SOLE_PROPRIETOR" and not ein:
        if entity_type not in ("NON_PROFIT", "PUBLIC_PROFIT"):  # already errored above
            issues.append(make_issue("ein", "warning",
                "EIN not provided. Strongly recommended for higher trust scores.",
                "Provide the 9-digit EIN to improve vetting results"))

    if not street and entity_type != "SOLE_PROPRIETOR":
        issues.append(make_issue("street", "warning",
            "No address provided. Recommended for higher trust scores."))

    return issues


# --- Campaign Validation ---

def validate_campaign(campaign, index):
    """Validate a single campaign record. Returns list of issues."""
    issues = []
    usecase = (campaign.get("usecase") or "").upper().strip()

    # Required fields
    if not campaign.get("brand_id", "").strip():
        issues.append(make_issue("brand_id", "error", "brand_id is required"))

    if not usecase:
        issues.append(make_issue("usecase", "error", "usecase is required"))
    elif usecase not in USE_CASES:
        issues.append(make_issue("usecase", "error",
            f"Invalid use case '{usecase}'",
            f"Must be one of: {', '.join(sorted(USE_CASES))}"))

    # Description validation
    desc = (campaign.get("description") or "").strip()
    if not desc:
        issues.append(make_issue("description", "error",
            "Description is required"))
    else:
        words = desc.split()
        if len(words) < 10:
            issues.append(make_issue("description", "error",
                f"Description is too short ({len(words)} words). Must be 10+ words.",
                "Describe specifically what messages you send, to whom, and why"))

        lower_desc = desc.lower()
        vague_found = [t for t in VAGUE_TERMS if t in lower_desc]
        if len(vague_found) > 2:
            issues.append(make_issue("description", "warning",
                f"Description contains vague terms: {', '.join(vague_found)}",
                "Replace with specific descriptions of your services"))

        # Use case alignment
        keywords = USECASE_KEYWORDS.get(usecase, [])
        if keywords and not any(k in lower_desc for k in keywords):
            issues.append(make_issue("description", "warning",
                f"Description doesn't contain keywords aligned with {usecase}",
                f"Consider including: {', '.join(keywords)}"))

        if usecase == "MARKETING" and "marketing" not in lower_desc:
            issues.append(make_issue("description", "warning",
                "MARKETING campaigns should explicitly mention 'marketing' in description"))

    # Sample message validation
    samples_found = 0
    for i in range(1, 6):
        sample_key = f"sample{i}"
        sample = (campaign.get(sample_key) or "").strip()
        if not sample:
            continue
        samples_found += 1

        if len(sample) < 20:
            issues.append(make_issue(sample_key, "warning",
                f"Sample message {i} is very short ({len(sample)} chars)",
                "Provide a realistic, detailed sample message"))

        if len(sample) > 1600:
            issues.append(make_issue(sample_key, "error",
                f"Sample message {i} exceeds 1600 character limit"))

        lower_sample = sample.lower()

        # Opt-out check (not required for 2FA)
        if usecase != "2FA":
            has_opt_out = any(term in lower_sample for term in OPT_OUT_TERMS)
            if not has_opt_out:
                issues.append(make_issue(sample_key, "error",
                    f"Sample message {i} missing opt-out language",
                    "Add 'Reply STOP to unsubscribe' or similar"))

        # Sender identification check
        display_name = (campaign.get("brand_display_name") or "").strip()
        if display_name and display_name.lower() not in lower_sample:
            # Check for any colon-prefix pattern (e.g., "CompanyName: message")
            if ":" not in sample[:50]:
                issues.append(make_issue(sample_key, "warning",
                    f"Sample message {i} should identify the sender by name",
                    "Start message with 'CompanyName: ...'"))

        # Spam trigger check
        spam_found = [t for t in SPAM_TRIGGERS if t in lower_sample]
        if spam_found:
            issues.append(make_issue(sample_key, "warning",
                f"Sample message {i} contains potential spam triggers: {', '.join(spam_found)}",
                "Avoid these terms to prevent carrier filtering (especially Verizon)"))

        # Excessive caps check
        upper_chars = sum(1 for c in sample if c.isupper())
        if len(sample) > 10 and upper_chars / len(sample) > 0.5:
            issues.append(make_issue(sample_key, "warning",
                f"Sample message {i} has excessive uppercase ({int(upper_chars/len(sample)*100)}%)",
                "Use normal capitalization to avoid carrier filtering"))

        # Marketing: data rates disclosure
        if usecase == "MARKETING":
            if "msg" not in lower_sample and "data rates" not in lower_sample:
                issues.append(make_issue(sample_key, "warning",
                    f"MARKETING sample {i} should include 'Msg & data rates may apply'"))

    if samples_found < 2 and usecase != "2FA":
        issues.append(make_issue("samples", "error",
            f"At least 2 sample messages required (found {samples_found})",
            "Provide sample1 and sample2 with realistic message examples"))
    elif samples_found < 1:
        issues.append(make_issue("samples", "error",
            "At least 1 sample message is required"))

    # Message flow validation
    flow = (campaign.get("message_flow") or "").strip()
    if not flow:
        issues.append(make_issue("message_flow", "error",
            "Message flow is required",
            "Document how users opt in, including consent mechanism, privacy policy, and terms"))
    else:
        lower_flow = flow.lower()
        flow_words = flow.split()

        if len(flow_words) < 30:
            issues.append(make_issue("message_flow", "warning",
                f"Message flow is too brief ({len(flow_words)} words)",
                "Provide comprehensive documentation of your opt-in process (30+ words)"))

        # Required components
        components = [
            (["opt-in", "opt in", "consent", "agree", "subscribe"], "opt-in process", "error"),
            (["privacy policy", "privacy"], "privacy policy reference", "warning"),
            (["terms", "conditions"], "terms and conditions reference", "warning"),
            (["stop", "unsubscribe", "opt out", "opt-out"], "opt-out instructions", "error"),
        ]

        for terms, name, sev in components:
            if not any(t in lower_flow for t in terms):
                issues.append(make_issue("message_flow", sev,
                    f"Message flow missing {name}",
                    f"Add description of {name} in your opt-in documentation"))

        # Check for URLs
        if not re.search(r'https?://', flow):
            issues.append(make_issue("message_flow", "warning",
                "Message flow should include URLs to opt-in form, privacy policy, or terms"))

        # Pre-checked box warning (but not "unchecked by default" which is compliant)
        if ("pre-check" in lower_flow or "pre check" in lower_flow or
                ("checked by default" in lower_flow and "unchecked by default" not in lower_flow)):
            issues.append(make_issue("message_flow", "error",
                "Pre-checked opt-in boxes are non-compliant",
                "Consent checkbox must be unchecked by default"))

    # Embedded link consistency
    all_samples = " ".join((campaign.get(f"sample{i}") or "") for i in range(1, 6))
    all_text = f"{desc} {all_samples} {flow}"
    has_urls = bool(re.search(r'https?://', all_samples))
    embedded_link = campaign.get("embedded_link", False)
    if has_urls and not embedded_link:
        issues.append(make_issue("embedded_link", "error",
            "Sample messages contain URLs but embedded_link is not enabled",
            "Set embedded_link to true when messages include URLs"))

    # Help message
    help_msg = (campaign.get("help_message") or "").strip()
    if not help_msg:
        issues.append(make_issue("help_message", "warning",
            "Help message not provided. Recommended for compliance.",
            "Add a help message with contact info, e.g., 'Reply HELP for support or contact support@company.com'"))
    else:
        if not re.search(r'(@|\.com|phone|call|email|\d{3}[-.\s]?\d{3}[-.\s]?\d{4})', help_msg, re.I):
            issues.append(make_issue("help_message", "warning",
                "Help message should include contact information (email, phone, or website)"))

    return issues


# --- Report Generation ---

def generate_report(data_type, items):
    """Validate all items and generate a report."""
    validate_fn = validate_brand if data_type == "brands" else validate_campaign

    report = {
        "type": data_type,
        "total": len(items),
        "passed": 0,
        "warnings": 0,
        "errors": 0,
        "items": [],
        "estimated_cost": None,
    }

    for i, item in enumerate(items):
        issues = validate_fn(item, i)
        error_count = sum(1 for iss in issues if iss["severity"] == "error")
        warning_count = sum(1 for iss in issues if iss["severity"] == "warning")

        if error_count > 0:
            status = "FAIL"
            report["errors"] += 1
        elif warning_count > 0:
            status = "WARNING"
            report["warnings"] += 1
        else:
            status = "PASS"
            report["passed"] += 1

        name = item.get("display_name") or item.get("brand_id") or f"Item {i+1}"
        report["items"].append({
            "index": i + 1,
            "name": name,
            "status": status,
            "error_count": error_count,
            "warning_count": warning_count,
            "issues": issues,
        })

    if data_type == "brands":
        ready = report["passed"] + report["warnings"]
        report["estimated_cost"] = f"${ready * 4} ({ready} brands x $4 each, non-refundable)"

    return report


def print_summary(report):
    """Print a human-readable summary to stderr."""
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"10DLC {report['type'].upper()} VALIDATION REPORT", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"Total: {report['total']} | Pass: {report['passed']} | "
          f"Warnings: {report['warnings']} | Errors: {report['errors']}", file=sys.stderr)

    if report.get("estimated_cost"):
        print(f"Estimated cost: {report['estimated_cost']}", file=sys.stderr)

    print(f"{'='*60}", file=sys.stderr)

    for item in report["items"]:
        icon = {"PASS": "OK", "WARNING": "WARN", "FAIL": "FAIL"}[item["status"]]
        print(f"\n[{icon}] #{item['index']} {item['name']}", file=sys.stderr)
        for iss in item["issues"]:
            sev = "ERROR" if iss["severity"] == "error" else "WARN"
            print(f"  [{sev}] {iss['field']}: {iss['message']}", file=sys.stderr)
            if iss.get("suggestion"):
                print(f"         -> {iss['suggestion']}", file=sys.stderr)

    print(f"\n{'='*60}", file=sys.stderr)


def main():
    if len(sys.argv) < 3:
        print("Usage: python validate.py <brands|campaigns> <input.json>", file=sys.stderr)
        print("  Input: JSON array of brand or campaign objects", file=sys.stderr)
        print("  Output: JSON validation report to stdout", file=sys.stderr)
        sys.exit(1)

    data_type = sys.argv[1]
    input_file = sys.argv[2]

    if data_type not in ("brands", "campaigns"):
        print(f"Error: first argument must be 'brands' or 'campaigns', got '{data_type}'", file=sys.stderr)
        sys.exit(1)

    with open(input_file, "r") as f:
        items = json.load(f)

    if not isinstance(items, list):
        items = [items]

    report = generate_report(data_type, items)
    print_summary(report)

    # JSON report to stdout
    print(json.dumps(report, indent=2))

    # Exit code
    if report["errors"] > 0:
        sys.exit(1)
    elif report["warnings"] > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
