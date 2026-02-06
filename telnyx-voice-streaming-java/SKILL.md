---
name: telnyx-voice-streaming-java
description: >-
  Stream call audio in real-time, fork media to external destinations, and
  transcribe speech live. Use for real-time analytics and AI integrations. This
  skill provides Java SDK examples.
metadata:
  author: telnyx
  product: voice-streaming
  language: java
---

# Telnyx Voice Streaming - Java

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

## Forking start

Call forking allows you to stream the media from a call to a specific target in realtime.

`POST /calls/{call_control_id}/actions/fork_start`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartForkingParams;
import com.telnyx.sdk.models.calls.actions.ActionStartForkingResponse;

ActionStartForkingResponse response = client.calls().actions().startForking("call_control_id");
```

## Forking stop

Stop forking a call.

`POST /calls/{call_control_id}/actions/fork_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopForkingParams;
import com.telnyx.sdk.models.calls.actions.ActionStopForkingResponse;

ActionStopForkingResponse response = client.calls().actions().stopForking("call_control_id");
```

## Streaming start

Start streaming the media from a call to a specific WebSocket address or Dialogflow connection in near-realtime.

`POST /calls/{call_control_id}/actions/streaming_start`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartStreamingParams;
import com.telnyx.sdk.models.calls.actions.ActionStartStreamingResponse;

ActionStartStreamingResponse response = client.calls().actions().startStreaming("call_control_id");
```

## Streaming stop

Stop streaming a call to a WebSocket.

`POST /calls/{call_control_id}/actions/streaming_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopStreamingParams;
import com.telnyx.sdk.models.calls.actions.ActionStopStreamingResponse;

ActionStopStreamingResponse response = client.calls().actions().stopStreaming("call_control_id");
```

## Transcription start

Start real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_start`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartTranscriptionParams;
import com.telnyx.sdk.models.calls.actions.ActionStartTranscriptionResponse;
import com.telnyx.sdk.models.calls.actions.TranscriptionStartRequest;

ActionStartTranscriptionParams params = ActionStartTranscriptionParams.builder()
    .callControlId("call_control_id")
    .transcriptionStartRequest(TranscriptionStartRequest.builder().build())
    .build();
ActionStartTranscriptionResponse response = client.calls().actions().startTranscription(params);
```

## Transcription stop

Stop real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopTranscriptionParams;
import com.telnyx.sdk.models.calls.actions.ActionStopTranscriptionResponse;

ActionStopTranscriptionResponse response = client.calls().actions().stopTranscription("call_control_id");
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
