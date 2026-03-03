---
name: telnyx-voice-gather-curl
description: >-
  Collect DTMF input and speech from callers using standard gather or AI-powered
  gather. Build interactive voice menus and AI voice assistants. This skill
  provides REST API (curl) examples.
metadata:
  author: telnyx
  product: voice-gather
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Gather - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Add messages to AI Assistant

Add messages to the conversation started by an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_add_messages`

Optional: `client_state` (string), `command_id` (string), `messages` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_add_messages"
```

## Start AI Assistant

Start an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_start`

Optional: `assistant` (object), `client_state` (string), `command_id` (string), `greeting` (string), `interruption_settings` (object), `transcription` (object), `voice` (string), `voice_settings` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "voice": "Telnyx.KokoroTTS.af",
  "greeting": "Hello, can you tell me your age and where you live?",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_start"
```

## Stop AI Assistant

Stop an AI assistant on the call.

`POST /calls/{call_control_id}/actions/ai_assistant_stop`

Optional: `client_state` (string), `command_id` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_stop"
```

## Gather

Gather DTMF signals to build interactive menus.

`POST /calls/{call_control_id}/actions/gather`

Optional: `client_state` (string), `command_id` (string), `gather_id` (string), `initial_timeout_millis` (int32), `inter_digit_timeout_millis` (int32), `maximum_digits` (int32), `minimum_digits` (int32), `terminating_digit` (string), `timeout_millis` (int32), `valid_digits` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "minimum_digits": 1,
  "maximum_digits": 10,
  "timeout_millis": 60000,
  "inter_digit_timeout_millis": 10000,
  "initial_timeout_millis": 10000,
  "terminating_digit": "#",
  "valid_digits": "123",
  "gather_id": "my_gather_id",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather"
```

## Gather stop

Stop current gather.

`POST /calls/{call_control_id}/actions/gather_stop`

Optional: `client_state` (string), `command_id` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather_stop"
```

## Gather using AI

Gather parameters defined in the request payload using a voice assistant.

`POST /calls/{call_control_id}/actions/gather_using_ai` — Required: `parameters`

Optional: `assistant` (object), `client_state` (string), `command_id` (string), `gather_ended_speech` (string), `greeting` (string), `interruption_settings` (object), `language` (object), `message_history` (array[object]), `send_message_history_updates` (boolean), `send_partial_results` (boolean), `transcription` (object), `user_response_timeout_ms` (integer), `voice` (string), `voice_settings` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "parameters": {
    "properties": {
      "age": {
        "description": "The age of the customer.",
        "type": "integer"
      },
      "location": {
        "description": "The location of the customer.",
        "type": "string"
      }
    },
    "required": [
      "age",
      "location"
    ],
    "type": "object"
  },
  "voice": "Telnyx.KokoroTTS.af",
  "greeting": "Hello, can you tell me your age and where you live?",
  "send_partial_results": false,
  "send_message_history_updates": false,
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "user_response_timeout_ms": 15000,
  "gather_ended_speech": "Thank you for providing the information."
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather_using_ai"
```

## Gather using audio

Play an audio file on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_audio`

Optional: `audio_url` (string), `client_state` (string), `command_id` (string), `inter_digit_timeout_millis` (int32), `invalid_audio_url` (string), `invalid_media_name` (string), `maximum_digits` (int32), `maximum_tries` (int32), `media_name` (string), `minimum_digits` (int32), `terminating_digit` (string), `timeout_millis` (int32), `valid_digits` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "audio_url": "http://example.com/message.wav",
  "media_name": "my_media_uploaded_to_media_storage_api",
  "invalid_audio_url": "http://example.com/invalid.wav",
  "invalid_media_name": "my_media_uploaded_to_media_storage_api",
  "minimum_digits": 1,
  "maximum_digits": 10,
  "maximum_tries": 3,
  "timeout_millis": 60000,
  "terminating_digit": "#",
  "valid_digits": "123",
  "inter_digit_timeout_millis": 10000,
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather_using_audio"
```

## Gather using speak

Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus.

`POST /calls/{call_control_id}/actions/gather_using_speak` — Required: `voice`, `payload`

Optional: `client_state` (string), `command_id` (string), `inter_digit_timeout_millis` (int32), `invalid_payload` (string), `language` (enum), `maximum_digits` (int32), `maximum_tries` (int32), `minimum_digits` (int32), `payload_type` (enum), `service_level` (enum), `terminating_digit` (string), `timeout_millis` (int32), `valid_digits` (string), `voice_settings` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "payload": "Say this on the call",
  "invalid_payload": "Say this on the call",
  "payload_type": "ssml",
  "service_level": "premium",
  "voice": "Telnyx.KokoroTTS.af",
  "language": "en-US",
  "minimum_digits": 1,
  "maximum_digits": 10,
  "maximum_tries": 3,
  "timeout_millis": 60000,
  "terminating_digit": "#",
  "valid_digits": "123",
  "inter_digit_timeout_millis": 10000,
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather_using_speak"
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `CallAIGatherEnded` | Call AI Gather Ended |
| `CallAIGatherMessageHistoryUpdated` | Call AI Gather Message History Updated |
| `CallAIGatherPartialResults` | Call AI Gather Partial Results |
| `callGatherEnded` | Call Gather Ended |

### Webhook payload fields

**`CallAIGatherEnded`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Telnyx connection ID used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.message_history` | array[object] | The history of the messages exchanged during the AI gather |
| `data.payload.result` | object | The result of the AI gather, its type depends of the `parameters` provided in the command |
| `data.payload.status` | enum | Reflects how command ended. |

**`CallAIGatherMessageHistoryUpdated`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Telnyx connection ID used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.message_history` | array[object] | The history of the messages exchanged during the AI gather |

**`CallAIGatherPartialResults`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Telnyx connection ID used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.message_history` | array[object] | The history of the messages exchanged during the AI gather |
| `data.payload.partial_results` | object | The partial result of the AI gather, its type depends of the `parameters` provided in the command |

**`callGatherEnded`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.digits` | string | The received DTMF digit or symbol. |
| `data.payload.status` | enum | Reflects how command ended. |
