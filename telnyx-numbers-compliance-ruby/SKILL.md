---
name: telnyx-numbers-compliance-ruby
description: >-
  Manage regulatory requirements, number bundles, supporting documents, and
  verified numbers for compliance. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: numbers-compliance
  language: ruby
---

# Telnyx Numbers Compliance - Ruby

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

## Retrieve Bundles

Get all allowed bundles.

`GET /bundle_pricing/billing_bundles`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.bundle_pricing.billing_bundles.list

puts(page)
```

## Get Bundle By Id

Get a single bundle by ID.

`GET /bundle_pricing/billing_bundles/{bundle_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

billing_bundle = telnyx.bundle_pricing.billing_bundles.retrieve("8661948c-a386-4385-837f-af00f40f111a")

puts(billing_bundle)
```

## Get User Bundles

Get a paginated list of user bundles.

`GET /bundle_pricing/user_bundles`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.bundle_pricing.user_bundles.list

puts(page)
```

## Create User Bundles

Creates multiple user bundles for the user.

`POST /bundle_pricing/user_bundles/bulk`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

user_bundle = telnyx.bundle_pricing.user_bundles.create

puts(user_bundle)
```

## Get Unused User Bundles

Returns all user bundles that aren't in use.

`GET /bundle_pricing/user_bundles/unused`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.bundle_pricing.user_bundles.list_unused

puts(response)
```

## Get User Bundle by Id

Retrieves a user bundle by its ID.

`GET /bundle_pricing/user_bundles/{user_bundle_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

user_bundle = telnyx.bundle_pricing.user_bundles.retrieve("ca1d2263-d1f1-43ac-ba53-248e7a4bb26a")

puts(user_bundle)
```

## Deactivate User Bundle

Deactivates a user bundle by its ID.

`DELETE /bundle_pricing/user_bundles/{user_bundle_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.bundle_pricing.user_bundles.deactivate("ca1d2263-d1f1-43ac-ba53-248e7a4bb26a")

puts(response)
```

## Get User Bundle Resources

Retrieves the resources of a user bundle by its ID.

`GET /bundle_pricing/user_bundles/{user_bundle_id}/resources`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.bundle_pricing.user_bundles.list_resources("ca1d2263-d1f1-43ac-ba53-248e7a4bb26a")

puts(response)
```

## List all document links

List all documents links ordered by created_at descending.

`GET /document_links`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.document_links.list

puts(page)
```

## List all documents

List all documents ordered by created_at descending.

`GET /documents`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.documents.list

puts(page)
```

## Upload a document

Upload a document.<br /><br />Uploaded files must be linked to a service within 30 minutes or they will be automatically deleted.

`POST /documents`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.documents.upload_json(document: {})

puts(response)
```

## Retrieve a document

Retrieve a document.

`GET /documents/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

document = telnyx.documents.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(document)
```

## Update a document

Update a document.

`PATCH /documents/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

document = telnyx.documents.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(document)
```

## Delete a document

Delete a document.<br /><br />A document can only be deleted if it's not linked to a service.

`DELETE /documents/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

document = telnyx.documents.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(document)
```

## Download a document

Download a document.

`GET /documents/{id}/download`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.documents.download("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Generate a temporary download link for a document

Generates a temporary pre-signed URL that can be used to download the document directly from the storage backend without authentication.

`GET /documents/{id}/download_link`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.documents.generate_download_link("550e8400-e29b-41d4-a716-446655440000")

puts(response)
```

## List all requirements

List all requirements with filtering, sorting, and pagination

`GET /requirements`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.requirements.list

puts(page)
```

## Retrieve a document requirement

Retrieve a document requirement record

`GET /requirements/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement = telnyx.requirements.retrieve("a9dad8d5-fdbd-49d7-aa23-39bb08a5ebaa")

puts(requirement)
```

## List all requirement types

List all requirement types ordered by created_at descending

`GET /requirement_types`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_types = telnyx.requirement_types.list

puts(requirement_types)
```

## Retrieve a requirement types

Retrieve a requirement type by id

`GET /requirement_types/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_type = telnyx.requirement_types.retrieve("a38c217a-8019-48f8-bff6-0fdd9939075b")

puts(requirement_type)
```

## Retrieve regulatory requirements

`GET /regulatory_requirements`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

regulatory_requirement = telnyx.regulatory_requirements.retrieve

puts(regulatory_requirement)
```

## List requirement groups

`GET /requirement_groups`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_groups = telnyx.requirement_groups.list

puts(requirement_groups)
```

## Create a new requirement group

`POST /requirement_groups` — Required: `country_code`, `phone_number_type`, `action`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_group = telnyx.requirement_groups.create(action: :ordering, country_code: "US", phone_number_type: :local)

puts(requirement_group)
```

## Get a single requirement group by ID

`GET /requirement_groups/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_group = telnyx.requirement_groups.retrieve("id")

puts(requirement_group)
```

## Update requirement values in requirement group

`PATCH /requirement_groups/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_group = telnyx.requirement_groups.update("id")

puts(requirement_group)
```

## Delete a requirement group by ID

`DELETE /requirement_groups/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_group = telnyx.requirement_groups.delete("id")

puts(requirement_group)
```

## Submit a Requirement Group for Approval

`POST /requirement_groups/{id}/submit_for_approval`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

requirement_group = telnyx.requirement_groups.submit_for_approval("id")

puts(requirement_group)
```

## List all Verified Numbers

Gets a paginated list of Verified Numbers.

`GET /verified_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.verified_numbers.list

puts(page)
```

## Request phone number verification

Initiates phone number verification procedure.

`POST /verified_numbers` — Required: `phone_number`, `verification_method`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verified_number = telnyx.verified_numbers.create(phone_number: "+15551234567", verification_method: :sms)

puts(verified_number)
```

## Retrieve a verified number

`GET /verified_numbers/{phone_number}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verified_number_data_wrapper = telnyx.verified_numbers.retrieve("+15551234567")

puts(verified_number_data_wrapper)
```

## Delete a verified number

`DELETE /verified_numbers/{phone_number}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verified_number_data_wrapper = telnyx.verified_numbers.delete("+15551234567")

puts(verified_number_data_wrapper)
```

## Submit verification code

`POST /verified_numbers/{phone_number}/actions/verify` — Required: `verification_code`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

verified_number_data_wrapper = telnyx.verified_numbers.actions.submit_verification_code("+15551234567", verification_code: "123456")

puts(verified_number_data_wrapper)
```
