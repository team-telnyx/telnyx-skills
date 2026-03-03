---
name: telnyx-numbers-curl
description: >-
  Search for available phone numbers by location and features, check coverage,
  and place orders. Use when acquiring new phone numbers. This skill provides
  REST API (curl) examples.
metadata:
  author: telnyx
  product: numbers
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List Advanced Orders

`GET /advanced_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/advanced_orders"
```

## Create Advanced Order

`POST /advanced_orders`

Optional: `area_code` (string), `comments` (string), `country_code` (string), `customer_reference` (string), `features` (array[object]), `phone_number_type` (enum), `quantity` (integer), `requirement_group_id` (uuid)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "requirement_group_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}' \
  "https://api.telnyx.com/v2/advanced_orders"
```

## Update Advanced Order

`PATCH /advanced_orders/{advanced-order-id}/requirement_group`

Optional: `area_code` (string), `comments` (string), `country_code` (string), `customer_reference` (string), `features` (array[object]), `phone_number_type` (enum), `quantity` (integer), `requirement_group_id` (uuid)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "requirement_group_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}' \
  "https://api.telnyx.com/v2/advanced_orders/{advanced-order-id}/requirement_group"
```

## Get Advanced Order

`GET /advanced_orders/{order_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/advanced_orders/{order_id}"
```

## List available phone number blocks

`GET /available_phone_number_blocks`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/available_phone_number_blocks"
```

## List available phone numbers

`GET /available_phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/available_phone_numbers"
```

## Retrieve all comments

`GET /comments`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/comments"
```

## Create a comment

`POST /comments`

Optional: `body` (string), `comment_record_id` (uuid), `comment_record_type` (enum), `commenter` (string), `commenter_type` (enum), `created_at` (date-time), `id` (uuid), `read_at` (date-time), `updated_at` (date-time)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12ade33a-21c0-473b-b055-b3c836e1c292",
  "body": "Hi there, ....",
  "commenter": "user@company.com",
  "commenter_type": "user",
  "comment_record_type": "sub_number_order",
  "comment_record_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
  "read_at": "2018-01-01T00:00:00.000000Z",
  "created_at": "2018-01-01T00:00:00.000000Z",
  "updated_at": "2018-01-01T00:00:00.000000Z"
}' \
  "https://api.telnyx.com/v2/comments"
```

## Retrieve a comment

`GET /comments/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/comments/{id}"
```

## Mark a comment as read

`PATCH /comments/{id}/read`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/comments/{id}/read"
```

## Get country coverage

`GET /country_coverage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/country_coverage"
```

## Get coverage for a specific country

`GET /country_coverage/countries/{country_code}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/country_coverage/countries/US"
```

## List customer service records

List customer service records.

`GET /customer_service_records`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/customer_service_records"
```

## Create a customer service record

Create a new customer service record for the provided phone number.

`POST /customer_service_records`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/customer_service_records"
```

## Verify CSR phone number coverage

Verify the coverage for a list of phone numbers.

