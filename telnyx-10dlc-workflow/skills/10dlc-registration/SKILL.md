---
name: 10dlc-registration
description: >-
  Register 10DLC brands and campaigns for A2P SMS in the USA. Handles individual
  and bulk registration from any file format. Validates all data before spending
  money, provides campaign templates, and tracks status across registrations.
metadata:
  author: telnyx
  product: 10dlc
  requires:
    bins:
      - telnyx
    env:
      - TELNYX_API_KEY
---

# 10DLC Registration

Register brands, submit campaigns, and assign phone numbers for compliant A2P SMS messaging in the USA.

## How This Skill Works

**You (the agent) handle the flexible parts. Scripts handle the deterministic parts.**

| Task | Who | How |
|------|-----|-----|
| Read user's file (any format) | Agent | Read the file, parse it, map columns |
| Map messy column names to API fields | Agent | Use the fuzzy mapping table below |
| Validate all data before spending money | Script | `python {baseDir}/scripts/validate.py brands data.json` |
| Show costs and get user confirmation | Agent | Present validation results, ask to proceed |
| Create brands | Script | `python {baseDir}/scripts/create_brands.py data.json` |
| Coordinate sole prop OTP verification | Agent | Ask user for PINs, run verify commands |
| Validate campaign data | Script | `python {baseDir}/scripts/validate.py campaigns data.json` |
| Submit campaigns | Script | `python {baseDir}/scripts/submit_campaigns.py data.json` |
| Pull status across all registrations | Script | `python {baseDir}/scripts/status_report.py` |
| Explain failures and recommend next steps | Agent | Use troubleshooting section below |
| Assign phone numbers | Agent | Run CLI commands per user's instructions |

**CRITICAL: Brand registration costs $4 per brand (non-refundable). Campaign submission costs a non-refundable 3-month fee. ALWAYS run validation and get user confirmation before executing.**

---

## Multi-Session Workflow

10DLC registration takes 1-3 weeks due to carrier review times. This means multiple agent sessions:

```
Session 1 (~10 min)         Wait 1-7 business days       Session 2 (~10 min)         Wait 3-7 business days       Session 3 (~5 min)
───────────────────         ─────────────────────        ───────────────────         ─────────────────────        ──────────────────
Read file, map columns      Brand vetting by TCR         Check brand status          Campaign carrier review      Check campaign status
Validate brands                                          Submit campaigns for                                     Assign phone numbers
Get cost approval                                        approved brands                                          Done — numbers are live
Create brands                                            Handle any rejections
```

Tell the user upfront: "This process takes 1-3 weeks total because brands and campaigns need carrier review. I'll help you through each step. You'll get an email from Telnyx when brands are approved — come back and run this skill again to continue."

## Prerequisites

```bash
# Install Telnyx CLI
go install github.com/team-telnyx/telnyx-cli/cmd/telnyx@latest

# Set API key
export TELNYX_API_KEY=your_key

# Python 3 (no pip packages needed — scripts use only stdlib)
python3 --version
```

---

## Phase 1: Gather Brand Information

### From a File

The user may provide data in any format: Excel (.xlsx), CSV, TSV, Google Sheets export, or even a pasted table. Read the file and map columns to the required fields below using fuzzy matching.

**Common column name mappings:**

| Required Field | Common Aliases |
|---|---|
| `display_name` | Company Name, Brand Name, Business Name, DBA, Name |
| `entity_type` | Entity Type, Business Type, Type, Organization Type |
| `vertical` | Vertical, Industry, Sector, Category |
| `email` | Email, Contact Email, Brand Email, Support Email |
| `country` | Country, Country Code (almost always "US") |
| `company_name` | Legal Name, Legal Company Name, Registered Name |
| `ein` | EIN, Tax ID, Tax Number, FEIN, Federal Tax ID |
| `phone` | Phone, Phone Number, Contact Phone, Business Phone |
| `website` | Website, URL, Web, Homepage |
| `street` | Street, Address, Street Address, Address Line 1 |
| `city` | City |
| `state` | State, State Code |
| `postal_code` | Zip, Zip Code, Postal Code, ZIP |
| `first_name` | First Name, Owner First Name |
| `last_name` | Last Name, Owner Last Name |

