---
name: telnyx-account-notifications-python
description: >-
  Configure notification channels and settings for account alerts and events.
  This skill provides Python SDK examples.
metadata:
  author: telnyx
  product: account-notifications
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Notifications - Python

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

## List notification channels

List notification channels.

`GET /notification_channels`

```python
page = client.notification_channels.list()
page = page.data[0]
print(page.id)
```

## Create a notification channel

Create a notification channel.

`POST /notification_channels`

Optional: `channel_destination` (string), `channel_type_id` (enum), `created_at` (date-time), `id` (string), `notification_profile_id` (string), `updated_at` (date-time)

```python
notification_channel = client.notification_channels.create()
print(notification_channel.data)
```

## Get a notification channel

Get a notification channel.

`GET /notification_channels/{id}`

```python
notification_channel = client.notification_channels.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_channel.data)
```

## Update a notification channel

Update a notification channel.

`PATCH /notification_channels/{id}`

Optional: `channel_destination` (string), `channel_type_id` (enum), `created_at` (date-time), `id` (string), `notification_profile_id` (string), `updated_at` (date-time)

```python
notification_channel = client.notification_channels.update(
    notification_channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_channel.data)
```

## Delete a notification channel

Delete a notification channel.

`DELETE /notification_channels/{id}`

```python
notification_channel = client.notification_channels.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_channel.data)
```

## List all Notifications Events Conditions

Returns a list of your notifications events conditions.

`GET /notification_event_conditions`

```python
page = client.notification_event_conditions.list()
page = page.data[0]
print(page.id)
```

## List all Notifications Events

Returns a list of your notifications events.

`GET /notification_events`

```python
page = client.notification_events.list()
page = page.data[0]
print(page.id)
```

## List all Notifications Profiles

Returns a list of your notifications profiles.

`GET /notification_profiles`

```python
page = client.notification_profiles.list()
page = page.data[0]
print(page.id)
```

## Create a notification profile

Create a notification profile.

`POST /notification_profiles`

Optional: `created_at` (date-time), `id` (string), `name` (string), `updated_at` (date-time)

```python
notification_profile = client.notification_profiles.create()
print(notification_profile.data)
```

## Get a notification profile

Get a notification profile.

`GET /notification_profiles/{id}`

```python
notification_profile = client.notification_profiles.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_profile.data)
```

## Update a notification profile

Update a notification profile.

`PATCH /notification_profiles/{id}`

Optional: `created_at` (date-time), `id` (string), `name` (string), `updated_at` (date-time)

```python
notification_profile = client.notification_profiles.update(
    notification_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_profile.data)
```

## Delete a notification profile

Delete a notification profile.

`DELETE /notification_profiles/{id}`

```python
notification_profile = client.notification_profiles.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_profile.data)
```

## List notification settings

List notification settings.

`GET /notification_settings`

```python
page = client.notification_settings.list()
page = page.data[0]
print(page.id)
```

## Add a Notification Setting

Add a notification setting.

`POST /notification_settings`

Optional: `associated_record_type` (string), `associated_record_type_value` (string), `created_at` (date-time), `id` (string), `notification_channel_id` (string), `notification_event_condition_id` (string), `notification_profile_id` (string), `parameters` (array[object]), `status` (enum), `updated_at` (date-time)

```python
notification_setting = client.notification_settings.create()
print(notification_setting.data)
```

## Get a notification setting

Get a notification setting.

`GET /notification_settings/{id}`

```python
notification_setting = client.notification_settings.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_setting.data)
```

## Delete a notification setting

Delete a notification setting.

`DELETE /notification_settings/{id}`

```python
notification_setting = client.notification_settings.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(notification_setting.data)
```
