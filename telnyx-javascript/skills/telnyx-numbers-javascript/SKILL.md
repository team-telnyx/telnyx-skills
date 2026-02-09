---
name: telnyx-numbers-javascript
description: >-
  Search for available phone numbers by location and features, check coverage,
  and place orders. Use when acquiring new phone numbers. This skill provides
  JavaScript SDK examples.
metadata:
  author: telnyx
  product: numbers
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers - JavaScript

## Installation

```bash
npm install telnyx
```

## Setup

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'], // This is the default and can be omitted
});
```

All examples below assume `client` is already initialized as shown above.

## Get country coverage

`GET /country_coverage`

```javascript
const countryCoverage = await client.countryCoverage.retrieve();

console.log(countryCoverage.data);
```

## Get coverage for a specific country

`GET /country_coverage/countries/{country_code}`

```javascript
const response = await client.countryCoverage.retrieveCountry('US');

console.log(response.data);
```

## Create an inventory coverage request

Creates an inventory coverage request.

`GET /inventory_coverage`

```javascript
const inventoryCoverages = await client.inventoryCoverage.list();

console.log(inventoryCoverages.data);
```

## List number reservations

Gets a paginated list of phone number reservations.

`GET /number_reservations`

```javascript
// Automatically fetches more pages as needed.
for await (const numberReservation of client.numberReservations.list()) {
  console.log(numberReservation.id);
}
```

## Create a number reservation

Creates a Phone Number Reservation for multiple numbers.

`POST /number_reservations`

```javascript
const numberReservation = await client.numberReservations.create();

console.log(numberReservation.data);
```

## Retrieve a number reservation

Gets a single phone number reservation.

`GET /number_reservations/{number_reservation_id}`

```javascript
const numberReservation = await client.numberReservations.retrieve('number_reservation_id');

console.log(numberReservation.data);
```

## Extend a number reservation

Extends reservation expiry time on all phone numbers.

`POST /number_reservations/{number_reservation_id}/actions/extend`

```javascript
const response = await client.numberReservations.actions.extend('number_reservation_id');

console.log(response.data);
```

## List number orders

Get a paginated list of number orders.

`GET /number_orders`

```javascript
// Automatically fetches more pages as needed.
for await (const numberOrderListResponse of client.numberOrders.list()) {
  console.log(numberOrderListResponse.id);
}
```

## Create a number order

Creates a phone number order.

`POST /number_orders`

```javascript
const numberOrder = await client.numberOrders.create();

console.log(numberOrder.data);
```

## Retrieve a number order

Get an existing phone number order.

`GET /number_orders/{number_order_id}`

```javascript
const numberOrder = await client.numberOrders.retrieve('number_order_id');

console.log(numberOrder.data);
```

## Update a number order

Updates a phone number order.

`PATCH /number_orders/{number_order_id}`

```javascript
const numberOrder = await client.numberOrders.update('number_order_id');

console.log(numberOrder.data);
```

## List number block orders

Get a paginated list of number block orders.

`GET /number_block_orders`

```javascript
// Automatically fetches more pages as needed.
for await (const numberBlockOrder of client.numberBlockOrders.list()) {
  console.log(numberBlockOrder.id);
}
```

## Create a number block order

Creates a phone number block order.

`POST /number_block_orders` — Required: `starting_number`, `range`

```javascript
const numberBlockOrder = await client.numberBlockOrders.create({
  range: 10,
  starting_number: '+19705555000',
});

console.log(numberBlockOrder.data);
```

## Retrieve a number block order

Get an existing phone number block order.

`GET /number_block_orders/{number_block_order_id}`

```javascript
const numberBlockOrder = await client.numberBlockOrders.retrieve('number_block_order_id');

console.log(numberBlockOrder.data);
```

## Retrieve a list of phone numbers associated to orders

Get a list of phone numbers associated to orders.

`GET /number_order_phone_numbers`

```javascript
const numberOrderPhoneNumbers = await client.numberOrderPhoneNumbers.list();