If columns are ambiguous, ask the user to confirm the mapping before proceeding.

### From Conversation

Ask the user for:
1. How many brands to register?
2. For each brand: company name, entity type, industry, contact email
3. Then gather remaining required fields per entity type (see below)

---

## Phase 2: Validate Before Spending Money

Once you've gathered and mapped the data, write it as a JSON array and run the validation script:

```bash
# Write the mapped data to a temp file, then validate
python3 {baseDir}/scripts/validate.py brands /tmp/brands.json
```

The script checks every rule below automatically. It outputs a JSON report to stdout and a human-readable summary to stderr. Exit code 0 = all pass, 1 = errors found, 2 = warnings only.

Present the validation results to the user before proceeding.

**Reference: The rules the script enforces (for your understanding, do not re-implement):**

### Brand Validation Rules

#### Required Fields by Entity Type

**All entity types require:** `country`, `display_name`, `email`, `entity_type`, `vertical`

| Field | SOLE_PROPRIETOR | PRIVATE_PROFIT | PUBLIC_PROFIT | NON_PROFIT | GOVERNMENT |
|---|---|---|---|---|---|
| `company_name` | - | Required | Required | Required | Required |
| `ein` | - | Recommended | Required | Required | Recommended |
| `first_name` | Required | - | - | - | - |
| `last_name` | Required | - | - | - | - |
| `phone` | Required (for OTP) | Recommended | Recommended | Recommended | Recommended |
| `street` | Recommended | Recommended | Recommended | Recommended | Recommended |
| `city` | Recommended | Recommended | Recommended | Recommended | Recommended |
| `state` | Recommended | Recommended | Recommended | Recommended | Recommended |
| `postal_code` | Recommended | Recommended | Recommended | Recommended | Recommended |
| `website` | - | Recommended | Recommended | Recommended | - |
| `stock_exchange` | - | - | Required | - | - |
| `stock_symbol` | - | - | Required | - | - |
| `business_contact_email` | - | - | Required | - | - |

#### Field Format Validation

| Field | Rule | Example |
|---|---|---|
| `ein` | Exactly 9 digits, no dashes | `123456789` not `12-3456789` |
| `country` | ISO2 code | `US` |
| `email` | Valid email format | `admin@company.com` |
| `phone` | E.164 format | `+15551234567` |
| `entity_type` | Must be one of: `SOLE_PROPRIETOR`, `PRIVATE_PROFIT`, `PUBLIC_PROFIT`, `NON_PROFIT`, `GOVERNMENT` | |
| `postal_code` | 5-digit US zip | `10001` |
| `state` | 2-letter US state code | `NY` |
| `website` | Must start with http:// or https:// | `https://acme.com` |

#### Entity Type Detection Hints

If the user doesn't know the entity type, help them:
- **LLC, Inc, Corp, Ltd** → likely `PRIVATE_PROFIT`
- **Publicly traded / has stock ticker** → `PUBLIC_PROFIT`
- **501(c)(3), charity, foundation** → `NON_PROFIT`
- **Individual, freelancer, solo** → `SOLE_PROPRIETOR`
- **City, county, federal, agency** → `GOVERNMENT`

#### Vertical Values

`AGRICULTURE`, `AUTOMOTIVE`, `BANKING`, `COMMUNICATION`, `CONSTRUCTION`, `EDUCATION`, `ELECTRONICS`, `ENERGY`, `ENGINEERING`, `ENTERTAINMENT`, `FINANCIAL`, `FOOD_BEVERAGE`, `GOVERNMENT`, `HEALTHCARE`, `HOSPITALITY`, `INSURANCE`, `JEWELRY`, `LEGAL`, `MANUFACTURING`, `MEDIA`, `NOT_FOR_PROFIT`, `OIL_AND_GAS`, `POSTAL`, `PROFESSIONAL`, `REAL_ESTATE`, `RELIGION`, `RETAIL`, `TECHNOLOGY`, `TOBACCO`, `TRANSPORTATION`

