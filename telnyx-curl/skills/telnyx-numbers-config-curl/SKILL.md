---
name: telnyx-numbers-config-curl
description: >-
  Configure phone number settings including caller ID, call forwarding,
  messaging enablement, and connection assignments. This skill provides REST API
  (curl) examples.
metadata:
  author: telnyx
  product: numbers-config
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers Config - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Bulk update phone number profiles

`POST /messaging_numbers_bulk_updates` — Required: `messaging_profile_id`, `numbers`

Optional: `assign_only` (boolean)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messaging_profile_id": "string",
  "numbers": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/messaging_numbers_bulk_updates"
```

## Retrieve bulk update status

`GET /messaging_numbers_bulk_updates/{order_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_numbers_bulk_updates/{order_id}"
```

## List mobile phone numbers with messaging settings

`GET /mobile_phone_numbers/messaging`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/mobile_phone_numbers/messaging"
```

## Retrieve a mobile phone number with messaging settings

`GET /mobile_phone_numbers/{id}/messaging`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/mobile_phone_numbers/{id}/messaging"
```

## List phone numbers

`GET /phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers?sort=connection_name&handle_messaging_profile_error=false"
```

## Verify ownership of phone numbers

Verifies ownership of the provided phone numbers and returns a mapping of numbers to their IDs, plus a list of numbers not found in the account.

`POST /phone_numbers/actions/verify_ownership` — Required: `phone_numbers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "+15551234567"
  ]
}' \
  "https://api.telnyx.com/v2/phone_numbers/actions/verify_ownership"
```

## Lists the phone numbers jobs

`GET /phone_numbers/jobs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/jobs?sort=created_at"
```

## Delete a batch of numbers

Creates a new background job to delete a batch of numbers.

`POST /phone_numbers/jobs/delete_phone_numbers` — Required: `phone_numbers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/phone_numbers/jobs/delete_phone_numbers"
```

## Update the emergency settings from a batch of numbers

Creates a background job to update the emergency settings of a collection of phone numbers.

`POST /phone_numbers/jobs/update_emergency_settings` — Required: `emergency_enabled`, `phone_numbers`

Optional: `emergency_address_id` (['string', 'null'])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "string"
  ],
  "emergency_enabled": true
}' \
  "https://api.telnyx.com/v2/phone_numbers/jobs/update_emergency_settings"
```

## Update a batch of numbers

Creates a new background job to update a batch of numbers.

`POST /phone_numbers/jobs/update_phone_numbers` — Required: `phone_numbers`

Optional: `billing_group_id` (string), `connection_id` (string), `customer_reference` (string), `deletion_lock_enabled` (boolean), `external_pin` (string), `hd_voice_enabled` (boolean), `tags` (array[string]), `voice` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "string"
  ],
  "customer_reference": "MY REF 001",
  "voice": {
    "tech_prefix_enabled": true,
    "translated_number": "+13035559999",
    "caller_id_name_enabled": true,
    "call_forwarding": {
      "call_forwarding_enabled": true,
      "forwards_to": "+13035559123",
      "forwarding_type": "always"
    },
    "cnam_listing": {
      "cnam_listing_enabled": true,
      "cnam_listing_details": "example"
    },
    "usage_payment_method": "pay-per-minute",
    "media_features": {
      "rtp_auto_adjust_enabled": true,
      "accept_any_rtp_packets_enabled": true,
      "t38_fax_gateway_enabled": true
    },
    "call_recording": {
      "inbound_call_recording_enabled": true,
      "inbound_call_recording_format": "wav",
      "inbound_call_recording_channels": "single"
    },
    "inbound_call_screening": "disabled"
  }
}' \
  "https://api.telnyx.com/v2/phone_numbers/jobs/update_phone_numbers"
```

## Retrieve a phone numbers job

`GET /phone_numbers/jobs/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/jobs/{id}"
```

## List phone numbers with messaging settings

`GET /phone_numbers/messaging`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/messaging"
```

## Slim List phone numbers

