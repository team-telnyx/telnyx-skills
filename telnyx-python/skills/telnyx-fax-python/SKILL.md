---
name: telnyx-fax-python
description: >-
  Send and receive faxes programmatically. Manage fax applications and media.
  This skill provides Python SDK examples.
metadata:
  author: telnyx
  product: fax
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Fax - Python

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

## List all Fax Applications

This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response.

`GET /fax_applications`

```python
page = client.fax_applications.list()
page = page.data[0]
print(page.id)
```

## Creates a Fax Application

Creates a new Fax Application based on the parameters sent in the request.

`POST /fax_applications` — Required: `application_name`, `webhook_event_url`

```python
fax_application = client.fax_applications.create(
    application_name="fax-router",
    webhook_event_url="https://example.com",
)
print(fax_application.data)
```

## Retrieve a Fax Application

Return the details of an existing Fax Application inside the 'data' attribute of the response.

`GET /fax_applications/{id}`

```python
fax_application = client.fax_applications.retrieve(
    "1293384261075731499",
)
print(fax_application.data)
```

## Update a Fax Application

Updates settings of an existing Fax Application based on the parameters of the request.

`PATCH /fax_applications/{id}` — Required: `application_name`, `webhook_event_url`

```python
fax_application = client.fax_applications.update(
    id="1293384261075731499",
    application_name="fax-router",
    webhook_event_url="https://example.com",
)
print(fax_application.data)
```

## Deletes a Fax Application

Permanently deletes a Fax Application.

`DELETE /fax_applications/{id}`

```python
fax_application = client.fax_applications.delete(
    "1293384261075731499",
)
print(fax_application.data)
```

## View a list of faxes

`GET /faxes`

```python
page = client.faxes.list()
page = page.data[0]
print(page.id)
```

## Send a fax

Send a fax.

`POST /faxes` — Required: `connection_id`, `from`, `to`

```python
fax = client.faxes.create(
    connection_id="234423",
    from_="+13125790015",
    to="+13127367276",
)
print(fax.data)
```

## View a fax

`GET /faxes/{id}`

```python
fax = client.faxes.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(fax.data)
```

## Delete a fax

`DELETE /faxes/{id}`

```python
client.faxes.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Cancel a fax

Cancel the outbound fax that is in one of the following states: `queued`, `media.processed`, `originated` or `sending`

`POST /faxes/{id}/actions/cancel`

```python
response = client.faxes.actions.cancel(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.data)
```

## Refresh a fax

Refreshes the inbound fax's media_url when it has expired

`POST /faxes/{id}/actions/refresh`

```python
response = client.faxes.actions.refresh(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.data)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `fax.delivered` | Fax Delivered |
| `fax.failed` | Fax Failed |
| `fax.media.processed` | Fax Media Processed |
| `fax.queued` | Fax Queued |
| `fax.sending.started` | Fax Sending Started |
