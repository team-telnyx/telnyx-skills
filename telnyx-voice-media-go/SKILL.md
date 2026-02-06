---
name: telnyx-voice-media-go
description: >-
  Play audio files, use text-to-speech, and record calls. Use when building IVR
  systems, playing announcements, or recording conversations. This skill
  provides Go SDK examples.
metadata:
  author: telnyx
  product: voice-media
  language: go
---

# Telnyx Voice Media - Go

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

## Play audio URL

Play an audio file on the call.

`POST /calls/{call_control_id}/actions/playback_start`

```go
response, err := client.Calls.Actions.StartPlayback(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartPlaybackParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Stop audio playback

Stop audio being played on the call.

`POST /calls/{call_control_id}/actions/playback_stop`

```go
response, err := client.Calls.Actions.StopPlayback(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopPlaybackParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Record pause

Pause recording the call.

`POST /calls/{call_control_id}/actions/record_pause`

```go
response, err := client.Calls.Actions.PauseRecording(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionPauseRecordingParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Record resume

Resume recording the call.

`POST /calls/{call_control_id}/actions/record_resume`

```go
response, err := client.Calls.Actions.ResumeRecording(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionResumeRecordingParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Recording start

Start recording the call.

`POST /calls/{call_control_id}/actions/record_start` — Required: `format`, `channels`

```go
response, err := client.Calls.Actions.StartRecording(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartRecordingParams{
    Channels: telnyx.CallActionStartRecordingParamsChannelsSingle,
    Format: telnyx.CallActionStartRecordingParamsFormatWav,
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Recording stop

Stop recording the call.

`POST /calls/{call_control_id}/actions/record_stop`

```go
response, err := client.Calls.Actions.StopRecording(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopRecordingParams{
    StopRecordingRequest: telnyx.StopRecordingRequestParam{

    },
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Speak text

Convert text to speech and play it back on the call.

`POST /calls/{call_control_id}/actions/speak` — Required: `payload`, `voice`

```go
response, err := client.Calls.Actions.Speak(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionSpeakParams{
    Payload: "Say this on the call",
    Voice: "female",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callPlaybackStarted` | Call Playback Started |
| `callPlaybackEnded` | Call Playback Ended |
| `callSpeakEnded` | Call Speak Ended |
| `callRecordingSaved` | Call Recording Saved |
| `callRecordingError` | Call Recording Error |
| `callRecordingTranscriptionSaved` | Call Recording Transcription Saved |
| `callSpeakStarted` | Call Speak Started |
