---
name: telnyx-verify-curl
description: >-
  Look up phone number information (carrier, type, caller name) and verify users
  via SMS/voice OTP. Use for phone verification and data enrichment. This skill
  provides REST API (curl) examples.
metadata:
  author: telnyx
  product: verify
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Verify - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Lookup phone number data

Returns information about the provided phone number.

`GET /number_lookup/{phone_number}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_lookup/+18665552368"
```

## List verifications by phone number

`GET /verifications/by_phone_number/{phone_number}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234"
```

## Verify verification code by phone number

`POST /verifications/by_phone_number/{phone_number}/actions/verify` — Required: `code`, `verify_profile_id`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "code": "17686",
  "verify_profile_id": "12ade33a-21c0-473b-b055-b3c836e1c292"
}' \
  "https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234/actions/verify"
```

## Trigger Call verification

`POST /verifications/call` — Required: `phone_number`, `verify_profile_id`

Optional: `custom_code` (['string', 'null']), `extension` (['string', 'null']), `timeout_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_number": "+13035551234",
  "verify_profile_id": "12ade33a-21c0-473b-b055-b3c836e1c292",
  "custom_code": "43612",
  "timeout_secs": 300,
  "extension": "1www2WABCDw9"
}' \
  "https://api.telnyx.com/v2/verifications/call"
```

## Trigger Flash call verification

`POST /verifications/flashcall` — Required: `phone_number`, `verify_profile_id`

Optional: `timeout_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_number": "+13035551234",
  "verify_profile_id": "12ade33a-21c0-473b-b055-b3c836e1c292",
  "timeout_secs": 300
}' \
  "https://api.telnyx.com/v2/verifications/flashcall"
```

## Trigger SMS verification

`POST /verifications/sms` — Required: `phone_number`, `verify_profile_id`

Optional: `custom_code` (['string', 'null']), `timeout_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_number": "+13035551234",
  "verify_profile_id": "12ade33a-21c0-473b-b055-b3c836e1c292",
  "custom_code": "43612",
  "timeout_secs": 300
}' \
  "https://api.telnyx.com/v2/verifications/sms"
```

## Retrieve verification

`GET /verifications/{verification_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verifications/12ade33a-21c0-473b-b055-b3c836e1c292"
```

## Verify verification code by ID

`POST /verifications/{verification_id}/actions/verify`

Optional: `code` (string), `status` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "code": "17686",
  "status": "accepted"
}' \
  "https://api.telnyx.com/v2/verifications/12ade33a-21c0-473b-b055-b3c836e1c292/actions/verify"
```

## List all Verify profiles

Gets a paginated list of Verify profiles.

`GET /verify_profiles`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verify_profiles"
```

## Create a Verify profile

Creates a new Verify profile to associate verifications with.

`POST /verify_profiles` — Required: `name`

Optional: `call` (object), `flashcall` (object), `language` (string), `rcs` (object), `sms` (object), `webhook_failover_url` (string), `webhook_url` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Test Profile",
  "webhook_url": "http://example.com/webhook",
  "webhook_failover_url": "http://example.com/webhook/failover",
  "language": "en-US"
}' \
  "https://api.telnyx.com/v2/verify_profiles"
```

## Retrieve Verify profile message templates

List all Verify profile message templates.

`GET /verify_profiles/templates`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verify_profiles/templates"
```

## Create message template

Create a new Verify profile message template.

`POST /verify_profiles/templates` — Required: `text`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "text": "Your {{app_name}} verification code is: {{code}}."
}' \
  "https://api.telnyx.com/v2/verify_profiles/templates"
```

## Update message template

Update an existing Verify profile message template.

`PATCH /verify_profiles/templates/{template_id}` — Required: `text`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "text": "Your {{app_name}} verification code is: {{code}}."
}' \
  "https://api.telnyx.com/v2/verify_profiles/templates/12ade33a-21c0-473b-b055-b3c836e1c292"
```

## Retrieve Verify profile

Gets a single Verify profile.

`GET /verify_profiles/{verify_profile_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verify_profiles/12ade33a-21c0-473b-b055-b3c836e1c292"
```

## Update Verify profile

`PATCH /verify_profiles/{verify_profile_id}`

Optional: `call` (object), `flashcall` (object), `language` (string), `name` (string), `rcs` (object), `sms` (object), `webhook_failover_url` (string), `webhook_url` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Test Profile",
  "webhook_url": "http://example.com/webhook",
  "webhook_failover_url": "http://example.com/webhook/failover",
  "language": "en-US"
}' \
  "https://api.telnyx.com/v2/verify_profiles/12ade33a-21c0-473b-b055-b3c836e1c292"
```

## Delete Verify profile

`DELETE /verify_profiles/{verify_profile_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/verify_profiles/12ade33a-21c0-473b-b055-b3c836e1c292"
```
