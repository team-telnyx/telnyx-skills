---
name: telnyx-numbers-compliance-curl
description: >-
  Manage regulatory requirements, number bundles, supporting documents, and
  verified numbers for compliance. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: numbers-compliance
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers Compliance - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Retrieve Bundles

Get all allowed bundles.

`GET /bundle_pricing/billing_bundles`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/bundle_pricing/billing_bundles"
```

## Get Bundle By Id

Get a single bundle by ID.

`GET /bundle_pricing/billing_bundles/{bundle_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/bundle_pricing/billing_bundles/8661948c-a386-4385-837f-af00f40f111a"
```

## Get User Bundles

Get a paginated list of user bundles.

`GET /bundle_pricing/user_bundles`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/bundle_pricing/user_bundles"
```

## Create User Bundles

Creates multiple user bundles for the user.

`POST /bundle_pricing/user_bundles/bulk`

Optional: `idempotency_key` (uuid), `items` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "idempotency_key": "12ade33a-21c0-473b-b055-b3c836e1c292"
}' \
  "https://api.telnyx.com/v2/bundle_pricing/user_bundles/bulk"
```

## Get Unused User Bundles

Returns all user bundles that aren't in use.

`GET /bundle_pricing/user_bundles/unused`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/bundle_pricing/user_bundles/unused"
```

## Get User Bundle by Id

Retrieves a user bundle by its ID.

`GET /bundle_pricing/user_bundles/{user_bundle_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/bundle_pricing/user_bundles/ca1d2263-d1f1-43ac-ba53-248e7a4bb26a"
```

## Deactivate User Bundle

Deactivates a user bundle by its ID.

`DELETE /bundle_pricing/user_bundles/{user_bundle_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/bundle_pricing/user_bundles/ca1d2263-d1f1-43ac-ba53-248e7a4bb26a"
```

## Get User Bundle Resources

Retrieves the resources of a user bundle by its ID.

`GET /bundle_pricing/user_bundles/{user_bundle_id}/resources`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/bundle_pricing/user_bundles/ca1d2263-d1f1-43ac-ba53-248e7a4bb26a/resources"
```

## List all document links

List all documents links ordered by created_at descending.

`GET /document_links`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/document_links"
```

## List all documents

List all documents ordered by created_at descending.

`GET /documents`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/documents?filter={'filename': {'contains': 'invoice'}, 'customer_reference': {'in': ['REF001', 'REF002']}, 'created_at': {'gt': '2021-01-01T00:00:00Z'}}&sort=['filename']"
```

## Upload a document

Upload a document.<br /><br />Uploaded files must be linked to a service within 30 minutes or they will be automatically deleted.

`POST /documents`

Optional: `customer_reference` (string), `file` (byte), `filename` (string), `url` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "file=@/path/to/file" \
  -F "customer_reference=MY REF 001" \
  "https://api.telnyx.com/v2/documents"
```

## Retrieve a document

Retrieve a document.

`GET /documents/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/documents/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Update a document

Update a document.

`PATCH /documents/{id}`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/documents/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a document

Delete a document.<br /><br />A document can only be deleted if it's not linked to a service.

`DELETE /documents/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/documents/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Download a document

Download a document.

`GET /documents/{id}/download`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/documents/6a09cdc3-8948-47f0-aa62-74ac943d6c58/download"
```

## Generate a temporary download link for a document

Generates a temporary pre-signed URL that can be used to download the document directly from the storage backend without authentication.

`GET /documents/{id}/download_link`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/documents/550e8400-e29b-41d4-a716-446655440000/download_link"
```

## Update requirement group for a phone number order

`POST /number_order_phone_numbers/{id}/requirement_group` — Required: `requirement_group_id`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "requirement_group_id": "550e8400-e29b-41d4-a716-446655440000"
}' \
  "https://api.telnyx.com/v2/number_order_phone_numbers/{id}/requirement_group"
```

## Retrieve regulatory requirements for a list of phone numbers

`GET /phone_numbers_regulatory_requirements`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers_regulatory_requirements"
```

## Retrieve regulatory requirements

