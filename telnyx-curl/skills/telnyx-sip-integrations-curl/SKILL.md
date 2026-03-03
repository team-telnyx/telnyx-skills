---
name: telnyx-sip-integrations-curl
description: >-
  Manage call recordings, media storage, Dialogflow integration, and external
  connections for SIP trunking. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: sip-integrations
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Sip Integrations - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Retrieve a stored credential

Returns the information about custom storage credentials.

`GET /custom_storage_credentials/{connection_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/custom_storage_credentials/{connection_id}"
```

## Create a custom storage credential

Creates a custom storage credentials configuration.

`POST /custom_storage_credentials/{connection_id}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/custom_storage_credentials/{connection_id}"
```

## Update a stored credential

Updates a stored custom credentials configuration.

`PUT /custom_storage_credentials/{connection_id}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/custom_storage_credentials/{connection_id}"
```

## Delete a stored credential

Deletes a stored custom credentials configuration.

`DELETE /custom_storage_credentials/{connection_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/custom_storage_credentials/{connection_id}"
```

## Retrieve stored Dialogflow Connection

Return details of the Dialogflow connection associated with the given CallControl connection.

`GET /dialogflow_connections/{connection_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/dialogflow_connections/{connection_id}"
```

## Create a Dialogflow Connection

Save Dialogflow Credentiails to Telnyx, so it can be used with other Telnyx services.

`POST /dialogflow_connections/{connection_id}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/dialogflow_connections/{connection_id}"
```

## Update stored Dialogflow Connection

Updates a stored Dialogflow Connection.

`PUT /dialogflow_connections/{connection_id}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/dialogflow_connections/{connection_id}"
```

## Delete stored Dialogflow Connection

Deletes a stored Dialogflow Connection.

`DELETE /dialogflow_connections/{connection_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/dialogflow_connections/{connection_id}"
```

## List all External Connections

This endpoint returns a list of your External Connections inside the 'data' attribute of the response.

`GET /external_connections`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections"
```

## Creates an External Connection

Creates a new External Connection based on the parameters sent in the request.

`POST /external_connections` — Required: `external_sip_connection`, `outbound`

Optional: `active` (boolean), `inbound` (object), `tags` (array[string]), `webhook_event_failover_url` (uri), `webhook_event_url` (uri), `webhook_timeout_secs` (['integer', 'null'])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "active": false,
  "external_sip_connection": "zoom",
  "tags": [
    "tag1",
    "tag2"
  ],
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25,
  "outbound": {}
}' \
  "https://api.telnyx.com/v2/external_connections"
```

## List all log messages

Retrieve a list of log messages for all external connections associated with your account.

`GET /external_connections/log_messages`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/log_messages"
```

## Retrieve a log message

Retrieve a log message for an external connection associated with your account.

`GET /external_connections/log_messages/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/log_messages/1293384261075731499"
```

## Dismiss a log message

Dismiss a log message for an external connection associated with your account.

`DELETE /external_connections/log_messages/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/external_connections/log_messages/1293384261075731499"
```

## Retrieve an External Connection

Return the details of an existing External Connection inside the 'data' attribute of the response.

`GET /external_connections/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499"
```

## Update an External Connection

Updates settings of an existing External Connection based on the parameters of the request.

`PATCH /external_connections/{id}` — Required: `outbound`

Optional: `active` (boolean), `inbound` (object), `tags` (array[string]), `webhook_event_failover_url` (uri), `webhook_event_url` (uri), `webhook_timeout_secs` (['integer', 'null'])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "active": false,
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "tags": [
    "tag1",
    "tag2"
  ],
  "webhook_timeout_secs": 25,
  "outbound": {}
}' \
  "https://api.telnyx.com/v2/external_connections/1293384261075731499"
```

## Deletes an External Connection

Permanently deletes an External Connection.

`DELETE /external_connections/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/external_connections/1293384261075731499"
```

## List all civic addresses and locations

Returns the civic addresses and locations from Microsoft Teams.

