---
name: telnyx-voice-java
description: >-
  Make and receive calls, transfer, bridge, and manage call lifecycle with Call
  Control. Includes application management and call events. This skill provides
  Java SDK examples.
metadata:
  author: telnyx
  product: voice
  language: java
---

# Telnyx Voice - Java

## Installation

```bash
// Add to pom.xml or build.gradle - see https://github.com/team-telnyx/telnyx-java
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## Answer call

Answer an incoming call.

`POST /calls/{call_control_id}/actions/answer`

```java
import com.telnyx.sdk.models.calls.actions.ActionAnswerParams;
import com.telnyx.sdk.models.calls.actions.ActionAnswerResponse;

ActionAnswerResponse response = client.calls().actions().answer("call_control_id");
```

## Bridge calls

Bridge two call control calls.

`POST /calls/{call_control_id}/actions/bridge` — Required: `call_control_id`

```java
import com.telnyx.sdk.models.calls.actions.ActionBridgeParams;
import com.telnyx.sdk.models.calls.actions.ActionBridgeResponse;

ActionBridgeParams params = ActionBridgeParams.builder()
    .callControlIdToBridge("call_control_id")
    .callControlId("v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg")
    .build();
ActionBridgeResponse response = client.calls().actions().bridge(params);
```

## Dial

Dial a number or SIP URI from a given connection.

`POST /calls` — Required: `connection_id`, `to`, `from`

```java
import com.telnyx.sdk.models.calls.CallDialParams;
import com.telnyx.sdk.models.calls.CallDialResponse;

CallDialParams params = CallDialParams.builder()
    .connectionId("7267xxxxxxxxxxxxxx")
    .from("+18005550101")
    .to("+18005550100 or sip:username@sip.telnyx.com")
    .build();
CallDialResponse response = client.calls().dial(params);
```

## Hangup call

Hang up the call.

`POST /calls/{call_control_id}/actions/hangup`

```java
import com.telnyx.sdk.models.calls.actions.ActionHangupParams;
import com.telnyx.sdk.models.calls.actions.ActionHangupResponse;

ActionHangupResponse response = client.calls().actions().hangup("call_control_id");
```

## Transfer call

Transfer a call to a new destination.

`POST /calls/{call_control_id}/actions/transfer` — Required: `to`

```java
import com.telnyx.sdk.models.calls.actions.ActionTransferParams;
import com.telnyx.sdk.models.calls.actions.ActionTransferResponse;

ActionTransferParams params = ActionTransferParams.builder()
    .callControlId("call_control_id")
    .to("+18005550100 or sip:username@sip.telnyx.com")
    .build();
ActionTransferResponse response = client.calls().actions().transfer(params);
```

## List all active calls for given connection

Lists all active calls for given connection.

`GET /connections/{connection_id}/active_calls`

```java
import com.telnyx.sdk.models.connections.ConnectionListActiveCallsPage;
import com.telnyx.sdk.models.connections.ConnectionListActiveCallsParams;

ConnectionListActiveCallsPage page = client.connections().listActiveCalls("1293384261075731461");
```

## List call control applications

Return a list of call control applications.

`GET /call_control_applications`

```java
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationListPage;
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationListParams;

CallControlApplicationListPage page = client.callControlApplications().list();
```

## Create a call control application

Create a call control application.

`POST /call_control_applications` — Required: `application_name`, `webhook_event_url`

```java
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationCreateParams;
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationCreateResponse;

CallControlApplicationCreateParams params = CallControlApplicationCreateParams.builder()
    .applicationName("call-router")
    .webhookEventUrl("https://example.com")
    .build();
CallControlApplicationCreateResponse callControlApplication = client.callControlApplications().create(params);
```

## Retrieve a call control application

Retrieves the details of an existing call control application.

`GET /call_control_applications/{id}`

```java
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationRetrieveParams;
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationRetrieveResponse;

CallControlApplicationRetrieveResponse callControlApplication = client.callControlApplications().retrieve("id");
```

## Update a call control application

Updates settings of an existing call control application.

`PATCH /call_control_applications/{id}` — Required: `application_name`, `webhook_event_url`

```java
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationUpdateParams;
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationUpdateResponse;

CallControlApplicationUpdateParams params = CallControlApplicationUpdateParams.builder()
    .id("id")
    .applicationName("call-router")
    .webhookEventUrl("https://example.com")
    .build();
CallControlApplicationUpdateResponse callControlApplication = client.callControlApplications().update(params);
```

## Delete a call control application

Deletes a call control application.

`DELETE /call_control_applications/{id}`

```java
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationDeleteParams;
import com.telnyx.sdk.models.callcontrolapplications.CallControlApplicationDeleteResponse;

CallControlApplicationDeleteResponse callControlApplication = client.callControlApplications().delete("id");
```

## List call events

Filters call events by given filter parameters.

`GET /call_events`

```java
import com.telnyx.sdk.models.callevents.CallEventListPage;
import com.telnyx.sdk.models.callevents.CallEventListParams;

CallEventListPage page = client.callEvents().list();
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
