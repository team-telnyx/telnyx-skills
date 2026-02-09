---
name: telnyx-voice-media-ruby
description: >-
  Play audio files, use text-to-speech, and record calls. Use when building IVR
  systems, playing announcements, or recording conversations. This skill
  provides Ruby SDK examples.
metadata:
  author: telnyx
  product: voice-media
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Media - Ruby

## Installation

```bash
gem install telnyx
```

## Setup

```ruby
require "telnyx"

client = Telnyx::Client.new(
  api_key: ENV["TELNYX_API_KEY"], # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Play audio URL

Play an audio file on the call.

`POST /calls/{call_control_id}/actions/playback_start`

```ruby
response = client.calls.actions.start_playback("call_control_id")

puts(response)
```

## Stop audio playback

Stop audio being played on the call.

`POST /calls/{call_control_id}/actions/playback_stop`

```ruby
response = client.calls.actions.stop_playback("call_control_id")

puts(response)
```

## Record pause

Pause recording the call.

`POST /calls/{call_control_id}/actions/record_pause`

```ruby
response = client.calls.actions.pause_recording("call_control_id")

puts(response)
```

## Record resume

Resume recording the call.

`POST /calls/{call_control_id}/actions/record_resume`

```ruby
response = client.calls.actions.resume_recording("call_control_id")

puts(response)
```

## Recording start

Start recording the call.

`POST /calls/{call_control_id}/actions/record_start` — Required: `format`, `channels`

```ruby
response = client.calls.actions.start_recording("call_control_id", channels: :single, format_: :wav)

puts(response)
```

## Recording stop

Stop recording the call.

`POST /calls/{call_control_id}/actions/record_stop`

```ruby
response = client.calls.actions.stop_recording("call_control_id")

puts(response)
```

## Speak text

Convert text to speech and play it back on the call.

`POST /calls/{call_control_id}/actions/speak` — Required: `payload`, `voice`

```ruby
response = client.calls.actions.speak("call_control_id", payload: "Say this on the call", voice: "female")

puts(response)
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
