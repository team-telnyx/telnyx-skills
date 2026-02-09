---
name: telnyx-voice-gather-ruby
description: >-
  Collect DTMF input and speech from callers using standard gather or AI-powered
  gather. Build interactive voice menus and AI voice assistants. This skill
  provides Ruby SDK examples.
metadata:
  author: telnyx
  product: voice-gather
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Gather - Ruby

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

## Add messages to AI Assistant

Add messages to the conversation started by an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_add_messages`

```ruby
response = client.calls.actions.add_ai_assistant_messages("call_control_id")

puts(response)
```

## Start AI Assistant

Start an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_start`

```ruby
response = client.calls.actions.start_ai_assistant("call_control_id")

puts(response)
```

## Stop AI Assistant

Stop an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_stop`

```ruby
response = client.calls.actions.stop_ai_assistant("call_control_id")

puts(response)
```

## Gather stop

Stop current gather.

`POST /calls/{call_control_id}/actions/gather_stop`

```ruby
response = client.calls.actions.stop_gather("call_control_id")

puts(response)
```

## Gather using AI

Gather parameters defined in the request payload using a voice assistant.

`POST /calls/{call_control_id}/actions/gather_using_ai` — Required: `parameters`

```ruby
response = client.calls.actions.gather_using_ai(
  "call_control_id",
  parameters: {properties: "bar", required: "bar", type: "bar"}
)

puts(response)
```

## Gather using audio

Play an audio file on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_audio`

```ruby
response = client.calls.actions.gather_using_audio("call_control_id")

puts(response)
```

## Gather using speak

Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_speak` — Required: `voice`, `payload`

```ruby
response = client.calls.actions.gather_using_speak("call_control_id", payload: "say this on call", voice: "male")

puts(response)
```

## Gather

Gather DTMF signals to build interactive menus.

`POST /calls/{call_control_id}/actions/gather`

```ruby
response = client.calls.actions.gather("call_control_id")

puts(response)
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
