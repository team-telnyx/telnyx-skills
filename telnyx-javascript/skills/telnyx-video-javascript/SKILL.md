---
name: telnyx-video-javascript
description: >-
  Create and manage video rooms for real-time video communication and
  conferencing. This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: video
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Video - JavaScript

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

## View a list of room compositions.

`GET /room_compositions`

```javascript
// Automatically fetches more pages as needed.
for await (const roomComposition of client.roomCompositions.list()) {
  console.log(roomComposition.id);
}
```

## Create a room composition.

Asynchronously create a room composition.

`POST /room_compositions`

```javascript
const roomComposition = await client.roomCompositions.create();

console.log(roomComposition.data);
```

## View a room composition.

`GET /room_compositions/{room_composition_id}`

```javascript
const roomComposition = await client.roomCompositions.retrieve(
  '5219b3af-87c6-4c08-9b58-5a533d893e21',
);

console.log(roomComposition.data);
```

## Delete a room composition.

Synchronously delete a room composition.

`DELETE /room_compositions/{room_composition_id}`

```javascript
await client.roomCompositions.delete('5219b3af-87c6-4c08-9b58-5a533d893e21');
```

## View a list of room participants.

`GET /room_participants`

```javascript
// Automatically fetches more pages as needed.
for await (const roomParticipant of client.roomParticipants.list()) {
  console.log(roomParticipant.id);
}
```

## View a room participant.

`GET /room_participants/{room_participant_id}`

```javascript
const roomParticipant = await client.roomParticipants.retrieve(
  '0ccc7b54-4df3-4bca-a65a-3da1ecc777f0',
);

console.log(roomParticipant.data);
```

## View a list of room recordings.

`GET /room_recordings`

```javascript
// Automatically fetches more pages as needed.
for await (const roomRecordingListResponse of client.roomRecordings.list()) {
  console.log(roomRecordingListResponse.id);
}
```

## Delete several room recordings in a bulk.

`DELETE /room_recordings`

```javascript
const response = await client.roomRecordings.deleteBulk();

console.log(response.data);
```

## View a room recording.

`GET /room_recordings/{room_recording_id}`

```javascript
const roomRecording = await client.roomRecordings.retrieve('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(roomRecording.data);
```

## Delete a room recording.

Synchronously delete a Room Recording.

`DELETE /room_recordings/{room_recording_id}`

```javascript
await client.roomRecordings.delete('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');
```

## View a list of room sessions.

`GET /room_sessions`

```javascript
// Automatically fetches more pages as needed.
for await (const roomSession of client.rooms.sessions.list0()) {
  console.log(roomSession.id);
}
```

## View a room session.

`GET /room_sessions/{room_session_id}`

```javascript
const session = await client.rooms.sessions.retrieve('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(session.data);
```

## End a room session.

Note: this will also kick all participants currently present in the room

`POST /room_sessions/{room_session_id}/actions/end`

```javascript
const response = await client.rooms.sessions.actions.end('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(response.data);
```

## Kick participants from a room session.

`POST /room_sessions/{room_session_id}/actions/kick`

```javascript
const response = await client.rooms.sessions.actions.kick('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(response.data);
```

## Mute participants in room session.

`POST /room_sessions/{room_session_id}/actions/mute`

```javascript
const response = await client.rooms.sessions.actions.mute('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(response.data);
```

## Unmute participants in room session.

`POST /room_sessions/{room_session_id}/actions/unmute`

```javascript
const response = await client.rooms.sessions.actions.unmute('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(response.data);
```

## View a list of room participants.

`GET /room_sessions/{room_session_id}/participants`

```javascript
// Automatically fetches more pages as needed.
for await (const roomParticipant of client.rooms.sessions.retrieveParticipants(
  '0ccc7b54-4df3-4bca-a65a-3da1ecc777f0',
)) {
  console.log(roomParticipant.id);
}
```

## View a list of rooms.

`GET /rooms`

```javascript
// Automatically fetches more pages as needed.
for await (const room of client.rooms.list()) {
  console.log(room.id);
}
```

## Create a room.

Synchronously create a Room.

`POST /rooms`

```javascript
const room = await client.rooms.create();

console.log(room.data);
```

## View a room.

`GET /rooms/{room_id}`

```javascript
const room = await client.rooms.retrieve('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(room.data);
```

## Update a room.

Synchronously update a Room.

`PATCH /rooms/{room_id}`

```javascript
const room = await client.rooms.update('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');

console.log(room.data);
```

## Delete a room.

Synchronously delete a Room.

`DELETE /rooms/{room_id}`

```javascript
await client.rooms.delete('0ccc7b54-4df3-4bca-a65a-3da1ecc777f0');
```

## Create Client Token to join a room.

Synchronously create an Client Token to join a Room.

`POST /rooms/{room_id}/actions/generate_join_client_token`

```javascript
const response = await client.rooms.actions.generateJoinClientToken(
  '0ccc7b54-4df3-4bca-a65a-3da1ecc777f0',
);

console.log(response.data);
```

## Refresh Client Token to join a room.

Synchronously refresh an Client Token to join a Room.

`POST /rooms/{room_id}/actions/refresh_client_token` — Required: `refresh_token`

```javascript
const response = await client.rooms.actions.refreshClientToken(
  '0ccc7b54-4df3-4bca-a65a-3da1ecc777f0',
  {
    refresh_token:
      'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0ZWxueXhfdGVsZXBob255IiwiZXhwIjoxNTkwMDEwMTQzLCJpYXQiOjE1ODc1OTA5NDMsImlzcyI6InRlbG55eF90ZWxlcGhvbnkiLCJqdGkiOiJiOGM3NDgzNy1kODllLTRhNjUtOWNmMi0zNGM3YTZmYTYwYzgiLCJuYmYiOjE1ODc1OTA5NDIsInN1YiI6IjVjN2FjN2QwLWRiNjUtNGYxMS05OGUxLWVlYzBkMWQ1YzZhZSIsInRlbF90b2tlbiI6InJqX1pra1pVT1pNeFpPZk9tTHBFVUIzc2lVN3U2UmpaRmVNOXMtZ2JfeENSNTZXRktGQUppTXlGMlQ2Q0JSbWxoX1N5MGlfbGZ5VDlBSThzRWlmOE1USUlzenl6U2xfYURuRzQ4YU81MHlhSEd1UlNZYlViU1ltOVdJaVEwZz09IiwidHlwIjoiYWNjZXNzIn0.gNEwzTow5MLLPLQENytca7pUN79PmPj6FyqZWW06ZeEmesxYpwKh0xRtA0TzLh6CDYIRHrI8seofOO0YFGDhpQ',
  },
);

console.log(response.data);
```

## View a list of room sessions.

`GET /rooms/{room_id}/sessions`

```javascript
// Automatically fetches more pages as needed.
for await (const roomSession of client.rooms.sessions.list1(
  '0ccc7b54-4df3-4bca-a65a-3da1ecc777f0',
)) {
  console.log(roomSession.id);
}
```
