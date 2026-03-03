---
name: telnyx-texml-curl
description: >-
  Build voice applications using TeXML markup language (TwiML-compatible).
  Manage applications, calls, conferences, recordings, queues, and streams. This
  skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: texml
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Texml - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Fetch multiple call resources

Returns multiple call resources for an account.

`GET /texml/Accounts/{account_sid}/Calls`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls?Page=1&PageSize=10&To=+1312345678&From=+1312345678&Status=no-answer&StartTime=2023-05-22&StartTime_gt=2023-05-22&StartTime_lt=2023-05-22&EndTime=2023-05-22&EndTime_gt=2023-05-22&EndTime_lt=2023-05-22"
```

## Initiate an outbound call

Initiate an outbound TeXML call.

`POST /texml/Accounts/{account_sid}/Calls` — Required: `To`, `From`, `ApplicationSid`

Optional: `AsyncAmd` (boolean), `AsyncAmdStatusCallback` (string), `AsyncAmdStatusCallbackMethod` (enum), `CallerId` (string), `CancelPlaybackOnDetectMessageEnd` (boolean), `CancelPlaybackOnMachineDetection` (boolean), `CustomHeaders` (array[object]), `DetectionMode` (enum), `FallbackUrl` (string), `MachineDetection` (enum), `MachineDetectionSilenceTimeout` (integer), `MachineDetectionSpeechEndThreshold` (integer), `MachineDetectionSpeechThreshold` (integer), `MachineDetectionTimeout` (integer), `PreferredCodecs` (string), `Record` (boolean), `RecordingChannels` (enum), `RecordingStatusCallback` (string), `RecordingStatusCallbackEvent` (string), `RecordingStatusCallbackMethod` (enum), `RecordingTimeout` (integer), `RecordingTrack` (enum), `SendRecordingUrl` (boolean), `SipAuthPassword` (string), `SipAuthUsername` (string), `SipRegion` (enum), `StatusCallback` (string), `StatusCallbackEvent` (enum), `StatusCallbackMethod` (enum), `SuperviseCallSid` (string), `SupervisingRole` (enum), `Texml` (string), `TimeLimit` (integer), `Timeout` (integer), `Trim` (enum), `Url` (string), `UrlMethod` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "ApplicationSid": "string",
  "To": "+16175551212",
  "From": "+16175551212",
  "CallerId": "Info",
  "Url": "https://www.example.com/instructions.xml",
  "UrlMethod": "GET",
  "FallbackUrl": "https://www.example.com/instructions-fallback.xml",
  "StatusCallback": "https://www.example.com/callback",
  "StatusCallbackMethod": "GET",
  "StatusCallbackEvent": "initiated",
  "MachineDetection": "Enable",
  "DetectionMode": "Premium",
  "AsyncAmd": true,
  "AsyncAmdStatusCallback": "https://www.example.com/callback",
  "AsyncAmdStatusCallbackMethod": "GET",
  "MachineDetectionTimeout": 5000,
  "MachineDetectionSpeechThreshold": 2000,
  "MachineDetectionSpeechEndThreshold": 2000,
  "MachineDetectionSilenceTimeout": 2000,
  "CancelPlaybackOnMachineDetection": false,
  "CancelPlaybackOnDetectMessageEnd": false,
  "PreferredCodecs": "PCMA,PCMU",
  "Record": false,
  "RecordingChannels": "dual",
  "RecordingStatusCallback": "https://example.com/recording_status_callback",
  "RecordingStatusCallbackMethod": "GET",
  "RecordingStatusCallbackEvent": "in-progress completed absent",
  "RecordingTimeout": 5,
  "RecordingTrack": "inbound",
  "SendRecordingUrl": false,
  "SipAuthPassword": "1234",
  "SipAuthUsername": "user",
  "Trim": "trim-silence",
  "CustomHeaders": [
    {
      "name": "X-Custom-Header",
      "value": "custom-value"
    }
  ],
  "SipRegion": "Canada",
  "SuperviseCallSid": "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
  "SupervisingRole": "monitor",
  "Timeout": 60,
  "TimeLimit": 3600,
  "Texml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Say>Hello</Say></Response>"
}' \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls"
```

## Fetch a call

Returns an individual call identified by its CallSid.

`GET /texml/Accounts/{account_sid}/Calls/{call_sid}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}"
```

## Update call

Update TeXML call.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}"
```

## Fetch recordings for a call

Returns recordings for a call identified by call_sid.

`GET /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json"
```

## Request recording for a call

Starts recording with specified parameters for call idientified by call_sid.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json"
```

## Update recording on a call

Updates recording resource for particular call.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{recording_sid}.json`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings/6a09cdc3-8948-47f0-aa62-74ac943d6c58.json"
```

## Request siprec session for a call

Starts siprec session with specified parameters for call idientified by call_sid.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json"
```

## Updates siprec session for a call

Updates siprec session identified by siprec_sid.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{siprec_sid}.json`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{siprec_sid}.json"
```

## Start streaming media from a call.

Starts streaming media from a call to a specific WebSocket address.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Streams.json`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Streams.json"
```

## Update streaming on a call

Updates streaming resource for particular call.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Streams/{streaming_sid}.json`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls/{call_sid}/Streams/6a09cdc3-8948-47f0-aa62-74ac943d6c58.json"
```

## List conference resources

Lists conference resources.

`GET /texml/Accounts/{account_sid}/Conferences`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences?Page=1&PageSize=10&FriendlyName=weekly_review_call&Status=in-progress&DateCreated=>=2023-05-22&DateUpdated=>=2023-05-22"
```

## Fetch a conference resource