#### Common Mistakes to Catch

- **EIN has dashes**: Strip dashes, must be 9 digits only
- **P.O. Box address**: TCR rejects P.O. Boxes. Must be a physical street address.
- **EIN doesn't match legal name**: The EIN must match IRS records exactly. Even "Inc" vs "Inc." can cause issues. Warn the user.
- **No website for private/public company**: Not required, but significantly impacts vetting score (trust score 0-100). Strongly recommend providing one.
- **Sole proprietor trying to use MARKETING use case**: Sole props are limited to 2FA, CUSTOMER_CARE, DELIVERY_NOTIFICATION, ACCOUNT_NOTIFICATION only.

### Present Validation Results

Show the user a summary table before proceeding:

```
Brand Validation Results:
| # | Brand Name | Entity Type | Status | Issues |
|---|-----------|-------------|--------|--------|
| 1 | Acme Corp | PRIVATE_PROFIT | READY | None |
| 2 | Beta LLC | PRIVATE_PROFIT | WARNING | No website (lower trust score) |
| 3 | Jane Doe | SOLE_PROPRIETOR | ERROR | Missing phone (required for OTP) |

Estimated cost: 2 brands x $4 = $8 (Brand #3 needs fixes first)

Proceed with brands 1 and 2? (Y/N)
```

---

## Phase 3: Create Brands

After the user confirms, run the creation script:

```bash
# Dry run first — shows commands without executing
python3 {baseDir}/scripts/create_brands.py /tmp/brands.json --dry-run

# Execute — creates brands, outputs JSON with brand IDs
python3 {baseDir}/scripts/create_brands.py /tmp/brands.json
```

The script automatically:
- Runs validation first (refuses to execute if errors exist)
- Creates each brand via CLI
- Extracts and records brand IDs from responses
- Flags sole proprietor brands that need OTP verification
- Pauses between API calls to avoid rate limits
- Outputs a JSON results report with brand IDs and status

Present the results to the user.

### Sole Proprietor OTP Verification

This requires the actual business owner's phone. Coordinate with the user:

```bash
# Step 1: Trigger OTP to brand owner's phone
telnyx messaging-10dlc brand trigger-sms-otp <brand-id> \
  --pin-sms "Your Telnyx verification PIN is @OTP_PIN@" \
  --success-sms "Verification successful!"

# Step 2: Ask user for the PIN they received, then verify
telnyx messaging-10dlc brand verify-sms-otp <brand-id> \
  --otp-pin <pin-from-user>
```

Tell the user: "An SMS was sent to [phone number]. Please tell me the PIN you received."

### Track Results

Maintain a running status table:

```
Registration Progress:
| Brand | Brand ID | Status | Next Step |
|-------|----------|--------|-----------|
| Acme Corp | br_abc123 | PENDING_VETTING | Wait 1-7 business days for approval |
| Beta LLC | br_def456 | VERIFIED | Ready for campaign |
| Jane Doe | br_ghi789 | OTP_SENT | Waiting for PIN from owner |
```

### What to Tell the User Before Ending Session 1

> "Your brands have been submitted. Here's what happens next:
> - Brand vetting takes 1-7 business days. You'll get an email from Telnyx when each brand is reviewed.
> - When you get the approval email, come back and run this skill again. I'll check status and submit campaigns.
> - Save these brand IDs — you'll need them next time: [list brand IDs]"

---

## Phase 4: Submit Campaigns

**This is Session 2.** The user comes back after getting a brand approval email from Telnyx.

Start by checking status:

```bash
# Quick status check
python3 {baseDir}/scripts/status_report.py

# Or check a specific brand
telnyx messaging-10dlc brand retrieve <brand-id>
```

When brands are approved, help the user build campaign data. Use the templates below as starting points, customize with the user's details, then validate and submit:

