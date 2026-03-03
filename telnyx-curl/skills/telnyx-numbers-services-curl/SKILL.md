---
name: telnyx-numbers-services-curl
description: >-
  Configure voicemail, voice channels, and emergency (E911) services for your
  phone numbers. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: numbers-services
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers Services - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List your voice channels for non-US zones

Returns the non-US voice channels for your account.

`GET /channel_zones`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/channel_zones"
```

## Update voice channels for non-US Zones

Update the number of Voice Channels for the Non-US Zones.

`PUT /channel_zones/{channel_zone_id}` — Required: `channels`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "channels": 0
}' \
  "https://api.telnyx.com/v2/channel_zones/{channel_zone_id}"
```

## List dynamic emergency addresses

Returns the dynamic emergency addresses according to filters

`GET /dynamic_emergency_addresses`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/dynamic_emergency_addresses"
```

## Create a dynamic emergency address.

Creates a dynamic emergency address.

`POST /dynamic_emergency_addresses` — Required: `house_number`, `street_name`, `locality`, `administrative_area`, `postal_code`, `country_code`

Optional: `created_at` (string), `extended_address` (string), `house_suffix` (string), `id` (string), `record_type` (string), `sip_geolocation_id` (string), `status` (enum), `street_post_directional` (string), `street_pre_directional` (string), `street_suffix` (string), `updated_at` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f1",
  "record_type": "dynamic_emergency_address",
  "sip_geolocation_id": "XYZ123",
  "status": "pending",
  "house_number": "600",
  "street_name": "Congress",
  "street_suffix": "St",
  "locality": "Austin",
  "administrative_area": "TX",
  "postal_code": "78701",
  "country_code": "US",
  "created_at": "2018-02-02T22:25:27.521Z",
  "updated_at": "2018-02-02T22:25:27.521Z"
}' \
  "https://api.telnyx.com/v2/dynamic_emergency_addresses"
```

## Get a dynamic emergency address

Returns the dynamic emergency address based on the ID provided

`GET /dynamic_emergency_addresses/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/dynamic_emergency_addresses/{id}"
```

## Delete a dynamic emergency address

Deletes the dynamic emergency address based on the ID provided

`DELETE /dynamic_emergency_addresses/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/dynamic_emergency_addresses/{id}"
```

## List dynamic emergency endpoints

Returns the dynamic emergency endpoints according to filters

`GET /dynamic_emergency_endpoints`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/dynamic_emergency_endpoints"
```

## Create a dynamic emergency endpoint.

Creates a dynamic emergency endpoints.

`POST /dynamic_emergency_endpoints` — Required: `dynamic_emergency_address_id`, `callback_number`, `caller_name`

Optional: `created_at` (string), `id` (string), `record_type` (string), `sip_from_id` (string), `status` (enum), `updated_at` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
  "record_type": "dynamic_emergency_endpoint",
  "dynamic_emergency_address_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
  "status": "pending",
  "sip_from_id": "FXDFWEDF",
  "callback_number": "+13125550000",
  "caller_name": "Jane Doe Desk Phone",
  "created_at": "2018-02-02T22:25:27.521Z",
  "updated_at": "2018-02-02T22:25:27.521Z"
}' \
  "https://api.telnyx.com/v2/dynamic_emergency_endpoints"
```

## Get a dynamic emergency endpoint

Returns the dynamic emergency endpoint based on the ID provided

`GET /dynamic_emergency_endpoints/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/dynamic_emergency_endpoints/{id}"
```

## Delete a dynamic emergency endpoint

Deletes the dynamic emergency endpoint based on the ID provided

`DELETE /dynamic_emergency_endpoints/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/dynamic_emergency_endpoints/{id}"
```

## List your voice channels for US Zone

Returns the US Zone voice channels for your account.

`GET /inbound_channels`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/inbound_channels"
```

## Update voice channels for US Zone

Update the number of Voice Channels for the US Zone.

`PATCH /inbound_channels` — Required: `channels`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "channels": 7
}' \
  "https://api.telnyx.com/v2/inbound_channels"
```

## List All Numbers using Channel Billing

Retrieve a list of all phone numbers using Channel Billing, grouped by Zone.

`GET /list`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/list"
```

## List Numbers using Channel Billing for a specific Zone

Retrieve a list of phone numbers using Channel Billing for a specific Zone.

`GET /list/{channel_zone_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/list/{channel_zone_id}"
```

## Get voicemail

Returns the voicemail settings for a phone number

`GET /phone_numbers/{phone_number_id}/voicemail`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/{phone_number_id}/voicemail"
```

## Create voicemail

Create voicemail settings for a phone number

`POST /phone_numbers/{phone_number_id}/voicemail`

Optional: `enabled` (boolean), `pin` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "1234",
  "enabled": true
}' \
  "https://api.telnyx.com/v2/phone_numbers/{phone_number_id}/voicemail"
```

## Update voicemail

Update voicemail settings for a phone number

`PATCH /phone_numbers/{phone_number_id}/voicemail`

Optional: `enabled` (boolean), `pin` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "1234",
  "enabled": true
}' \
  "https://api.telnyx.com/v2/phone_numbers/{phone_number_id}/voicemail"
```
