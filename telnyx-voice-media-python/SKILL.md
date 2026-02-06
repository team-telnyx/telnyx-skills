---
name: telnyx-voice-media-python
description: >-
  Play audio files, use text-to-speech, and record calls. Use when building IVR
  systems, playing announcements, or recording conversations. This skill
  provides Python SDK examples.
metadata:
  author: telnyx
  product: voice-media
  language: python
---

# Telnyx Voice Media - Python

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

## Play audio URL

Play an audio file on the call.

`POST /calls/{call_control_id}/actions/playback_start`

```python
response = client.calls.actions.start_playback(
    call_control_id="call_control_id",
)
print(response.data)
```

## Stop audio playback

Stop audio being played on the call.

`POST /calls/{call_control_id}/actions/playback_stop`

```python
response = client.calls.actions.stop_playback(
    call_control_id="call_control_id",
)
print(response.data)
```

## Record pause

Pause recording the call.

`POST /calls/{call_control_id}/actions/record_pause`

```python
response = client.calls.actions.pause_recording(
    call_control_id="call_control_id",
)
print(response.data)
```

## Record resume

Resume recording the call.

`POST /calls/{call_control_id}/actions/record_resume`

```python
response = client.calls.actions.resume_recording(
    call_control_id="call_control_id",
)
print(response.data)
```

## Recording start

Start recording the call.

`POST /calls/{call_control_id}/actions/record_start` — Required: `format`, `channels`

```python
response = client.calls.actions.start_recording(
    call_control_id="call_control_id",
    channels="single",
    format="wav",
)
print(response.data)
```

## Recording stop

Stop recording the call.

`POST /calls/{call_control_id}/actions/record_stop`

```python
response = client.calls.actions.stop_recording(
    call_control_id="call_control_id",
)
print(response.data)
```

## Speak text

Convert text to speech and play it back on the call.

`POST /calls/{call_control_id}/actions/speak` — Required: `payload`, `voice`

```python
response = client.calls.actions.speak(
    call_control_id="call_control_id",
    payload="Say this on the call",
    voice="female",
)
print(response.data)
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