```bash
# Validate campaign data
python3 {baseDir}/scripts/validate.py campaigns /tmp/campaigns.json

# Dry run
python3 {baseDir}/scripts/submit_campaigns.py /tmp/campaigns.json --dry-run

# Submit (checks brand qualification automatically before each submission)
python3 {baseDir}/scripts/submit_campaigns.py /tmp/campaigns.json
```

The submission script automatically checks brand qualification before each campaign and refuses to submit if validation fails.

### Campaign Validation Rules

**CRITICAL: Campaigns CANNOT be edited after submission (only sample messages can be changed). Description, use case, and message flow are permanent. Validate thoroughly.**

#### Description Validation

- Must be 10+ words minimum
- Must be specific to the business and messaging purpose
- Must align with the declared use case
- Avoid vague terms: "various", "general", "different", "multiple"
- For MARKETING: explicitly mention "marketing" in description
- For CUSTOMER_CARE: include words like "support", "service", "help"

**Good:** "Acme Corp sends order confirmation and shipping updates to customers who purchase products through our e-commerce platform at acme.com"

**Bad:** "We send various messages to customers about different things"

#### Sample Message Validation

- At least 2 sample messages required for most use cases
- Each sample must be 20+ characters
- Each sample MUST include opt-out language: "Reply STOP to unsubscribe" or equivalent
- For MARKETING: include "Msg & data rates may apply"
- Messages must identify the sender by company name
- No informal language (hey, ur, omg)
- No spam triggers (FREE, WIN, ACT NOW, excessive caps/punctuation)
- If messages contain URLs, set `--embedded-link` flag to true
- Messages under 1600 characters

**Opt-out keywords to include:** STOP, UNSUBSCRIBE, OPT OUT, CANCEL, END, QUIT

#### Message Flow Validation

Must document how users opt in. Required components:
- How users give consent (web form, verbal, etc.)
- Privacy policy reference
- Terms and conditions reference
- Opt-out instructions
- Data rate disclosure
- Should include URLs to actual consent forms/policies
- Must be 30+ words

**Good:** "Customers opt in to receive SMS notifications by checking the 'Receive SMS updates' checkbox during checkout at https://acme.com/checkout. The checkbox is unchecked by default. Our privacy policy is at https://acme.com/privacy and terms at https://acme.com/terms. Customers can opt out at any time by replying STOP. Msg & data rates may apply."

**Bad:** "Customers sign up on our website."

### Campaign Templates

Use these as starting points. Customize the company name and details.

#### CUSTOMER_CARE Template

```bash
telnyx messaging-10dlc campaign-builder submit \
  --brand-id <brand-id> \
  --usecase CUSTOMER_CARE \
  --description "[COMPANY] sends customer support communications including order updates, service notifications, and account alerts to customers who have opted in through our platform at [WEBSITE]." \
  --sample1 "[COMPANY]: Your order #12345 has been shipped and is estimated to arrive on March 5. Track your package at [WEBSITE]/track. Reply STOP to unsubscribe." \
  --sample2 "[COMPANY]: Your support ticket #67890 has been updated. A representative has responded to your inquiry. Reply STOP to opt out." \
  --message-flow "Customers opt in to receive SMS notifications by providing their phone number and checking the SMS consent checkbox during account registration at [WEBSITE]/register. The checkbox is unchecked by default. Our privacy policy is available at [WEBSITE]/privacy and terms of service at [WEBSITE]/terms. Customers can opt out at any time by replying STOP. Msg & data rates may apply." \
  --help-message "[COMPANY] support: Reply HELP for assistance or contact us at [EMAIL] or [PHONE]. Reply STOP to opt out." \
  --optin-message "You have been subscribed to [COMPANY] SMS notifications. Reply HELP for help, STOP to cancel. Msg & data rates may apply." \
  --optout-message "You have been unsubscribed from [COMPANY] messages. You will no longer receive SMS from us. Reply START to re-subscribe." \
  --subscriber-optin \
  --subscriber-optout \
  --subscriber-help
```

