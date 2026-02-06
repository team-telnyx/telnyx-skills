---
name: telnyx-voice-gather-javascript
description: >-
  Collect DTMF input and speech from callers using standard gather or AI-powered
  gather. Build interactive voice menus and AI voice assistants. This skill
  provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: voice-gather
  language: javascript
---

# Telnyx Voice Gather - JavaScript

## Installation

```bash
npm install telnyx
```

## Setup

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'], // This is the default and can be omitted
});
```

All examples below assume `client` is already initialized as shown above.

## Add messages to AI Assistant

Add messages to the conversation started by an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_add_messages`

```javascript
const response = await client.calls.actions.addAIAssistantMessages('call_control_id');

console.log(response.data);
```

## Start AI Assistant

Start an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_start`

```javascript
const response = await client.calls.actions.startAIAssistant('call_control_id');

console.log(response.data);
```

## Stop AI Assistant

Stop an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_stop`

```javascript
const response = await client.calls.actions.stopAIAssistant('call_control_id');

console.log(response.data);
```

## Gather stop

Stop current gather.

`POST /calls/{call_control_id}/actions/gather_stop`

```javascript
const response = await client.calls.actions.stopGather('call_control_id');

console.log(response.data);
```

## Gather using AI

Gather parameters defined in the request payload using a voice assistant.

`POST /calls/{call_control_id}/actions/gather_using_ai` — Required: `parameters`

```javascript
const response = await client.calls.actions.gatherUsingAI('call_control_id', {
  parameters: {
    properties: 'bar',
    required: 'bar',
    type: 'bar',
  },
});

console.log(response.data);
```

## Gather using audio

Play an audio file on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_audio`

```javascript
const response = await client.calls.actions.gatherUsingAudio('call_control_id');

console.log(response.data);
```

## Gather using speak

Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_speak` — Required: `voice`, `payload`

```javascript
const response = await client.calls.actions.gatherUsingSpeak('call_control_id', {
  payload: 'say this on call',
  voice: 'male',
});

console.log(response.data);
```

## Gather

Gather DTMF signals to build interactive menus.

`POST /calls/{call_control_id}/actions/gather`

```javascript
const response = await client.calls.actions.gather('call_control_id');

console.log(response.data);
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
