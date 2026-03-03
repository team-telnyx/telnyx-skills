---
name: telnyx-account-curl
description: >-
  Manage account balance, payments, invoices, webhooks, and view audit logs and
  detail records. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: account
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List Audit Logs

Retrieve a list of audit log entries.

`GET /audit_events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/audit_events?sort=desc"
```

## Get user balance details

`GET /balance`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/balance"
```

## Get monthly charges breakdown

Retrieve a detailed breakdown of monthly charges for phone numbers in a specified date range.

`GET /charges_breakdown`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/charges_breakdown?start_date=2025-05-01&end_date=2025-06-01&format=json"
```

## Get monthly charges summary

Retrieve a summary of monthly charges for a specified date range.

`GET /charges_summary`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/charges_summary?start_date=2025-05-01&end_date=2025-06-01"
```

## Search detail records

Search for any detail record across the Telnyx Platform

`GET /detail_records`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/detail_records"
```

## List invoices

Retrieve a paginated list of invoices.

`GET /invoices`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/invoices?sort=period_start"
```

## Get invoice by ID

Retrieve a single invoice by its unique identifier.

`GET /invoices/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/invoices/{id}?action=json"
```

## List auto recharge preferences

Returns the payment auto recharge preferences.

`GET /payment/auto_recharge_prefs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/payment/auto_recharge_prefs"
```

## Update auto recharge preferences

Update payment auto recharge preferences.

`PATCH /payment/auto_recharge_prefs`

Optional: `enabled` (boolean), `invoice_enabled` (boolean), `preference` (enum), `recharge_amount` (string), `threshold_amount` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "threshold_amount": "104.00",
  "recharge_amount": "104.00",
  "enabled": true,
  "invoice_enabled": true,
  "preference": "credit_paypal"
}' \
  "https://api.telnyx.com/v2/payment/auto_recharge_prefs"
```

## List User Tags

List all user tags.

`GET /user_tags`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/user_tags"
```

## Create a stored payment transaction

`POST /v2/payment/stored_payment_transactions` — Required: `amount`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": "120.00"
}' \
  "https://api.telnyx.com/v2/v2/payment/stored_payment_transactions"
```

## List webhook deliveries

Lists webhook_deliveries for the authenticated user

`GET /webhook_deliveries`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/webhook_deliveries"
```

## Find webhook_delivery details by ID

Provides webhook_delivery debug data, such as timestamps, delivery status and attempts.

`GET /webhook_deliveries/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/webhook_deliveries/C9C0797E-901D-4349-A33C-C2C8F31A92C2"
```