#### 2FA Template

```bash
telnyx messaging-10dlc campaign-builder submit \
  --brand-id <brand-id> \
  --usecase 2FA \
  --description "[COMPANY] sends one-time verification codes for two-factor authentication to secure user account access on our platform at [WEBSITE]." \
  --sample1 "[COMPANY]: Your verification code is 483921. This code expires in 10 minutes. Do not share this code with anyone. Reply STOP to opt out." \
  --sample2 "[COMPANY]: A login attempt was detected from a new device. Your security code is 729104. Reply STOP to unsubscribe." \
  --message-flow "Users receive verification codes when they enable two-factor authentication in their account settings at [WEBSITE]/security. Users consent to SMS verification during the 2FA setup process. Privacy policy: [WEBSITE]/privacy. Terms: [WEBSITE]/terms. Users can disable 2FA in settings or reply STOP to opt out of SMS codes. Msg & data rates may apply." \
  --help-message "[COMPANY] verification: Reply HELP for support or visit [WEBSITE]/support. Reply STOP to opt out of verification codes." \
  --subscriber-optin \
  --subscriber-optout \
  --subscriber-help
```

#### MARKETING Template

```bash
telnyx messaging-10dlc campaign-builder submit \
  --brand-id <brand-id> \
  --usecase MARKETING \
  --description "[COMPANY] sends marketing SMS promotions, product announcements, and exclusive offers to customers who have explicitly opted in to our marketing communications at [WEBSITE]." \
  --sample1 "[COMPANY]: This week only — 20% off your next purchase with code SAVE20. Shop now at [WEBSITE]. Msg & data rates may apply. Reply STOP to unsubscribe." \
  --sample2 "[COMPANY]: New arrivals just landed! Check out our latest collection at [WEBSITE]/new. Msg & data rates may apply. Reply STOP to opt out." \
  --message-flow "Customers opt in to marketing SMS by entering their phone number and checking the 'Subscribe to SMS marketing' checkbox on our website at [WEBSITE]/subscribe. The checkbox is unchecked by default and clearly labeled as marketing SMS consent. Our privacy policy is at [WEBSITE]/privacy and terms at [WEBSITE]/terms. Customers may opt out at any time by replying STOP or UNSUBSCRIBE. Msg & data rates may apply." \
  --help-message "[COMPANY] marketing: Reply HELP for support or contact [EMAIL]. Reply STOP to unsubscribe from marketing messages. Msg & data rates may apply." \
  --optin-message "Welcome to [COMPANY] SMS marketing! You'll receive exclusive offers and updates. Reply HELP for help, STOP to cancel. Msg & data rates may apply." \
  --optout-message "You have been unsubscribed from [COMPANY] marketing messages. You will no longer receive promotional SMS. Reply START to re-subscribe." \
  --embedded-link \
  --subscriber-optin \
  --subscriber-optout \
  --subscriber-help
```

#### DELIVERY_NOTIFICATION Template

```bash
telnyx messaging-10dlc campaign-builder submit \
  --brand-id <brand-id> \
  --usecase DELIVERY_NOTIFICATION \
  --description "[COMPANY] sends shipping and delivery status updates to customers who have placed orders through our e-commerce platform at [WEBSITE]." \
  --sample1 "[COMPANY]: Your order #12345 has shipped via UPS. Tracking: 1Z999AA10123456784. Estimated delivery: March 5. Reply STOP to opt out." \
  --sample2 "[COMPANY]: Your package is out for delivery today and will arrive by 5pm. Reply STOP to unsubscribe from delivery updates." \
  --message-flow "Customers opt in to delivery notifications by providing their phone number during checkout at [WEBSITE]/checkout and consenting to receive order and shipping updates via SMS. Consent checkbox is unchecked by default. Privacy policy: [WEBSITE]/privacy. Terms: [WEBSITE]/terms. Customers can opt out by replying STOP at any time. Msg & data rates may apply." \
  --help-message "[COMPANY] shipping updates: Reply HELP for support or email [EMAIL]. Reply STOP to opt out of delivery notifications." \
  --subscriber-optin \
  --subscriber-optout \
  --subscriber-help
```

