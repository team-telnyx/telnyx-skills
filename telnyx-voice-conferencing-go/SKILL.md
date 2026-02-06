---
name: telnyx-voice-conferencing-go
description: >-
  Create and manage conference calls, queues, and multi-party sessions. Use when
  building call centers or conferencing applications. This skill provides Go SDK
  examples.
metadata:
  author: telnyx
  product: voice-conferencing
  language: go
---

# Telnyx Voice Conferencing - Go

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
import (
  "context"
  "fmt"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

client := telnyx.NewClient(
  option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
)
```

All examples below assume `client` is already initialized as shown above.

## Enqueue call

Put the call in a queue.

`POST /calls/{call_control_id}/actions/enqueue` — Required: `queue_name`

```go
response, err := client.Calls.Actions.Enqueue(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionEnqueueParams{
    QueueName: "support",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Remove call from a queue

Removes the call from a queue.

`POST /calls/{call_control_id}/actions/leave_queue`

```go
response, err := client.Calls.Actions.LeaveQueue(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionLeaveQueueParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## List conferences

Lists conferences.

`GET /conferences`

```go
page, err := client.Conferences.List(context.TODO(), telnyx.ConferenceListParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
```

## Create conference

Create a conference from an existing call leg using a `call_control_id` and a conference name.

`POST /conferences` — Required: `call_control_id`, `name`

```go
conference, err := client.Conferences.New(context.TODO(), telnyx.ConferenceNewParams{
  CallControlID: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  Name: "Business",
})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", conference.Data)
```

## Retrieve a conference

Retrieve an existing conference

`GET /conferences/{id}`

```go
conference, err := client.Conferences.Get(
  context.TODO(),
  "id",
  telnyx.ConferenceGetParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", conference.Data)
```

## Hold conference participants

Hold a list of participants in a conference call

`POST /conferences/{id}/actions/hold`

```go
response, err := client.Conferences.Actions.Hold(
  context.TODO(),
  "id",
  telnyx.ConferenceActionHoldParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Join a conference

Join an existing call leg to a conference.

`POST /conferences/{id}/actions/join` — Required: `call_control_id`

```go
response, err := client.Conferences.Actions.Join(
  context.TODO(),
  "id",
  telnyx.ConferenceActionJoinParams{
    CallControlID: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Leave a conference

Removes a call leg from a conference and moves it back to parked state.

`POST /conferences/{id}/actions/leave` — Required: `call_control_id`

```go
response, err := client.Conferences.Actions.Leave(
  context.TODO(),
  "id",
  telnyx.ConferenceActionLeaveParams{
    CallControlID: "c46e06d7-b78f-4b13-96b6-c576af9640ff",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Mute conference participants

Mute a list of participants in a conference call

`POST /conferences/{id}/actions/mute`

```go
response, err := client.Conferences.Actions.Mute(
  context.TODO(),
  "id",
  telnyx.ConferenceActionMuteParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Play audio to conference participants

Play audio to all or some participants on a conference call.

`POST /conferences/{id}/actions/play`

```go
response, err := client.Conferences.Actions.Play(
  context.TODO(),
  "id",
  telnyx.ConferenceActionPlayParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Conference recording pause

Pause conference recording.

`POST /conferences/{id}/actions/record_pause`

```go
response, err := client.Conferences.Actions.RecordPause(
  context.TODO(),
  "id",
  telnyx.ConferenceActionRecordPauseParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Conference recording resume

Resume conference recording.

`POST /conferences/{id}/actions/record_resume`

```go
response, err := client.Conferences.Actions.RecordResume(
  context.TODO(),
  "id",
  telnyx.ConferenceActionRecordResumeParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Conference recording start

Start recording the conference.

`POST /conferences/{id}/actions/record_start` — Required: `format`

```go
response, err := client.Conferences.Actions.RecordStart(
  context.TODO(),
  "id",
  telnyx.ConferenceActionRecordStartParams{
    Format: telnyx.ConferenceActionRecordStartParamsFormatWav,
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Conference recording stop

Stop recording the conference.

`POST /conferences/{id}/actions/record_stop`

```go
response, err := client.Conferences.Actions.RecordStop(
  context.TODO(),
  "id",
  telnyx.ConferenceActionRecordStopParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Speak text to conference participants

Convert text to speech and play it to all or some participants.

`POST /conferences/{id}/actions/speak` — Required: `payload`, `voice`

```go
response, err := client.Conferences.Actions.Speak(
  context.TODO(),
  "id",
  telnyx.ConferenceActionSpeakParams{
    Payload: "Say this to participants",
    Voice: "female",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Stop audio being played on the conference

Stop audio being played to all or some participants on a conference call.

`POST /conferences/{id}/actions/stop`

```go
response, err := client.Conferences.Actions.Stop(
  context.TODO(),
  "id",
  telnyx.ConferenceActionStopParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Unhold conference participants

Unhold a list of participants in a conference call

`POST /conferences/{id}/actions/unhold` — Required: `call_control_ids`

```go
response, err := client.Conferences.Actions.Unhold(
  context.TODO(),
  "id",
  telnyx.ConferenceActionUnholdParams{
    CallControlIDs: []string{"v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"},
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Unmute conference participants

Unmute a list of participants in a conference call

`POST /conferences/{id}/actions/unmute`

```go
response, err := client.Conferences.Actions.Unmute(
  context.TODO(),
  "id",
  telnyx.ConferenceActionUnmuteParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Update conference participant

Update conference participant supervisor_role

`POST /conferences/{id}/actions/update` — Required: `call_control_id`, `supervisor_role`

```go
action, err := client.Conferences.Actions.Update(
  context.TODO(),
  "id",
  telnyx.ConferenceActionUpdateParams{
    UpdateConference: telnyx.UpdateConferenceParam{
      CallControlID: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
      SupervisorRole: telnyx.UpdateConferenceSupervisorRoleWhisper,
    },
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", action.Data)
```

## List conference participants

Lists conference participants

`GET /conferences/{conference_id}/participants`

```go
page, err := client.Conferences.ListParticipants(
  context.TODO(),
  "conference_id",
  telnyx.ConferenceListParticipantsParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
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
