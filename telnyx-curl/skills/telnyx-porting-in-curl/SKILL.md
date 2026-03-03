---
name: telnyx-porting-in-curl
description: >-
  Port phone numbers into Telnyx. Check portability, create port orders, upload
  LOA documents, and track porting status. This skill provides REST API (curl)
  examples.
metadata:
  author: telnyx
  product: porting-in
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Porting In - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Run a portability check

Runs a portability check, returning the results immediately.

`POST /portability_checks`

Optional: `phone_numbers` (array[string])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "+13035550000",
    "+13035550001",
    "+13035550002"
  ]
}' \
  "https://api.telnyx.com/v2/portability_checks"
```

## List all porting events

Returns a list of all porting events.

`GET /porting/events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/events"
```

## Show a porting event

Show a specific porting event.

`GET /porting/events/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/events/{id}"
```

## Republish a porting event

Republish a specific porting event.

`POST /porting/events/{id}/republish`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting/events/{id}/republish"
```

## Preview the LOA configuration parameters

Preview the LOA template that would be generated without need to create LOA configuration.

`POST /porting/loa_configuration/preview`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting/loa_configuration/preview"
```

## List LOA configurations

List the LOA configurations.

`GET /porting/loa_configurations`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/loa_configurations"
```

## Create a LOA configuration

Create a LOA configuration.

`POST /porting/loa_configurations`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting/loa_configurations"
```

## Retrieve a LOA configuration

Retrieve a specific LOA configuration.

`GET /porting/loa_configurations/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/loa_configurations/{id}"
```

## Update a LOA configuration

Update a specific LOA configuration.

`PATCH /porting/loa_configurations/{id}`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting/loa_configurations/{id}"
```

## Delete a LOA configuration

Delete a specific LOA configuration.

`DELETE /porting/loa_configurations/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/porting/loa_configurations/{id}"
```

## Preview a LOA configuration

Preview a specific LOA configuration.

`GET /porting/loa_configurations/{id}/preview`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/loa_configurations/{id}/preview"
```

## List porting related reports

List the reports generated about porting operations.

`GET /porting/reports`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/reports"
```

## Create a porting related report

Generate reports about porting operations.

`POST /porting/reports`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting/reports"
```

## Retrieve a report

Retrieve a specific report generated.

`GET /porting/reports/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/reports/{id}"
```

## List available carriers in the UK

List available carriers in the UK.

`GET /porting/uk_carriers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting/uk_carriers"
```

## List all porting orders

Returns a list of your porting order.

`GET /porting_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders"
```

## Create a porting order

Creates a new porting order object.

`POST /porting_orders` — Required: `phone_numbers`

Optional: `customer_group_reference` (string), `customer_reference` (['string', 'null'])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "+13035550000",
    "+13035550001",
    "+13035550002"
  ],
  "customer_reference": "Acct 123abc",
  "customer_group_reference": "Group-456"
}' \
  "https://api.telnyx.com/v2/porting_orders"
```

## List all exception types

Returns a list of all possible exception types for a porting order.

`GET /porting_orders/exception_types`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/exception_types"
```

## List all phone number configurations

Returns a list of phone number configurations paginated.

`GET /porting_orders/phone_number_configurations`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/phone_number_configurations"
```

## Create a list of phone number configurations

Creates a list of phone number configurations.

`POST /porting_orders/phone_number_configurations`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/phone_number_configurations"
```

## Retrieve a porting order

Retrieves the details of an existing porting order.

`GET /porting_orders/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}"
```

## Edit a porting order

Edits the details of an existing porting order.

`PATCH /porting_orders/{id}`

Optional: `activation_settings` (object), `customer_group_reference` (string), `customer_reference` (string), `documents` (object), `end_user` (object), `messaging` (object), `misc` (object), `phone_number_configuration` (object), `requirement_group_id` (uuid), `requirements` (array[object]), `user_feedback` (object), `webhook_url` (uri)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "requirement_group_id": "DE748D99-06FA-4D90-9F9A-F4B62696BADA"
}' \
  "https://api.telnyx.com/v2/porting_orders/{id}"
```

## Delete a porting order

Deletes an existing porting order.

`DELETE /porting_orders/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/porting_orders/{id}"
```

## Activate every number in a porting order asynchronously.

Activate each number in a porting order asynchronously.

`POST /porting_orders/{id}/actions/activate`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/actions/activate"
```

## Cancel a porting order

`POST /porting_orders/{id}/actions/cancel`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/actions/cancel"
```

## Submit a porting order.

Confirm and submit your porting order.

`POST /porting_orders/{id}/actions/confirm`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/actions/confirm"
```

## Share a porting order

Creates a sharing token for a porting order.

`POST /porting_orders/{id}/actions/share`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/actions/share"
```

