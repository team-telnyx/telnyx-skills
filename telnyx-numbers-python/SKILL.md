---
name: telnyx-numbers-python
description: >-
  Search for available phone numbers by location and features, check coverage,
  and place orders. Use when acquiring new phone numbers. This skill provides
  Python SDK examples.
metadata:
  author: telnyx
  product: numbers
  language: python
---

# Telnyx Numbers - Python

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

## Get country coverage

`GET /country_coverage`

```python
country_coverage = client.country_coverage.retrieve()
print(country_coverage.data)
```

## Get coverage for a specific country

`GET /country_coverage/countries/{country_code}`

```python
response = client.country_coverage.retrieve_country(
    "US",
)
print(response.data)
```

## Create an inventory coverage request

Creates an inventory coverage request.

`GET /inventory_coverage`

```python
inventory_coverages = client.inventory_coverage.list()
print(inventory_coverages.data)
```

## List number reservations

Gets a paginated list of phone number reservations.

`GET /number_reservations`

```python
page = client.number_reservations.list()
page = page.data[0]
print(page.id)
```

## Create a number reservation

Creates a Phone Number Reservation for multiple numbers.

`POST /number_reservations`

```python
number_reservation = client.number_reservations.create()
print(number_reservation.data)
```

## Retrieve a number reservation

Gets a single phone number reservation.

`GET /number_reservations/{number_reservation_id}`

```python
number_reservation = client.number_reservations.retrieve(
    "number_reservation_id",
)
print(number_reservation.data)
```

## Extend a number reservation

Extends reservation expiry time on all phone numbers.

`POST /number_reservations/{number_reservation_id}/actions/extend`

```python
response = client.number_reservations.actions.extend(
    "number_reservation_id",
)
print(response.data)
```

## List number orders

Get a paginated list of number orders.

`GET /number_orders`

```python
page = client.number_orders.list()
page = page.data[0]
print(page.id)
```

## Create a number order

Creates a phone number order.

`POST /number_orders`

```python
number_order = client.number_orders.create()
print(number_order.data)
```

## Retrieve a number order

Get an existing phone number order.

`GET /number_orders/{number_order_id}`

```python
number_order = client.number_orders.retrieve(
    "number_order_id",
)
print(number_order.data)
```

## Update a number order

Updates a phone number order.

`PATCH /number_orders/{number_order_id}`

```python
number_order = client.number_orders.update(
    number_order_id="number_order_id",
)
print(number_order.data)
```

## List number block orders

Get a paginated list of number block orders.

`GET /number_block_orders`

```python
page = client.number_block_orders.list()
page = page.data[0]
print(page.id)
```

## Create a number block order

Creates a phone number block order.

`POST /number_block_orders` — Required: `starting_number`, `range`

```python
number_block_order = client.number_block_orders.create(
    range=10,
    starting_number="+19705555000",
)
print(number_block_order.data)
```

## Retrieve a number block order

Get an existing phone number block order.

`GET /number_block_orders/{number_block_order_id}`

```python
number_block_order = client.number_block_orders.retrieve(
    "number_block_order_id",
)
print(number_block_order.data)
```

## Retrieve a list of phone numbers associated to orders

Get a list of phone numbers associated to orders.

`GET /number_order_phone_numbers`

```python
number_order_phone_numbers = client.number_order_phone_numbers.list()
print(number_order_phone_numbers.data)
```

## Update requirement group for a phone number order

`POST /number_order_phone_numbers/{id}/requirement_group` — Required: `requirement_group_id`

```python
response = client.number_order_phone_numbers.update_requirement_group(
    id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.data)
```

## Retrieve a single phone number within a number order.

Get an existing phone number in number order.

`GET /number_order_phone_numbers/{number_order_phone_number_id}`

```python
number_order_phone_number = client.number_order_phone_numbers.retrieve(
    "number_order_phone_number_id",
)
print(number_order_phone_number.data)
```

## Update requirements for a single phone number within a number order.

Updates requirements for a single phone number within a number order.

`PATCH /number_order_phone_numbers/{number_order_phone_number_id}`

```python
response = client.number_order_phone_numbers.update_requirements(
    number_order_phone_number_id="number_order_phone_number_id",
)
print(response.data)
```

## List sub number orders

Get a paginated list of sub number orders.

`GET /sub_number_orders`

```python
sub_number_orders = client.sub_number_orders.list()
print(sub_number_orders.data)
```

## Update requirement group for a sub number order