console.log(numberOrderPhoneNumbers.data);
```

## Update requirement group for a phone number order

`POST /number_order_phone_numbers/{id}/requirement_group` — Required: `requirement_group_id`

```javascript
const response = await client.numberOrderPhoneNumbers.updateRequirementGroup(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { requirement_group_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(response.data);
```

## Retrieve a single phone number within a number order.

Get an existing phone number in number order.

`GET /number_order_phone_numbers/{number_order_phone_number_id}`

```javascript
const numberOrderPhoneNumber = await client.numberOrderPhoneNumbers.retrieve(
  'number_order_phone_number_id',
);

console.log(numberOrderPhoneNumber.data);
```

## Update requirements for a single phone number within a number order.

Updates requirements for a single phone number within a number order.

`PATCH /number_order_phone_numbers/{number_order_phone_number_id}`

```javascript
const response = await client.numberOrderPhoneNumbers.updateRequirements(
  'number_order_phone_number_id',
);

console.log(response.data);
```

## List sub number orders

Get a paginated list of sub number orders.

`GET /sub_number_orders`

```javascript
const subNumberOrders = await client.subNumberOrders.list();

console.log(subNumberOrders.data);
```

## Update requirement group for a sub number order

`POST /sub_number_orders/{id}/requirement_group` — Required: `requirement_group_id`

```javascript
const response = await client.subNumberOrders.updateRequirementGroup(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { requirement_group_id: 'a4b201f9-8646-4e54-a7d2-b2e403eeaf8c' },
);

console.log(response.data);
```

## Retrieve a sub number order

Get an existing sub number order.

`GET /sub_number_orders/{sub_number_order_id}`

```javascript
const subNumberOrder = await client.subNumberOrders.retrieve('sub_number_order_id');

console.log(subNumberOrder.data);
```

## Update a sub number order's requirements

Updates a sub number order.

`PATCH /sub_number_orders/{sub_number_order_id}`

```javascript
const subNumberOrder = await client.subNumberOrders.update('sub_number_order_id');

console.log(subNumberOrder.data);
```

## Cancel a sub number order

Allows you to cancel a sub number order in 'pending' status.

`PATCH /sub_number_orders/{sub_number_order_id}/cancel`

```javascript
const response = await client.subNumberOrders.cancel('sub_number_order_id');

console.log(response.data);
```

## Create a sub number orders report

Create a CSV report for sub number orders.

`POST /sub_number_orders/report`

```javascript
const subNumberOrdersReport = await client.subNumberOrdersReport.create();

console.log(subNumberOrdersReport.data);
```

## Retrieve a sub number orders report

Get the status and details of a sub number orders report.

`GET /sub_number_orders/report/{report_id}`

```javascript
const subNumberOrdersReport = await client.subNumberOrdersReport.retrieve(
  '12ade33a-21c0-473b-b055-b3c836e1c293',
);

console.log(subNumberOrdersReport.data);
```

## Download a sub number orders report

Download the CSV file for a completed sub number orders report.

`GET /sub_number_orders/report/{report_id}/download`

```javascript
const response = await client.subNumberOrdersReport.download(
  '12ade33a-21c0-473b-b055-b3c836e1c293',
);

console.log(response);
```

## List Advanced Orders

`GET /advanced_orders`

```javascript
const advancedOrders = await client.advancedOrders.list();

console.log(advancedOrders.data);
```

## Create Advanced Order

`POST /advanced_orders`

```javascript
const advancedOrder = await client.advancedOrders.create();

console.log(advancedOrder.id);
```

## Update Advanced Order

`PATCH /advanced_orders/{advanced-order-id}/requirement_group`

```javascript
const response = await client.advancedOrders.updateRequirementGroup(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response.id);
```

## Get Advanced Order

`GET /advanced_orders/{order_id}`

```javascript
const advancedOrder = await client.advancedOrders.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(advancedOrder.id);
```

## List inexplicit number orders

Get a paginated list of inexplicit number orders.

`GET /inexplicit_number_orders`

```javascript
// Automatically fetches more pages as needed.
for await (const inexplicitNumberOrderResponse of client.inexplicitNumberOrders.list()) {
  console.log(inexplicitNumberOrderResponse.id);
}
```

## Create an inexplicit number order

Create an inexplicit number order to programmatically purchase phone numbers without specifying exact numbers.

`POST /inexplicit_number_orders` — Required: `ordering_groups`

```javascript
const inexplicitNumberOrder = await client.inexplicitNumberOrders.create({
  ordering_groups: [
    {
      count_requested: 'count_requested',
      country_iso: 'US',
      phone_number_type: 'phone_number_type',
    },
  ],
});

console.log(inexplicitNumberOrder.data);
```

## Retrieve an inexplicit number order

Get an existing inexplicit number order by ID.

`GET /inexplicit_number_orders/{id}`

```javascript
const inexplicitNumberOrder = await client.inexplicitNumberOrders.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(inexplicitNumberOrder.data);
```

## Retrieve all comments

`GET /comments`

```javascript
const comments = await client.comments.list();

console.log(comments.data);
```

## Create a comment

`POST /comments`

```javascript
const comment = await client.comments.create();

console.log(comment.data);
```

## Retrieve a comment

`GET /comments/{id}`

```javascript
const comment = await client.comments.retrieve('id');

console.log(comment.data);
```

## Mark a comment as read

`PATCH /comments/{id}/read`

```javascript
const response = await client.comments.markAsRead('id');

console.log(response.data);
```

## List available phone number blocks

`GET /available_phone_number_blocks`

```javascript
const availablePhoneNumberBlocks = await client.availablePhoneNumberBlocks.list();

console.log(availablePhoneNumberBlocks.data);
```

## List available phone numbers

`GET /available_phone_numbers`

```javascript
const availablePhoneNumbers = await client.availablePhoneNumbers.list();

console.log(availablePhoneNumbers.data);
```

## Retrieve the features for a list of numbers

`POST /numbers_features` — Required: `phone_numbers`

```javascript
const numbersFeature = await client.numbersFeatures.create({ phone_numbers: ['string'] });

console.log(numbersFeature.data);
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `numberOrderStatusUpdate` | Number Order Status Update |