#### ACCOUNT_NOTIFICATION Template

```bash
telnyx messaging-10dlc campaign-builder submit \
  --brand-id <brand-id> \
  --usecase ACCOUNT_NOTIFICATION \
  --description "[COMPANY] sends account-related notifications including balance alerts, payment confirmations, and account activity updates to registered users at [WEBSITE]." \
  --sample1 "[COMPANY]: Your payment of $49.99 has been processed. Your new balance is $150.00. View details at [WEBSITE]/account. Reply STOP to opt out." \
  --sample2 "[COMPANY]: Your account settings have been updated. If you did not make this change, contact support at [EMAIL]. Reply STOP to unsubscribe." \
  --message-flow "Users opt in to account notifications during account registration at [WEBSITE]/register by providing their phone number and checking the SMS notifications checkbox. The checkbox is unchecked by default. Privacy policy: [WEBSITE]/privacy. Terms: [WEBSITE]/terms. Users can manage notification preferences in account settings or reply STOP to opt out. Msg & data rates may apply." \
  --help-message "[COMPANY] account alerts: Reply HELP for support or contact [EMAIL]. Reply STOP to opt out of account notifications." \
  --subscriber-optin \
  --subscriber-optout \
  --subscriber-help
```

### Campaign Submission Checklist

Before submitting, verify:

- [ ] Brand is approved (status is not PENDING)
- [ ] Brand qualifies for the chosen use case (ran qualify-by-usecase)
- [ ] Description is 10+ words and specific to the business
- [ ] At least 2 sample messages provided
- [ ] All samples include opt-out language (STOP/unsubscribe)
- [ ] All samples identify the sender by name
- [ ] Message flow describes opt-in process with URLs
- [ ] If messages contain URLs, `--embedded-link` is set
- [ ] For MARKETING: samples include "Msg & data rates may apply"
- [ ] User has confirmed and understands the campaign cost is non-refundable

### Check Campaign Cost Before Submitting

```bash
telnyx messaging-10dlc campaign usecase get-cost --usecase CUSTOMER_CARE
```

Show the user the cost and get confirmation before submitting.

### What to Tell the User Before Ending Session 2

> "Your campaigns have been submitted. Here's what happens next:
> - Campaign review takes 3-7 business days. You'll get an email from Telnyx when each campaign is reviewed.
> - When you get the approval email, come back and run this skill again. I'll assign your phone numbers and you'll be live.
> - Save these campaign IDs — you'll need them next time: [list campaign IDs]"

---

## Phase 5: Assign Phone Numbers

**This is Session 3.** The user comes back after getting a campaign approval email from Telnyx.

```bash
# Check campaign status first
telnyx messaging-10dlc campaign retrieve <campaign-id>

# Assign individual number
telnyx messaging-10dlc phone-number-campaign create \
  --phone-number +15551234567 \
  --campaign-id <campaign-id>

# Or assign all numbers on a messaging profile
telnyx messaging-10dlc phone-number-assignment-by-profile assign \
  --messaging-profile-id <profile-id> \
  --campaign-id <campaign-id>
```

After assignment, tell the user: "You're live! Your phone numbers are now registered for 10DLC messaging."

---

## Status Tracking

Run the status report script for a consolidated view:

```bash
# Full status report (all brands, campaigns, assignments)
python3 {baseDir}/scripts/status_report.py

# Check specific brands
python3 {baseDir}/scripts/status_report.py --brand-ids br_abc123,br_def456

# JSON output for programmatic use
python3 {baseDir}/scripts/status_report.py --json
```

The script pulls all brands, campaigns (with per-carrier MNO status), and phone number assignments, then outputs a formatted table and identifies next steps automatically.

For individual lookups, the CLI commands are also available:

