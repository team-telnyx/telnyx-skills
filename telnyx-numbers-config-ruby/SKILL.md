---
name: telnyx-numbers-config-ruby
description: >-
  Configure phone number settings including caller ID, call forwarding,
  messaging enablement, and connection assignments. This skill provides Ruby SDK
  examples.
metadata:
  author: telnyx
  product: numbers-config
  language: ruby
---

# Telnyx Numbers Config - Ruby

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

## Lists the phone number blocks jobs

`GET /phone_number_blocks/jobs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_number_blocks.jobs.list

puts(page)
```

## Retrieves a phone number blocks job

`GET /phone_number_blocks/jobs/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

job = telnyx.phone_number_blocks.jobs.retrieve("id")

puts(job)
```

## Deletes all numbers associated with a phone number block

Creates a new background job to delete all the phone numbers associated with the given block.

`POST /phone_number_blocks/jobs/delete_phone_number_block` — Required: `phone_number_block_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_number_blocks.jobs.delete_phone_number_block(
  phone_number_block_id: "f3946371-7199-4261-9c3d-81a0d7935146"
)

puts(response)
```

## List phone numbers

`GET /phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_numbers.list

puts(page)
```

## Retrieve a phone number

`GET /phone_numbers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

phone_number = telnyx.phone_numbers.retrieve("1293384261075731499")

puts(phone_number)
```

## Update a phone number

`PATCH /phone_numbers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

phone_number = telnyx.phone_numbers.update("1293384261075731499")

puts(phone_number)
```

## Delete a phone number

`DELETE /phone_numbers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

phone_number = telnyx.phone_numbers.delete("1293384261075731499")

puts(phone_number)
```

## Change the bundle status for a phone number (set to being in a bundle or remove from a bundle)

`PATCH /phone_numbers/{id}/actions/bundle_status_change` — Required: `bundle_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_numbers.actions.change_bundle_status(
  "1293384261075731499",
  bundle_id: "5194d8fc-87e6-4188-baa9-1c434bbe861b"
)

puts(response)
```

## Enable emergency for a phone number

`POST /phone_numbers/{id}/actions/enable_emergency` — Required: `emergency_enabled`, `emergency_address_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_numbers.actions.enable_emergency(
  "1293384261075731499",
  emergency_address_id: "53829456729313",
  emergency_enabled: true
)

puts(response)
```

## Retrieve a phone number with voice settings

`GET /phone_numbers/{id}/voice`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

voice = telnyx.phone_numbers.voice.retrieve("1293384261075731499")

puts(voice)
```

## Update a phone number with voice settings

`PATCH /phone_numbers/{id}/voice`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

voice = telnyx.phone_numbers.voice.update("1293384261075731499")

puts(voice)
```

## Verify ownership of phone numbers

Verifies ownership of the provided phone numbers and returns a mapping of numbers to their IDs, plus a list of numbers not found in the account.

`POST /phone_numbers/actions/verify_ownership` — Required: `phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_numbers.actions.verify_ownership(phone_numbers: ["+15551234567"])

puts(response)
```

## List CSV downloads

`GET /phone_numbers/csv_downloads`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_numbers.csv_downloads.list

puts(page)
```

## Create a CSV download

`POST /phone_numbers/csv_downloads`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

csv_download = telnyx.phone_numbers.csv_downloads.create

puts(csv_download)
```

## Retrieve a CSV download

`GET /phone_numbers/csv_downloads/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

csv_download = telnyx.phone_numbers.csv_downloads.retrieve("id")

puts(csv_download)
```

## Lists the phone numbers jobs

`GET /phone_numbers/jobs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_numbers.jobs.list

puts(page)
```

## Retrieve a phone numbers job

`GET /phone_numbers/jobs/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

job = telnyx.phone_numbers.jobs.retrieve("id")

puts(job)
```

## Delete a batch of numbers

Creates a new background job to delete a batch of numbers.

`POST /phone_numbers/jobs/delete_phone_numbers` — Required: `phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_numbers.jobs.delete_batch(phone_numbers: ["+19705555098", "+19715555098", "32873127836"])

puts(response)
```

## Update the emergency settings from a batch of numbers

Creates a background job to update the emergency settings of a collection of phone numbers.

`POST /phone_numbers/jobs/update_emergency_settings` — Required: `emergency_enabled`, `phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_numbers.jobs.update_emergency_settings_batch(
  emergency_enabled: true,
  phone_numbers: ["+19705555098", "+19715555098", "32873127836"]
)

puts(response)
```

## Update a batch of numbers

Creates a new background job to update a batch of numbers.

`POST /phone_numbers/jobs/update_phone_numbers` — Required: `phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.phone_numbers.jobs.update_batch(phone_numbers: ["1583466971586889004", "+13127367254"])

puts(response)
```

## Retrieve regulatory requirements for a list of phone numbers

`GET /phone_numbers/regulatory_requirements`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

phone_numbers_regulatory_requirement = telnyx.phone_numbers_regulatory_requirements.retrieve

puts(phone_numbers_regulatory_requirement)
```

## Slim List phone numbers

List phone numbers, This endpoint is a lighter version of the /phone_numbers endpoint having higher performance and rate limit.

`GET /phone_numbers/slim`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_numbers.slim_list

puts(page)
```

## List phone numbers with voice settings

`GET /phone_numbers/voice`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.phone_numbers.voice.list

puts(page)
```

## List Mobile Phone Numbers

`GET /v2/mobile_phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.mobile_phone_numbers.list

puts(page)
```

## Retrieve a Mobile Phone Number

`GET /v2/mobile_phone_numbers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

mobile_phone_number = telnyx.mobile_phone_numbers.retrieve("id")

puts(mobile_phone_number)
```

## Update a Mobile Phone Number

`PATCH /v2/mobile_phone_numbers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

mobile_phone_number = telnyx.mobile_phone_numbers.update("id")

puts(mobile_phone_number)
```
