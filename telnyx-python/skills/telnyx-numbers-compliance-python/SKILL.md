---
name: telnyx-numbers-compliance-python
description: >-
  Manage regulatory requirements, number bundles, supporting documents, and
  verified numbers for compliance. This skill provides Python SDK examples.
metadata:
  author: telnyx
  product: numbers-compliance
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers Compliance - Python

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

## Retrieve Bundles

Get all allowed bundles.

`GET /bundle_pricing/billing_bundles`

```python
page = client.bundle_pricing.billing_bundles.list()
page = page.data[0]
print(page.id)
```

## Get Bundle By Id

Get a single bundle by ID.

`GET /bundle_pricing/billing_bundles/{bundle_id}`

```python
billing_bundle = client.bundle_pricing.billing_bundles.retrieve(
    bundle_id="8661948c-a386-4385-837f-af00f40f111a",
)
print(billing_bundle.data)
```

## Get User Bundles

Get a paginated list of user bundles.

`GET /bundle_pricing/user_bundles`

```python
page = client.bundle_pricing.user_bundles.list()
page = page.data[0]
print(page.id)
```

## Create User Bundles

Creates multiple user bundles for the user.

`POST /bundle_pricing/user_bundles/bulk`

Optional: `idempotency_key` (uuid), `items` (array[object])

```python
user_bundle = client.bundle_pricing.user_bundles.create()
print(user_bundle.data)
```

## Get Unused User Bundles

Returns all user bundles that aren't in use.

`GET /bundle_pricing/user_bundles/unused`

```python
response = client.bundle_pricing.user_bundles.list_unused()
print(response.data)
```

## Get User Bundle by Id

Retrieves a user bundle by its ID.

`GET /bundle_pricing/user_bundles/{user_bundle_id}`

```python
user_bundle = client.bundle_pricing.user_bundles.retrieve(
    user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
)
print(user_bundle.data)
```

## Deactivate User Bundle

Deactivates a user bundle by its ID.

`DELETE /bundle_pricing/user_bundles/{user_bundle_id}`

```python
response = client.bundle_pricing.user_bundles.deactivate(
    user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
)
print(response.data)
```

## Get User Bundle Resources

Retrieves the resources of a user bundle by its ID.

`GET /bundle_pricing/user_bundles/{user_bundle_id}/resources`

```python
response = client.bundle_pricing.user_bundles.list_resources(
    user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
)
print(response.data)
```

## List all document links

List all documents links ordered by created_at descending.

`GET /document_links`

```python
page = client.document_links.list()
page = page.data[0]
print(page.id)
```

## List all documents

List all documents ordered by created_at descending.

`GET /documents`

```python
page = client.documents.list()
page = page.data[0]
print(page.id)
```

## Upload a document

Upload a document.<br /><br />Uploaded files must be linked to a service within 30 minutes or they will be automatically deleted.

`POST /documents`

Optional: `customer_reference` (string), `file` (byte), `filename` (string), `url` (string)

```python
response = client.documents.upload_json(
    document={},
)
print(response.data)
```

## Retrieve a document

Retrieve a document.

`GET /documents/{id}`

```python
document = client.documents.retrieve(
    "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
)
print(document.data)
```

## Update a document

Update a document.

`PATCH /documents/{id}`

```python
document = client.documents.update(
    document_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
)
print(document.data)
```

## Delete a document

Delete a document.<br /><br />A document can only be deleted if it's not linked to a service.

`DELETE /documents/{id}`

```python
document = client.documents.delete(
    "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
)
print(document.data)
```

## Download a document

Download a document.

`GET /documents/{id}/download`

```python
response = client.documents.download(
    "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
)
print(response)
content = response.read()
print(content)
```

## Generate a temporary download link for a document

Generates a temporary pre-signed URL that can be used to download the document directly from the storage backend without authentication.

`GET /documents/{id}/download_link`

```python
response = client.documents.generate_download_link(
    "550e8400-e29b-41d4-a716-446655440000",
)
print(response.data)
```

## List all requirements

List all requirements with filtering, sorting, and pagination

`GET /requirements`

```python
page = client.requirements.list()
page = page.data[0]
print(page.id)
```

## Retrieve a document requirement

Retrieve a document requirement record

`GET /requirements/{id}`

```python
requirement = client.requirements.retrieve(
    "a9dad8d5-fdbd-49d7-aa23-39bb08a5ebaa",
)
print(requirement.data)
```

## List all requirement types

List all requirement types ordered by created_at descending

`GET /requirement_types`

```python
requirement_types = client.requirement_types.list()
print(requirement_types.data)
```

## Retrieve a requirement types

Retrieve a requirement type by id

`GET /requirement_types/{id}`

```python
requirement_type = client.requirement_types.retrieve(
    "a38c217a-8019-48f8-bff6-0fdd9939075b",
)
print(requirement_type.data)
```

## Retrieve regulatory requirements

`GET /regulatory_requirements`

```python
regulatory_requirement = client.regulatory_requirements.retrieve()
print(regulatory_requirement.data)
```

## List requirement groups

`GET /requirement_groups`

```python
requirement_groups = client.requirement_groups.list()
print(requirement_groups)
```

## Create a new requirement group

`POST /requirement_groups` — Required: `country_code`, `phone_number_type`, `action`

Optional: `customer_reference` (string), `regulatory_requirements` (array[object])

```python
requirement_group = client.requirement_groups.create(
    action="ordering",
    country_code="US",
    phone_number_type="local",
)
print(requirement_group.id)
```

## Get a single requirement group by ID

`GET /requirement_groups/{id}`

```python
requirement_group = client.requirement_groups.retrieve(
    "id",
)
print(requirement_group.id)
```

## Update requirement values in requirement group

`PATCH /requirement_groups/{id}`

Optional: `customer_reference` (string), `regulatory_requirements` (array[object])

```python
requirement_group = client.requirement_groups.update(
    id="id",
)
print(requirement_group.id)
```

## Delete a requirement group by ID

`DELETE /requirement_groups/{id}`

```python
requirement_group = client.requirement_groups.delete(
    "id",
)
print(requirement_group.id)
```

## Submit a Requirement Group for Approval

`POST /requirement_groups/{id}/submit_for_approval`

```python
requirement_group = client.requirement_groups.submit_for_approval(
    "id",
)
print(requirement_group.id)
```

## List all Verified Numbers

Gets a paginated list of Verified Numbers.

`GET /verified_numbers`

```python
page = client.verified_numbers.list()
page = page.data[0]
print(page.phone_number)
```

## Request phone number verification

Initiates phone number verification procedure.

`POST /verified_numbers` — Required: `phone_number`, `verification_method`

Optional: `extension` (string)

```python
verified_number = client.verified_numbers.create(
    phone_number="+15551234567",
    verification_method="sms",
)
print(verified_number.phone_number)
```

## Retrieve a verified number

`GET /verified_numbers/{phone_number}`

```python
verified_number_data_wrapper = client.verified_numbers.retrieve(
    "+15551234567",
)
print(verified_number_data_wrapper.data)
```

## Delete a verified number

`DELETE /verified_numbers/{phone_number}`

```python
verified_number_data_wrapper = client.verified_numbers.delete(
    "+15551234567",
)
print(verified_number_data_wrapper.data)
```

## Submit verification code

`POST /verified_numbers/{phone_number}/actions/verify` — Required: `verification_code`

```python
verified_number_data_wrapper = client.verified_numbers.actions.submit_verification_code(
    phone_number="+15551234567",
    verification_code="123456",
)
print(verified_number_data_wrapper.data)
```
