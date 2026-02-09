---
name: telnyx-voice-conferencing-javascript
description: >-
  Create and manage conference calls, queues, and multi-party sessions. Use when
  building call centers or conferencing applications. This skill provides
  JavaScript SDK examples.
metadata:
  author: telnyx
  product: voice-conferencing
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Conferencing - JavaScript

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

## Enqueue call

Put the call in a queue.

`POST /calls/{call_control_id}/actions/enqueue` — Required: `queue_name`

```javascript
const response = await client.calls.actions.enqueue('call_control_id', { queue_name: 'support' });

console.log(response.data);
```

## Remove call from a queue

Removes the call from a queue.

`POST /calls/{call_control_id}/actions/leave_queue`

```javascript
const response = await client.calls.actions.leaveQueue('call_control_id');

console.log(response.data);
```

## List conferences

Lists conferences.

`GET /conferences`

```javascript
// Automatically fetches more pages as needed.
for await (const conference of client.conferences.list()) {
  console.log(conference.id);
}
```

## Create conference

Create a conference from an existing call leg using a `call_control_id` and a conference name.

`POST /conferences` — Required: `call_control_id`, `name`

```javascript
const conference = await client.conferences.create({
  call_control_id: 'v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg',
  name: 'Business',
});

console.log(conference.data);
```

## Retrieve a conference

Retrieve an existing conference

`GET /conferences/{id}`

```javascript
const conference = await client.conferences.retrieve('id');

console.log(conference.data);
```

## Hold conference participants

Hold a list of participants in a conference call

`POST /conferences/{id}/actions/hold`

```javascript
const response = await client.conferences.actions.hold('id');

console.log(response.data);
```

## Join a conference

Join an existing call leg to a conference.

`POST /conferences/{id}/actions/join` — Required: `call_control_id`

```javascript
const response = await client.conferences.actions.join('id', {
  call_control_id: 'v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg',
});

console.log(response.data);
```

## Leave a conference

Removes a call leg from a conference and moves it back to parked state.

`POST /conferences/{id}/actions/leave` — Required: `call_control_id`

```javascript
const response = await client.conferences.actions.leave('id', {
  call_control_id: 'c46e06d7-b78f-4b13-96b6-c576af9640ff',
});

console.log(response.data);
```

## Mute conference participants

Mute a list of participants in a conference call

`POST /conferences/{id}/actions/mute`

```javascript
const response = await client.conferences.actions.mute('id');

console.log(response.data);
```

## Play audio to conference participants

Play audio to all or some participants on a conference call.

`POST /conferences/{id}/actions/play`

```javascript
const response = await client.conferences.actions.play('id');

console.log(response.data);
```

## Conference recording pause

Pause conference recording.

`POST /conferences/{id}/actions/record_pause`

```javascript
const response = await client.conferences.actions.recordPause('id');

console.log(response.data);
```

## Conference recording resume

Resume conference recording.

`POST /conferences/{id}/actions/record_resume`

```javascript
const response = await client.conferences.actions.recordResume('id');

console.log(response.data);
```

## Conference recording start

Start recording the conference.

`POST /conferences/{id}/actions/record_start` — Required: `format`

```javascript
const response = await client.conferences.actions.recordStart('id', { format: 'wav' });

console.log(response.data);
```

## Conference recording stop

Stop recording the conference.

`POST /conferences/{id}/actions/record_stop`

```javascript
const response = await client.conferences.actions.recordStop('id');

console.log(response.data);
```

## Speak text to conference participants

Convert text to speech and play it to all or some participants.

`POST /conferences/{id}/actions/speak` — Required: `payload`, `voice`

```javascript
const response = await client.conferences.actions.speak('id', {
  payload: 'Say this to participants',
  voice: 'female',
});

console.log(response.data);
```

## Stop audio being played on the conference

Stop audio being played to all or some participants on a conference call.

`POST /conferences/{id}/actions/stop`

```javascript
const response = await client.conferences.actions.stop('id');

console.log(response.data);
```

## Unhold conference participants

Unhold a list of participants in a conference call

`POST /conferences/{id}/actions/unhold` — Required: `call_control_ids`

```javascript
const response = await client.conferences.actions.unhold('id', {
  call_control_ids: ['v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg'],
});

console.log(response.data);
```

## Unmute conference participants

Unmute a list of participants in a conference call

`POST /conferences/{id}/actions/unmute`

```javascript
const response = await client.conferences.actions.unmute('id');

console.log(response.data);
```

## Update conference participant

Update conference participant supervisor_role

`POST /conferences/{id}/actions/update` — Required: `call_control_id`, `supervisor_role`

```javascript
const action = await client.conferences.actions.update('id', {
  call_control_id: 'v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg',
  supervisor_role: 'whisper',
});

console.log(action.data);
```

## List conference participants

Lists conference participants

`GET /conferences/{conference_id}/participants`

```javascript
// Automatically fetches more pages as needed.
for await (const conferenceListParticipantsResponse of client.conferences.listParticipants(
  'conference_id',
)) {
  console.log(conferenceListParticipantsResponse.id);
}
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callEnqueued` | Call Enqueued |
| `callLeftQueue` | Call Left Queue |
| `conferenceCreated` | Conference Created |
| `conferenceEnded` | Conference Ended |
| `conferenceFloorChanged` | Conference Floor Changed |
| `conferenceParticipantJoined` | Conference Participant Joined |
| `conferenceParticipantLeft` | Conference Participant Left |
| `conferenceParticipantPlaybackEnded` | Conference Participant Playback Ended |
| `conferenceParticipantPlaybackStarted` | Conference Participant Playback Started |
| `conferenceParticipantSpeakEnded` | Conference Participant Speak Ended |
| `conferenceParticipantSpeakStarted` | Conference Participant Speak Started |
| `conferencePlaybackEnded` | Conference Playback Ended |
| `conferencePlaybackStarted` | Conference Playback Started |
| `conferenceRecordingSaved` | Conference Recording Saved |
| `conferenceSpeakEnded` | Conference Speak Ended |
| `conferenceSpeakStarted` | Conference Speak Started |
