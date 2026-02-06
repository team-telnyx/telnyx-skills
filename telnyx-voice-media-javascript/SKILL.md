---
name: telnyx-voice-media-javascript
description: >-
  Play audio files, use text-to-speech, and record calls. Use when building IVR
  systems, playing announcements, or recording conversations. This skill
  provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: voice-media
  language: javascript
---

# Telnyx Voice Media - JavaScript

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

## Play audio URL

Play an audio file on the call.

`POST /calls/{call_control_id}/actions/playback_start`

```javascript
const response = await client.calls.actions.startPlayback('call_control_id');

console.log(response.data);
```

## Stop audio playback

Stop audio being played on the call.

`POST /calls/{call_control_id}/actions/playback_stop`

```javascript
const response = await client.calls.actions.stopPlayback('call_control_id');

console.log(response.data);
```

## Record pause

Pause recording the call.

`POST /calls/{call_control_id}/actions/record_pause`

```javascript
const response = await client.calls.actions.pauseRecording('call_control_id');

console.log(response.data);
```

## Record resume

Resume recording the call.

`POST /calls/{call_control_id}/actions/record_resume`

```javascript
const response = await client.calls.actions.resumeRecording('call_control_id');

console.log(response.data);
```

## Recording start

Start recording the call.

`POST /calls/{call_control_id}/actions/record_start` — Required: `format`, `channels`

```javascript
const response = await client.calls.actions.startRecording('call_control_id', {
  channels: 'single',
  format: 'wav',
});

console.log(response.data);
```

## Recording stop

Stop recording the call.

`POST /calls/{call_control_id}/actions/record_stop`

```javascript
const response = await client.calls.actions.stopRecording('call_control_id');

console.log(response.data);
```

## Speak text

Convert text to speech and play it back on the call.

`POST /calls/{call_control_id}/actions/speak` — Required: `payload`, `voice`

```javascript
const response = await client.calls.actions.speak('call_control_id', {
  payload: 'Say this on the call',
  voice: 'female',
});

console.log(response.data);
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
