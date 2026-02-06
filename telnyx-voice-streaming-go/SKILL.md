---
name: telnyx-voice-streaming-go
description: >-
  Stream call audio in real-time, fork media to external destinations, and
  transcribe speech live. Use for real-time analytics and AI integrations. This
  skill provides Go SDK examples.
metadata:
  author: telnyx
  product: voice-streaming
  language: go
---

# Telnyx Voice Streaming - Go

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

## Forking start

Call forking allows you to stream the media from a call to a specific target in realtime.

`POST /calls/{call_control_id}/actions/fork_start`

```go
response, err := client.Calls.Actions.StartForking(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartForkingParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Forking stop

Stop forking a call.

`POST /calls/{call_control_id}/actions/fork_stop`

```go
response, err := client.Calls.Actions.StopForking(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopForkingParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Streaming start

Start streaming the media from a call to a specific WebSocket address or Dialogflow connection in near-realtime.

`POST /calls/{call_control_id}/actions/streaming_start`

```go
response, err := client.Calls.Actions.StartStreaming(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartStreamingParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Streaming stop

Stop streaming a call to a WebSocket.

`POST /calls/{call_control_id}/actions/streaming_stop`

```go
response, err := client.Calls.Actions.StopStreaming(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopStreamingParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Transcription start

Start real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_start`

```go
response, err := client.Calls.Actions.StartTranscription(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartTranscriptionParams{
    TranscriptionStartRequest: telnyx.TranscriptionStartRequestParam{

    },
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Transcription stop

Stop real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_stop`

```go
response, err := client.Calls.Actions.StopTranscription(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopTranscriptionParams{

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
| `callForkStarted` | Call Fork Started |
| `callForkStopped` | Call Fork Stopped |
| `callStreamingStarted` | Call Streaming Started |
| `callStreamingStopped` | Call Streaming Stopped |
| `callStreamingFailed` | Call Streaming Failed |
| `transcription` | Transcription |