`GET /regulatory_requirements`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/regulatory_requirements"
```

## List requirement groups

`GET /requirement_groups`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/requirement_groups"
```

## Create a new requirement group

`POST /requirement_groups` — Required: `country_code`, `phone_number_type`, `action`

Optional: `customer_reference` (string), `regulatory_requirements` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "country_code": "US",
  "phone_number_type": "local",
  "action": "ordering",
  "customer_reference": "My Requirement Group"
}' \
  "https://api.telnyx.com/v2/requirement_groups"
```

## Get a single requirement group by ID

`GET /requirement_groups/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/requirement_groups/{id}"
```

## Update requirement values in requirement group

`PATCH /requirement_groups/{id}`

Optional: `customer_reference` (string), `regulatory_requirements` (array[object])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_reference": "0002"
}' \
  "https://api.telnyx.com/v2/requirement_groups/{id}"
```

## Delete a requirement group by ID

`DELETE /requirement_groups/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/requirement_groups/{id}"
```

## Submit a Requirement Group for Approval

`POST /requirement_groups/{id}/submit_for_approval`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/requirement_groups/{id}/submit_for_approval"
```

## List all requirement types

List all requirement types ordered by created_at descending

`GET /requirement_types`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/requirement_types?sort=['name']"
```

## Retrieve a requirement types

Retrieve a requirement type by id

`GET /requirement_types/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/requirement_types/a38c217a-8019-48f8-bff6-0fdd9939075b"
```

## List all requirements

List all requirements with filtering, sorting, and pagination

`GET /requirements`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/requirements?sort=['country_code']"
```

## Retrieve a document requirement

Retrieve a document requirement record

`GET /requirements/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/requirements/a9dad8d5-fdbd-49d7-aa23-39bb08a5ebaa"
```

## Update requirement group for a sub number order

`POST /sub_number_orders/{id}/requirement_group` — Required: `requirement_group_id`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "requirement_group_id": "a4b201f9-8646-4e54-a7d2-b2e403eeaf8c"
}' \
  "https://api.telnyx.com/v2/sub_number_orders/{id}/requirement_group"
```

## List all user addresses

Returns a list of your user addresses.

`GET /user_addresses`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/user_addresses?sort=street_address"
```

## Creates a user address

Creates a user address.

`POST /user_addresses` — Required: `first_name`, `last_name`, `business_name`, `street_address`, `locality`, `country_code`

Optional: `administrative_area` (string), `borough` (string), `customer_reference` (string), `extended_address` (string), `neighborhood` (string), `phone_number` (string), `postal_code` (string), `skip_address_verification` (boolean)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_reference": "MY REF 001",
  "first_name": "Alfred",
  "last_name": "Foster",
  "business_name": "Toy-O'Kon",
  "phone_number": "+12125559000",
  "street_address": "600 Congress Avenue",
  "extended_address": "14th Floor",
  "locality": "Austin",
  "administrative_area": "TX",
  "neighborhood": "Ciudad de los deportes",
  "borough": "Guadalajara",
  "postal_code": "78701",
  "country_code": "US"
}' \
  "https://api.telnyx.com/v2/user_addresses"
```

## Retrieve a user address

Retrieves the details of an existing user address.

`GET /user_addresses/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/user_addresses/{id}"
```

## List all Verified Numbers

Gets a paginated list of Verified Numbers.

`GET /verified_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verified_numbers"
```

## Request phone number verification

Initiates phone number verification procedure.

`POST /verified_numbers` — Required: `phone_number`, `verification_method`

Optional: `extension` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_number": "+15551234567",
  "verification_method": "sms",
  "extension": "ww243w1"
}' \
  "https://api.telnyx.com/v2/verified_numbers"
```

## Retrieve a verified number

`GET /verified_numbers/{phone_number}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/verified_numbers/+15551234567"
```

## Delete a verified number

`DELETE /verified_numbers/{phone_number}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/verified_numbers/+15551234567"
```

## Submit verification code

`POST /verified_numbers/{phone_number}/actions/verify` — Required: `verification_code`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "verification_code": "123456"
}' \
  "https://api.telnyx.com/v2/verified_numbers/+15551234567/actions/verify"
```
