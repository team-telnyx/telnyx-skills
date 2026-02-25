---
name: telnyx-messaging-python
description: >-
  Send and receive SMS/MMS messages, manage messaging-enabled phone numbers, and
  handle opt-outs. Use when building messaging applications, implementing 2FA,
  or sending notifications. This skill provides Python SDK examples.
metadata:
  author: telnyx
  product: messaging
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Messaging - Python

## Installation

```bash
pip install telnyx
```

## Setup

```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),  # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Send a message

Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages` — Required: `to`

Optional: `auto_detect` (boolean), `encoding` (enum), `from` (string), `media_urls` (array[string]), `messaging_profile_id` (string), `send_at` (date-time), `subject` (string), `text` (string), `type` (enum), `use_profile_webhooks` (boolean), `webhook_failover_url` (url), `webhook_url` (url)

```python
response = client.messages.send(
    to="+18445550001",
)
print(response.data)
```

## Retrieve a message

Note: This API endpoint can only retrieve messages that are no older than 10 days since their creation.

`GET /messages/{id}`

```python
message = client.messages.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(message.data)
```

## Cancel a scheduled message

Cancel a scheduled message that has not yet been sent.

`DELETE /messages/{id}`

```python
response = client.messages.cancel_scheduled(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.id)
```

## Send a Whatsapp message

`POST /messages/whatsapp` — Required: `from`, `to`, `whatsapp_message`

Optional: `type` (enum), `webhook_url` (url)

```python
response = client.messages.send_whatsapp(
    from_="+13125551234",
    to="+13125551234",
    whatsapp_message={},
)
print(response.data)
```

## Send a group MMS message

`POST /messages/group_mms` — Required: `from`, `to`

Optional: `media_urls` (array[string]), `subject` (string), `text` (string), `use_profile_webhooks` (boolean), `webhook_failover_url` (url), `webhook_url` (url)

```python
response = client.messages.send_group_mms(
    from_="+13125551234",
    to=["+18655551234", "+14155551234"],
)
print(response.data)
```

## Send a long code message

`POST /messages/long_code` — Required: `from`, `to`

Optional: `auto_detect` (boolean), `encoding` (enum), `media_urls` (array[string]), `subject` (string), `text` (string), `type` (enum), `use_profile_webhooks` (boolean), `webhook_failover_url` (url), `webhook_url` (url)

```python
response = client.messages.send_long_code(
    from_="+18445550001",
    to="+13125550002",
)
print(response.data)
```

## Send a message using number pool

`POST /messages/number_pool` — Required: `to`, `messaging_profile_id`

Optional: `auto_detect` (boolean), `encoding` (enum), `media_urls` (array[string]), `subject` (string), `text` (string), `type` (enum), `use_profile_webhooks` (boolean), `webhook_failover_url` (url), `webhook_url` (url)

```python
response = client.messages.send_number_pool(
    messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
    to="+13125550002",
)
print(response.data)
```

## Schedule a message

Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages/schedule` — Required: `to`

Optional: `auto_detect` (boolean), `from` (string), `media_urls` (array[string]), `messaging_profile_id` (string), `send_at` (date-time), `subject` (string), `text` (string), `type` (enum), `use_profile_webhooks` (boolean), `webhook_failover_url` (url), `webhook_url` (url)

```python
response = client.messages.schedule(
    to="+18445550001",
)
print(response.data)
```

## Send a short code message

`POST /messages/short_code` — Required: `from`, `to`

Optional: `auto_detect` (boolean), `encoding` (enum), `media_urls` (array[string]), `subject` (string), `text` (string), `type` (enum), `use_profile_webhooks` (boolean), `webhook_failover_url` (url), `webhook_url` (url)

```python
response = client.messages.send_short_code(
    from_="+18445550001",
    to="+18445550001",
)
print(response.data)
```

## List opt-outs

Retrieve a list of opt-out blocks.

`GET /messaging_optouts`

```python
page = client.messaging_optouts.list()
page = page.data[0]
print(page.messaging_profile_id)
```

## Retrieve a phone number with messaging settings

`GET /phone_numbers/{id}/messaging`

```python
messaging = client.phone_numbers.messaging.retrieve(
    "id",
)
print(messaging.data)
```

## Update the messaging profile and/or messaging product of a phone number

`PATCH /phone_numbers/{id}/messaging`

Optional: `messaging_product` (string), `messaging_profile_id` (string), `tags` (array[string])

```python
messaging = client.phone_numbers.messaging.update(
    id="id",
)
print(messaging.data)
```

## List phone numbers with messaging settings

`GET /phone_numbers/messaging`

```python
page = client.phone_numbers.messaging.list()
page = page.data[0]
print(page.id)
```

## Retrieve a mobile phone number with messaging settings

`GET /mobile_phone_numbers/{id}/messaging`

```python
messaging = client.mobile_phone_numbers.messaging.retrieve(
    "id",
)
print(messaging.data)
```

## List mobile phone numbers with messaging settings

`GET /mobile_phone_numbers/messaging`

```python
page = client.mobile_phone_numbers.messaging.list()
page = page.data[0]
print(page.id)
```

## Bulk update phone number profiles

`POST /messaging_numbers/bulk_updates` — Required: `messaging_profile_id`, `numbers`

Optional: `assign_only` (boolean)

```python
messaging_numbers_bulk_update = client.messaging_numbers_bulk_updates.create(
    messaging_profile_id="00000000-0000-0000-0000-000000000000",
    numbers=["+18880000000", "+18880000001", "+18880000002"],
)
print(messaging_numbers_bulk_update.data)
```

## Retrieve bulk update status

`GET /messaging_numbers/bulk_updates/{order_id}`

```python
messaging_numbers_bulk_update = client.messaging_numbers_bulk_updates.retrieve(
    "order_id",
)
print(messaging_numbers_bulk_update.data)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `deliveryUpdate` | Delivery Update |
| `inboundMessage` | Inbound Message |
| `replacedLinkClick` | Replaced Link Click |

