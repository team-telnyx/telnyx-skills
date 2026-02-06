---
name: telnyx-voice-conferencing-python
description: >-
  Create and manage conference calls, queues, and multi-party sessions. Use when
  building call centers or conferencing applications. This skill provides Python
  SDK examples.
metadata:
  author: telnyx
  product: voice-conferencing
  language: python
---

# Telnyx Voice Conferencing - Python

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

## Enqueue call

Put the call in a queue.

`POST /calls/{call_control_id}/actions/enqueue` — Required: `queue_name`

```python
response = client.calls.actions.enqueue(
    call_control_id="call_control_id",
    queue_name="support",
)
print(response.data)
```

## Remove call from a queue

Removes the call from a queue.

`POST /calls/{call_control_id}/actions/leave_queue`

```python
response = client.calls.actions.leave_queue(
    call_control_id="call_control_id",
)
print(response.data)
```

## List conferences

Lists conferences.

`GET /conferences`

```python
page = client.conferences.list()
page = page.data[0]
print(page.id)
```

## Create conference

Create a conference from an existing call leg using a `call_control_id` and a conference name.

`POST /conferences` — Required: `call_control_id`, `name`

```python
conference = client.conferences.create(
    call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
    name="Business",
)
print(conference.data)
```

## Retrieve a conference

Retrieve an existing conference

`GET /conferences/{id}`

```python
conference = client.conferences.retrieve(
    id="id",
)
print(conference.data)
```

## Hold conference participants

Hold a list of participants in a conference call

`POST /conferences/{id}/actions/hold`

```python
response = client.conferences.actions.hold(
    id="id",
)
print(response.data)
```

## Join a conference

Join an existing call leg to a conference.

`POST /conferences/{id}/actions/join` — Required: `call_control_id`

```python
response = client.conferences.actions.join(
    id="id",
    call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
)
print(response.data)
```

## Leave a conference

Removes a call leg from a conference and moves it back to parked state.

`POST /conferences/{id}/actions/leave` — Required: `call_control_id`

```python
response = client.conferences.actions.leave(
    id="id",
    call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
)
print(response.data)
```

## Mute conference participants

Mute a list of participants in a conference call

`POST /conferences/{id}/actions/mute`

```python
response = client.conferences.actions.mute(
    id="id",
)
print(response.data)
```

## Play audio to conference participants

Play audio to all or some participants on a conference call.

`POST /conferences/{id}/actions/play`

```python
response = client.conferences.actions.play(
    id="id",
)
print(response.data)
```

## Conference recording pause

Pause conference recording.

`POST /conferences/{id}/actions/record_pause`

```python
response = client.conferences.actions.record_pause(
    id="id",
)
print(response.data)
```

## Conference recording resume

Resume conference recording.

`POST /conferences/{id}/actions/record_resume`

```python
response = client.conferences.actions.record_resume(
    id="id",
)
print(response.data)
```

## Conference recording start

Start recording the conference.

`POST /conferences/{id}/actions/record_start` — Required: `format`

```python
response = client.conferences.actions.record_start(
    id="id",
    format="wav",
)
print(response.data)
```

## Conference recording stop

Stop recording the conference.

`POST /conferences/{id}/actions/record_stop`

```python
response = client.conferences.actions.record_stop(
    id="id",
)
print(response.data)
```

## Speak text to conference participants

Convert text to speech and play it to all or some participants.

`POST /conferences/{id}/actions/speak` — Required: `payload`, `voice`

```python
response = client.conferences.actions.speak(
    id="id",
    payload="Say this to participants",
    voice="female",
)
print(response.data)
```

## Stop audio being played on the conference

Stop audio being played to all or some participants on a conference call.

`POST /conferences/{id}/actions/stop`

```python
response = client.conferences.actions.stop(
    id="id",
)
print(response.data)
```

## Unhold conference participants

Unhold a list of participants in a conference call

`POST /conferences/{id}/actions/unhold` — Required: `call_control_ids`

```python
response = client.conferences.actions.unhold(
    id="id",
    call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
)
print(response.data)
```

## Unmute conference participants

Unmute a list of participants in a conference call

`POST /conferences/{id}/actions/unmute`

```python
response = client.conferences.actions.unmute(
    id="id",
)
print(response.data)
```

## Update conference participant

Update conference participant supervisor_role

`POST /conferences/{id}/actions/update` — Required: `call_control_id`, `supervisor_role`

```python
action = client.conferences.actions.update(
    id="id",
    call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
    supervisor_role="whisper",
)
print(action.data)
```

## List conference participants

Lists conference participants

`GET /conferences/{conference_id}/participants`

```python
page = client.conferences.list_participants(
    conference_id="conference_id",
)
page = page.data[0]
print(page.id)
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
