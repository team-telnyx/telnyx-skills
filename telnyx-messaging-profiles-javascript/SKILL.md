---
name: telnyx-messaging-profiles-javascript
description: >-
  Create and manage messaging profiles with number pools, sticky sender, and
  geomatch features. Configure short codes for high-volume messaging. This skill
  provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: messaging-profiles
  language: javascript
---

# Telnyx Messaging Profiles - JavaScript

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

## List messaging profiles

`GET /messaging_profiles`

```javascript
// Automatically fetches more pages as needed.
for await (const messagingProfile of client.messagingProfiles.list()) {
  console.log(messagingProfile.id);
}
```

## Create a messaging profile

`POST /messaging_profiles` — Required: `name`, `whitelisted_destinations`

```javascript
const messagingProfile = await client.messagingProfiles.create({
  name: 'My name',
  whitelisted_destinations: ['US'],
});

console.log(messagingProfile.data);
```

## Retrieve a messaging profile

`GET /messaging_profiles/{id}`

```javascript
const messagingProfile = await client.messagingProfiles.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(messagingProfile.data);
```

## Update a messaging profile

`PATCH /messaging_profiles/{id}`

```javascript
const messagingProfile = await client.messagingProfiles.update(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(messagingProfile.data);
```

## Delete a messaging profile

`DELETE /messaging_profiles/{id}`

```javascript
const messagingProfile = await client.messagingProfiles.delete(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(messagingProfile.data);
```

## List phone numbers associated with a messaging profile

`GET /messaging_profiles/{id}/phone_numbers`

```javascript
// Automatically fetches more pages as needed.
for await (const phoneNumberWithMessagingSettings of client.messagingProfiles.listPhoneNumbers(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(phoneNumberWithMessagingSettings.id);
}
```

## List short codes associated with a messaging profile

`GET /messaging_profiles/{id}/short_codes`

```javascript
// Automatically fetches more pages as needed.
for await (const shortCode of client.messagingProfiles.listShortCodes(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(shortCode.messaging_profile_id);
}
```

## List Auto-Response Settings

`GET /messaging_profiles/{profile_id}/autoresp_configs`

```javascript
const autorespConfigs = await client.messagingProfiles.autorespConfigs.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(autorespConfigs.data);
```

## Create auto-response setting

`POST /messaging_profiles/{profile_id}/autoresp_configs` — Required: `op`, `keywords`, `country_code`

```javascript
const autoRespConfigResponse = await client.messagingProfiles.autorespConfigs.create('profile_id', {
  country_code: 'US',
  keywords: ['keyword1', 'keyword2'],
  op: 'start',
});

console.log(autoRespConfigResponse.data);
```

## Get Auto-Response Setting

`GET /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}`

```javascript
const autoRespConfigResponse = await client.messagingProfiles.autorespConfigs.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { profile_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(autoRespConfigResponse.data);
```

## Update Auto-Response Setting

`PUT /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}` — Required: `op`, `keywords`, `country_code`

```javascript
const autoRespConfigResponse = await client.messagingProfiles.autorespConfigs.update(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    profile_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
    country_code: 'US',
    keywords: ['keyword1', 'keyword2'],
    op: 'start',
  },
);

console.log(autoRespConfigResponse.data);
```

## Delete Auto-Response Setting

`DELETE /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}`

```javascript
const autorespConfig = await client.messagingProfiles.autorespConfigs.delete(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { profile_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(autorespConfig);
```

## List short codes

`GET /short_codes`

```javascript
// Automatically fetches more pages as needed.
for await (const shortCode of client.shortCodes.list()) {
  console.log(shortCode.messaging_profile_id);
}
```

## Retrieve a short code

`GET /short_codes/{id}`

```javascript
const shortCode = await client.shortCodes.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(shortCode.data);
```

## Update short code

Update the settings for a specific short code.

`PATCH /short_codes/{id}` — Required: `messaging_profile_id`

```javascript
const shortCode = await client.shortCodes.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  messaging_profile_id: 'abc85f64-5717-4562-b3fc-2c9600000000',
});

console.log(shortCode.data);
```
