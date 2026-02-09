---
name: telnyx-voice-streaming-ruby
description: >-
  Stream call audio in real-time, fork media to external destinations, and
  transcribe speech live. Use for real-time analytics and AI integrations. This
  skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: voice-streaming
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Streaming - Ruby

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

## Forking start

Call forking allows you to stream the media from a call to a specific target in realtime.

`POST /calls/{call_control_id}/actions/fork_start`

```ruby
response = client.calls.actions.start_forking("call_control_id")

puts(response)
```

## Forking stop

Stop forking a call.

`POST /calls/{call_control_id}/actions/fork_stop`

```ruby
response = client.calls.actions.stop_forking("call_control_id")

puts(response)
```

## Streaming start

Start streaming the media from a call to a specific WebSocket address or Dialogflow connection in near-realtime.

`POST /calls/{call_control_id}/actions/streaming_start`

```ruby
response = client.calls.actions.start_streaming("call_control_id")

puts(response)
```

## Streaming stop

Stop streaming a call to a WebSocket.

`POST /calls/{call_control_id}/actions/streaming_stop`

```ruby
response = client.calls.actions.stop_streaming("call_control_id")

puts(response)
```

## Transcription start

Start real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_start`

```ruby
response = client.calls.actions.start_transcription("call_control_id")

puts(response)
```

## Transcription stop

Stop real-time transcription.

`POST /calls/{call_control_id}/actions/transcription_stop`

```ruby
response = client.calls.actions.stop_transcription("call_control_id")

puts(response)
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
