---
name: telnyx-account-management-ruby
description: >-
  Manage sub-accounts for reseller and enterprise scenarios. This skill provides
  Ruby SDK examples.
metadata:
  author: telnyx
  product: account-management
  language: ruby
---

# Telnyx Account Management - Ruby

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

## Lists accounts managed by the current user.

Lists the accounts managed by the current user.

`GET /managed_accounts`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.managed_accounts.list

puts(page)
```

## Create a new managed account.

Create a new managed account owned by the authenticated user.

`POST /managed_accounts` — Required: `business_name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

managed_account = telnyx.managed_accounts.create(business_name: "Larry's Cat Food Inc")

puts(managed_account)
```

## Retrieve a managed account

Retrieves the details of a single managed account.

`GET /managed_accounts/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

managed_account = telnyx.managed_accounts.retrieve("id")

puts(managed_account)
```

## Update a managed account

Update a single managed account.

`PATCH /managed_accounts/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

managed_account = telnyx.managed_accounts.update("id")

puts(managed_account)
```

## Disables a managed account

Disables a managed account, forbidding it to use Telnyx services, including sending or receiving phone calls and SMS messages.

`POST /managed_accounts/{id}/actions/disable`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.managed_accounts.actions.disable("id")

puts(response)
```

## Enables a managed account

Enables a managed account and its sub-users to use Telnyx services.

`POST /managed_accounts/{id}/actions/enable`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.managed_accounts.actions.enable("id")

puts(response)
```

## Update the amount of allocatable global outbound channels allocated to a specific managed account.

`PATCH /managed_accounts/{id}/update_global_channel_limit`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.managed_accounts.update_global_channel_limit("id")

puts(response)
```

## Display information about allocatable global outbound channels for the current user.

`GET /managed_accounts/allocatable_global_outbound_channels`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.managed_accounts.get_allocatable_global_outbound_channels

puts(response)
```
