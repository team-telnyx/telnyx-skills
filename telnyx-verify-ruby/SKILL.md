---
name: telnyx-verify-ruby
description: >-
  Look up phone number information (carrier, type, caller name) and verify users
  via SMS/voice OTP. Use for phone verification and data enrichment. This skill
  provides Ruby SDK examples.
metadata:
  author: telnyx
  product: verify
  language: ruby
---

# Telnyx Verify - Ruby

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

## Lookup phone number data

Returns information about the provided phone number.

`GET /number_lookup/{phone_number}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_lookup = telnyx.number_lookup.retrieve("+18665552368")

puts(number_lookup)
```

## Trigger Call verification

`POST /verifications/call` — Required: `phone_number`, `verify_profile_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

create_verification_response = telnyx.verifications.trigger_call(
  phone_number: "+13035551234",
  verify_profile_id: "12ade33a-21c0-473b-b055-b3c836e1c292"
)

puts(create_verification_response)
```

## Trigger Flash call verification

`POST /verifications/flashcall` — Required: `phone_number`, `verify_profile_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

create_verification_response = telnyx.verifications.trigger_flashcall(
  phone_number: "+13035551234",
  verify_profile_id: "12ade33a-21c0-473b-b055-b3c836e1c292"
)

puts(create_verification_response)
```

## Trigger SMS verification

`POST /verifications/sms` — Required: `phone_number`, `verify_profile_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

create_verification_response = telnyx.verifications.trigger_sms(
  phone_number: "+13035551234",
  verify_profile_id: "12ade33a-21c0-473b-b055-b3c836e1c292"
)

puts(create_verification_response)
```

## Retrieve verification

`GET /verifications/{verification_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verification = telnyx.verifications.retrieve("12ade33a-21c0-473b-b055-b3c836e1c292")

puts(verification)
```

## Verify verification code by ID

`POST /verifications/{verification_id}/actions/verify`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verify_verification_code_response = telnyx.verifications.actions.verify("12ade33a-21c0-473b-b055-b3c836e1c292")

puts(verify_verification_code_response)
```

## List verifications by phone number

`GET /verifications/by_phone_number/{phone_number}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

by_phone_numbers = telnyx.verifications.by_phone_number.list("+13035551234")

puts(by_phone_numbers)
```

## Verify verification code by phone number

`POST /verifications/by_phone_number/{phone_number}/actions/verify` — Required: `code`, `verify_profile_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verify_verification_code_response = telnyx.verifications.by_phone_number.actions.verify(
  "+13035551234",
  code: "17686",
  verify_profile_id: "12ade33a-21c0-473b-b055-b3c836e1c292"
)

puts(verify_verification_code_response)
```

## List all Verify profiles

Gets a paginated list of Verify profiles.

`GET /verify_profiles`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.verify_profiles.list

puts(page)
```

## Create a Verify profile

Creates a new Verify profile to associate verifications with.

`POST /verify_profiles` — Required: `name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verify_profile_data = telnyx.verify_profiles.create(name: "Test Profile")

puts(verify_profile_data)
```

## Retrieve Verify profile

Gets a single Verify profile.

`GET /verify_profiles/{verify_profile_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verify_profile_data = telnyx.verify_profiles.retrieve("12ade33a-21c0-473b-b055-b3c836e1c292")

puts(verify_profile_data)
```

## Update Verify profile

`PATCH /verify_profiles/{verify_profile_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verify_profile_data = telnyx.verify_profiles.update("12ade33a-21c0-473b-b055-b3c836e1c292")

puts(verify_profile_data)
```

## Delete Verify profile

`DELETE /verify_profiles/{verify_profile_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verify_profile_data = telnyx.verify_profiles.delete("12ade33a-21c0-473b-b055-b3c836e1c292")

puts(verify_profile_data)
```

## Retrieve Verify profile message templates

List all Verify profile message templates.

`GET /verify_profiles/templates`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.verify_profiles.retrieve_templates

puts(response)
```

## Create message template

Create a new Verify profile message template.

`POST /verify_profiles/templates` — Required: `text`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

message_template = telnyx.verify_profiles.create_template(text: "Your {{app_name}} verification code is: {{code}}.")

puts(message_template)
```

## Update message template

Update an existing Verify profile message template.

`PATCH /verify_profiles/templates/{template_id}` — Required: `text`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

message_template = telnyx.verify_profiles.update_template(
  "12ade33a-21c0-473b-b055-b3c836e1c292",
  text: "Your {{app_name}} verification code is: {{code}}."
)

puts(message_template)
```