Returns a conference resource.

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}"
```

## Update a conference resource

Updates a conference resource.

`POST /texml/Accounts/{account_sid}/Conferences/{conference_sid}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}"
```

## List conference participants

Lists conference participants

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants"
```

## Dial a new conference participant

Dials a new conference participant

`POST /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants"
```

## Get conference participant resource

Gets conference participant resource

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}"
```

## Update a conference participant

Updates a conference participant

`POST /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}"
```

## Delete a conference participant

Deletes a conference participant

`DELETE /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}"
```

## List conference recordings

Lists conference recordings

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings"
```

## Fetch recordings for a conference

Returns recordings for a conference identified by conference_sid.

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json"
```

## List queue resources

Lists queue resources.

`GET /texml/Accounts/{account_sid}/Queues`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Queues?Page=1&PageSize=10&DateCreated=>=2023-05-22&DateUpdated=>=2023-05-22"
```

## Create a new queue

Creates a new queue resource.

`POST /texml/Accounts/{account_sid}/Queues`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Queues"
```

## Fetch a queue resource

Returns a queue resource.

`GET /texml/Accounts/{account_sid}/Queues/{queue_sid}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Queues/{queue_sid}"
```

## Update a queue resource

Updates a queue resource.

`POST /texml/Accounts/{account_sid}/Queues/{queue_sid}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Queues/{queue_sid}"
```

## Delete a queue resource

Delete a queue resource.

`DELETE /texml/Accounts/{account_sid}/Queues/{queue_sid}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Queues/{queue_sid}"
```

## Fetch multiple recording resources

Returns multiple recording resources for an account.

`GET /texml/Accounts/{account_sid}/Recordings.json`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Recordings.json?Page=1&PageSize=10&DateCreated=2023-05-22T00:00:00Z"
```

## Fetch recording resource

Returns recording resource identified by recording id.

`GET /texml/Accounts/{account_sid}/Recordings/{recording_sid}.json`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Recordings/6a09cdc3-8948-47f0-aa62-74ac943d6c58.json"
```

## Delete recording resource

Deletes recording resource identified by recording id.

`DELETE /texml/Accounts/{account_sid}/Recordings/{recording_sid}.json`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Recordings/6a09cdc3-8948-47f0-aa62-74ac943d6c58.json"
```

## List recording transcriptions

Returns multiple recording transcription resources for an account.

`GET /texml/Accounts/{account_sid}/Transcriptions.json`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Transcriptions.json?PageSize=10"
```

## Fetch a recording transcription resource

Returns the recording transcription resource identified by its ID.

`GET /texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Transcriptions/6a09cdc3-8948-47f0-aa62-74ac943d6c58.json"
```

## Delete a recording transcription

Permanently deletes a recording transcription.

`DELETE /texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Transcriptions/6a09cdc3-8948-47f0-aa62-74ac943d6c58.json"
```

## Create a TeXML secret

Create a TeXML secret which can be later used as a Dynamic Parameter for TeXML when using Mustache Templates in your TeXML.

`POST /texml/secrets` — Required: `name`, `value`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "My Secret Name",
  "value": "My Secret Value"
}' \
  "https://api.telnyx.com/v2/texml/secrets"
```

## List all TeXML Applications

Returns a list of your TeXML Applications.

`GET /texml_applications`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml_applications?sort=friendly_name"
```

## Creates a TeXML Application

Creates a TeXML Application.

`POST /texml_applications` — Required: `friendly_name`, `voice_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `call_cost_in_webhooks` (boolean), `dtmf_type` (enum), `first_command_timeout` (boolean), `first_command_timeout_secs` (integer), `inbound` (object), `outbound` (object), `status_callback` (uri), `status_callback_method` (enum), `tags` (array[string]), `voice_fallback_url` (uri), `voice_method` (enum)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "friendly_name": "call-router",
  "active": false,
  "anchorsite_override": "Amsterdam, Netherlands",
  "dtmf_type": "Inband",
  "first_command_timeout": true,
  "first_command_timeout_secs": 10,
  "tags": [
    "tag1",
    "tag2"
  ],
  "voice_url": "https://example.com",
  "voice_fallback_url": "https://fallback.example.com",
  "voice_method": "get",
  "status_callback": "https://example.com",
  "status_callback_method": "get"
}' \
  "https://api.telnyx.com/v2/texml_applications"
```

## Retrieve a TeXML Application

Retrieves the details of an existing TeXML Application.

`GET /texml_applications/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/texml_applications/1293384261075731499"
```

## Update a TeXML Application

Updates settings of an existing TeXML Application.

`PATCH /texml_applications/{id}` — Required: `friendly_name`, `voice_url`

Optional: `active` (boolean), `anchorsite_override` (enum), `call_cost_in_webhooks` (boolean), `dtmf_type` (enum), `first_command_timeout` (boolean), `first_command_timeout_secs` (integer), `inbound` (object), `outbound` (object), `status_callback` (uri), `status_callback_method` (enum), `tags` (array[string]), `voice_fallback_url` (uri), `voice_method` (enum)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "friendly_name": "call-router",
  "active": false,
  "anchorsite_override": "Amsterdam, Netherlands",
  "dtmf_type": "Inband",
  "first_command_timeout": true,
  "first_command_timeout_secs": 10,
  "voice_url": "https://example.com",
  "voice_fallback_url": "https://fallback.example.com",
  "voice_method": "get",
  "status_callback": "https://example.com",
  "status_callback_method": "get",
  "tags": [
    "tag1",
    "tag2"
  ]
}' \
  "https://api.telnyx.com/v2/texml_applications/1293384261075731499"
```

## Deletes a TeXML Application

Deletes a TeXML Application.

`DELETE /texml_applications/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/texml_applications/1293384261075731499"
```
