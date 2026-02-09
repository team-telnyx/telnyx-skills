---
name: telnyx-numbers-java
description: >-
  Search for available phone numbers by location and features, check coverage,
  and place orders. Use when acquiring new phone numbers. This skill provides
  Java SDK examples.
metadata:
  author: telnyx
  product: numbers
  language: java
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers - Java

## Installation

```text
// See https://github.com/team-telnyx/telnyx-java for Maven/Gradle setup
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## Get country coverage

`GET /country_coverage`

```java
import com.telnyx.sdk.models.countrycoverage.CountryCoverageRetrieveParams;
import com.telnyx.sdk.models.countrycoverage.CountryCoverageRetrieveResponse;

CountryCoverageRetrieveResponse countryCoverage = client.countryCoverage().retrieve();
```

## Get coverage for a specific country

`GET /country_coverage/countries/{country_code}`

```java
import com.telnyx.sdk.models.countrycoverage.CountryCoverageRetrieveCountryParams;
import com.telnyx.sdk.models.countrycoverage.CountryCoverageRetrieveCountryResponse;

CountryCoverageRetrieveCountryResponse response = client.countryCoverage().retrieveCountry("US");
```

## Create an inventory coverage request

Creates an inventory coverage request.

`GET /inventory_coverage`

```java
import com.telnyx.sdk.models.inventorycoverage.InventoryCoverageListParams;
import com.telnyx.sdk.models.inventorycoverage.InventoryCoverageListResponse;

InventoryCoverageListResponse inventoryCoverages = client.inventoryCoverage().list();
```

## List number reservations

Gets a paginated list of phone number reservations.

`GET /number_reservations`

```java
import com.telnyx.sdk.models.numberreservations.NumberReservationListPage;
import com.telnyx.sdk.models.numberreservations.NumberReservationListParams;

NumberReservationListPage page = client.numberReservations().list();
```

## Create a number reservation

Creates a Phone Number Reservation for multiple numbers.

`POST /number_reservations`

```java
import com.telnyx.sdk.models.numberreservations.NumberReservationCreateParams;
import com.telnyx.sdk.models.numberreservations.NumberReservationCreateResponse;

NumberReservationCreateResponse numberReservation = client.numberReservations().create();
```

## Retrieve a number reservation

Gets a single phone number reservation.

`GET /number_reservations/{number_reservation_id}`

```java
import com.telnyx.sdk.models.numberreservations.NumberReservationRetrieveParams;
import com.telnyx.sdk.models.numberreservations.NumberReservationRetrieveResponse;

NumberReservationRetrieveResponse numberReservation = client.numberReservations().retrieve("number_reservation_id");
```

## Extend a number reservation

Extends reservation expiry time on all phone numbers.

`POST /number_reservations/{number_reservation_id}/actions/extend`

```java
import com.telnyx.sdk.models.numberreservations.actions.ActionExtendParams;
import com.telnyx.sdk.models.numberreservations.actions.ActionExtendResponse;

ActionExtendResponse response = client.numberReservations().actions().extend("number_reservation_id");
```

## List number orders

Get a paginated list of number orders.

`GET /number_orders`

```java
import com.telnyx.sdk.models.numberorders.NumberOrderListPage;
import com.telnyx.sdk.models.numberorders.NumberOrderListParams;

NumberOrderListPage page = client.numberOrders().list();
```

## Create a number order

Creates a phone number order.

`POST /number_orders`

```java
import com.telnyx.sdk.models.numberorders.NumberOrderCreateParams;
import com.telnyx.sdk.models.numberorders.NumberOrderCreateResponse;

NumberOrderCreateResponse numberOrder = client.numberOrders().create();
```

## Retrieve a number order

Get an existing phone number order.

`GET /number_orders/{number_order_id}`

```java
import com.telnyx.sdk.models.numberorders.NumberOrderRetrieveParams;
import com.telnyx.sdk.models.numberorders.NumberOrderRetrieveResponse;

NumberOrderRetrieveResponse numberOrder = client.numberOrders().retrieve("number_order_id");
```

## Update a number order

Updates a phone number order.

`PATCH /number_orders/{number_order_id}`

```java
import com.telnyx.sdk.models.numberorders.NumberOrderUpdateParams;
import com.telnyx.sdk.models.numberorders.NumberOrderUpdateResponse;