### Webhook payload fields

**`deliveryUpdate`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.occurred_at` | date-time | ISO 8601 formatted date indicating when the resource was created. |
| `data.payload.record_type` | enum | Identifies the type of the resource. |
| `data.payload.direction` | enum | The direction of the message. |
| `data.payload.id` | uuid | Identifies the type of resource. |
| `data.payload.type` | enum | The type of message. |
| `data.payload.messaging_profile_id` | string | Unique identifier for a messaging profile. |
| `data.payload.organization_id` | uuid | The id of the organization the messaging profile belongs to. |
| `data.payload.to` | array[object] |  |
| `data.payload.cc` | array[object] |  |
| `data.payload.text` | string | Message body (i.e., content) as a non-empty string. |
| `data.payload.subject` | ['string', 'null'] | Subject of multimedia message |
| `data.payload.media` | array[object] |  |
| `data.payload.webhook_url` | url | The URL where webhooks related to this message will be sent. |
| `data.payload.webhook_failover_url` | url | The failover URL where webhooks related to this message will be sent if sending to the primary URL fails. |
| `data.payload.encoding` | string | Encoding scheme used for the message body. |
| `data.payload.parts` | integer | Number of parts into which the message's body must be split. |
| `data.payload.tags` | array[string] | Tags associated with the resource. |
| `data.payload.cost` | ['object', 'null'] |  |
| `data.payload.cost_breakdown` | ['object', 'null'] | Detailed breakdown of the message cost components. |
| `data.payload.tcr_campaign_id` | ['string', 'null'] | The Campaign Registry (TCR) campaign ID associated with the message. |
| `data.payload.tcr_campaign_billable` | boolean | Indicates whether the TCR campaign is billable. |
| `data.payload.tcr_campaign_registered` | ['string', 'null'] | The registration status of the TCR campaign. |
| `data.payload.received_at` | date-time | ISO 8601 formatted date indicating when the message request was received. |
| `data.payload.sent_at` | date-time | ISO 8601 formatted date indicating when the message was sent. |
| `data.payload.completed_at` | date-time | ISO 8601 formatted date indicating when the message was finalized. |
| `data.payload.valid_until` | date-time | Message must be out of the queue by this time or else it will be discarded and marked as 'sending_failed'. |
| `data.payload.errors` | array[object] | These errors may point at addressees when referring to unsuccessful/unconfirmed delivery statuses. |
| `data.payload.smart_encoding_applied` | boolean | Indicates whether smart encoding was applied to this message. |
| `meta.attempt` | integer | Number of attempts to deliver the webhook event. |
| `meta.delivered_to` | url | The webhook URL the event was delivered to. |

**`inboundMessage`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.occurred_at` | date-time | ISO 8601 formatted date indicating when the resource was created. |
| `data.payload.record_type` | enum | Identifies the type of the resource. |
| `data.payload.direction` | enum | The direction of the message. |
| `data.payload.id` | uuid | Identifies the type of resource. |
| `data.payload.type` | enum | The type of message. |
| `data.payload.messaging_profile_id` | string | Unique identifier for a messaging profile. |
| `data.payload.organization_id` | string | Unique identifier for a messaging profile. |
| `data.payload.to` | array[object] |  |
| `data.payload.cc` | array[object] |  |
| `data.payload.text` | string | Message body (i.e., content) as a non-empty string. |
| `data.payload.subject` | ['string', 'null'] | Message subject. |
| `data.payload.media` | array[object] |  |
| `data.payload.webhook_url` | url | The URL where webhooks related to this message will be sent. |
| `data.payload.webhook_failover_url` | url | The failover URL where webhooks related to this message will be sent if sending to the primary URL fails. |
| `data.payload.encoding` | string | Encoding scheme used for the message body. |
| `data.payload.parts` | integer | Number of parts into which the message's body must be split. |
| `data.payload.tags` | array[string] | Tags associated with the resource. |
| `data.payload.cost` | ['object', 'null'] |  |
| `data.payload.cost_breakdown` | ['object', 'null'] | Detailed breakdown of the message cost components. |
| `data.payload.tcr_campaign_id` | ['string', 'null'] | The Campaign Registry (TCR) campaign ID associated with the message. |
| `data.payload.tcr_campaign_billable` | boolean | Indicates whether the TCR campaign is billable. |
| `data.payload.tcr_campaign_registered` | ['string', 'null'] | The registration status of the TCR campaign. |
| `data.payload.received_at` | date-time | ISO 8601 formatted date indicating when the message request was received. |
| `data.payload.sent_at` | date-time | Not used for inbound messages. |
| `data.payload.completed_at` | date-time | Not used for inbound messages. |
| `data.payload.valid_until` | date-time | Not used for inbound messages. |
| `data.payload.errors` | array[object] | These errors may point at addressees when referring to unsuccessful/unconfirmed delivery statuses. |

**`replacedLinkClick`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | string | Identifies the type of the resource. |
| `data.url` | string | The original link that was sent in the message. |
| `data.to` | string | Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short code). |
| `data.message_id` | uuid | The message ID associated with the clicked link. |
| `data.time_clicked` | date-time | ISO 8601 formatted date indicating when the message request was received. |
