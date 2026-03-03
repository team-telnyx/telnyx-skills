---
name: telnyx-porting-out-curl
description: >-
  Manage port-out requests when numbers are being ported away from Telnyx. List,
  view, and update port-out status. This skill provides REST API (curl)
  examples.
metadata:
  author: telnyx
  product: porting-out
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Porting Out - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List portout requests

Returns the portout requests according to filters

`GET /portouts`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts"
```

## List all port-out events

Returns a list of all port-out events.

`GET /portouts/events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/events"
```

## Show a port-out event

Show a specific port-out event.

`GET /portouts/events/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/events/{id}"
```

## Republish a port-out event

Republish a specific port-out event.

`POST /portouts/events/{id}/republish`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/portouts/events/{id}/republish"
```

## List eligible port-out rejection codes for a specific order

Given a port-out ID, list rejection codes that are eligible for that port-out

`GET /portouts/rejections/{portout_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/rejections/329d6658-8f93-405d-862f-648776e8afd7"
```

## List port-out related reports

List the reports generated about port-out operations.

`GET /portouts/reports`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/reports"
```

## Create a port-out related report

Generate reports about port-out operations.

`POST /portouts/reports`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/portouts/reports"
```

## Retrieve a report

Retrieve a specific report generated.

`GET /portouts/reports/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/reports/{id}"
```

## Get a portout request

Returns the portout request based on the ID provided

`GET /portouts/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/{id}"
```

## List all comments for a portout request

Returns a list of comments for a portout request.

`GET /portouts/{id}/comments`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/{id}/comments"
```

## Create a comment on a portout request

Creates a comment on a portout request.

`POST /portouts/{id}/comments`

Optional: `body` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/portouts/{id}/comments"
```

## List supporting documents on a portout request

List every supporting documents for a portout request.

`GET /portouts/{id}/supporting_documents`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/portouts/{id}/supporting_documents"
```

## Create a list of supporting documents on a portout request

Creates a list of supporting documents on a portout request.

`POST /portouts/{id}/supporting_documents`

Optional: `documents` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/portouts/{id}/supporting_documents"
```

## Update Status

Authorize or reject portout request

`PATCH /portouts/{id}/{status}` — Required: `reason`

Optional: `host_messaging` (boolean)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "reason": "I do not recognize this transaction",
  "host_messaging": false
}' \
  "https://api.telnyx.com/v2/portouts/{id}/{status}"
```