NumberOrderUpdateResponse numberOrder = client.numberOrders().update("number_order_id");
```

## List number block orders

Get a paginated list of number block orders.

`GET /number_block_orders`

```java
import com.telnyx.sdk.models.numberblockorders.NumberBlockOrderListPage;
import com.telnyx.sdk.models.numberblockorders.NumberBlockOrderListParams;

NumberBlockOrderListPage page = client.numberBlockOrders().list();
```

## Create a number block order

Creates a phone number block order.

`POST /number_block_orders` — Required: `starting_number`, `range`

```java
import com.telnyx.sdk.models.numberblockorders.NumberBlockOrderCreateParams;
import com.telnyx.sdk.models.numberblockorders.NumberBlockOrderCreateResponse;

NumberBlockOrderCreateParams params = NumberBlockOrderCreateParams.builder()
    .range(10L)
    .startingNumber("+19705555000")
    .build();
NumberBlockOrderCreateResponse numberBlockOrder = client.numberBlockOrders().create(params);
```

## Retrieve a number block order

Get an existing phone number block order.

`GET /number_block_orders/{number_block_order_id}`

```java
import com.telnyx.sdk.models.numberblockorders.NumberBlockOrderRetrieveParams;
import com.telnyx.sdk.models.numberblockorders.NumberBlockOrderRetrieveResponse;

NumberBlockOrderRetrieveResponse numberBlockOrder = client.numberBlockOrders().retrieve("number_block_order_id");
```

## Retrieve a list of phone numbers associated to orders

Get a list of phone numbers associated to orders.

`GET /number_order_phone_numbers`

```java
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberListParams;
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberListResponse;

NumberOrderPhoneNumberListResponse numberOrderPhoneNumbers = client.numberOrderPhoneNumbers().list();
```

## Update requirement group for a phone number order

`POST /number_order_phone_numbers/{id}/requirement_group` — Required: `requirement_group_id`

```java
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberUpdateRequirementGroupParams;
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberUpdateRequirementGroupResponse;

NumberOrderPhoneNumberUpdateRequirementGroupParams params = NumberOrderPhoneNumberUpdateRequirementGroupParams.builder()
    .id("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .requirementGroupId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .build();
NumberOrderPhoneNumberUpdateRequirementGroupResponse response = client.numberOrderPhoneNumbers().updateRequirementGroup(params);
```

## Retrieve a single phone number within a number order.

Get an existing phone number in number order.

`GET /number_order_phone_numbers/{number_order_phone_number_id}`

```java
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberRetrieveParams;
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberRetrieveResponse;

NumberOrderPhoneNumberRetrieveResponse numberOrderPhoneNumber = client.numberOrderPhoneNumbers().retrieve("number_order_phone_number_id");
```

## Update requirements for a single phone number within a number order.

Updates requirements for a single phone number within a number order.

`PATCH /number_order_phone_numbers/{number_order_phone_number_id}`

```java
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberUpdateRequirementsParams;
import com.telnyx.sdk.models.numberorderphonenumbers.NumberOrderPhoneNumberUpdateRequirementsResponse;

NumberOrderPhoneNumberUpdateRequirementsResponse response = client.numberOrderPhoneNumbers().updateRequirements("number_order_phone_number_id");
```

## List sub number orders

Get a paginated list of sub number orders.

`GET /sub_number_orders`

```java
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderListParams;
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderListResponse;

SubNumberOrderListResponse subNumberOrders = client.subNumberOrders().list();
```

## Update requirement group for a sub number order

`POST /sub_number_orders/{id}/requirement_group` — Required: `requirement_group_id`

```java
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderUpdateRequirementGroupParams;
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderUpdateRequirementGroupResponse;

SubNumberOrderUpdateRequirementGroupParams params = SubNumberOrderUpdateRequirementGroupParams.builder()
    .id("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .requirementGroupId("a4b201f9-8646-4e54-a7d2-b2e403eeaf8c")
    .build();
SubNumberOrderUpdateRequirementGroupResponse response = client.subNumberOrders().updateRequirementGroup(params);
```

## Retrieve a sub number order

Get an existing sub number order.

`GET /sub_number_orders/{sub_number_order_id}`

```java
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderRetrieveParams;
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderRetrieveResponse;

SubNumberOrderRetrieveResponse subNumberOrder = client.subNumberOrders().retrieve("sub_number_order_id");
```

## Update a sub number order's requirements

Updates a sub number order.

`PATCH /sub_number_orders/{sub_number_order_id}`

```java
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderUpdateParams;
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderUpdateResponse;

SubNumberOrderUpdateResponse subNumberOrder = client.subNumberOrders().update("sub_number_order_id");
```

## Cancel a sub number order

Allows you to cancel a sub number order in 'pending' status.

`PATCH /sub_number_orders/{sub_number_order_id}/cancel`

```java
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderCancelParams;
import com.telnyx.sdk.models.subnumberorders.SubNumberOrderCancelResponse;

SubNumberOrderCancelResponse response = client.subNumberOrders().cancel("sub_number_order_id");
```

## Create a sub number orders report

Create a CSV report for sub number orders.

`POST /sub_number_orders/report`

```java
import com.telnyx.sdk.models.subnumberordersreport.SubNumberOrdersReportCreateParams;
import com.telnyx.sdk.models.subnumberordersreport.SubNumberOrdersReportCreateResponse;

SubNumberOrdersReportCreateResponse subNumberOrdersReport = client.subNumberOrdersReport().create();
```

## Retrieve a sub number orders report

Get the status and details of a sub number orders report.

`GET /sub_number_orders/report/{report_id}`

```java
import com.telnyx.sdk.models.subnumberordersreport.SubNumberOrdersReportRetrieveParams;
import com.telnyx.sdk.models.subnumberordersreport.SubNumberOrdersReportRetrieveResponse;

SubNumberOrdersReportRetrieveResponse subNumberOrdersReport = client.subNumberOrdersReport().retrieve("12ade33a-21c0-473b-b055-b3c836e1c293");
```

## Download a sub number orders report

Download the CSV file for a completed sub number orders report.

`GET /sub_number_orders/report/{report_id}/download`

```java
import com.telnyx.sdk.models.subnumberordersreport.SubNumberOrdersReportDownloadParams;

String response = client.subNumberOrdersReport().download("12ade33a-21c0-473b-b055-b3c836e1c293");
```

## List Advanced Orders

`GET /advanced_orders`

```java
import com.telnyx.sdk.models.advancedorders.AdvancedOrderListParams;
import com.telnyx.sdk.models.advancedorders.AdvancedOrderListResponse;

AdvancedOrderListResponse advancedOrders = client.advancedOrders().list();
```

## Create Advanced Order

`POST /advanced_orders`

```java
import com.telnyx.sdk.models.advancedorders.AdvancedOrder;
import com.telnyx.sdk.models.advancedorders.AdvancedOrderCreateParams;
import com.telnyx.sdk.models.advancedorders.AdvancedOrderCreateResponse;

AdvancedOrder params = AdvancedOrder.builder().build();
AdvancedOrderCreateResponse advancedOrder = client.advancedOrders().create(params);
```

## Update Advanced Order

`PATCH /advanced_orders/{advanced-order-id}/requirement_group`

```java
import com.telnyx.sdk.models.advancedorders.AdvancedOrder;
import com.telnyx.sdk.models.advancedorders.AdvancedOrderUpdateRequirementGroupParams;
import com.telnyx.sdk.models.advancedorders.AdvancedOrderUpdateRequirementGroupResponse;

AdvancedOrderUpdateRequirementGroupParams params = AdvancedOrderUpdateRequirementGroupParams.builder()
    .advancedOrderId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .advancedOrder(AdvancedOrder.builder().build())
    .build();
AdvancedOrderUpdateRequirementGroupResponse response = client.advancedOrders().updateRequirementGroup(params);
```

## Get Advanced Order

`GET /advanced_orders/{order_id}`

```java
import com.telnyx.sdk.models.advancedorders.AdvancedOrderRetrieveParams;
import com.telnyx.sdk.models.advancedorders.AdvancedOrderRetrieveResponse;

AdvancedOrderRetrieveResponse advancedOrder = client.advancedOrders().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## List inexplicit number orders

Get a paginated list of inexplicit number orders.

`GET /inexplicit_number_orders`

```java
import com.telnyx.sdk.models.inexplicitnumberorders.InexplicitNumberOrderListPage;
import com.telnyx.sdk.models.inexplicitnumberorders.InexplicitNumberOrderListParams;

InexplicitNumberOrderListPage page = client.inexplicitNumberOrders().list();
```

## Create an inexplicit number order

Create an inexplicit number order to programmatically purchase phone numbers without specifying exact numbers.

`POST /inexplicit_number_orders` — Required: `ordering_groups`

```java
import com.telnyx.sdk.models.inexplicitnumberorders.InexplicitNumberOrderCreateParams;
import com.telnyx.sdk.models.inexplicitnumberorders.InexplicitNumberOrderCreateResponse;

InexplicitNumberOrderCreateParams params = InexplicitNumberOrderCreateParams.builder()
    .addOrderingGroup(InexplicitNumberOrderCreateParams.OrderingGroup.builder()
        .countRequested("count_requested")
        .countryIso(InexplicitNumberOrderCreateParams.OrderingGroup.CountryIso.US)
        .phoneNumberType("phone_number_type")
        .build())
    .build();
InexplicitNumberOrderCreateResponse inexplicitNumberOrder = client.inexplicitNumberOrders().create(params);
```

## Retrieve an inexplicit number order

Get an existing inexplicit number order by ID.

`GET /inexplicit_number_orders/{id}`

```java
import com.telnyx.sdk.models.inexplicitnumberorders.InexplicitNumberOrderRetrieveParams;
import com.telnyx.sdk.models.inexplicitnumberorders.InexplicitNumberOrderRetrieveResponse;

InexplicitNumberOrderRetrieveResponse inexplicitNumberOrder = client.inexplicitNumberOrders().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Retrieve all comments

`GET /comments`

```java
import com.telnyx.sdk.models.comments.CommentListParams;
import com.telnyx.sdk.models.comments.CommentListResponse;

CommentListResponse comments = client.comments().list();
```

## Create a comment

`POST /comments`

```java
import com.telnyx.sdk.models.comments.CommentCreateParams;
import com.telnyx.sdk.models.comments.CommentCreateResponse;

CommentCreateResponse comment = client.comments().create();
```

## Retrieve a comment

`GET /comments/{id}`

```java
import com.telnyx.sdk.models.comments.CommentRetrieveParams;
import com.telnyx.sdk.models.comments.CommentRetrieveResponse;

CommentRetrieveResponse comment = client.comments().retrieve("id");
```

## Mark a comment as read

`PATCH /comments/{id}/read`

```java
import com.telnyx.sdk.models.comments.CommentMarkAsReadParams;
import com.telnyx.sdk.models.comments.CommentMarkAsReadResponse;

CommentMarkAsReadResponse response = client.comments().markAsRead("id");
```

## List available phone number blocks

`GET /available_phone_number_blocks`

```java
import com.telnyx.sdk.models.availablephonenumberblocks.AvailablePhoneNumberBlockListParams;
import com.telnyx.sdk.models.availablephonenumberblocks.AvailablePhoneNumberBlockListResponse;

AvailablePhoneNumberBlockListResponse availablePhoneNumberBlocks = client.availablePhoneNumberBlocks().list();
```

## List available phone numbers

`GET /available_phone_numbers`

```java
import com.telnyx.sdk.models.availablephonenumbers.AvailablePhoneNumberListParams;
import com.telnyx.sdk.models.availablephonenumbers.AvailablePhoneNumberListResponse;

AvailablePhoneNumberListResponse availablePhoneNumbers = client.availablePhoneNumbers().list();
```

## Retrieve the features for a list of numbers

`POST /numbers_features` — Required: `phone_numbers`

```java
import com.telnyx.sdk.models.numbersfeatures.NumbersFeatureCreateParams;
import com.telnyx.sdk.models.numbersfeatures.NumbersFeatureCreateResponse;

NumbersFeatureCreateParams params = NumbersFeatureCreateParams.builder()
    .addPhoneNumber("string")
    .build();
NumbersFeatureCreateResponse numbersFeature = client.numbersFeatures().create(params);
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `numberOrderStatusUpdate` | Number Order Status Update |
