---
name: telnyx-account-notifications-javascript
description: >-
  Configure notification channels and settings for account alerts and events.
  This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: account-notifications
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Notifications - JavaScript

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

## List notification channels

List notification channels.

`GET /notification_channels`

```javascript
// Automatically fetches more pages as needed.
for await (const notificationChannel of client.notificationChannels.list()) {
  console.log(notificationChannel.id);
}
```

## Create a notification channel

Create a notification channel.

`POST /notification_channels`

Optional: `channel_destination` (string), `channel_type_id` (enum), `created_at` (date-time), `id` (string), `notification_profile_id` (string), `updated_at` (date-time)

```javascript
const notificationChannel = await client.notificationChannels.create();

console.log(notificationChannel.data);
```

## Get a notification channel

Get a notification channel.

`GET /notification_channels/{id}`

```javascript
const notificationChannel = await client.notificationChannels.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationChannel.data);
```

## Update a notification channel

Update a notification channel.

`PATCH /notification_channels/{id}`

Optional: `channel_destination` (string), `channel_type_id` (enum), `created_at` (date-time), `id` (string), `notification_profile_id` (string), `updated_at` (date-time)

```javascript
const notificationChannel = await client.notificationChannels.update(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationChannel.data);
```

## Delete a notification channel

Delete a notification channel.

`DELETE /notification_channels/{id}`

```javascript
const notificationChannel = await client.notificationChannels.delete(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationChannel.data);
```

## List all Notifications Events Conditions

Returns a list of your notifications events conditions.

`GET /notification_event_conditions`

```javascript
// Automatically fetches more pages as needed.
for await (const notificationEventConditionListResponse of client.notificationEventConditions.list()) {
  console.log(notificationEventConditionListResponse.id);
}
```

## List all Notifications Events

Returns a list of your notifications events.

`GET /notification_events`

```javascript
// Automatically fetches more pages as needed.
for await (const notificationEventListResponse of client.notificationEvents.list()) {
  console.log(notificationEventListResponse.id);
}
```

## List all Notifications Profiles

Returns a list of your notifications profiles.

`GET /notification_profiles`

```javascript
// Automatically fetches more pages as needed.
for await (const notificationProfile of client.notificationProfiles.list()) {
  console.log(notificationProfile.id);
}
```

## Create a notification profile

Create a notification profile.

`POST /notification_profiles`

Optional: `created_at` (date-time), `id` (string), `name` (string), `updated_at` (date-time)

```javascript
const notificationProfile = await client.notificationProfiles.create();

console.log(notificationProfile.data);
```

## Get a notification profile

Get a notification profile.

`GET /notification_profiles/{id}`

```javascript
const notificationProfile = await client.notificationProfiles.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationProfile.data);
```

## Update a notification profile

Update a notification profile.

`PATCH /notification_profiles/{id}`

Optional: `created_at` (date-time), `id` (string), `name` (string), `updated_at` (date-time)

```javascript
const notificationProfile = await client.notificationProfiles.update(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationProfile.data);
```

## Delete a notification profile

Delete a notification profile.

`DELETE /notification_profiles/{id}`

```javascript
const notificationProfile = await client.notificationProfiles.delete(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationProfile.data);
```

## List notification settings

List notification settings.

`GET /notification_settings`

```javascript
// Automatically fetches more pages as needed.
for await (const notificationSetting of client.notificationSettings.list()) {
  console.log(notificationSetting.id);
}
```

## Add a Notification Setting

Add a notification setting.

`POST /notification_settings`

Optional: `associated_record_type` (string), `associated_record_type_value` (string), `created_at` (date-time), `id` (string), `notification_channel_id` (string), `notification_event_condition_id` (string), `notification_profile_id` (string), `parameters` (array[object]), `status` (enum), `updated_at` (date-time)

```javascript
const notificationSetting = await client.notificationSettings.create();

console.log(notificationSetting.data);
```

## Get a notification setting

Get a notification setting.

`GET /notification_settings/{id}`

```javascript
const notificationSetting = await client.notificationSettings.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationSetting.data);
```

## Delete a notification setting

Delete a notification setting.

`DELETE /notification_settings/{id}`

```javascript
const notificationSetting = await client.notificationSettings.delete(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(notificationSetting.data);
```