`POST /sub_number_orders/{id}/requirement_group` — Required: `requirement_group_id`

```python
response = client.sub_number_orders.update_requirement_group(
    id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
)
print(response.data)
```

## Retrieve a sub number order

Get an existing sub number order.

`GET /sub_number_orders/{sub_number_order_id}`

```python
sub_number_order = client.sub_number_orders.retrieve(
    sub_number_order_id="sub_number_order_id",
)
print(sub_number_order.data)
```

## Update a sub number order's requirements

Updates a sub number order.

`PATCH /sub_number_orders/{sub_number_order_id}`

```python
sub_number_order = client.sub_number_orders.update(
    sub_number_order_id="sub_number_order_id",
)
print(sub_number_order.data)
```

## Cancel a sub number order

Allows you to cancel a sub number order in 'pending' status.

`PATCH /sub_number_orders/{sub_number_order_id}/cancel`

```python
response = client.sub_number_orders.cancel(
    "sub_number_order_id",
)
print(response.data)
```

## Create a sub number orders report

Create a CSV report for sub number orders.

`POST /sub_number_orders/report`

```python
sub_number_orders_report = client.sub_number_orders_report.create()
print(sub_number_orders_report.data)
```

## Retrieve a sub number orders report

Get the status and details of a sub number orders report.

`GET /sub_number_orders/report/{report_id}`

```python
sub_number_orders_report = client.sub_number_orders_report.retrieve(
    "12ade33a-21c0-473b-b055-b3c836e1c293",
)
print(sub_number_orders_report.data)
```

## Download a sub number orders report

Download the CSV file for a completed sub number orders report.

`GET /sub_number_orders/report/{report_id}/download`

```python
response = client.sub_number_orders_report.download(
    "12ade33a-21c0-473b-b055-b3c836e1c293",
)
print(response)
```

## List Advanced Orders

`GET /advanced_orders`

```python
advanced_orders = client.advanced_orders.list()
print(advanced_orders.data)
```

## Create Advanced Order

`POST /advanced_orders`

```python
advanced_order = client.advanced_orders.create()
print(advanced_order.id)
```

## Update Advanced Order

`PATCH /advanced_orders/{advanced-order-id}/requirement_group`

```python
response = client.advanced_orders.update_requirement_group(
    advanced_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.id)
```

## Get Advanced Order

`GET /advanced_orders/{order_id}`

```python
advanced_order = client.advanced_orders.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(advanced_order.id)
```

## List inexplicit number orders

Get a paginated list of inexplicit number orders.

`GET /inexplicit_number_orders`

```python
page = client.inexplicit_number_orders.list()
page = page.data[0]
print(page.id)
```

## Create an inexplicit number order

Create an inexplicit number order to programmatically purchase phone numbers without specifying exact numbers.

`POST /inexplicit_number_orders` — Required: `ordering_groups`

```python
inexplicit_number_order = client.inexplicit_number_orders.create(
    ordering_groups=[{
        "count_requested": "count_requested",
        "country_iso": "US",
        "phone_number_type": "phone_number_type",
    }],
)
print(inexplicit_number_order.data)
```

## Retrieve an inexplicit number order

Get an existing inexplicit number order by ID.

`GET /inexplicit_number_orders/{id}`

```python
inexplicit_number_order = client.inexplicit_number_orders.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(inexplicit_number_order.data)
```

## Retrieve all comments

`GET /comments`

```python
comments = client.comments.list()
print(comments.data)
```

## Create a comment

`POST /comments`

```python
comment = client.comments.create()
print(comment.data)
```

## Retrieve a comment

`GET /comments/{id}`

```python
comment = client.comments.retrieve(
    "id",
)
print(comment.data)
```

## Mark a comment as read

`PATCH /comments/{id}/read`

```python
response = client.comments.mark_as_read(
    "id",
)
print(response.data)
```

## List available phone number blocks

`GET /available_phone_number_blocks`

```python
available_phone_number_blocks = client.available_phone_number_blocks.list()
print(available_phone_number_blocks.data)
```

## List available phone numbers

`GET /available_phone_numbers`

```python
available_phone_numbers = client.available_phone_numbers.list()
print(available_phone_numbers.data)
```

## Retrieve the features for a list of numbers

`POST /numbers_features` — Required: `phone_numbers`

```python
numbers_feature = client.numbers_features.create(
    phone_numbers=["string"],
)
print(numbers_feature.data)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `numberOrderStatusUpdate` | Number Order Status Update |
