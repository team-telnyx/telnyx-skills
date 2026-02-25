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
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

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
  "os"

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

## SIP Refer a call

Initiate a SIP Refer on a Call Control call.

`POST /calls/{call_control_id}/actions/refer` — Required: `sip_address`

Optional: `client_state` (string), `command_id` (string), `custom_headers` (array[object]), `sip_auth_password` (string), `sip_auth_username` (string), `sip_headers` (array[object])

```go
	response, err := client.Calls.Actions.Refer(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionReferParams{
			SipAddress: "sip:username@sip.non-telnyx-address.com",
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

Optional: `client_state` (string), `command_id` (string), `duration_millis` (int32)

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

Optional: `client_state` (string), `connector_name` (string), `include_metadata_custom_headers` (enum), `secure` (enum), `session_timeout_secs` (integer), `sip_transport` (enum), `siprec_track` (enum)

```go
	response, err := client.Calls.Actions.StartSiprec(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStartSiprecParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

Optional: `client_state` (string), `command_id` (string)

```go
	response, err := client.Calls.Actions.StopSiprec(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStopSiprecParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

Optional: `client_state` (string), `command_id` (string), `direction` (enum), `noise_suppression_engine` (enum), `noise_suppression_engine_config` (object)

```go
	response, err := client.Calls.Actions.StartNoiseSuppression(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStartNoiseSuppressionParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

Optional: `client_state` (string), `command_id` (string)

```go
	response, err := client.Calls.Actions.StopNoiseSuppression(
		context.TODO(),
		"call_control_id",
		telnyx.CallActionStopNoiseSuppressionParams{},
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
| `callReferStarted` | Call Refer Started |
| `callReferCompleted` | Call Refer Completed |
| `callReferFailed` | Call Refer Failed |
| `callSiprecStarted` | Call Siprec Started |
| `callSiprecStopped` | Call Siprec Stopped |
| `callSiprecFailed` | Call Siprec Failed |

### Webhook payload fields

**`callReferStarted`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Unique ID for controlling the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.sip_notify_response` | integer | SIP NOTIFY event status for tracking the REFER attempt. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |

**`callReferCompleted`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Unique ID for controlling the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.sip_notify_response` | integer | SIP NOTIFY event status for tracking the REFER attempt. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |

**`callReferFailed`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Unique ID for controlling the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.sip_notify_response` | integer | SIP NOTIFY event status for tracking the REFER attempt. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |

**`callSiprecStarted`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |

**`callSiprecStopped`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.hangup_cause` | string | Q850 reason why the SIPREC session was stopped. |

**`callSiprecFailed`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.failure_cause` | string | Q850 reason why siprec session failed. |
