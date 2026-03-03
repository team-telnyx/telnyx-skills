---
name: telnyx-voice-curl
description: >-
  Make and receive calls, transfer, bridge, and manage call lifecycle with Call
  Control. Includes application management and call events. This skill provides
  REST API (curl) examples.
metadata:
  author: telnyx
  product: voice
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List call control applications

Return a list of call control applications.

`GET /call_control_applications`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/call_control_applications?sort=connection_name"
```

## Create a call control application

Create a call control application.

`POST /call_control_applications` — Required: `application_name`, `webhook_event_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `call_cost_in_webhooks` (boolean), `dtmf_type` (enum), `first_command_timeout` (boolean), `first_command_timeout_secs` (integer), `inbound` (object), `outbound` (object), `redact_dtmf_debug_logging` (boolean), `webhook_api_version` (enum), `webhook_event_failover_url` (url), `webhook_timeout_secs` (['integer', 'null'])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "application_name": "call-router",
  "webhook_event_url": "https://example.com",
  "anchorsite_override": "Amsterdam, Netherlands",
  "dtmf_type": "Inband",
  "first_command_timeout": true,
  "first_command_timeout_secs": 10,
  "webhook_api_version": "1",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25,
  "redact_dtmf_debug_logging": true
}' \
  "https://api.telnyx.com/v2/call_control_applications"
```

## Retrieve a call control application

Retrieves the details of an existing call control application.

`GET /call_control_applications/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/call_control_applications/1293384261075731499"
```

## Update a call control application

Updates settings of an existing call control application.

`PATCH /call_control_applications/{id}` — Required: `application_name`, `webhook_event_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `call_cost_in_webhooks` (boolean), `dtmf_type` (enum), `first_command_timeout` (boolean), `first_command_timeout_secs` (integer), `inbound` (object), `outbound` (object), `redact_dtmf_debug_logging` (boolean), `tags` (array[string]), `webhook_api_version` (enum), `webhook_event_failover_url` (url), `webhook_timeout_secs` (['integer', 'null'])

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "application_name": "call-router",
  "webhook_event_url": "https://example.com",
  "anchorsite_override": "Amsterdam, Netherlands",
  "dtmf_type": "Inband",
  "first_command_timeout": true,
  "first_command_timeout_secs": 10,
  "tags": [
    "tag1",
    "tag2"
  ],
  "webhook_api_version": "1",
  "webhook_event_failover_url": "https://failover.example.com",
  "webhook_timeout_secs": 25,
  "redact_dtmf_debug_logging": true
}' \
  "https://api.telnyx.com/v2/call_control_applications/1293384261075731499"
```

## Delete a call control application

Deletes a call control application.

`DELETE /call_control_applications/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/call_control_applications/1293384261075731499"
```

## Dial

Dial a number or SIP URI from a given connection.

`POST /calls` — Required: `connection_id`, `to`, `from`

Optional: `answering_machine_detection` (enum), `answering_machine_detection_config` (object), `audio_url` (string), `billing_group_id` (uuid), `bridge_intent` (boolean), `bridge_on_answer` (boolean), `client_state` (string), `command_id` (string), `conference_config` (object), `custom_headers` (array[object]), `dialogflow_config` (object), `enable_dialogflow` (boolean), `from_display_name` (string), `link_to` (string), `media_encryption` (enum), `media_name` (string), `park_after_unbridge` (string), `preferred_codecs` (string), `record` (enum), `record_channels` (enum), `record_custom_file_name` (string), `record_format` (enum), `record_max_length` (int32), `record_timeout_secs` (int32), `record_track` (enum), `record_trim` (enum), `send_silence_when_idle` (boolean), `sip_auth_password` (string), `sip_auth_username` (string), `sip_headers` (array[object]), `sip_region` (enum), `sip_transport_protocol` (enum), `sound_modifications` (object), `stream_auth_token` (string), `stream_bidirectional_codec` (enum), `stream_bidirectional_mode` (enum), `stream_bidirectional_sampling_rate` (enum), `stream_bidirectional_target_legs` (enum), `stream_codec` (enum), `stream_establish_before_call_originate` (boolean), `stream_track` (enum), `stream_url` (string), `supervise_call_control_id` (string), `supervisor_role` (enum), `time_limit_secs` (int32), `timeout_secs` (int32), `transcription` (boolean), `transcription_config` (object), `webhook_url` (string), `webhook_url_method` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "to": "string",
  "from": "+18005550101",
  "from_display_name": "Company Name",
  "connection_id": "string",
  "audio_url": "http://example.com/message.wav",
  "media_name": "my_media_uploaded_to_media_storage_api",
  "preferred_codecs": "G722,PCMU,PCMA,G729,OPUS,VP8,H264",
  "timeout_secs": 60,
  "time_limit_secs": 600,
  "custom_headers": [
    {
      "name": "head_1",
      "value": "val_1"
    },
    {
      "name": "head_2",
      "value": "val_2"
    }
  ],
  "billing_group_id": "f5586561-8ff0-4291-a0ac-84fe544797bd",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "link_to": "ilditnZK_eVysupV21KzmzN_sM29ygfauQojpm4BgFtfX5hXAcjotg==",
  "bridge_intent": true,
  "bridge_on_answer": true,
  "park_after_unbridge": "self",
  "sip_headers": [
    {
      "name": "User-to-User",
      "value": "value"
    }
  ],
  "sound_modifications": {
    "pitch": 0.8,
    "semitone": -2,
    "octaves": 0.1,
    "track": "both"
  },
  "stream_url": "wss://www.example.com/websocket",
  "stream_track": "both_tracks",
  "stream_codec": "PCMA",
  "stream_bidirectional_mode": "rtp",
  "stream_bidirectional_codec": "G722",
  "stream_bidirectional_target_legs": "both",
  "stream_bidirectional_sampling_rate": 16000,
  "stream_establish_before_call_originate": true,
  "send_silence_when_idle": true,
  "webhook_url": "https://www.example.com/server-b/",
  "webhook_url_method": "GET",
  "record": "record-from-answer",
  "record_channels": "single",
  "record_format": "wav",
  "record_max_length": 1000,
  "record_timeout_secs": 100,
  "record_track": "outbound",
  "record_trim": "trim-silence",
  "record_custom_file_name": "my_recording_file_name",
  "supervise_call_control_id": "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  "enable_dialogflow": true,
  "transcription": true,
  "transcription_config": {
    "transcription_engine": "Google",
    "transcription_engine_config": {
      "transcription_engine": "Google",
      "language": "en"
    },
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
  },
  "sip_region": "Canada",
  "stream_auth_token": "your-auth-token"
}' \
  "https://api.telnyx.com/v2/calls"
```