## List all porting activation jobs

Returns a list of your porting activation jobs.

`GET /porting_orders/{id}/activation_jobs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/activation_jobs"
```

## Retrieve a porting activation job

Returns a porting activation job.

`GET /porting_orders/{id}/activation_jobs/{activationJobId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/activation_jobs/{activationJobId}"
```

## Update a porting activation job

Updates the activation time of a porting activation job.

`PATCH /porting_orders/{id}/activation_jobs/{activationJobId}`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/activation_jobs/{activationJobId}"
```

## List additional documents

Returns a list of additional documents for a porting order.

`GET /porting_orders/{id}/additional_documents`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/additional_documents"
```

## Create a list of additional documents

Creates a list of additional documents for a porting order.

`POST /porting_orders/{id}/additional_documents`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/additional_documents"
```

## Delete an additional document

Deletes an additional document for a porting order.

`DELETE /porting_orders/{id}/additional_documents/{additional_document_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/porting_orders/{id}/additional_documents/{additional_document_id}"
```

## List allowed FOC dates

Returns a list of allowed FOC dates for a porting order.

`GET /porting_orders/{id}/allowed_foc_windows`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/allowed_foc_windows"
```

## List all comments of a porting order

Returns a list of all comments of a porting order.

`GET /porting_orders/{id}/comments`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/comments"
```

## Create a comment for a porting order

Creates a new comment for a porting order.

`POST /porting_orders/{id}/comments`

Optional: `body` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "body": "Please, let me know when the port completes"
}' \
  "https://api.telnyx.com/v2/porting_orders/{id}/comments"
```

## Download a porting order loa template

`GET /porting_orders/{id}/loa_template`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/loa_template?loa_configuration_id=a36c2277-446b-4d11-b4ea-322e02a5c08d"
```

## List porting order requirements

Returns a list of all requirements based on country/number type for this porting order.

`GET /porting_orders/{id}/requirements`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/requirements"
```

## Retrieve the associated V1 sub_request_id and port_request_id

`GET /porting_orders/{id}/sub_request`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/sub_request"
```

## List verification codes

Returns a list of verification codes for a porting order.

`GET /porting_orders/{id}/verification_codes`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{id}/verification_codes"
```

## Send the verification codes

Send the verification code for all porting phone numbers.

`POST /porting_orders/{id}/verification_codes/send`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/verification_codes/send"
```

## Verify the verification code for a list of phone numbers

Verifies the verification code for a list of phone numbers.

`POST /porting_orders/{id}/verification_codes/verify`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{id}/verification_codes/verify"
```

## List action requirements for a porting order

Returns a list of action requirements for a specific porting order.

`GET /porting_orders/{porting_order_id}/action_requirements`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/action_requirements"
```

## Initiate an action requirement

Initiates a specific action requirement for a porting order.

`POST /porting_orders/{porting_order_id}/action_requirements/{id}/initiate`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/action_requirements/{id}/initiate"
```

## List all associated phone numbers

Returns a list of all associated phone numbers for a porting order.

`GET /porting_orders/{porting_order_id}/associated_phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/associated_phone_numbers"
```

## Create an associated phone number

Creates a new associated phone number for a porting order.

`POST /porting_orders/{porting_order_id}/associated_phone_numbers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/associated_phone_numbers"
```

## Delete an associated phone number

Deletes an associated phone number from a porting order.

`DELETE /porting_orders/{porting_order_id}/associated_phone_numbers/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/associated_phone_numbers/{id}"
```

## List all phone number blocks

Returns a list of all phone number blocks of a porting order.

`GET /porting_orders/{porting_order_id}/phone_number_blocks`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/phone_number_blocks"
```

## Create a phone number block

Creates a new phone number block.

`POST /porting_orders/{porting_order_id}/phone_number_blocks`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/phone_number_blocks"
```

## Delete a phone number block

Deletes a phone number block.

`DELETE /porting_orders/{porting_order_id}/phone_number_blocks/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/phone_number_blocks/{id}"
```

## List all phone number extensions

Returns a list of all phone number extensions of a porting order.

`GET /porting_orders/{porting_order_id}/phone_number_extensions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/phone_number_extensions"
```

## Create a phone number extension

Creates a new phone number extension.

`POST /porting_orders/{porting_order_id}/phone_number_extensions`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/phone_number_extensions"
```

## Delete a phone number extension

Deletes a phone number extension.

`DELETE /porting_orders/{porting_order_id}/phone_number_extensions/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/porting_orders/{porting_order_id}/phone_number_extensions/{id}"
```

## List all porting phone numbers

Returns a list of your porting phone numbers.

`GET /porting_phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/porting_phone_numbers"
```
