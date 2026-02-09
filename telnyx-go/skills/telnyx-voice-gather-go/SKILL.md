---
name: telnyx-voice-gather-go
description: >-
  Collect DTMF input and speech from callers using standard gather or AI-powered
  gather. Build interactive voice menus and AI voice assistants. This skill
  provides Go SDK examples.
metadata:
  author: telnyx
  product: voice-gather
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Gather - Go

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
import (
  "context"
  "fmt"
  "os"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

client := telnyx.NewClient(
  option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
)
```

All examples below assume `client` is already initialized as shown above.

## Add messages to AI Assistant

Add messages to the conversation started by an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_add_messages`

```go
	response, err := client.Calls.Actions.AddAIAssistantMessages(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionAddAIAssistantMessagesParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Start AI Assistant

Start an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_start`

```go
	response, err := client.Calls.Actions.StartAIAssistant(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStartAIAssistantParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Stop AI Assistant

Stop an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_stop`

```go
	response, err := client.Calls.Actions.StopAIAssistant(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStopAIAssistantParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Gather stop

Stop current gather.

`POST /calls/{call_control_id}/actions/gather_stop`

```go
	response, err := client.Calls.Actions.StopGather(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStopGatherParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Gather using AI

Gather parameters defined in the request payload using a voice assistant.

`POST /calls/{call_control_id}/actions/gather_using_ai` — Required: `parameters`

```go
	response, err := client.Calls.Actions.GatherUsingAI(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionGatherUsingAIParams{
			Parameters: map[string]any{
				"properties": "bar",
				"required":   "bar",
				"type":       "bar",
			},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Gather using audio

Play an audio file on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_audio`

```go
	response, err := client.Calls.Actions.GatherUsingAudio(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionGatherUsingAudioParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Gather using speak

Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_speak` — Required: `voice`, `payload`

```go
	response, err := client.Calls.Actions.GatherUsingSpeak(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionGatherUsingSpeakParams{
			Payload: "say this on call",
			Voice:   "male",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Gather

Gather DTMF signals to build interactive menus.

`POST /calls/{call_control_id}/actions/gather`

```go
	response, err := client.Calls.Actions.Gather(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionGatherParams{},
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
| `callGatherEnded` | Call Gather Ended |
| `CallAIGatherEnded` | Call AI Gather Ended |
| `CallAIGatherMessageHistoryUpdated` | Call AI Gather Message History Updated |
| `CallAIGatherPartialResults` | Call AI Gather Partial Results |
| `CallConversationEnded` | Call Conversation Ended |
| `callPlaybackStarted` | Call Playback Started |
| `callPlaybackEnded` | Call Playback Ended |
| `callDtmfReceived` | Call Dtmf Received |