## Retrieve a call status

Returns the status of a call (data is available 10 minutes after call ended).

`GET /calls/{call_control_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/calls/{call_control_id}"
```

## Answer call

Answer an incoming call.

`POST /calls/{call_control_id}/actions/answer`

Optional: `billing_group_id` (uuid), `client_state` (string), `command_id` (string), `custom_headers` (array[object]), `preferred_codecs` (enum), `record` (enum), `record_channels` (enum), `record_custom_file_name` (string), `record_format` (enum), `record_max_length` (int32), `record_timeout_secs` (int32), `record_track` (enum), `record_trim` (enum), `send_silence_when_idle` (boolean), `sip_headers` (array[object]), `sound_modifications` (object), `stream_bidirectional_codec` (enum), `stream_bidirectional_mode` (enum), `stream_bidirectional_target_legs` (enum), `stream_codec` (enum), `stream_track` (enum), `stream_url` (string), `transcription` (boolean), `transcription_config` (object), `webhook_retries_policies` (object), `webhook_url` (string), `webhook_url_method` (enum), `webhook_urls` (object), `webhook_urls_method` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "billing_group_id": "f5586561-8ff0-4291-a0ac-84fe544797bd",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "custom_headers": [
    {
      "name": "head_1",
      "value": "val_1"
    },
    {
      "name": "head_2",
      "value": "val_2"
    }
  ],
  "preferred_codecs": "G722,PCMU,PCMA,G729,OPUS,VP8,H264",
  "sip_headers": [
    {
      "name": "User-to-User",
      "value": "value"
    }
  ],
  "sound_modifications": {
    "pitch": 0.8,
    "semitone": -2,
    "octaves": 0.1,
    "track": "both"
  },
  "stream_url": "wss://www.example.com/websocket",
  "stream_track": "both_tracks",
  "stream_codec": "PCMA",
  "stream_bidirectional_mode": "rtp",
  "stream_bidirectional_codec": "G722",
  "stream_bidirectional_target_legs": "both",
  "send_silence_when_idle": true,
  "webhook_url": "https://www.example.com/server-b/",
  "webhook_url_method": "GET",
  "transcription": true,
  "transcription_config": {
    "transcription_engine": "Google",
    "transcription_engine_config": {
      "transcription_engine": "Google",
      "language": "en"
    },
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
  },
  "record": "record-from-answer",
  "record_channels": "single",
  "record_format": "wav",
  "record_max_length": 1000,
  "record_timeout_secs": 100,
  "record_track": "outbound",
  "record_trim": "trim-silence",
  "record_custom_file_name": "my_recording_file_name",
  "webhook_urls": {
    "call.hangup": "https://www.example.com/webhooks/hangup",
    "call.bridge": "https://www.example.com/webhooks/bridge"
  },
  "webhook_urls_method": "POST",
  "webhook_retries_policies": {
    "call.hangup": {
      "retries_ms": [
        1000,
        2000,
        5000
      ]
    }
  }
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer"
```

## Bridge calls

Bridge two call control calls.

`POST /calls/{call_control_id}/actions/bridge` — Required: `call_control_id`

Optional: `client_state` (string), `command_id` (string), `hold_after_unbridge` (boolean), `mute_dtmf` (enum), `park_after_unbridge` (string), `play_ringtone` (boolean), `prevent_double_bridge` (boolean), `queue` (string), `record` (enum), `record_channels` (enum), `record_custom_file_name` (string), `record_format` (enum), `record_max_length` (int32), `record_timeout_secs` (int32), `record_track` (enum), `record_trim` (enum), `ringtone` (enum), `video_room_context` (string), `video_room_id` (uuid)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "call_control_id": "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "queue": "support",
  "video_room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
  "video_room_context": "Alice",
  "prevent_double_bridge": true,
  "park_after_unbridge": "self",
  "play_ringtone": true,
  "ringtone": "pl",
  "record": "record-from-answer",
  "record_channels": "single",
  "record_format": "wav",
  "record_max_length": 1000,
  "record_timeout_secs": 100,
  "record_track": "outbound",
  "record_trim": "trim-silence",
  "record_custom_file_name": "my_recording_file_name",
  "mute_dtmf": "opposite",
  "hold_after_unbridge": true
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/bridge"
```