`POST /customer_service_records/phone_number_coverages`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/customer_service_records/phone_number_coverages"
```

## Get a customer service record

Get a specific customer service record.

`GET /customer_service_records/{customer_service_record_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/customer_service_records/{customer_service_record_id}"
```

## List inexplicit number orders

Get a paginated list of inexplicit number orders.

`GET /inexplicit_number_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/inexplicit_number_orders"
```

## Create an inexplicit number order

Create an inexplicit number order to programmatically purchase phone numbers without specifying exact numbers.

`POST /inexplicit_number_orders` — Required: `ordering_groups`

Optional: `billing_group_id` (string), `connection_id` (string), `customer_reference` (string), `messaging_profile_id` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "ordering_groups": [
    {}
  ]
}' \
  "https://api.telnyx.com/v2/inexplicit_number_orders"
```

## Retrieve an inexplicit number order

Get an existing inexplicit number order by ID.

`GET /inexplicit_number_orders/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/inexplicit_number_orders/{id}"
```

## Create an inventory coverage request

Creates an inventory coverage request.

`GET /inventory_coverage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/inventory_coverage"
```

## List mobile network operators

Telnyx has a set of GSM mobile operators partners that are available through our mobile network roaming.

`GET /mobile_network_operators`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/mobile_network_operators"
```

## List network coverage locations

List all locations and the interfaces that region supports

`GET /network_coverage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/network_coverage"
```

## List number block orders

Get a paginated list of number block orders.

`GET /number_block_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_block_orders"
```

## Create a number block order

Creates a phone number block order.

`POST /number_block_orders` — Required: `starting_number`, `range`

Optional: `connection_id` (string), `created_at` (date-time), `customer_reference` (string), `errors` (string), `id` (uuid), `messaging_profile_id` (string), `phone_numbers_count` (integer), `record_type` (string), `requirements_met` (boolean), `status` (enum), `updated_at` (date-time)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12ade33a-21c0-473b-b055-b3c836e1c292",
  "record_type": "number_block_order",
  "starting_number": "+19705555000",
  "range": 10,
  "phone_numbers_count": 10,
  "connection_id": "346789098765567",
  "messaging_profile_id": "abc85f64-5717-4562-b3fc-2c9600",
  "customer_reference": "MY REF 001",
  "created_at": "2018-01-01T00:00:00.000000Z",
  "updated_at": "2018-01-01T00:00:00.000000Z",
  "requirements_met": true,
  "errors": "Number is already on hold"
}' \
  "https://api.telnyx.com/v2/number_block_orders"
```

## Retrieve a number block order

Get an existing phone number block order.

`GET /number_block_orders/{number_block_order_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_block_orders/{number_block_order_id}"
```

## Retrieve a list of phone numbers associated to orders

Get a list of phone numbers associated to orders.

`GET /number_order_phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_order_phone_numbers"
```

## Retrieve a single phone number within a number order.

Get an existing phone number in number order.

`GET /number_order_phone_numbers/{number_order_phone_number_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_order_phone_numbers/{number_order_phone_number_id}"
```

## Update requirements for a single phone number within a number order.

Updates requirements for a single phone number within a number order.

`PATCH /number_order_phone_numbers/{number_order_phone_number_id}`

Optional: `regulatory_requirements` (array[object])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/number_order_phone_numbers/{number_order_phone_number_id}"
```

## List number orders

Get a paginated list of number orders.

`GET /number_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_orders"
```

## Create a number order

Creates a phone number order.

`POST /number_orders`

Optional: `billing_group_id` (string), `connection_id` (string), `customer_reference` (string), `messaging_profile_id` (string), `phone_numbers` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "connection_id": "346789098765567",
  "messaging_profile_id": "abc85f64-5717-4562-b3fc-2c9600",
  "billing_group_id": "abc85f64-5717-4562-b3fc-2c9600",
  "customer_reference": "MY REF 001"
}' \
  "https://api.telnyx.com/v2/number_orders"
```

## Retrieve a number order

Get an existing phone number order.

`GET /number_orders/{number_order_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_orders/{number_order_id}"
```

## Update a number order

Updates a phone number order.

`PATCH /number_orders/{number_order_id}`

Optional: `customer_reference` (string), `regulatory_requirements` (array[object])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_reference": "MY REF 001"
}' \
  "https://api.telnyx.com/v2/number_orders/{number_order_id}"
```

## List number reservations

Gets a paginated list of phone number reservations.

`GET /number_reservations`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_reservations"
```

## Create a number reservation

Creates a Phone Number Reservation for multiple numbers.

`POST /number_reservations`

Optional: `created_at` (date-time), `customer_reference` (string), `id` (uuid), `phone_numbers` (array[object]), `record_type` (string), `status` (enum), `updated_at` (date-time)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "12ade33a-21c0-473b-b055-b3c836e1c292",
  "record_type": "number_reservation",
  "customer_reference": "MY REF 001",
  "created_at": "2018-01-01T00:00:00.000000Z",
  "updated_at": "2018-01-01T00:00:00.000000Z"
}' \
  "https://api.telnyx.com/v2/number_reservations"
