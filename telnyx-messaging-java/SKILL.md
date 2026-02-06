---
name: telnyx-messaging-java
description: >-
  Send and receive SMS/MMS messages, manage messaging-enabled phone numbers, and
  handle opt-outs. Use when building messaging applications, implementing 2FA,
  or sending notifications. This skill provides Java SDK examples.
metadata:
  author: telnyx
  product: messaging
  language: java
---

# Telnyx Messaging - Java

## Installation

```bash
// Add to pom.xml or build.gradle - see https://github.com/team-telnyx/telnyx-java
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## Send a message

Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages` — Required: `to`

```java
import com.telnyx.sdk.models.messages.MessageSendParams;
import com.telnyx.sdk.models.messages.MessageSendResponse;

MessageSendParams params = MessageSendParams.builder()
    .to("+18445550001")
    .build();
MessageSendResponse response = client.messages().send(params);
```

## Retrieve a message

Note: This API endpoint can only retrieve messages that are no older than 10 days since their creation.

`GET /messages/{id}`

```java
import com.telnyx.sdk.models.messages.MessageRetrieveParams;
import com.telnyx.sdk.models.messages.MessageRetrieveResponse;

MessageRetrieveResponse message = client.messages().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Cancel a scheduled message

Cancel a scheduled message that has not yet been sent.

`DELETE /messages/{id}`

```java
import com.telnyx.sdk.models.messages.MessageCancelScheduledParams;
import com.telnyx.sdk.models.messages.MessageCancelScheduledResponse;

