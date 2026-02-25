---
name: telnyx-fax-ruby
description: >-
  Send and receive faxes programmatically. Manage fax applications and media.
  This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: fax
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Fax - Ruby

## Installation

```bash
gem install telnyx
```

## Setup

```ruby
require "telnyx"

client = Telnyx::Client.new(
  api_key: ENV["TELNYX_API_KEY"], # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## List all Fax Applications

This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response.

`GET /fax_applications`

```ruby
page = client.fax_applications.list

puts(page)
```

## Creates a Fax Application

Creates a new Fax Application based on the parameters sent in the request.

`POST /fax_applications` — Required: `application_name`, `webhook_event_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `inbound` (object), `outbound` (object), `tags` (array[string]), `webhook_event_failover_url` (uri), `webhook_timeout_secs` (['integer', 'null'])

```ruby
fax_application = client.fax_applications.create(application_name: "fax-router", webhook_event_url: "https://example.com")

puts(fax_application)
```

## Retrieve a Fax Application

Return the details of an existing Fax Application inside the 'data' attribute of the response.

`GET /fax_applications/{id}`

```ruby
fax_application = client.fax_applications.retrieve("1293384261075731499")

puts(fax_application)
```

## Update a Fax Application

Updates settings of an existing Fax Application based on the parameters of the request.

`PATCH /fax_applications/{id}` — Required: `application_name`, `webhook_event_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `fax_email_recipient` (['string', 'null']), `inbound` (object), `outbound` (object), `tags` (array[string]), `webhook_event_failover_url` (uri), `webhook_timeout_secs` (['integer', 'null'])

```ruby
fax_application = client.fax_applications.update(
  "1293384261075731499",
  application_name: "fax-router",
  webhook_event_url: "https://example.com"
)

puts(fax_application)
```

## Deletes a Fax Application

Permanently deletes a Fax Application.

`DELETE /fax_applications/{id}`

```ruby
fax_application = client.fax_applications.delete("1293384261075731499")

puts(fax_application)
```

## View a list of faxes

`GET /faxes`

```ruby
page = client.faxes.list

puts(page)
```

## Send a fax

Send a fax.

`POST /faxes` — Required: `connection_id`, `from`, `to`

Optional: `black_threshold` (integer), `client_state` (string), `from_display_name` (string), `media_name` (string), `media_url` (string), `monochrome` (boolean), `preview_format` (enum), `quality` (enum), `store_media` (boolean), `store_preview` (boolean), `t38_enabled` (boolean), `webhook_url` (string)

```ruby
fax = client.faxes.create(connection_id: "234423", from: "+13125790015", to: "+13127367276")

puts(fax)
```

## View a fax

`GET /faxes/{id}`

```ruby
fax = client.faxes.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(fax)
```

## Delete a fax

`DELETE /faxes/{id}`

```ruby
result = client.faxes.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(result)
```

## Cancel a fax

Cancel the outbound fax that is in one of the following states: `queued`, `media.processed`, `originated` or `sending`

`POST /faxes/{id}/actions/cancel`

```ruby
response = client.faxes.actions.cancel("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(response)
```

## Refresh a fax

Refreshes the inbound fax's media_url when it has expired

`POST /faxes/{id}/actions/refresh`

```ruby
response = client.faxes.actions.refresh("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(response)
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
