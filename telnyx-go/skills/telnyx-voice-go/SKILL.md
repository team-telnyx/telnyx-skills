---
name: telnyx-voice-go
description: >-
  Make and receive calls, transfer, bridge, and manage call lifecycle with Call
  Control. Includes application management and call events. This skill provides
  Go SDK examples.
metadata:
  author: telnyx
  product: voice
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice - Go

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

## Answer call

Answer an incoming call.

`POST /calls/{call_control_id}/actions/answer`

```go
	response, err := client.Calls.Actions.Answer(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionAnswerParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Bridge calls

Bridge two call control calls.

`POST /calls/{call_control_id}/actions/bridge` — Required: `call_control_id`

```go
	response, err := client.Calls.Actions.Bridge(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionBridgeParams{
			CallControlIDToBridgeWith: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Dial

Dial a number or SIP URI from a given connection.

`POST /calls` — Required: `connection_id`, `to`, `from`

```go
	response, err := client.Calls.Dial(context.TODO(), telnyx.CallDialParams{
		ConnectionID: "7267xxxxxxxxxxxxxx",
		From:         "+18005550101",
		To: telnyx.CallDialParamsToUnion{
			OfString: telnyx.String("+18005550100"),
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Hangup call

Hang up the call.

`POST /calls/{call_control_id}/actions/hangup`

```go
	response, err := client.Calls.Actions.Hangup(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionHangupParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Transfer call

Transfer a call to a new destination.

`POST /calls/{call_control_id}/actions/transfer` — Required: `to`

```go
	response, err := client.Calls.Actions.Transfer(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionTransferParams{
			To: "+18005550100",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List all active calls for given connection

Lists all active calls for given connection.

`GET /connections/{connection_id}/active_calls`

```go
	page, err := client.Connections.ListActiveCalls(
		context.TODO(),
		"1293384261075731461",
		telnyx.ConnectionListActiveCallsParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## List call control applications

Return a list of call control applications.

`GET /call_control_applications`

```go
	page, err := client.CallControlApplications.List(context.TODO(), telnyx.CallControlApplicationListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create a call control application

Create a call control application.

`POST /call_control_applications` — Required: `application_name`, `webhook_event_url`

```go
	callControlApplication, err := client.CallControlApplications.New(context.TODO(), telnyx.CallControlApplicationNewParams{
		ApplicationName: "call-router",
		WebhookEventURL: "https://example.com",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", callControlApplication.Data)
```

## Retrieve a call control application

Retrieves the details of an existing call control application.

`GET /call_control_applications/{id}`

```go
	callControlApplication, err := client.CallControlApplications.Get(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", callControlApplication.Data)
```

## Update a call control application

Updates settings of an existing call control application.

`PATCH /call_control_applications/{id}` — Required: `application_name`, `webhook_event_url`

```go
	callControlApplication, err := client.CallControlApplications.Update(
		context.TODO(),
		"id",
		telnyx.CallControlApplicationUpdateParams{
			ApplicationName: "call-router",
			WebhookEventURL: "https://example.com",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", callControlApplication.Data)
```

## Delete a call control application

Deletes a call control application.

`DELETE /call_control_applications/{id}`

```go
	callControlApplication, err := client.CallControlApplications.Delete(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", callControlApplication.Data)
```

## List call events

Filters call events by given filter parameters.

`GET /call_events`

```go
	page, err := client.CallEvents.List(context.TODO(), telnyx.CallEventListParams{})
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
| `callAnswered` | Call Answered |
| `callStreamingStarted` | Call Streaming Started |
| `callStreamingStopped` | Call Streaming Stopped |
| `callStreamingFailed` | Call Streaming Failed |
| `callBridged` | Call Bridged |
| `callInitiated` | Call Initiated |
| `callHangup` | Call Hangup |
| `callRecordingSaved` | Call Recording Saved |
| `callMachineDetectionEnded` | Call Machine Detection Ended |
| `callMachineGreetingEnded` | Call Machine Greeting Ended |
| `callMachinePremiumDetectionEnded` | Call Machine Premium Detection Ended |
| `callMachinePremiumGreetingEnded` | Call Machine Premium Greeting Ended |
