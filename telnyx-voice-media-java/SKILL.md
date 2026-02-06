---
name: telnyx-voice-media-java
description: >-
  Play audio files, use text-to-speech, and record calls. Use when building IVR
  systems, playing announcements, or recording conversations. This skill
  provides Java SDK examples.
metadata:
  author: telnyx
  product: voice-media
  language: java
---

# Telnyx Voice Media - Java

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

## Play audio URL

Play an audio file on the call.

`POST /calls/{call_control_id}/actions/playback_start`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartPlaybackParams;
import com.telnyx.sdk.models.calls.actions.ActionStartPlaybackResponse;

ActionStartPlaybackResponse response = client.calls().actions().startPlayback("call_control_id");
```

## Stop audio playback

Stop audio being played on the call.

`POST /calls/{call_control_id}/actions/playback_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopPlaybackParams;
import com.telnyx.sdk.models.calls.actions.ActionStopPlaybackResponse;

ActionStopPlaybackResponse response = client.calls().actions().stopPlayback("call_control_id");
```

## Record pause

Pause recording the call.

`POST /calls/{call_control_id}/actions/record_pause`

```java
import com.telnyx.sdk.models.calls.actions.ActionPauseRecordingParams;
import com.telnyx.sdk.models.calls.actions.ActionPauseRecordingResponse;

ActionPauseRecordingResponse response = client.calls().actions().pauseRecording("call_control_id");
```

## Record resume

Resume recording the call.

`POST /calls/{call_control_id}/actions/record_resume`

```java
import com.telnyx.sdk.models.calls.actions.ActionResumeRecordingParams;
import com.telnyx.sdk.models.calls.actions.ActionResumeRecordingResponse;

ActionResumeRecordingResponse response = client.calls().actions().resumeRecording("call_control_id");
```

## Recording start

Start recording the call.

`POST /calls/{call_control_id}/actions/record_start` — Required: `format`, `channels`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartRecordingParams;
import com.telnyx.sdk.models.calls.actions.ActionStartRecordingResponse;

ActionStartRecordingParams params = ActionStartRecordingParams.builder()
    .callControlId("call_control_id")
    .channels(ActionStartRecordingParams.Channels.SINGLE)
    .format(ActionStartRecordingParams.Format.WAV)
    .build();
ActionStartRecordingResponse response = client.calls().actions().startRecording(params);
```

## Recording stop

Stop recording the call.

`POST /calls/{call_control_id}/actions/record_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopRecordingParams;
import com.telnyx.sdk.models.calls.actions.ActionStopRecordingResponse;
import com.telnyx.sdk.models.calls.actions.StopRecordingRequest;

ActionStopRecordingParams params = ActionStopRecordingParams.builder()
    .callControlId("call_control_id")
    .stopRecordingRequest(StopRecordingRequest.builder().build())
    .build();
ActionStopRecordingResponse response = client.calls().actions().stopRecording(params);
```

## Speak text

Convert text to speech and play it back on the call.

`POST /calls/{call_control_id}/actions/speak` — Required: `payload`, `voice`

```java
import com.telnyx.sdk.models.calls.actions.ActionSpeakParams;
import com.telnyx.sdk.models.calls.actions.ActionSpeakResponse;

ActionSpeakParams params = ActionSpeakParams.builder()
    .callControlId("call_control_id")
    .payload("Say this on the call")
    .voice("female")
    .build();
ActionSpeakResponse response = client.calls().actions().speak(params);
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
