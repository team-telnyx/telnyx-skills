---
name: telnyx-fax-curl
description: >-
  Send and receive faxes programmatically. Manage fax applications and media.
  This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: fax
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Fax - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List all Fax Applications

This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response.

`GET /fax_applications`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/fax_applications?sort=application_name"
```

## Creates a Fax Application

Creates a new Fax Application based on the parameters sent in the request.

`POST /fax_applications` — Required: `application_name`, `webhook_event_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `inbound` (object), `outbound` (object), `tags` (array[string]), `webhook_event_failover_url` (uri), `webhook_timeout_secs` (['integer', 'null'])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "application_name": "call-router",
  "active": false,
  "anchorsite_override": "Amsterdam, Netherlands",
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25,
  "tags": [
    "tag1",
    "tag2"
  ]
}' \
  "https://api.telnyx.com/v2/fax_applications"
```

## Retrieve a Fax Application

Return the details of an existing Fax Application inside the 'data' attribute of the response.

`GET /fax_applications/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/fax_applications/1293384261075731499"
```

## Update a Fax Application

Updates settings of an existing Fax Application based on the parameters of the request.

`PATCH /fax_applications/{id}` — Required: `application_name`, `webhook_event_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `fax_email_recipient` (['string', 'null']), `inbound` (object), `outbound` (object), `tags` (array[string]), `webhook_event_failover_url` (uri), `webhook_timeout_secs` (['integer', 'null'])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "application_name": "call-router",
  "active": false,
  "anchorsite_override": "Amsterdam, Netherlands",
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25,
  "fax_email_recipient": "user@example.com",
  "tags": [
    "tag1",
    "tag2"
  ]
}' \
  "https://api.telnyx.com/v2/fax_applications/1293384261075731499"
```

## Deletes a Fax Application

Permanently deletes a Fax Application.

`DELETE /fax_applications/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/fax_applications/1293384261075731499"
```

## View a list of faxes

`GET /faxes`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/faxes"
```

## Send a fax

Send a fax.

`POST /faxes` — Required: `connection_id`, `from`, `to`

Optional: `black_threshold` (integer), `client_state` (string), `from_display_name` (string), `media_name` (string), `media_url` (string), `monochrome` (boolean), `preview_format` (enum), `quality` (enum), `store_media` (boolean), `store_preview` (boolean), `t38_enabled` (boolean), `webhook_url` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "connection_id=234423" \
  -F "contents=@/path/to/file" \
  -F "to=+13127367276" \
  -F "from=+13125790015" \
  -F "quality=high" \
  "https://api.telnyx.com/v2/faxes"
```

## View a fax

`GET /faxes/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/faxes/{id}"
```

## Delete a fax

`DELETE /faxes/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/faxes/{id}"
```

## Cancel a fax

Cancel the outbound fax that is in one of the following states: `queued`, `media.processed`, `originated` or `sending`

`POST /faxes/{id}/actions/cancel`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/faxes/{id}/actions/cancel"
```

## Refresh a fax

Refreshes the inbound fax's media_url when it has expired

`POST /faxes/{id}/actions/refresh`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/faxes/{id}/actions/refresh"
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `fax.delivered` | Fax Delivered |
| `fax.failed` | Fax Failed |
| `fax.media.processed` | Fax Media Processed |
| `fax.queued` | Fax Queued |
| `fax.sending.started` | Fax Sending Started |

### Webhook payload fields

