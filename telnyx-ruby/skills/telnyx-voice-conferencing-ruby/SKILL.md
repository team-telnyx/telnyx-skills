---
name: telnyx-voice-conferencing-ruby
description: >-
  Create and manage conference calls, queues, and multi-party sessions. Use when
  building call centers or conferencing applications. This skill provides Ruby
  SDK examples.
metadata:
  author: telnyx
  product: voice-conferencing
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Conferencing - Ruby

## Installation

```bash
gem install telnyx
```

## Setup

```ruby
require "telnyx"

client = Telnyx::Client.new(
  api_key: ENV["TELNYX_API_KEY"], # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Enqueue call

Put the call in a queue.

`POST /calls/{call_control_id}/actions/enqueue` — Required: `queue_name`

```ruby
response = client.calls.actions.enqueue("call_control_id", queue_name: "support")

puts(response)
```

## Remove call from a queue

Removes the call from a queue.

`POST /calls/{call_control_id}/actions/leave_queue`

```ruby
response = client.calls.actions.leave_queue("call_control_id")

puts(response)
```

## List conferences

Lists conferences.

`GET /conferences`

```ruby
page = client.conferences.list

puts(page)
```

## Create conference

Create a conference from an existing call leg using a `call_control_id` and a conference name.

`POST /conferences` — Required: `call_control_id`, `name`

```ruby
conference = client.conferences.create(
  call_control_id: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  name: "Business"
)

puts(conference)
```

## Retrieve a conference

Retrieve an existing conference

`GET /conferences/{id}`

```ruby
conference = client.conferences.retrieve("id")

puts(conference)
```

## Hold conference participants

Hold a list of participants in a conference call

`POST /conferences/{id}/actions/hold`

```ruby
response = client.conferences.actions.hold("id")

puts(response)
```

## Join a conference

Join an existing call leg to a conference.

`POST /conferences/{id}/actions/join` — Required: `call_control_id`

```ruby
response = client.conferences.actions.join(
  "id",
  call_control_id: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"
)

puts(response)
```

## Leave a conference

Removes a call leg from a conference and moves it back to parked state.

`POST /conferences/{id}/actions/leave` — Required: `call_control_id`

```ruby
response = client.conferences.actions.leave("id", call_control_id: "c46e06d7-b78f-4b13-96b6-c576af9640ff")

puts(response)
```

## Mute conference participants

Mute a list of participants in a conference call

`POST /conferences/{id}/actions/mute`

```ruby
response = client.conferences.actions.mute("id")

puts(response)
```

## Play audio to conference participants

Play audio to all or some participants on a conference call.

`POST /conferences/{id}/actions/play`

```ruby
response = client.conferences.actions.play("id")

puts(response)
```

## Conference recording pause

Pause conference recording.

`POST /conferences/{id}/actions/record_pause`

```ruby
response = client.conferences.actions.record_pause("id")

puts(response)
```

## Conference recording resume

Resume conference recording.

`POST /conferences/{id}/actions/record_resume`

```ruby
response = client.conferences.actions.record_resume("id")

puts(response)
```

## Conference recording start

Start recording the conference.

`POST /conferences/{id}/actions/record_start` — Required: `format`

```ruby
response = client.conferences.actions.record_start("id", format_: :wav)

puts(response)
```

## Conference recording stop

Stop recording the conference.

`POST /conferences/{id}/actions/record_stop`

```ruby
response = client.conferences.actions.record_stop("id")

puts(response)
```

## Speak text to conference participants

Convert text to speech and play it to all or some participants.

`POST /conferences/{id}/actions/speak` — Required: `payload`, `voice`

```ruby
response = client.conferences.actions.speak("id", payload: "Say this to participants", voice: "female")

puts(response)
```

## Stop audio being played on the conference

Stop audio being played to all or some participants on a conference call.

`POST /conferences/{id}/actions/stop`

```ruby
response = client.conferences.actions.stop("id")

puts(response)
```

## Unhold conference participants

Unhold a list of participants in a conference call

`POST /conferences/{id}/actions/unhold` — Required: `call_control_ids`

```ruby
response = client.conferences.actions.unhold(
  "id",
  call_control_ids: ["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"]
)

puts(response)
```

## Unmute conference participants

Unmute a list of participants in a conference call

`POST /conferences/{id}/actions/unmute`

```ruby
response = client.conferences.actions.unmute("id")

puts(response)
```

## Update conference participant

Update conference participant supervisor_role

`POST /conferences/{id}/actions/update` — Required: `call_control_id`, `supervisor_role`

```ruby
action = client.conferences.actions.update(
  "id",
  call_control_id: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  supervisor_role: :whisper
)

puts(action)
```

## List conference participants

Lists conference participants

`GET /conferences/{conference_id}/participants`

```ruby
page = client.conferences.list_participants("conference_id")

puts(page)
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
