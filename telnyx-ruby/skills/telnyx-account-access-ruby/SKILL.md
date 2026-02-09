---
name: telnyx-account-access-ruby
description: >-
  Configure account addresses, authentication providers, IP access controls,
  billing groups, and integration secrets. This skill provides Ruby SDK
  examples.
metadata:
  author: telnyx
  product: account-access
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Access - Ruby

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

## List all addresses

Returns a list of your addresses.

`GET /addresses`

```ruby
page = client.addresses.list

puts(page)
```

## Creates an address

Creates an address.

`POST /addresses` — Required: `first_name`, `last_name`, `business_name`, `street_address`, `locality`, `country_code`

```ruby
address = client.addresses.create(
  business_name: "Toy-O'Kon",
  country_code: "US",
  first_name: "Alfred",
  last_name: "Foster",
  locality: "Austin",
  street_address: "600 Congress Avenue"
)

puts(address)
```

## Retrieve an address

Retrieves the details of an existing address.

`GET /addresses/{id}`

```ruby
address = client.addresses.retrieve("id")

puts(address)
```

## Deletes an address

Deletes an existing address.

`DELETE /addresses/{id}`

```ruby
address = client.addresses.delete("id")

puts(address)
```

## Accepts this address suggestion as a new emergency address for Operator Connect and finishes the uploads of the numbers associated with it to Microsoft.

`POST /addresses/{id}/actions/accept_suggestions`

```ruby
response = client.addresses.actions.accept_suggestions("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(response)
```

## Validate an address

Validates an address for emergency services.

`POST /addresses/actions/validate` — Required: `country_code`, `street_address`, `postal_code`

```ruby
response = client.addresses.actions.validate(
  country_code: "US",
  postal_code: "78701",
  street_address: "600 Congress Avenue"
)

puts(response)
```

## List all SSO authentication providers

Returns a list of your SSO authentication providers.

`GET /authentication_providers`

```ruby
page = client.authentication_providers.list

puts(page)
```

## Creates an authentication provider

Creates an authentication provider.

`POST /authentication_providers` — Required: `name`, `short_name`, `settings`

```ruby
authentication_provider = client.authentication_providers.create(
  name: "Okta",
  settings: {
    idp_cert_fingerprint: "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
    idp_entity_id: "https://myorg.myidp.com/saml/metadata",
    idp_sso_target_url: "https://myorg.myidp.com/trust/saml2/http-post/sso"
  },
  short_name: "myorg"
)

puts(authentication_provider)
```

## Retrieve an authentication provider

Retrieves the details of an existing authentication provider.

`GET /authentication_providers/{id}`

```ruby
authentication_provider = client.authentication_providers.retrieve("id")

puts(authentication_provider)
```

## Update an authentication provider

Updates settings of an existing authentication provider.

`PATCH /authentication_providers/{id}`

```ruby
authentication_provider = client.authentication_providers.update("id")

puts(authentication_provider)
```

## Deletes an authentication provider

Deletes an existing authentication provider.

`DELETE /authentication_providers/{id}`

```ruby
authentication_provider = client.authentication_providers.delete("id")

puts(authentication_provider)
```

## List all billing groups

`GET /billing_groups`

```ruby
page = client.billing_groups.list

puts(page)
```

## Create a billing group

`POST /billing_groups`

```ruby
billing_group = client.billing_groups.create

puts(billing_group)
```

## Get a billing group

`GET /billing_groups/{id}`

```ruby
billing_group = client.billing_groups.retrieve("f5586561-8ff0-4291-a0ac-84fe544797bd")

puts(billing_group)
```

## Update a billing group

`PATCH /billing_groups/{id}`

```ruby
billing_group = client.billing_groups.update("f5586561-8ff0-4291-a0ac-84fe544797bd")

puts(billing_group)
```

## Delete a billing group

`DELETE /billing_groups/{id}`

```ruby
billing_group = client.billing_groups.delete("f5586561-8ff0-4291-a0ac-84fe544797bd")

puts(billing_group)
```

## List integration secrets

Retrieve a list of all integration secrets configured by the user.

`GET /integration_secrets`

```ruby
page = client.integration_secrets.list

puts(page)
```

## Create a secret

Create a new secret with an associated identifier that can be used to securely integrate with other services.

`POST /integration_secrets` — Required: `identifier`, `type`

```ruby
integration_secret = client.integration_secrets.create(identifier: "my_secret", type: :bearer)

puts(integration_secret)
```

## Delete an integration secret

Delete an integration secret given its ID.

`DELETE /integration_secrets/{id}`

```ruby
result = client.integration_secrets.delete("id")

puts(result)
```

## List all Access IP Addresses

`GET /access_ip_address`

```ruby
page = client.access_ip_address.list

puts(page)
```

## Create new Access IP Address

`POST /access_ip_address` — Required: `ip_address`

```ruby
access_ip_address_response = client.access_ip_address.create(ip_address: "ip_address")

puts(access_ip_address_response)
```

## Retrieve an access IP address

`GET /access_ip_address/{access_ip_address_id}`

```ruby
access_ip_address_response = client.access_ip_address.retrieve("access_ip_address_id")

puts(access_ip_address_response)
```

## Delete access IP address

`DELETE /access_ip_address/{access_ip_address_id}`

```ruby
access_ip_address_response = client.access_ip_address.delete("access_ip_address_id")

puts(access_ip_address_response)
```

## List all Access IP Ranges

`GET /access_ip_ranges`

```ruby
page = client.access_ip_ranges.list

puts(page)
```

## Create new Access IP Range

`POST /access_ip_ranges` — Required: `cidr_block`

```ruby
access_ip_range = client.access_ip_ranges.create(cidr_block: "cidr_block")

puts(access_ip_range)
```

## Delete access IP ranges

`DELETE /access_ip_ranges/{access_ip_range_id}`

```ruby
access_ip_range = client.access_ip_ranges.delete("access_ip_range_id")

puts(access_ip_range)
```