## Hangup call

Hang up the call.

`POST /calls/{call_control_id}/actions/hangup`

Optional: `client_state` (string), `command_id` (string), `custom_headers` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "custom_headers": [
    {
      "name": "head_1",
      "value": "val_1"
    },
    {
      "name": "head_2",
      "value": "val_2"
    }
  ]
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/hangup"
```

## SIP Refer a call

Initiate a SIP Refer on a Call Control call.

`POST /calls/{call_control_id}/actions/refer` — Required: `sip_address`

Optional: `client_state` (string), `command_id` (string), `custom_headers` (array[object]), `sip_auth_password` (string), `sip_auth_username` (string), `sip_headers` (array[object])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "sip_address": "sip:username@sip.non-telnyx-address.com",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "custom_headers": [
    {
      "name": "head_1",
      "value": "val_1"
    },
    {
      "name": "head_2",
      "value": "val_2"
    }
  ],
  "sip_headers": [
    {
      "name": "User-to-User",
      "value": "value"
    }
  ]
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/refer"
```

## Reject a call

Reject an incoming call.

`POST /calls/{call_control_id}/actions/reject` — Required: `cause`

Optional: `client_state` (string), `command_id` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "cause": "USER_BUSY"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/reject"
```

## Send SIP info

Sends SIP info from this leg.

`POST /calls/{call_control_id}/actions/send_sip_info` — Required: `content_type`, `body`

Optional: `client_state` (string), `command_id` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "content_type": "application/json",
  "body": "{\"key\": \"value\", \"numValue\": 100}",
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901"
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/send_sip_info"
```

## Transfer call

Transfer a call to a new destination.

`POST /calls/{call_control_id}/actions/transfer` — Required: `to`

Optional: `answering_machine_detection` (enum), `answering_machine_detection_config` (object), `audio_url` (string), `client_state` (string), `command_id` (string), `custom_headers` (array[object]), `early_media` (boolean), `from` (string), `from_display_name` (string), `media_encryption` (enum), `media_name` (string), `mute_dtmf` (enum), `park_after_unbridge` (string), `preferred_codecs` (string), `record` (enum), `record_channels` (enum), `record_custom_file_name` (string), `record_format` (enum), `record_max_length` (int32), `record_timeout_secs` (int32), `record_track` (enum), `record_trim` (enum), `sip_auth_password` (string), `sip_auth_username` (string), `sip_headers` (array[object]), `sip_region` (enum), `sip_transport_protocol` (enum), `sound_modifications` (object), `target_leg_client_state` (string), `time_limit_secs` (int32), `timeout_secs` (int32), `webhook_retries_policies` (object), `webhook_url` (string), `webhook_url_method` (enum), `webhook_urls` (object), `webhook_urls_method` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "to": "+18005550100",
  "from": "+18005550101",
  "from_display_name": "Company Name",
  "audio_url": "http://example.com/message.wav",
  "early_media": false,
  "media_name": "my_media_uploaded_to_media_storage_api",
  "timeout_secs": 60,
  "time_limit_secs": 600,
  "park_after_unbridge": "self",
  "custom_headers": [
    {
      "name": "head_1",
      "value": "val_1"
    },
    {
      "name": "head_2",
      "value": "val_2"
    }
  ],
  "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "target_leg_client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
  "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
  "sip_auth_username": "username",
  "sip_auth_password": "password",
  "sip_headers": [
    {
      "name": "User-to-User",
      "value": "value"
    }
  ],
  "sound_modifications": {
    "pitch": 0.8,
    "semitone": -2,
    "octaves": 0.1,
    "track": "both"
  },
  "webhook_url": "https://www.example.com/server-b/",
  "webhook_url_method": "GET",
  "mute_dtmf": "opposite",
  "record": "record-from-answer",
  "record_channels": "single",
  "record_format": "wav",
  "record_max_length": 1000,
  "record_timeout_secs": 100,
  "record_track": "outbound",
  "record_trim": "trim-silence",
  "record_custom_file_name": "my_recording_file_name",
  "sip_region": "Canada",
  "preferred_codecs": "G722,PCMU,PCMA,G729,OPUS,VP8,H264",
  "webhook_urls": {
    "call.answered": "https://www.example.com/webhooks/answered",
    "call.hangup": "https://www.example.com/webhooks/hangup"
  },
  "webhook_urls_method": "POST",
  "webhook_retries_policies": {
    "call.answered": {
      "retries_ms": [
        1000,
        2000,
        5000
      ]
    }
  }
}' \
  "https://api.telnyx.com/v2/calls/{call_control_id}/actions/transfer"