**`fax.delivered`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.payload.call_duration_secs` | integer | The duration of the call in seconds. |
| `data.payload.connection_id` | string | The ID of the connection used to send the fax. |
| `data.payload.direction` | enum | The direction of the fax. |
| `data.payload.fax_id` | uuid | Identifies the fax. |
| `data.payload.original_media_url` | string | The original URL to the PDF used for the fax's media. |
| `data.payload.media_name` | string | The media_name used for the fax's media. |
| `data.payload.to` | string | The phone number, in E.164 format, the fax will be sent to or SIP URI |
| `data.payload.from` | string | The phone number, in E.164 format, the fax will be sent from. |
| `data.payload.user_id` | uuid | Identifier of the user to whom the fax belongs |
| `data.payload.page_count` | integer | Number of transferred pages |
| `data.payload.status` | enum | The status of the fax. |
| `data.payload.client_state` | string | State received from a command. |
| `meta.attempt` | integer | The delivery attempt number. |
| `meta.delivered_to` | uri | The URL the webhook was delivered to. |

**`fax.failed`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.payload.connection_id` | string | The ID of the connection used to send the fax. |
| `data.payload.direction` | enum | The direction of the fax. |
| `data.payload.fax_id` | uuid | Identifies the fax. |
| `data.payload.original_media_url` | string | The original URL to the PDF used for the fax's media. |
| `data.payload.media_name` | string | The media_name used for the fax's media. |
| `data.payload.to` | string | The phone number, in E.164 format, the fax will be sent to or SIP URI |
| `data.payload.from` | string | The phone number, in E.164 format, the fax will be sent from. |
| `data.payload.user_id` | uuid | Identifier of the user to whom the fax belongs |
| `data.payload.failure_reason` | enum | Cause of the sending failure |
| `data.payload.status` | enum | The status of the fax. |
| `data.payload.client_state` | string | State received from a command. |
| `meta.attempt` | integer | The delivery attempt number. |
| `meta.delivered_to` | uri | The URL the webhook was delivered to. |

**`fax.media.processed`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.payload.connection_id` | string | The ID of the connection used to send the fax. |
| `data.payload.direction` | enum | The direction of the fax. |
| `data.payload.fax_id` | uuid | Identifies the fax. |
| `data.payload.original_media_url` | string | The original URL to the PDF used for the fax's media. |
| `data.payload.media_name` | string | The media_name used for the fax's media. |
| `data.payload.to` | string | The phone number, in E.164 format, the fax will be sent to or SIP URI |
| `data.payload.from` | string | The phone number, in E.164 format, the fax will be sent from. |
| `data.payload.user_id` | uuid | Identifier of the user to whom the fax belongs |
| `data.payload.status` | enum | The status of the fax. |
| `data.payload.client_state` | string | State received from a command. |
| `meta.attempt` | integer | The delivery attempt number. |
| `meta.delivered_to` | uri | The URL the webhook was delivered to. |

**`fax.queued`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.payload.connection_id` | string | The ID of the connection used to send the fax. |
| `data.payload.direction` | enum | The direction of the fax. |
| `data.payload.fax_id` | uuid | Identifies the fax. |
| `data.payload.original_media_url` | string | The original URL to the PDF used for the fax's media. |
| `data.payload.media_name` | string | The media_name used for the fax's media. |
| `data.payload.to` | string | The phone number, in E.164 format, the fax will be sent to or SIP URI |
| `data.payload.from` | string | The phone number, in E.164 format, the fax will be sent from. |
| `data.payload.user_id` | uuid | Identifier of the user to whom the fax belongs |
| `data.payload.status` | enum | The status of the fax. |
| `data.payload.client_state` | string | State received from a command. |
| `meta.attempt` | integer | The delivery attempt number. |
| `meta.delivered_to` | uri | The URL the webhook was delivered to. |

**`fax.sending.started`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.payload.connection_id` | string | The ID of the connection used to send the fax. |
| `data.payload.direction` | enum | The direction of the fax. |
| `data.payload.fax_id` | uuid | Identifies the fax. |
| `data.payload.original_media_url` | string | The original URL to the PDF used for the fax's media. |
| `data.payload.media_name` | string | The media_name used for the fax's media. |
| `data.payload.to` | string | The phone number, in E.164 format, the fax will be sent to or SIP URI |
| `data.payload.from` | string | The phone number, in E.164 format, the fax will be sent from. |
| `data.payload.user_id` | uuid | Identifier of the user to whom the fax belongs |
| `data.payload.status` | enum | The status of the fax. |
| `data.payload.client_state` | string | State received from a command. |
| `meta.attempt` | integer | The delivery attempt number. |
| `meta.delivered_to` | uri | The URL the webhook was delivered to. |
