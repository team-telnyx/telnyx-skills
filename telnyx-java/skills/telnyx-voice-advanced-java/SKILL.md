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

```java
import com.telnyx.sdk.models.calls.actions.ActionStartSiprecParams;
import com.telnyx.sdk.models.calls.actions.ActionStartSiprecResponse;

ActionStartSiprecResponse response = client.calls().actions().startSiprec("call_control_id");
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopSiprecParams;
import com.telnyx.sdk.models.calls.actions.ActionStopSiprecResponse;

ActionStopSiprecResponse response = client.calls().actions().stopSiprec("call_control_id");
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartNoiseSuppressionParams;
import com.telnyx.sdk.models.calls.actions.ActionStartNoiseSuppressionResponse;

ActionStartNoiseSuppressionResponse response = client.calls().actions().startNoiseSuppression("call_control_id");
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

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
