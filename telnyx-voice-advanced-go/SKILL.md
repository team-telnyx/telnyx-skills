---
name: telnyx-voice-advanced-go
description: >-
  Advanced call control features including DTMF sending, SIPREC recording, noise
  suppression, client state, and supervisor controls. This skill provides Go SDK
  examples.
metadata:
  author: telnyx
  product: voice-advanced
  language: go
---

# Telnyx Voice Advanced - Go

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

## Update client state

Updates client state

`PUT /calls/{call_control_id}/actions/client_state_update` — Required: `client_state`

```go
response, err := client.Calls.Actions.UpdateClientState(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionUpdateClientStateParams{
    ClientState: "aGF2ZSBhIG5pY2UgZGF5ID1d",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Send DTMF

Sends DTMF tones from this leg.

`POST /calls/{call_control_id}/actions/send_dtmf` — Required: `digits`

```go
response, err := client.Calls.Actions.SendDtmf(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionSendDtmfParams{
    Digits: "1www2WABCDw9",
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## SIPREC start

Start siprec session to configured in SIPREC connector SRS.

`POST /calls/{call_control_id}/actions/siprec_start`

```go
response, err := client.Calls.Actions.StartSiprec(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartSiprecParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

```go
response, err := client.Calls.Actions.StopSiprec(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopSiprecParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

```go
response, err := client.Calls.Actions.StartNoiseSuppression(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStartNoiseSuppressionParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

```go
response, err := client.Calls.Actions.StopNoiseSuppression(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionStopNoiseSuppressionParams{

  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", response.Data)
```

## Switch supervisor role

Switch the supervisor role for a bridged call.

`POST /calls/{call_control_id}/actions/switch_supervisor_role` — Required: `role`

```go
response, err := client.Calls.Actions.SwitchSupervisorRole(
  context.TODO(),
  "call_control_id",
  telnyx.CallActionSwitchSupervisorRoleParams{
    Role: telnyx.CallActionSwitchSupervisorRoleParamsRoleBarge,
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
| `callSiprecStarted` | Call Siprec Started |
| `callSiprecStopped` | Call Siprec Stopped |
| `callSiprecFailed` | Call Siprec Failed |