```

## List all active calls for given connection

Lists all active calls for given connection.

`GET /connections/{connection_id}/active_calls`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/connections/1293384261075731461/active_calls"
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callAnswered` | Call Answered |
| `callBridged` | Call Bridged |
| `callHangup` | Call Hangup |
| `callInitiated` | Call Initiated |

### Webhook payload fields

**`callAnswered`**

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
| `data.payload.custom_headers` | array[object] | Custom headers set on answer command |
| `data.payload.sip_headers` | array[object] | User-to-User and Diversion headers from sip invite. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.start_time` | date-time | ISO 8601 datetime of when the call started. |
| `data.payload.state` | enum | State received from a command. |
| `data.payload.tags` | array[string] | Array of tags associated to number. |

**`callBridged`**

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

**`callHangup`**

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
| `data.payload.custom_headers` | array[object] | Custom headers set on answer command |
| `data.payload.sip_headers` | array[object] | User-to-User and Diversion headers from sip invite. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.start_time` | date-time | ISO 8601 datetime of when the call started. |
| `data.payload.state` | enum | State received from a command. |
| `data.payload.tags` | array[string] | Array of tags associated to number. |
| `data.payload.hangup_cause` | enum | The reason the call was ended (`call_rejected`, `normal_clearing`, `originator_cancel`, `timeout`, `time_limit`, `use... |
| `data.payload.hangup_source` | enum | The party who ended the call (`callee`, `caller`, `unknown`). |
| `data.payload.sip_hangup_cause` | string | The reason the call was ended (SIP response code). |
| `data.payload.call_quality_stats` | ['object', 'null'] | Call quality statistics aggregated from the CHANNEL_HANGUP_COMPLETE event. |

**`callInitiated`**

| Field | Type | Description |
|-------|------|-------------|
| `data.record_type` | enum | Identifies the type of the resource. |
| `data.event_type` | enum | The type of event being delivered. |
| `data.id` | uuid | Identifies the type of resource. |
| `data.occurred_at` | date-time | ISO 8601 datetime of when the event occurred. |
| `data.payload.call_control_id` | string | Call ID used to issue commands via Call Control API. |
| `data.payload.connection_id` | string | Call Control App ID (formerly Telnyx connection ID) used in the call. |
| `data.payload.connection_codecs` | string | The list of comma-separated codecs enabled for the connection. |
| `data.payload.offered_codecs` | string | The list of comma-separated codecs offered by caller. |
| `data.payload.call_leg_id` | string | ID that is unique to the call and can be used to correlate webhook events. |
| `data.payload.custom_headers` | array[object] | Custom headers from sip invite |
| `data.payload.sip_headers` | array[object] | User-to-User and Diversion headers from sip invite. |
| `data.payload.shaken_stir_attestation` | string | SHAKEN/STIR attestation level. |
| `data.payload.shaken_stir_validated` | boolean | Whether attestation was successfully validated or not. |
| `data.payload.call_session_id` | string | ID that is unique to the call session and can be used to correlate webhook events. |
| `data.payload.client_state` | string | State received from a command. |
| `data.payload.caller_id_name` | string | Caller id. |
| `data.payload.call_screening_result` | string | Call screening result. |
| `data.payload.from` | string | Number or SIP URI placing the call. |
| `data.payload.to` | string | Destination number or SIP URI of the call. |
| `data.payload.direction` | enum | Whether the call is `incoming` or `outgoing`. |
| `data.payload.state` | enum | State received from a command. |
| `data.payload.start_time` | date-time | ISO 8601 datetime of when the call started. |
| `data.payload.tags` | array[string] | Array of tags associated to number. |
