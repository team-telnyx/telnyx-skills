---
name: telnyx-video-curl
description: >-
  Create and manage video rooms for real-time video communication and
  conferencing. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: video
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Video - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## View a list of room compositions.

`GET /room_compositions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_compositions"
```

## Create a room composition.

Asynchronously create a room composition.

`POST /room_compositions`

Optional: `format` (string), `resolution` (string), `session_id` (uuid), `video_layout` (object), `webhook_event_failover_url` (uri), `webhook_event_url` (uri), `webhook_timeout_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "format": "mp4",
  "resolution": "800x600",
  "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777b0",
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25
}' \
  "https://api.telnyx.com/v2/room_compositions"
```

## View a room composition.

`GET /room_compositions/{room_composition_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_compositions/5219b3af-87c6-4c08-9b58-5a533d893e21"
```

## Delete a room composition.

Synchronously delete a room composition.

`DELETE /room_compositions/{room_composition_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/room_compositions/5219b3af-87c6-4c08-9b58-5a533d893e21"
```

## View a list of room participants.

`GET /room_participants`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_participants"
```

## View a room participant.

`GET /room_participants/{room_participant_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_participants/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0"
```

## View a list of room recordings.

`GET /room_recordings`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_recordings"
```

## Delete several room recordings in a bulk.

`DELETE /room_recordings`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/room_recordings"
```

## View a room recording.

`GET /room_recordings/{room_recording_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_recordings/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0"
```

## Delete a room recording.

Synchronously delete a Room Recording.

`DELETE /room_recordings/{room_recording_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/room_recordings/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0"
```

## View a list of room sessions.

`GET /room_sessions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_sessions?include_participants=True"
```

## View a room session.

`GET /room_sessions/{room_session_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_sessions/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0?include_participants=True"
```

## End a room session.

Note: this will also kick all participants currently present in the room

`POST /room_sessions/{room_session_id}/actions/end`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/room_sessions/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/actions/end"
```

## Kick participants from a room session.

`POST /room_sessions/{room_session_id}/actions/kick`

Optional: `exclude` (array[string]), `participants` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/room_sessions/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/actions/kick"
```

## Mute participants in room session.

`POST /room_sessions/{room_session_id}/actions/mute`

Optional: `exclude` (array[string]), `participants` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/room_sessions/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/actions/mute"
```

## Unmute participants in room session.

`POST /room_sessions/{room_session_id}/actions/unmute`

Optional: `exclude` (array[string]), `participants` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/room_sessions/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/actions/unmute"
```

## View a list of room participants.

`GET /room_sessions/{room_session_id}/participants`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/room_sessions/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/participants"
```

## View a list of rooms.

`GET /rooms`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/rooms?include_sessions=True"
```

## Create a room.

Synchronously create a Room.

`POST /rooms`

Optional: `enable_recording` (boolean), `max_participants` (integer), `unique_name` (string), `webhook_event_failover_url` (uri), `webhook_event_url` (uri), `webhook_timeout_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "unique_name": "My room",
  "max_participants": 10,
  "enable_recording": true,
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25
}' \
  "https://api.telnyx.com/v2/rooms"
```

## View a room.

`GET /rooms/{room_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/rooms/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0?include_sessions=True"
```

## Update a room.

Synchronously update a Room.

`PATCH /rooms/{room_id}`

Optional: `enable_recording` (boolean), `max_participants` (integer), `unique_name` (string), `webhook_event_failover_url` (uri), `webhook_event_url` (uri), `webhook_timeout_secs` (integer)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "unique_name": "My room",
  "max_participants": 10,
  "enable_recording": true,
  "webhook_event_url": "https://example.com",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25
}' \
  "https://api.telnyx.com/v2/rooms/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0"
```

## Delete a room.

Synchronously delete a Room.

`DELETE /rooms/{room_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/rooms/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0"
```

## Create Client Token to join a room.

Synchronously create an Client Token to join a Room.

`POST /rooms/{room_id}/actions/generate_join_client_token`

Optional: `refresh_token_ttl_secs` (integer), `token_ttl_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "token_ttl_secs": 600,
  "refresh_token_ttl_secs": 3600
}' \
  "https://api.telnyx.com/v2/rooms/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/actions/generate_join_client_token"
```

## Refresh Client Token to join a room.

Synchronously refresh an Client Token to join a Room.

`POST /rooms/{room_id}/actions/refresh_client_token` — Required: `refresh_token`

Optional: `token_ttl_secs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "token_ttl_secs": 600,
  "refresh_token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0ZWxueXhfdGVsZXBob255IiwiZXhwIjoxNTkwMDEwMTQzLCJpYXQiOjE1ODc1OTA5NDMsImlzcyI6InRlbG55eF90ZWxlcGhvbnkiLCJqdGkiOiJiOGM3NDgzNy1kODllLTRhNjUtOWNmMi0zNGM3YTZmYTYwYzgiLCJuYmYiOjE1ODc1OTA5NDIsInN1YiI6IjVjN2FjN2QwLWRiNjUtNGYxMS05OGUxLWVlYzBkMWQ1YzZhZSIsInRlbF90b2tlbiI6InJqX1pra1pVT1pNeFpPZk9tTHBFVUIzc2lVN3U2UmpaRmVNOXMtZ2JfeENSNTZXRktGQUppTXlGMlQ2Q0JSbWxoX1N5MGlfbGZ5VDlBSThzRWlmOE1USUlzenl6U2xfYURuRzQ4YU81MHlhSEd1UlNZYlViU1ltOVdJaVEwZz09IiwidHlwIjoiYWNjZXNzIn0.gNEwzTow5MLLPLQENytca7pUN79PmPj6FyqZWW06ZeEmesxYpwKh0xRtA0TzLh6CDYIRHrI8seofOO0YFGDhpQ"
}' \
  "https://api.telnyx.com/v2/rooms/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/actions/refresh_client_token"
```

## View a list of room sessions.

`GET /rooms/{room_id}/sessions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/rooms/0ccc7b54-4df3-4bca-a65a-3da1ecc777f0/sessions?include_participants=True"
```