```bash
telnyx messaging-10dlc brand retrieve <brand-id>
telnyx messaging-10dlc brand get-feedback <brand-id>
telnyx messaging-10dlc campaign retrieve <campaign-id>
telnyx messaging-10dlc campaign get-operation-status <campaign-id>
```

---

## Handling Failures

### Brand Rejection or Low Trust Score

```bash
# Get detailed feedback
telnyx messaging-10dlc brand get-feedback <brand-id>

# Request enhanced vetting (deeper review)
telnyx messaging-10dlc brand external-vetting order \
  --brand-id <brand-id> \
  --evp-id <evp-id> \
  --vetting-class ENHANCED

# Revet (available once immediately, then once per 3 months)
telnyx messaging-10dlc brand revet <brand-id>
```

**Common fixes for low trust scores:**
- Add a website (or improve existing one)
- Ensure EIN exactly matches IRS records for the legal name
- Provide complete physical address (no P.O. boxes)
- Add social media and business directory listings

### Campaign Rejection

**IMPORTANT: Description and use case CANNOT be changed. You must create a new campaign.**

```bash
# Check what carrier(s) rejected and why
telnyx messaging-10dlc campaign get-operation-status <campaign-id>

# For native Telnyx campaigns (TELNYX_FAILED or MNO_REJECTED), submit appeal
telnyx messaging-10dlc campaign submit-appeal <campaign-id> \
  --appeal-reason "The website has been updated to include the required privacy policy and terms of service."
```

**Common rejection reasons and fixes:**

| Rejection Reason | Fix |
|---|---|
| Insufficient description | Create new campaign with detailed, specific description |
| Missing opt-out in samples | Create new campaign with "Reply STOP to unsubscribe" in all samples |
| Content doesn't match use case | Create new campaign with correct use case or aligned content |
| Missing message flow | Create new campaign with documented opt-in process including URLs |
| Embedded links not declared | Create new campaign with `--embedded-link` flag |
| Carrier-specific content policy | Review carrier guidelines, avoid spam triggers, remove URL shorteners |

### Carrier-Specific Notes

- **T-Mobile**: Stricter on cannabis, CBD, debt relief, and political campaigns. Requires enhanced verification for these verticals.
- **Verizon**: Aggressive content filtering. Avoid words like "free", "win", "act now", excessive caps.
- **AT&T**: Throughput heavily tied to trust score. Low score = severe rate limiting.

---

## Use Cases Reference

| Use Case | Description | Sole Prop Eligible | Notes |
|---|---|---|---|
| `2FA` | Authentication codes | Yes | Highest throughput |
| `CUSTOMER_CARE` | Support messages | Yes | |
| `ACCOUNT_NOTIFICATION` | Account alerts | Yes | |
| `DELIVERY_NOTIFICATION` | Shipping updates | Yes | |
| `MARKETING` | Promotional messages | No | Requires "Msg & data rates" |
| `MIXED` | Multiple purposes | No | Most common for businesses |
| `POLLING_VOTING` | Polls and surveys | No | |
| `CHARITY` | Donation requests | No | |
| `POLITICAL` | Political campaigns | No | Enhanced verification needed |
| `PUBLIC_SERVICE_ANNOUNCEMENT` | Non-commercial PSAs | No | |
| `SECURITY_ALERT` | Security notifications | No | |

---

## Timeline Summary

| Step | Time | Cost |
|------|------|------|
| Brand creation | Instant | $4/brand (non-refundable) |
| Sole prop OTP verification | 1-5 minutes | Free |
| Brand vetting | 1-7 business days | Free |
| Enhanced vetting (optional) | 1-7 business days | Varies |
| Campaign qualification check | Instant | Free |
| Campaign submission | Instant | Non-refundable 3-month fee (varies by use case) |
| Campaign carrier review | 3-7 business days | Free |
| Phone number assignment | Instant | Free |

**Total timeline for a single brand end-to-end: 1-3 weeks**

For bulk registrations (10-20 brands), submit all brands on day 1. Campaigns can be submitted as brands get approved over the following days. Expect full completion in 2-4 weeks.
