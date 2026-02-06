---
name: telnyx-numbers-ruby
description: >-
  Search for available phone numbers by location and features, check coverage,
  and place orders. Use when acquiring new phone numbers. This skill provides
  Ruby SDK examples.
metadata:
  author: telnyx
  product: numbers
  language: ruby
---

# Telnyx Numbers - Ruby

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

## Get country coverage

`GET /country_coverage`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

country_coverage = telnyx.country_coverage.retrieve

puts(country_coverage)
```

## Get coverage for a specific country

`GET /country_coverage/countries/{country_code}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.country_coverage.retrieve_country("US")

puts(response)
```

## Create an inventory coverage request

Creates an inventory coverage request.

`GET /inventory_coverage`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inventory_coverages = telnyx.inventory_coverage.list

puts(inventory_coverages)
```

## List number reservations

Gets a paginated list of phone number reservations.

`GET /number_reservations`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.number_reservations.list

puts(page)
```

## Create a number reservation

Creates a Phone Number Reservation for multiple numbers.

`POST /number_reservations`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_reservation = telnyx.number_reservations.create

puts(number_reservation)
```

## Retrieve a number reservation

Gets a single phone number reservation.

`GET /number_reservations/{number_reservation_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_reservation = telnyx.number_reservations.retrieve("number_reservation_id")

puts(number_reservation)
```

## Extend a number reservation

Extends reservation expiry time on all phone numbers.

`POST /number_reservations/{number_reservation_id}/actions/extend`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.number_reservations.actions.extend_("number_reservation_id")

puts(response)
```

## List number orders

Get a paginated list of number orders.

`GET /number_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.number_orders.list

puts(page)
```

## Create a number order

Creates a phone number order.

`POST /number_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_order = telnyx.number_orders.create