MessageCancelScheduledResponse response = client.messages().cancelScheduled("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Send a Whatsapp message

`POST /messages/whatsapp` — Required: `from`, `to`, `whatsapp_message`

```java
import com.telnyx.sdk.models.messages.MessageSendWhatsappParams;
import com.telnyx.sdk.models.messages.MessageSendWhatsappResponse;

MessageSendWhatsappParams params = MessageSendWhatsappParams.builder()
    .from("+13125551234")
    .to("+13125551234")
    .whatsappMessage(MessageSendWhatsappParams.WhatsappMessage.builder().build())
    .build();
MessageSendWhatsappResponse response = client.messages().sendWhatsapp(params);
```

## Send a group MMS message

`POST /messages/group_mms` — Required: `from`, `to`

```java
import com.telnyx.sdk.models.messages.MessageSendGroupMmsParams;
import com.telnyx.sdk.models.messages.MessageSendGroupMmsResponse;

MessageSendGroupMmsParams params = MessageSendGroupMmsParams.builder()
    .from("+13125551234")
    .addTo("+18655551234")
    .addTo("+14155551234")
    .build();
MessageSendGroupMmsResponse response = client.messages().sendGroupMms(params);
```

## Send a long code message

`POST /messages/long_code` — Required: `from`, `to`

```java
import com.telnyx.sdk.models.messages.MessageSendLongCodeParams;
import com.telnyx.sdk.models.messages.MessageSendLongCodeResponse;

MessageSendLongCodeParams params = MessageSendLongCodeParams.builder()
    .from("+18445550001")
    .to("+13125550002")
    .build();
MessageSendLongCodeResponse response = client.messages().sendLongCode(params);
```

## Send a message using number pool

`POST /messages/number_pool` — Required: `to`, `messaging_profile_id`

```java
import com.telnyx.sdk.models.messages.MessageSendNumberPoolParams;
import com.telnyx.sdk.models.messages.MessageSendNumberPoolResponse;

MessageSendNumberPoolParams params = MessageSendNumberPoolParams.builder()
    .messagingProfileId("abc85f64-5717-4562-b3fc-2c9600000000")
    .to("+13125550002")
    .build();
MessageSendNumberPoolResponse response = client.messages().sendNumberPool(params);
```

## Schedule a message

Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool.

`POST /messages/schedule` — Required: `to`

```java
import com.telnyx.sdk.models.messages.MessageScheduleParams;
import com.telnyx.sdk.models.messages.MessageScheduleResponse;

MessageScheduleParams params = MessageScheduleParams.builder()
    .to("+18445550001")
    .build();
MessageScheduleResponse response = client.messages().schedule(params);
```

## Send a short code message

`POST /messages/short_code` — Required: `from`, `to`

```java
import com.telnyx.sdk.models.messages.MessageSendShortCodeParams;
import com.telnyx.sdk.models.messages.MessageSendShortCodeResponse;

MessageSendShortCodeParams params = MessageSendShortCodeParams.builder()
    .from("+18445550001")
    .to("+18445550001")
    .build();
MessageSendShortCodeResponse response = client.messages().sendShortCode(params);
```

## List opt-outs

Retrieve a list of opt-out blocks.

`GET /messaging_optouts`

```java
import com.telnyx.sdk.models.messagingoptouts.MessagingOptoutListPage;
import com.telnyx.sdk.models.messagingoptouts.MessagingOptoutListParams;

MessagingOptoutListPage page = client.messagingOptouts().list();
```

## Retrieve a phone number with messaging settings

`GET /phone_numbers/{id}/messaging`

```java
import com.telnyx.sdk.models.phonenumbers.messaging.MessagingRetrieveParams;
import com.telnyx.sdk.models.phonenumbers.messaging.MessagingRetrieveResponse;

MessagingRetrieveResponse messaging = client.phoneNumbers().messaging().retrieve("id");
```

## Update the messaging profile and/or messaging product of a phone number

`PATCH /phone_numbers/{id}/messaging`

```java
import com.telnyx.sdk.models.phonenumbers.messaging.MessagingUpdateParams;
import com.telnyx.sdk.models.phonenumbers.messaging.MessagingUpdateResponse;

MessagingUpdateResponse messaging = client.phoneNumbers().messaging().update("id");
```

## List phone numbers with messaging settings

`GET /phone_numbers/messaging`

```java
import com.telnyx.sdk.models.phonenumbers.messaging.MessagingListPage;
import com.telnyx.sdk.models.phonenumbers.messaging.MessagingListParams;

MessagingListPage page = client.phoneNumbers().messaging().list();
```

## Retrieve a mobile phone number with messaging settings

`GET /mobile_phone_numbers/{id}/messaging`

```java
import com.telnyx.sdk.models.mobilephonenumbers.messaging.MessagingRetrieveParams;
import com.telnyx.sdk.models.mobilephonenumbers.messaging.MessagingRetrieveResponse;

MessagingRetrieveResponse messaging = client.mobilePhoneNumbers().messaging().retrieve("id");
```

## List mobile phone numbers with messaging settings

`GET /mobile_phone_numbers/messaging`

```java
import com.telnyx.sdk.models.mobilephonenumbers.messaging.MessagingListPage;
import com.telnyx.sdk.models.mobilephonenumbers.messaging.MessagingListParams;

MessagingListPage page = client.mobilePhoneNumbers().messaging().list();
```

## Bulk update phone number profiles

`POST /messaging_numbers/bulk_updates` — Required: `messaging_profile_id`, `numbers`

```java
import com.telnyx.sdk.models.messagingnumbersbulkupdates.MessagingNumbersBulkUpdateCreateParams;
import com.telnyx.sdk.models.messagingnumbersbulkupdates.MessagingNumbersBulkUpdateCreateResponse;
import java.util.List;

MessagingNumbersBulkUpdateCreateParams params = MessagingNumbersBulkUpdateCreateParams.builder()
    .messagingProfileId("00000000-0000-0000-0000-000000000000")
    .numbers(List.of(
      "+18880000000",
      "+18880000001",
      "+18880000002"
    ))
    .build();
MessagingNumbersBulkUpdateCreateResponse messagingNumbersBulkUpdate = client.messagingNumbersBulkUpdates().create(params);
```

## Retrieve bulk update status

`GET /messaging_numbers/bulk_updates/{order_id}`

```java
import com.telnyx.sdk.models.messagingnumbersbulkupdates.MessagingNumbersBulkUpdateRetrieveParams;
import com.telnyx.sdk.models.messagingnumbersbulkupdates.MessagingNumbersBulkUpdateRetrieveResponse;

MessagingNumbersBulkUpdateRetrieveResponse messagingNumbersBulkUpdate = client.messagingNumbersBulkUpdates().retrieve("order_id");
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
