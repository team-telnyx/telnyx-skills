---
name: telnyx-messaging-profiles-curl
description: >-
  Create and manage messaging profiles with number pools, sticky sender, and
  geomatch features. Configure short codes for high-volume messaging. This skill
  provides REST API (curl) examples.
metadata:
  author: telnyx
  product: messaging-profiles
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Messaging Profiles - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List messaging profiles

`GET /messaging_profiles`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_profiles"
```

## Create a messaging profile

`POST /messaging_profiles` — Required: `name`, `whitelisted_destinations`

Optional: `ai_assistant_id` (['string', 'null']), `alpha_sender` (['string', 'null']), `daily_spend_limit` (string), `daily_spend_limit_enabled` (boolean), `enabled` (boolean), `health_webhook_url` (url), `mms_fall_back_to_sms` (boolean), `mms_transcoding` (boolean), `mobile_only` (boolean), `number_pool_settings` (['object', 'null']), `resource_group_id` (['string', 'null']), `smart_encoding` (boolean), `url_shortener_settings` (['object', 'null']), `webhook_api_version` (enum), `webhook_failover_url` (url), `webhook_url` (url)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "whitelisted_destinations": [
    "string"
  ],
  "number_pool_settings": {
    "toll_free_weight": 10,
    "long_code_weight": 1,
    "skip_unhealthy": true,
    "sticky_sender": false,
    "geomatch": false
  },
  "url_shortener_settings": {
    "domain": "example.ex",
    "prefix": "",
    "replace_blacklist_only": true,
    "send_webhooks": false
  }
}' \
  "https://api.telnyx.com/v2/messaging_profiles"
```

## Retrieve a messaging profile

`GET /messaging_profiles/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_profiles/{id}"
```

## Update a messaging profile

`PATCH /messaging_profiles/{id}`

Optional: `alpha_sender` (['string', 'null']), `created_at` (date-time), `daily_spend_limit` (string), `daily_spend_limit_enabled` (boolean), `enabled` (boolean), `id` (uuid), `mms_fall_back_to_sms` (boolean), `mms_transcoding` (boolean), `mobile_only` (boolean), `name` (string), `number_pool_settings` (['object', 'null']), `record_type` (enum), `smart_encoding` (boolean), `updated_at` (date-time), `url_shortener_settings` (['object', 'null']), `v1_secret` (string), `webhook_api_version` (enum), `webhook_failover_url` (url), `webhook_url` (url), `whitelisted_destinations` (array[string])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "number_pool_settings": {
    "toll_free_weight": 10,
    "long_code_weight": 1,
    "skip_unhealthy": true,
    "sticky_sender": false,
    "geomatch": false
  },
  "url_shortener_settings": {
    "domain": "example.ex",
    "prefix": "",
    "replace_blacklist_only": true,
    "send_webhooks": false
  }
}' \
  "https://api.telnyx.com/v2/messaging_profiles/{id}"
```

## Delete a messaging profile

`DELETE /messaging_profiles/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/messaging_profiles/{id}"
```

## List phone numbers associated with a messaging profile

`GET /messaging_profiles/{id}/phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_profiles/{id}/phone_numbers"
```

## List short codes associated with a messaging profile

`GET /messaging_profiles/{id}/short_codes`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_profiles/{id}/short_codes"
```

## List short codes

`GET /short_codes`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/short_codes"
```

## Retrieve a short code

`GET /short_codes/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/short_codes/{id}"
```

## Update short code

Update the settings for a specific short code.

`PATCH /short_codes/{id}` — Required: `messaging_profile_id`

Optional: `tags` (['array'])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messaging_profile_id": "string"
}' \
  "https://api.telnyx.com/v2/short_codes/{id}"
```
