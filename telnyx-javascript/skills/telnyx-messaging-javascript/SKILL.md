---
name: telnyx-messaging-javascript
description: >-
  Send and receive SMS/MMS messages, manage messaging-enabled phone numbers, and
  handle opt-outs. Use when building messaging applications, implementing 2FA,
  or sending notifications. This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: messaging
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Messaging - JavaScript

## Installation

```bash
npm install telnyx
```

## Setup

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'], // This is the default and can be omitted
});
```

All examples below assume `client` is already initialized as shown above.

## Send a message

Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages` — Required: `to`

```javascript
const response = await client.messages.send({ to: '+18445550001' });

console.log(response.data);
```

## Retrieve a message

Note: This API endpoint can only retrieve messages that are no older than 10 days since their creation.

`GET /messages/{id}`

```javascript
const message = await client.messages.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(message.data);
```

## Cancel a scheduled message

Cancel a scheduled message that has not yet been sent.

`DELETE /messages/{id}`

```javascript
const response = await client.messages.cancelScheduled('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(response.id);
```

## Send a Whatsapp message

`POST /messages/whatsapp` — Required: `from`, `to`, `whatsapp_message`

```javascript
const response = await client.messages.sendWhatsapp({
  from: '+13125551234',
  to: '+13125551234',
  whatsapp_message: {},
});

console.log(response.data);
```

## Send a group MMS message

`POST /messages/group_mms` — Required: `from`, `to`

```javascript
const response = await client.messages.sendGroupMms({
  from: '+13125551234',
  to: ['+18655551234', '+14155551234'],
});

console.log(response.data);
```

## Send a long code message

`POST /messages/long_code` — Required: `from`, `to`

```javascript
const response = await client.messages.sendLongCode({ from: '+18445550001', to: '+13125550002' });

console.log(response.data);
```

## Send a message using number pool

`POST /messages/number_pool` — Required: `to`, `messaging_profile_id`

```javascript
const response = await client.messages.sendNumberPool({
  messaging_profile_id: 'abc85f64-5717-4562-b3fc-2c9600000000',
  to: '+13125550002',
});

console.log(response.data);
```

## Schedule a message

Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages/schedule` — Required: `to`

```javascript
const response = await client.messages.schedule({ to: '+18445550001' });

console.log(response.data);
```

## Send a short code message

`POST /messages/short_code` — Required: `from`, `to`

```javascript
const response = await client.messages.sendShortCode({ from: '+18445550001', to: '+18445550001' });

console.log(response.data);
```

## List opt-outs

Retrieve a list of opt-out blocks.

`GET /messaging_optouts`

```javascript
// Automatically fetches more pages as needed.
for await (const messagingOptoutListResponse of client.messagingOptouts.list()) {
  console.log(messagingOptoutListResponse.messaging_profile_id);
}
```

## Retrieve a phone number with messaging settings

`GET /phone_numbers/{id}/messaging`

```javascript
const messaging = await client.phoneNumbers.messaging.retrieve('id');

console.log(messaging.data);
```

## Update the messaging profile and/or messaging product of a phone number

`PATCH /phone_numbers/{id}/messaging`

```javascript
const messaging = await client.phoneNumbers.messaging.update('id');

console.log(messaging.data);
```

## List phone numbers with messaging settings

`GET /phone_numbers/messaging`

```javascript
// Automatically fetches more pages as needed.
for await (const phoneNumberWithMessagingSettings of client.phoneNumbers.messaging.list()) {
  console.log(phoneNumberWithMessagingSettings.id);
}
```

## Retrieve a mobile phone number with messaging settings

`GET /mobile_phone_numbers/{id}/messaging`

```javascript
const messaging = await client.mobilePhoneNumbers.messaging.retrieve('id');

console.log(messaging.data);
```

## List mobile phone numbers with messaging settings

`GET /mobile_phone_numbers/messaging`

```javascript
// Automatically fetches more pages as needed.
for await (const messagingListResponse of client.mobilePhoneNumbers.messaging.list()) {
  console.log(messagingListResponse.id);
}
```

## Bulk update phone number profiles

`POST /messaging_numbers/bulk_updates` — Required: `messaging_profile_id`, `numbers`

```javascript
const messagingNumbersBulkUpdate = await client.messagingNumbersBulkUpdates.create({
  messaging_profile_id: '00000000-0000-0000-0000-000000000000',
  numbers: ['+18880000000', '+18880000001', '+18880000002'],
});

console.log(messagingNumbersBulkUpdate.data);
```

## Retrieve bulk update status

`GET /messaging_numbers/bulk_updates/{order_id}`

```javascript
const messagingNumbersBulkUpdate = await client.messagingNumbersBulkUpdates.retrieve('order_id');

console.log(messagingNumbersBulkUpdate.data);
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
