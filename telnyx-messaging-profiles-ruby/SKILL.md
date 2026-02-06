---
name: telnyx-messaging-profiles-ruby
description: >-
  Create and manage messaging profiles with number pools, sticky sender, and
  geomatch features. Configure short codes for high-volume messaging. This skill
  provides Ruby SDK examples.
metadata:
  author: telnyx
  product: messaging-profiles
  language: ruby
---

# Telnyx Messaging Profiles - Ruby

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

## List messaging profiles

`GET /messaging_profiles`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.messaging_profiles.list

puts(page)
```

## Create a messaging profile

`POST /messaging_profiles` — Required: `name`, `whitelisted_destinations`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging_profile = telnyx.messaging_profiles.create(name: "My name", whitelisted_destinations: ["US"])

puts(messaging_profile)
```

## Retrieve a messaging profile

`GET /messaging_profiles/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging_profile = telnyx.messaging_profiles.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(messaging_profile)
```

## Update a messaging profile

`PATCH /messaging_profiles/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging_profile = telnyx.messaging_profiles.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(messaging_profile)
```

## Delete a messaging profile

`DELETE /messaging_profiles/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messaging_profile = telnyx.messaging_profiles.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(messaging_profile)
```

## List phone numbers associated with a messaging profile

`GET /messaging_profiles/{id}/phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.messaging_profiles.list_phone_numbers("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(page)
```

## List short codes associated with a messaging profile

`GET /messaging_profiles/{id}/short_codes`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.messaging_profiles.list_short_codes("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(page)
```

## List Auto-Response Settings

`GET /messaging_profiles/{profile_id}/autoresp_configs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

autoresp_configs = telnyx.messaging_profiles.autoresp_configs.list("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(autoresp_configs)
```

## Create auto-response setting

`POST /messaging_profiles/{profile_id}/autoresp_configs` — Required: `op`, `keywords`, `country_code`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

auto_resp_config_response = telnyx.messaging_profiles.autoresp_configs.create(
  "profile_id",
  country_code: "US",
  keywords: ["keyword1", "keyword2"],
  op: :start
)

puts(auto_resp_config_response)
```

## Get Auto-Response Setting

`GET /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

auto_resp_config_response = telnyx.messaging_profiles.autoresp_configs.retrieve(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  profile_id: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
)

puts(auto_resp_config_response)
```

## Update Auto-Response Setting

`PUT /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}` — Required: `op`, `keywords`, `country_code`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

auto_resp_config_response = telnyx.messaging_profiles.autoresp_configs.update(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  profile_id: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  country_code: "US",
  keywords: ["keyword1", "keyword2"],
  op: :start
)

puts(auto_resp_config_response)
```

## Delete Auto-Response Setting

`DELETE /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

autoresp_config = telnyx.messaging_profiles.autoresp_configs.delete(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  profile_id: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
)

puts(autoresp_config)
```

## List short codes

`GET /short_codes`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.short_codes.list

puts(page)
```

## Retrieve a short code

`GET /short_codes/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

short_code = telnyx.short_codes.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(short_code)
```

## Update short code

Update the settings for a specific short code.

`PATCH /short_codes/{id}` — Required: `messaging_profile_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

short_code = telnyx.short_codes.update(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  messaging_profile_id: "abc85f64-5717-4562-b3fc-2c9600000000"
)

puts(short_code)
```
