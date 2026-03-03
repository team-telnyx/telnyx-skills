---
name: telnyx-webrtc-curl
description: >-
  Manage WebRTC credentials and mobile push notification settings. Use when
  building browser-based or mobile softphone applications. This skill provides
  REST API (curl) examples.
metadata:
  author: telnyx
  product: webrtc
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Webrtc - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List mobile push credentials

`GET /mobile_push_credentials`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/mobile_push_credentials"
```

## Creates a new mobile push credential

`POST /mobile_push_credentials`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/mobile_push_credentials"
```

## Retrieves a mobile push credential

Retrieves mobile push credential based on the given `push_credential_id`

`GET /mobile_push_credentials/{push_credential_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/mobile_push_credentials/0ccc7b76-4df3-4bca-a05a-3da1ecc389f0"
```

## Deletes a mobile push credential

Deletes a mobile push credential based on the given `push_credential_id`

`DELETE /mobile_push_credentials/{push_credential_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/mobile_push_credentials/0ccc7b76-4df3-4bca-a05a-3da1ecc389f0"
```

## List all credentials

List all On-demand Credentials.

`GET /telephony_credentials`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/telephony_credentials"
```

## Create a credential

Create a credential.

`POST /telephony_credentials` — Required: `connection_id`

Optional: `expires_at` (string), `name` (string), `tag` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "tag": "some_tag",
  "connection_id": "1234567890",
  "expires_at": "2018-02-02T22:25:27.521Z"
}' \
  "https://api.telnyx.com/v2/telephony_credentials"
```

## Get a credential

Get the details of an existing On-demand Credential.

`GET /telephony_credentials/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/telephony_credentials/{id}"
```

## Update a credential

Update an existing credential.

`PATCH /telephony_credentials/{id}`

Optional: `connection_id` (string), `expires_at` (string), `name` (string), `tag` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "tag": "some_tag",
  "connection_id": "987654321",
  "expires_at": "2018-02-02T22:25:27.521Z"
}' \
  "https://api.telnyx.com/v2/telephony_credentials/{id}"
```

## Delete a credential

Delete an existing credential.

`DELETE /telephony_credentials/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/telephony_credentials/{id}"
```
