---
name: telnyx-voice-advanced-java
description: >-
  Advanced call control features including DTMF sending, SIPREC recording, noise
  suppression, client state, and supervisor controls. This skill provides Java
  SDK examples.
metadata:
  author: telnyx
  product: voice-advanced
  language: java
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Advanced - Java

## Installation

```text
// See https://github.com/team-telnyx/telnyx-java for Maven/Gradle setup
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## Update client state

Updates client state

`PUT /calls/{call_control_id}/actions/client_state_update` — Required: `client_state`

```java
import com.telnyx.sdk.models.calls.actions.ActionUpdateClientStateParams;
import com.telnyx.sdk.models.calls.actions.ActionUpdateClientStateResponse;

ActionUpdateClientStateParams params = ActionUpdateClientStateParams.builder()
    .callControlId("call_control_id")
    .clientState("aGF2ZSBhIG5pY2UgZGF5ID1d")
    .build();
ActionUpdateClientStateResponse response = client.calls().actions().updateClientState(params);
```

## SIP Refer a call

Initiate a SIP Refer on a Call Control call.

`POST /calls/{call_control_id}/actions/refer` — Required: `sip_address`

Optional: `client_state` (string), `command_id` (string), `custom_headers` (array[object]), `sip_auth_password` (string), `sip_auth_username` (string), `sip_headers` (array[object])

```java
import com.telnyx.sdk.models.calls.actions.ActionReferParams;
import com.telnyx.sdk.models.calls.actions.ActionReferResponse;

ActionReferParams params = ActionReferParams.builder()
    .callControlId("call_control_id")
    .sipAddress("sip:username@sip.non-telnyx-address.com")
    .build();
ActionReferResponse response = client.calls().actions().refer(params);
```

## Send DTMF

Sends DTMF tones from this leg.

`POST /calls/{call_control_id}/actions/send_dtmf` — Required: `digits`

Optional: `client_state` (string), `command_id` (string), `duration_millis` (int32)

```java
import com.telnyx.sdk.models.calls.actions.ActionSendDtmfParams;
import com.telnyx.sdk.models.calls.actions.ActionSendDtmfResponse;

ActionSendDtmfParams params = ActionSendDtmfParams.builder()
    .callControlId("call_control_id")
    .digits("1www2WABCDw9")
    .build();
ActionSendDtmfResponse response = client.calls().actions().sendDtmf(params);
```

## SIPREC start

Start siprec session to configured in SIPREC connector SRS.

`POST /calls/{call_control_id}/actions/siprec_start`

Optional: `client_state` (string), `connector_name` (string), `include_metadata_custom_headers` (enum), `secure` (enum), `session_timeout_secs` (integer), `sip_transport` (enum), `siprec_track` (enum)

```java
import com.telnyx.sdk.models.calls.actions.ActionStartSiprecParams;
import com.telnyx.sdk.models.calls.actions.ActionStartSiprecResponse;

ActionStartSiprecResponse response = client.calls().actions().startSiprec("call_control_id");
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

Optional: `client_state` (string), `command_id` (string)

```java
import com.telnyx.sdk.models.calls.actions.ActionStopSiprecParams;
import com.telnyx.sdk.models.calls.actions.ActionStopSiprecResponse;

ActionStopSiprecResponse response = client.calls().actions().stopSiprec("call_control_id");
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

Optional: `client_state` (string), `command_id` (string), `direction` (enum), `noise_suppression_engine` (enum), `noise_suppression_engine_config` (object)

```java
import com.telnyx.sdk.models.calls.actions.ActionStartNoiseSuppressionParams;
import com.telnyx.sdk.models.calls.actions.ActionStartNoiseSuppressionResponse;

ActionStartNoiseSuppressionResponse response = client.calls().actions().startNoiseSuppression("call_control_id");
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

Optional: `client_state` (string), `command_id` (string)

```java
import com.telnyx.sdk.models.calls.actions.ActionStopNoiseSuppressionParams;
import com.telnyx.sdk.models.calls.actions.ActionStopNoiseSuppressionResponse;

ActionStopNoiseSuppressionResponse response = client.calls().actions().stopNoiseSuppression("call_control_id");
```

## Switch supervisor role

Switch the supervisor role for a bridged call.

`POST /calls/{call_control_id}/actions/switch_supervisor_role` — Required: `role`

```java
import com.telnyx.sdk.models.calls.actions.ActionSwitchSupervisorRoleParams;
import com.telnyx.sdk.models.calls.actions.ActionSwitchSupervisorRoleResponse;

ActionSwitchSupervisorRoleParams params = ActionSwitchSupervisorRoleParams.builder()
    .callControlId("call_control_id")
    .role(ActionSwitchSupervisorRoleParams.Role.BARGE)
    .build();
ActionSwitchSupervisorRoleResponse response = client.calls().actions().switchSupervisorRole(params);
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
