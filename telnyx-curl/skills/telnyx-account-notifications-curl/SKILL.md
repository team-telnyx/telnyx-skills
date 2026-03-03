---
name: telnyx-account-notifications-curl
description: >-
  Configure notification channels and settings for account alerts and events.
  This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: account-notifications
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Notifications - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List notification channels

List notification channels.

`GET /notification_channels`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_channels"
```

## Create a notification channel

Create a notification channel.

`POST /notification_channels`

Optional: `channel_destination` (string), `channel_type_id` (enum), `created_at` (date-time), `id` (string), `notification_profile_id` (string), `updated_at` (date-time)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "notification_profile_id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "channel_destination": "+13125550000",
  "created_at": "2019-10-15T10:07:15.527Z",
  "updated_at": "2019-10-15T10:07:15.527Z"
}' \
  "https://api.telnyx.com/v2/notification_channels"
```

## Get a notification channel

Get a notification channel.

`GET /notification_channels/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_channels/{id}"
```

## Update a notification channel

Update a notification channel.

`PATCH /notification_channels/{id}`

Optional: `channel_destination` (string), `channel_type_id` (enum), `created_at` (date-time), `id` (string), `notification_profile_id` (string), `updated_at` (date-time)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "notification_profile_id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "channel_destination": "+13125550000",
  "created_at": "2019-10-15T10:07:15.527Z",
  "updated_at": "2019-10-15T10:07:15.527Z"
}' \
  "https://api.telnyx.com/v2/notification_channels/{id}"
```

## Delete a notification channel

Delete a notification channel.

`DELETE /notification_channels/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/notification_channels/{id}"
```

## List all Notifications Events Conditions

Returns a list of your notifications events conditions.

`GET /notification_event_conditions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_event_conditions"
```

## List all Notifications Events

Returns a list of your notifications events.

`GET /notification_events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_events"
```

## List all Notifications Profiles

Returns a list of your notifications profiles.

`GET /notification_profiles`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_profiles"
```

## Create a notification profile

Create a notification profile.

`POST /notification_profiles`

Optional: `created_at` (date-time), `id` (string), `name` (string), `updated_at` (date-time)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "created_at": "2019-10-15T10:07:15.527Z",
  "updated_at": "2019-10-15T10:07:15.527Z"
}' \
  "https://api.telnyx.com/v2/notification_profiles"
```

## Get a notification profile

Get a notification profile.

`GET /notification_profiles/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_profiles/{id}"
```

## Update a notification profile

Update a notification profile.

`PATCH /notification_profiles/{id}`

Optional: `created_at` (date-time), `id` (string), `name` (string), `updated_at` (date-time)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "created_at": "2019-10-15T10:07:15.527Z",
  "updated_at": "2019-10-15T10:07:15.527Z"
}' \
  "https://api.telnyx.com/v2/notification_profiles/{id}"
```

## Delete a notification profile

Delete a notification profile.

`DELETE /notification_profiles/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/notification_profiles/{id}"
```

## List notification settings

List notification settings.

`GET /notification_settings`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_settings"
```

## Add a Notification Setting

Add a notification setting.

`POST /notification_settings`

Optional: `associated_record_type` (string), `associated_record_type_value` (string), `created_at` (date-time), `id` (string), `notification_channel_id` (string), `notification_event_condition_id` (string), `notification_profile_id` (string), `parameters` (array[object]), `status` (enum), `updated_at` (date-time)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "8eb5b5f9-5893-423c-9f15-b487713d44d4",
  "notification_event_condition_id": "70c7c5cb-dce2-4124-accb-870d39dbe852",
  "notification_profile_id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "associated_record_type": "phone_number",
  "associated_record_type_value": "+13125550000",
  "status": "enable-received",
  "notification_channel_id": "12455643-3cf1-4683-ad23-1cd32f7d5e0a",
  "created_at": "2019-10-15T10:07:15.527Z",
  "updated_at": "2019-10-15T10:07:15.527Z"
}' \
  "https://api.telnyx.com/v2/notification_settings"
```

## Get a notification setting

Get a notification setting.

`GET /notification_settings/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/notification_settings/{id}"
```

## Delete a notification setting

Delete a notification setting.

`DELETE /notification_settings/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/notification_settings/{id}"
```