`GET /external_connections/{id}/civic_addresses`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/civic_addresses"
```

## Retrieve a Civic Address

Return the details of an existing Civic Address with its Locations inside the 'data' attribute of the response.

`GET /external_connections/{id}/civic_addresses/{address_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/civic_addresses/318fb664-d341-44d2-8405-e6bfb9ced6d9"
```

## Update a location's static emergency address

`PATCH /external_connections/{id}/locations/{location_id}` — Required: `static_emergency_address_id`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "static_emergency_address_id": "550e8400-e29b-41d4-a716-446655440000"
}' \
  "https://api.telnyx.com/v2/external_connections/{id}/locations/{location_id}"
```

## List all phone numbers

Returns a list of all active phone numbers associated with the given external connection.

`GET /external_connections/{id}/phone_numbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/phone_numbers"
```

## Retrieve a phone number

Return the details of a phone number associated with the given external connection.

`GET /external_connections/{id}/phone_numbers/{phone_number_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/phone_numbers/1234567889"
```

## Update a phone number

Asynchronously update settings of the phone number associated with the given external connection.

`PATCH /external_connections/{id}/phone_numbers/{phone_number_id}`

Optional: `location_id` (uuid)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/external_connections/1293384261075731499/phone_numbers/1234567889"
```

## List all Releases

Returns a list of your Releases for the given external connection.

`GET /external_connections/{id}/releases`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/releases"
```

## Retrieve a Release request

Return the details of a Release request and its phone numbers.

`GET /external_connections/{id}/releases/{release_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/releases/7b6a6449-b055-45a6-81f6-f6f0dffa4cc6"
```

## List all Upload requests

Returns a list of your Upload requests for the given external connection.

`GET /external_connections/{id}/uploads`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/uploads"
```

## Creates an Upload request

Creates a new Upload request to Microsoft teams with the included phone numbers.

`POST /external_connections/{id}/uploads` — Required: `number_ids`

Optional: `additional_usages` (array[string]), `civic_address_id` (uuid), `location_id` (uuid), `usage` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "number_ids": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/external_connections/1293384261075731499/uploads"
```

## Refresh the status of all Upload requests

Forces a recheck of the status of all pending Upload requests for the given external connection in the background.

`POST /external_connections/{id}/uploads/refresh`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/external_connections/1293384261075731499/uploads/refresh"
```

## Get the count of pending upload requests

Returns the count of all pending upload requests for the given external connection.

`GET /external_connections/{id}/uploads/status`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/uploads/status"
```

## Retrieve an Upload request

Return the details of an Upload request and its phone numbers.

`GET /external_connections/{id}/uploads/{ticket_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/external_connections/1293384261075731499/uploads/7b6a6449-b055-45a6-81f6-f6f0dffa4cc6"
```

## Retry an Upload request

If there were any errors during the upload process, this endpoint will retry the upload request.

`POST /external_connections/{id}/uploads/{ticket_id}/retry`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/external_connections/1293384261075731499/uploads/7b6a6449-b055-45a6-81f6-f6f0dffa4cc6/retry"
```

## List uploaded media

Returns a list of stored media files.

`GET /media`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/media"
```

## Upload media

Upload media file to Telnyx so it can be used with other Telnyx services

`POST /media` — Required: `media_url`

Optional: `media_name` (string), `ttl_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "media=@/path/to/file" \
  -F "ttl_secs=86400" \
  -F "media_name=my_file" \
  "https://api.telnyx.com/v2/media"
```

## Retrieve stored media

Returns the information about a stored media file.

`GET /media/{media_name}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/media/{media_name}"
```

## Update stored media

Updates a stored media file.

`PUT /media/{media_name}`

Optional: `media_url` (string), `ttl_secs` (integer)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "media=@/path/to/file" \
  -F "ttl_secs=86400" \
  "https://api.telnyx.com/v2/media/{media_name}"
```

## Deletes stored media

Deletes a stored media file.

`DELETE /media/{media_name}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/media/{media_name}"
```

## Download stored media

Downloads a stored media file.

`GET /media/{media_name}/download`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/media/{media_name}/download"
```

## Refresh Operator Connect integration

This endpoint will make an asynchronous request to refresh the Operator Connect integration with Microsoft Teams for the current user.

`POST /operator_connect/actions/refresh`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/operator_connect/actions/refresh"
```

## List all recording transcriptions

Returns a list of your recording transcriptions.

`GET /recording_transcriptions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/recording_transcriptions"
```

## Retrieve a recording transcription

Retrieves the details of an existing recording transcription.

`GET /recording_transcriptions/{recording_transcription_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/recording_transcriptions/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a recording transcription

Permanently deletes a recording transcription.

`DELETE /recording_transcriptions/{recording_transcription_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/recording_transcriptions/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## List all call recordings

Returns a list of your call recordings.

`GET /recordings`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/recordings"
```

## Delete a list of call recordings

Permanently deletes a list of call recordings.

`POST /recordings/actions/delete`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/recordings/actions/delete"
```

## Retrieve a call recording

Retrieves the details of an existing call recording.

`GET /recordings/{recording_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/recordings/{recording_id}"
```

## Delete a call recording

Permanently deletes a call recording.

`DELETE /recordings/{recording_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/recordings/{recording_id}"
```

## Create a SIPREC connector

Creates a new SIPREC connector configuration.

`POST /siprec_connectors`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/siprec_connectors"
```

## Retrieve a SIPREC connector

Returns details of a stored SIPREC connector.

`GET /siprec_connectors/{connector_name}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/siprec_connectors/{connector_name}"
```

## Update a SIPREC connector

Updates a stored SIPREC connector configuration.

`PUT /siprec_connectors/{connector_name}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/siprec_connectors/{connector_name}"
```

## Delete a SIPREC connector

Deletes a stored SIPREC connector.

`DELETE /siprec_connectors/{connector_name}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/siprec_connectors/{connector_name}"
```