```

## Retrieve a number reservation

Gets a single phone number reservation.

`GET /number_reservations/{number_reservation_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/number_reservations/{number_reservation_id}"
```

## Extend a number reservation

Extends reservation expiry time on all phone numbers.

`POST /number_reservations/{number_reservation_id}/actions/extend`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/number_reservations/{number_reservation_id}/actions/extend"
```

## Retrieve the features for a list of numbers

`POST /numbers_features` — Required: `phone_numbers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/numbers_features"
```

## Lists the phone number blocks jobs

`GET /phone_number_blocks/jobs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_number_blocks/jobs?sort=created_at"
```

## Deletes all numbers associated with a phone number block

Creates a new background job to delete all the phone numbers associated with the given block.

`POST /phone_number_blocks/jobs/delete_phone_number_block` — Required: `phone_number_block_id`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_number_block_id": "string"
}' \
  "https://api.telnyx.com/v2/phone_number_blocks/jobs/delete_phone_number_block"
```

## Retrieves a phone number blocks job

`GET /phone_number_blocks/jobs/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_number_blocks/jobs/{id}"
```

## List sub number orders

Get a paginated list of sub number orders.

`GET /sub_number_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/sub_number_orders"
```

## Retrieve a sub number order

Get an existing sub number order.

`GET /sub_number_orders/{sub_number_order_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/sub_number_orders/{sub_number_order_id}"
```

## Update a sub number order's requirements

Updates a sub number order.

`PATCH /sub_number_orders/{sub_number_order_id}`

Optional: `regulatory_requirements` (array[object])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/sub_number_orders/{sub_number_order_id}"
```

## Cancel a sub number order

Allows you to cancel a sub number order in 'pending' status.

`PATCH /sub_number_orders/{sub_number_order_id}/cancel`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/sub_number_orders/{sub_number_order_id}/cancel"
```

## Create a sub number orders report

Create a CSV report for sub number orders.

`POST /sub_number_orders_report`

Optional: `country_code` (string), `created_at_gt` (date-time), `created_at_lt` (date-time), `customer_reference` (string), `order_request_id` (uuid), `status` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "status": "success",
  "country_code": "US",
  "created_at_gt": "2023-04-05T10:22:08.230549Z",
  "created_at_lt": "2025-06-05T10:22:08.230549Z",
  "order_request_id": "12ade33a-21c0-473b-b055-b3c836e1c293",
  "customer_reference": "STRING"
}' \
  "https://api.telnyx.com/v2/sub_number_orders_report"
```

## Retrieve a sub number orders report

Get the status and details of a sub number orders report.

`GET /sub_number_orders_report/{report_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/sub_number_orders_report/12ade33a-21c0-473b-b055-b3c836e1c293"
```

## Download a sub number orders report

Download the CSV file for a completed sub number orders report.

`GET /sub_number_orders_report/{report_id}/download`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/sub_number_orders_report/12ade33a-21c0-473b-b055-b3c836e1c293/download"
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `numberOrderStatusUpdate` | Number Order Status Update |

### Webhook payload fields

**`numberOrderStatusUpdate`**

| Field | Type | Description |
|-------|------|-------------|
| `data.event_type` | string | The type of event being sent |
| `data.id` | uuid | Unique identifier for the event |
| `data.occurred_at` | date-time | ISO 8601 timestamp of when the event occurred |
| `data.payload.id` | uuid |  |
| `data.payload.record_type` | string |  |
| `data.payload.phone_numbers_count` | integer | The count of phone numbers in the number order. |
| `data.payload.connection_id` | string | Identifies the connection associated with this phone number. |
| `data.payload.messaging_profile_id` | string | Identifies the messaging profile associated with the phone number. |
| `data.payload.billing_group_id` | string | Identifies the messaging profile associated with the phone number. |
| `data.payload.phone_numbers` | array[object] |  |
| `data.payload.sub_number_orders_ids` | array[string] |  |
| `data.payload.status` | enum | The status of the order. |
| `data.payload.customer_reference` | string | A customer reference string for customer look ups. |
| `data.payload.created_at` | date-time | An ISO 8901 datetime string denoting when the number order was created. |
| `data.payload.updated_at` | date-time | An ISO 8901 datetime string for when the number order was updated. |
| `data.payload.requirements_met` | boolean | True if all requirements are met for every phone number, false otherwise. |
| `data.record_type` | string | Type of record |
| `meta.attempt` | integer | Webhook delivery attempt number |
| `meta.delivered_to` | uri | URL where the webhook was delivered |
