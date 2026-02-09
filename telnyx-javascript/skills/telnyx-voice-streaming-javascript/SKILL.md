---
name: telnyx-voice-streaming-javascript
description: >-
  Stream call audio in real-time, fork media to external destinations, and
  transcribe speech live. Use for real-time analytics and AI integrations. This
  skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: voice-streaming
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Streaming - JavaScript

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

## Forking start

Call forking allows you to stream the media from a call to a specific target in realtime.

`POST /calls/{call_control_id}/actions/fork_start`

```javascript
const response = await client.calls.actions.startForking('call_control_id');

console.log(response.data);
```

## Forking stop

Stop forking a call.

`POST /calls/{call_control_id}/actions/fork_stop`

```javascript
const response = await client.calls.actions.stopForking('call_control_id');

console.log(response.data);
```

## Streaming start

Start streaming the media from a call to a specific WebSocket address or Dialogflow connection in near-realtime.

`POST /calls/{call_control_id}/actions/streaming_start`

```javascript
const response = await client.calls.actions.startStreaming('call_control_id');

console.log(response.data);
```

## Streaming stop

Stop streaming a call to a WebSocket.

`POST /calls/{call_control_id}/actions/streaming_stop`

```javascript
const response = await client.calls.actions.stopStreaming('call_control_id');

console.log(response.data);
```

## Transcription start

Start real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_start`

```javascript
const response = await client.calls.actions.startTranscription('call_control_id');

console.log(response.data);
```

## Transcription stop

Stop real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_stop`

```javascript
const response = await client.calls.actions.stopTranscription('call_control_id');

console.log(response.data);
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