List phone numbers, This endpoint is a lighter version of the /phone_numbers endpoint having higher performance and rate limit.

`GET /phone_numbers/slim`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/slim?sort=connection_name"
```

## List phone numbers with voice settings

`GET /phone_numbers/voice`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/voice?sort=connection_name"
```

## Retrieve a phone number

`GET /phone_numbers/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/1293384261075731499"
```

## Update a phone number

`PATCH /phone_numbers/{id}`

Optional: `address_id` (string), `billing_group_id` (string), `connection_id` (string), `customer_reference` (string), `external_pin` (string), `hd_voice_enabled` (boolean), `id` (string), `tags` (array[string])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "hd_voice_enabled": true,
  "customer_reference": "MY REF 001"
}' \
  "https://api.telnyx.com/v2/phone_numbers/1293384261075731499"
```

## Delete a phone number

`DELETE /phone_numbers/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/phone_numbers/1293384261075731499"
```

## Change the bundle status for a phone number (set to being in a bundle or remove from a bundle)

`PATCH /phone_numbers/{id}/actions/bundle_status_change` — Required: `bundle_id`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "bundle_id": "string"
}' \
  "https://api.telnyx.com/v2/phone_numbers/1293384261075731499/actions/bundle_status_change"
```

## Enable emergency for a phone number

`POST /phone_numbers/{id}/actions/enable_emergency` — Required: `emergency_enabled`, `emergency_address_id`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "emergency_enabled": true,
  "emergency_address_id": "string"
}' \
  "https://api.telnyx.com/v2/phone_numbers/1293384261075731499/actions/enable_emergency"
```

## Retrieve a phone number with messaging settings

`GET /phone_numbers/{id}/messaging`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/{id}/messaging"
```

## Update the messaging profile and/or messaging product of a phone number

`PATCH /phone_numbers/{id}/messaging`

Optional: `messaging_product` (string), `messaging_profile_id` (string), `tags` (array[string])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messaging_product": "P2P"
}' \
  "https://api.telnyx.com/v2/phone_numbers/{id}/messaging"
```

## Retrieve a phone number with voice settings

`GET /phone_numbers/{id}/voice`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/1293384261075731499/voice"
```

## Update a phone number with voice settings

`PATCH /phone_numbers/{id}/voice`

Optional: `call_forwarding` (object), `call_recording` (object), `caller_id_name_enabled` (boolean), `cnam_listing` (object), `inbound_call_screening` (enum), `media_features` (object), `tech_prefix_enabled` (boolean), `translated_number` (string), `usage_payment_method` (enum)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "call_forwarding": {
    "call_forwarding_enabled": true,
    "forwards_to": "+13035559123",
    "forwarding_type": "always"
  },
  "cnam_listing": {
    "cnam_listing_enabled": true,
    "cnam_listing_details": "example"
  },
  "media_features": {
    "rtp_auto_adjust_enabled": true,
    "accept_any_rtp_packets_enabled": true,
    "t38_fax_gateway_enabled": true
  },
  "call_recording": {
    "inbound_call_recording_enabled": true,
    "inbound_call_recording_format": "wav",
    "inbound_call_recording_channels": "single"
  }
}' \
  "https://api.telnyx.com/v2/phone_numbers/1293384261075731499/voice"
```

## List Mobile Phone Numbers

`GET /v2/mobile_phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/v2/mobile_phone_numbers"
```

## Retrieve a Mobile Phone Number

`GET /v2/mobile_phone_numbers/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/v2/mobile_phone_numbers/{id}"
```

## Update a Mobile Phone Number

`PATCH /v2/mobile_phone_numbers/{id}`

Optional: `call_forwarding` (object), `call_recording` (object), `caller_id_name_enabled` (boolean), `cnam_listing` (object), `connection_id` (['string', 'null']), `customer_reference` (['string', 'null']), `inbound` (object), `inbound_call_screening` (enum), `noise_suppression` (boolean), `outbound` (object), `tags` (array[string])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/v2/mobile_phone_numbers/{id}"
```
