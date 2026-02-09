---
name: telnyx-voice-gather-python
description: >-
  Collect DTMF input and speech from callers using standard gather or AI-powered
  gather. Build interactive voice menus and AI voice assistants. This skill
  provides Python SDK examples.
metadata:
  author: telnyx
  product: voice-gather
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Gather - Python

## Installation

```bash
pip install telnyx
```

## Setup

```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),  # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Add messages to AI Assistant

Add messages to the conversation started by an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_add_messages`

```python
response = client.calls.actions.add_ai_assistant_messages(
    call_control_id="call_control_id",
)
print(response.data)
```

## Start AI Assistant

Start an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_start`

```python
response = client.calls.actions.start_ai_assistant(
    call_control_id="call_control_id",
)
print(response.data)
```

## Stop AI Assistant

Stop an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_stop`

```python
response = client.calls.actions.stop_ai_assistant(
    call_control_id="call_control_id",
)
print(response.data)
```

## Gather stop

Stop current gather.

`POST /calls/{call_control_id}/actions/gather_stop`

```python
response = client.calls.actions.stop_gather(
    call_control_id="call_control_id",
)
print(response.data)
```

## Gather using AI

Gather parameters defined in the request payload using a voice assistant.

`POST /calls/{call_control_id}/actions/gather_using_ai` — Required: `parameters`

```python
response = client.calls.actions.gather_using_ai(
    call_control_id="call_control_id",
    parameters={
        "properties": "bar",
        "required": "bar",
        "type": "bar",
    },
)
print(response.data)
```

## Gather using audio

Play an audio file on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_audio`

```python
response = client.calls.actions.gather_using_audio(
    call_control_id="call_control_id",
)
print(response.data)
```

## Gather using speak

Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_speak` — Required: `voice`, `payload`

```python
response = client.calls.actions.gather_using_speak(
    call_control_id="call_control_id",
    payload="say this on call",
    voice="male",
)
print(response.data)
```

## Gather

Gather DTMF signals to build interactive menus.

`POST /calls/{call_control_id}/actions/gather`

```python
response = client.calls.actions.gather(
    call_control_id="call_control_id",
)
print(response.data)
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