puts(number_order)
```

## Retrieve a number order

Get an existing phone number order.

`GET /number_orders/{number_order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_order = telnyx.number_orders.retrieve("number_order_id")

puts(number_order)
```

## Update a number order

Updates a phone number order.

`PATCH /number_orders/{number_order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_order = telnyx.number_orders.update("number_order_id")

puts(number_order)
```

## List number block orders

Get a paginated list of number block orders.

`GET /number_block_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.number_block_orders.list

puts(page)
```

## Create a number block order

Creates a phone number block order.

`POST /number_block_orders` — Required: `starting_number`, `range`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_block_order = telnyx.number_block_orders.create(range: 10, starting_number: "+19705555000")

puts(number_block_order)
```

## Retrieve a number block order

Get an existing phone number block order.

`GET /number_block_orders/{number_block_order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_block_order = telnyx.number_block_orders.retrieve("number_block_order_id")

puts(number_block_order)
```

## Retrieve a list of phone numbers associated to orders

Get a list of phone numbers associated to orders.

`GET /number_order_phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_order_phone_numbers = telnyx.number_order_phone_numbers.list

puts(number_order_phone_numbers)
```

## Update requirement group for a phone number order

`POST /number_order_phone_numbers/{id}/requirement_group` — Required: `requirement_group_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.number_order_phone_numbers.update_requirement_group(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  requirement_group_id: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
)

puts(response)
```

## Retrieve a single phone number within a number order.

Get an existing phone number in number order.

`GET /number_order_phone_numbers/{number_order_phone_number_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

number_order_phone_number = telnyx.number_order_phone_numbers.retrieve("number_order_phone_number_id")

puts(number_order_phone_number)
```

## Update requirements for a single phone number within a number order.

Updates requirements for a single phone number within a number order.

`PATCH /number_order_phone_numbers/{number_order_phone_number_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.number_order_phone_numbers.update_requirements("number_order_phone_number_id")

puts(response)
```

## List sub number orders

Get a paginated list of sub number orders.

`GET /sub_number_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

sub_number_orders = telnyx.sub_number_orders.list

puts(sub_number_orders)
```

## Update requirement group for a sub number order

`POST /sub_number_orders/{id}/requirement_group` — Required: `requirement_group_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.sub_number_orders.update_requirement_group(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  requirement_group_id: "a4b201f9-8646-4e54-a7d2-b2e403eeaf8c"
)

puts(response)
```

## Retrieve a sub number order

Get an existing sub number order.

`GET /sub_number_orders/{sub_number_order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

sub_number_order = telnyx.sub_number_orders.retrieve("sub_number_order_id")

puts(sub_number_order)
```

## Update a sub number order's requirements

Updates a sub number order.

`PATCH /sub_number_orders/{sub_number_order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

sub_number_order = telnyx.sub_number_orders.update("sub_number_order_id")

puts(sub_number_order)
```

## Cancel a sub number order

Allows you to cancel a sub number order in 'pending' status.

`PATCH /sub_number_orders/{sub_number_order_id}/cancel`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.sub_number_orders.cancel("sub_number_order_id")

puts(response)
```

## Create a sub number orders report

Create a CSV report for sub number orders.

`POST /sub_number_orders/report`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

sub_number_orders_report = telnyx.sub_number_orders_report.create

puts(sub_number_orders_report)
```

## Retrieve a sub number orders report

Get the status and details of a sub number orders report.

`GET /sub_number_orders/report/{report_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

sub_number_orders_report = telnyx.sub_number_orders_report.retrieve("12ade33a-21c0-473b-b055-b3c836e1c293")

puts(sub_number_orders_report)
```

## Download a sub number orders report

Download the CSV file for a completed sub number orders report.

`GET /sub_number_orders/report/{report_id}/download`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.sub_number_orders_report.download("12ade33a-21c0-473b-b055-b3c836e1c293")

puts(response)
```

## List Advanced Orders

`GET /advanced_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

advanced_orders = telnyx.advanced_orders.list

puts(advanced_orders)
```

## Create Advanced Order

`POST /advanced_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

advanced_order = telnyx.advanced_orders.create

puts(advanced_order)
```

## Update Advanced Order

`PATCH /advanced_orders/{advanced-order-id}/requirement_group`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.advanced_orders.update_requirement_group("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(response)
```

## Get Advanced Order

`GET /advanced_orders/{order_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

advanced_order = telnyx.advanced_orders.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(advanced_order)
```

## List inexplicit number orders

Get a paginated list of inexplicit number orders.

`GET /inexplicit_number_orders`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.inexplicit_number_orders.list

puts(page)
```

## Create an inexplicit number order

Create an inexplicit number order to programmatically purchase phone numbers without specifying exact numbers.

`POST /inexplicit_number_orders` — Required: `ordering_groups`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inexplicit_number_order = telnyx.inexplicit_number_orders.create(
  ordering_groups: [{count_requested: "count_requested", country_iso: :US, phone_number_type: "phone_number_type"}]
)

puts(inexplicit_number_order)
```

## Retrieve an inexplicit number order

Get an existing inexplicit number order by ID.

`GET /inexplicit_number_orders/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inexplicit_number_order = telnyx.inexplicit_number_orders.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(inexplicit_number_order)
```

## Retrieve all comments

`GET /comments`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

comments = telnyx.comments.list

puts(comments)
```

## Create a comment

`POST /comments`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

comment = telnyx.comments.create

puts(comment)
```

## Retrieve a comment

`GET /comments/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

comment = telnyx.comments.retrieve("id")

puts(comment)
```

## Mark a comment as read

`PATCH /comments/{id}/read`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.comments.mark_as_read("id")

puts(response)
```

## List available phone number blocks

`GET /available_phone_number_blocks`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

available_phone_number_blocks = telnyx.available_phone_number_blocks.list

puts(available_phone_number_blocks)
```

## List available phone numbers

`GET /available_phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

available_phone_numbers = telnyx.available_phone_numbers.list

puts(available_phone_numbers)
```

## Retrieve the features for a list of numbers

`POST /numbers_features` — Required: `phone_numbers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

numbers_feature = telnyx.numbers_features.create(phone_numbers: ["string"])

puts(numbers_feature)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `numberOrderStatusUpdate` | Number Order Status Update |
