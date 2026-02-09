---
name: telnyx-voice-gather-java
description: >-
  Collect DTMF input and speech from callers using standard gather or AI-powered
  gather. Build interactive voice menus and AI voice assistants. This skill
  provides Java SDK examples.
metadata:
  author: telnyx
  product: voice-gather
  language: java
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Gather - Java

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

## Add messages to AI Assistant

Add messages to the conversation started by an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_add_messages`

```java
import com.telnyx.sdk.models.calls.actions.ActionAddAiAssistantMessagesParams;
import com.telnyx.sdk.models.calls.actions.ActionAddAiAssistantMessagesResponse;

ActionAddAiAssistantMessagesResponse response = client.calls().actions().addAiAssistantMessages("call_control_id");
```

## Start AI Assistant

Start an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_start`

```java
import com.telnyx.sdk.models.calls.actions.ActionStartAiAssistantParams;
import com.telnyx.sdk.models.calls.actions.ActionStartAiAssistantResponse;

ActionStartAiAssistantResponse response = client.calls().actions().startAiAssistant("call_control_id");
```

## Stop AI Assistant

Stop an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopAiAssistantParams;
import com.telnyx.sdk.models.calls.actions.ActionStopAiAssistantResponse;

ActionStopAiAssistantResponse response = client.calls().actions().stopAiAssistant("call_control_id");
```

## Gather stop

Stop current gather.

`POST /calls/{call_control_id}/actions/gather_stop`

```java
import com.telnyx.sdk.models.calls.actions.ActionStopGatherParams;
import com.telnyx.sdk.models.calls.actions.ActionStopGatherResponse;

ActionStopGatherResponse response = client.calls().actions().stopGather("call_control_id");
```

## Gather using AI

Gather parameters defined in the request payload using a voice assistant.

`POST /calls/{call_control_id}/actions/gather_using_ai` — Required: `parameters`

```java
import com.telnyx.sdk.core.JsonValue;
import com.telnyx.sdk.models.calls.actions.ActionGatherUsingAiParams;
import com.telnyx.sdk.models.calls.actions.ActionGatherUsingAiResponse;

ActionGatherUsingAiParams params = ActionGatherUsingAiParams.builder()
    .callControlId("call_control_id")
    .parameters(ActionGatherUsingAiParams.Parameters.builder()
        .putAdditionalProperty("properties", JsonValue.from("bar"))
        .putAdditionalProperty("required", JsonValue.from("bar"))
        .putAdditionalProperty("type", JsonValue.from("bar"))
        .build())
    .build();
ActionGatherUsingAiResponse response = client.calls().actions().gatherUsingAi(params);
```

## Gather using audio

Play an audio file on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_audio`

```java
import com.telnyx.sdk.models.calls.actions.ActionGatherUsingAudioParams;
import com.telnyx.sdk.models.calls.actions.ActionGatherUsingAudioResponse;

ActionGatherUsingAudioResponse response = client.calls().actions().gatherUsingAudio("call_control_id");
```

## Gather using speak

Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_speak` — Required: `voice`, `payload`

```java
import com.telnyx.sdk.models.calls.actions.ActionGatherUsingSpeakParams;
import com.telnyx.sdk.models.calls.actions.ActionGatherUsingSpeakResponse;

ActionGatherUsingSpeakParams params = ActionGatherUsingSpeakParams.builder()
    .callControlId("call_control_id")
    .payload("say this on call")
    .voice("male")
    .build();
ActionGatherUsingSpeakResponse response = client.calls().actions().gatherUsingSpeak(params);
```

## Gather

Gather DTMF signals to build interactive menus.

`POST /calls/{call_control_id}/actions/gather`

```java
import com.telnyx.sdk.models.calls.actions.ActionGatherParams;
import com.telnyx.sdk.models.calls.actions.ActionGatherResponse;

ActionGatherResponse response = client.calls().actions().gather("call_control_id");
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
