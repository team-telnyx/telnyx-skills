---
name: telnyx-account-ruby
description: >-
  Manage account balance, payments, invoices, webhooks, and view audit logs and
  detail records. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: account
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account - Ruby

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

## List Audit Logs

Retrieve a list of audit log entries.

`GET /audit_events`

```ruby
page = client.audit_events.list

puts(page)
```

## Get user balance details

`GET /balance`

```ruby
balance = client.balance.retrieve

puts(balance)
```

## Search detail records

Search for any detail record across the Telnyx Platform

`GET /detail_records`

```ruby
page = client.detail_records.list

puts(page)
```

## List invoices

Retrieve a paginated list of invoices.

`GET /invoices`

```ruby
page = client.invoices.list

puts(page)
```

## Get invoice by ID

Retrieve a single invoice by its unique identifier.

`GET /invoices/{id}`

```ruby
invoice = client.invoices.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(invoice)
```

## List auto recharge preferences

Returns the payment auto recharge preferences.

`GET /payments/auto_recharge_prefs`

```ruby
auto_recharge_prefs = client.payment.auto_recharge_prefs.list

puts(auto_recharge_prefs)
```

## Update auto recharge preferences

Update payment auto recharge preferences.

`PATCH /payments/auto_recharge_prefs`

Optional: `enabled` (boolean), `invoice_enabled` (boolean), `preference` (enum), `recharge_amount` (string), `threshold_amount` (string)

```ruby
auto_recharge_pref = client.payment.auto_recharge_prefs.update

puts(auto_recharge_pref)
```

## List User Tags

List all user tags.

`GET /user_tags`

```ruby
user_tags = client.user_tags.list

puts(user_tags)
```

## List webhook deliveries

Lists webhook_deliveries for the authenticated user

`GET /webhook_deliveries`

```ruby
page = client.webhook_deliveries.list

puts(page)
```

## Find webhook_delivery details by ID

Provides webhook_delivery debug data, such as timestamps, delivery status and attempts.

`GET /webhook_deliveries/{id}`

```ruby
webhook_delivery = client.webhook_deliveries.retrieve("C9C0797E-901D-4349-A33C-C2C8F31A92C2")

puts(webhook_delivery)
```
