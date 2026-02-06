---
name: telnyx-messaging-ruby
description: >-
  Send and receive SMS/MMS messages, manage messaging-enabled phone numbers, and
  handle opt-outs. Use when building messaging applications, implementing 2FA,
  or sending notifications. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: messaging
  language: ruby
---

# Telnyx Messaging - Ruby

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

## Send a message

Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages` — Required: `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.send_(to: "+18445550001")

puts(response)
```

## Retrieve a message

Note: This API endpoint can only retrieve messages that are no older than 10 days since their creation.

`GET /messages/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

message = telnyx.messages.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(message)
```

## Cancel a scheduled message

Cancel a scheduled message that has not yet been sent.

`DELETE /messages/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.cancel_scheduled("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(response)
```

## Send a Whatsapp message

`POST /messages/whatsapp` — Required: `from`, `to`, `whatsapp_message`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.send_whatsapp(from: "+13125551234", to: "+13125551234", whatsapp_message: {})

puts(response)
```

## Send a group MMS message

`POST /messages/group_mms` — Required: `from`, `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.send_group_mms(from: "+13125551234", to: ["+18655551234", "+14155551234"])

puts(response)
```

## Send a long code message

`POST /messages/long_code` — Required: `from`, `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.send_long_code(from: "+18445550001", to: "+13125550002")

puts(response)
```

## Send a message using number pool

`POST /messages/number_pool` — Required: `to`, `messaging_profile_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.send_number_pool(
  messaging_profile_id: "abc85f64-5717-4562-b3fc-2c9600000000",
  to: "+13125550002"
)

puts(response)
```

## Schedule a message

Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages/schedule` — Required: `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.schedule(to: "+18445550001")

puts(response)
```

## Send a short code message

`POST /messages/short_code` — Required: `from`, `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.messages.send_short_code(from: "+18445550001", to: "+18445550001")

puts(response)
```

## List opt-outs

Retrieve a list of opt-out blocks.

`GET /messaging_optouts`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.messaging_optouts.list

puts(page)
```

## Retrieve a phone number with messaging settings

`GET /phone_numbers/{id}/messaging`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging = telnyx.phone_numbers.messaging.retrieve("id")

puts(messaging)
```

## Update the messaging profile and/or messaging product of a phone number

`PATCH /phone_numbers/{id}/messaging`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging = telnyx.phone_numbers.messaging.update("id")

puts(messaging)
```

## List phone numbers with messaging settings

`GET /phone_numbers/messaging`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_numbers.messaging.list

puts(page)
```

## Retrieve a mobile phone number with messaging settings

`GET /mobile_phone_numbers/{id}/messaging`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging = telnyx.mobile_phone_numbers.messaging.retrieve("id")

puts(messaging)
```

## List mobile phone numbers with messaging settings

`GET /mobile_phone_numbers/messaging`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.mobile_phone_numbers.messaging.list

puts(page)
```

## Bulk update phone number profiles

`POST /messaging_numbers/bulk_updates` — Required: `messaging_profile_id`, `numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging_numbers_bulk_update = telnyx.messaging_numbers_bulk_updates.create(
  messaging_profile_id: "00000000-0000-0000-0000-000000000000",
  numbers: ["+18880000000", "+18880000001", "+18880000002"]
)

puts(messaging_numbers_bulk_update)
```

## Retrieve bulk update status

`GET /messaging_numbers/bulk_updates/{order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging_numbers_bulk_update = telnyx.messaging_numbers_bulk_updates.retrieve("order_id")

puts(messaging_numbers_bulk_update)
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
