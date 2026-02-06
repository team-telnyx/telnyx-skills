---
name: telnyx-account-notifications-ruby
description: >-
  Configure notification channels and settings for account alerts and events.
  This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: account-notifications
  language: ruby
---

# Telnyx Account Notifications - Ruby

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

## List notification channels

List notification channels.

`GET /notification_channels`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.notification_channels.list

puts(page)
```

## Create a notification channel

Create a notification channel.

`POST /notification_channels`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_channel = telnyx.notification_channels.create

puts(notification_channel)
```

## Get a notification channel

Get a notification channel.

`GET /notification_channels/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_channel = telnyx.notification_channels.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_channel)
```

## Update a notification channel

Update a notification channel.

`PATCH /notification_channels/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_channel = telnyx.notification_channels.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_channel)
```

## Delete a notification channel

Delete a notification channel.

`DELETE /notification_channels/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_channel = telnyx.notification_channels.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_channel)
```

## List all Notifications Events Conditions

Returns a list of your notifications events conditions.

`GET /notification_event_conditions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.notification_event_conditions.list

puts(page)
```

## List all Notifications Events

Returns a list of your notifications events.

`GET /notification_events`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.notification_events.list

puts(page)
```

## List all Notifications Profiles

Returns a list of your notifications profiles.

`GET /notification_profiles`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.notification_profiles.list

puts(page)
```

## Create a notification profile

Create a notification profile.

`POST /notification_profiles`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_profile = telnyx.notification_profiles.create

puts(notification_profile)
```

## Get a notification profile

Get a notification profile.

`GET /notification_profiles/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_profile = telnyx.notification_profiles.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_profile)
```

## Update a notification profile

Update a notification profile.

`PATCH /notification_profiles/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_profile = telnyx.notification_profiles.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_profile)
```

## Delete a notification profile

Delete a notification profile.

`DELETE /notification_profiles/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_profile = telnyx.notification_profiles.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_profile)
```

## List notification settings

List notification settings.

`GET /notification_settings`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.notification_settings.list

puts(page)
```

## Add a Notification Setting

Add a notification setting.

`POST /notification_settings`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_setting = telnyx.notification_settings.create

puts(notification_setting)
```

## Get a notification setting

Get a notification setting.

`GET /notification_settings/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_setting = telnyx.notification_settings.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_setting)
```

## Delete a notification setting

Delete a notification setting.

`DELETE /notification_settings/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

notification_setting = telnyx.notification_settings.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(notification_setting)
```
