---
name: telnyx-texml-javascript
description: >-
  Build voice applications using TeXML markup language (TwiML-compatible).
  Manage applications, calls, conferences, recordings, queues, and streams. This
  skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: texml
  language: javascript
---

# Telnyx Texml - JavaScript

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

## List all TeXML Applications

Returns a list of your TeXML Applications.

`GET /texml_applications`

```javascript
// Automatically fetches more pages as needed.
for await (const texmlApplication of client.texmlApplications.list()) {
  console.log(texmlApplication.id);
}
```

## Creates a TeXML Application

Creates a TeXML Application.

`POST /texml_applications` — Required: `friendly_name`, `voice_url`

```javascript
const texmlApplication = await client.texmlApplications.create({
  friendly_name: 'call-router',
  voice_url: 'https://example.com',
});

console.log(texmlApplication.data);
```

## Retrieve a TeXML Application

Retrieves the details of an existing TeXML Application.

`GET /texml_applications/{id}`

```javascript
const texmlApplication = await client.texmlApplications.retrieve('1293384261075731499');

console.log(texmlApplication.data);
```

## Update a TeXML Application

Updates settings of an existing TeXML Application.

`PATCH /texml_applications/{id}` — Required: `friendly_name`, `voice_url`

```javascript
const texmlApplication = await client.texmlApplications.update('1293384261075731499', {
  friendly_name: 'call-router',
  voice_url: 'https://example.com',
});

console.log(texmlApplication.data);
```

## Deletes a TeXML Application

Deletes a TeXML Application.

`DELETE /texml_applications/{id}`

```javascript
const texmlApplication = await client.texmlApplications.delete('1293384261075731499');

console.log(texmlApplication.data);
```

## Fetch multiple call resources

Returns multiple call resouces for an account.

`GET /texml/Accounts/{account_sid}/Calls`

```javascript
const response = await client.texml.accounts.calls.retrieveCalls('account_sid');

console.log(response.calls);
```

## Initiate an outbound call

Initiate an outbound TeXML call.

`POST /texml/Accounts/{account_sid}/Calls` — Required: `To`, `From`, `ApplicationSid`

```javascript
const response = await client.texml.accounts.calls.calls('account_sid', {
  ApplicationSid: 'example-app-sid',
  From: '+13120001234',
  To: '+13121230000',
});

console.log(response.from);
```

## Fetch a call

Returns an individual call identified by its CallSid.

`GET /texml/Accounts/{account_sid}/Calls/{call_sid}`

```javascript
const call = await client.texml.accounts.calls.retrieve('call_sid', { account_sid: 'account_sid' });

console.log(call.account_sid);
```

## Update call

Update TeXML call.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}`

```javascript
const call = await client.texml.accounts.calls.update('call_sid', { account_sid: 'account_sid' });

console.log(call.account_sid);
```

## List conference participants

Lists conference participants

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants`

```javascript
const response = await client.texml.accounts.conferences.participants.retrieveParticipants(
  'conference_sid',
  { account_sid: 'account_sid' },
);

console.log(response.end);
```

## Dial a new conference participant

Dials a new conference participant

`POST /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants`

```javascript
const response = await client.texml.accounts.conferences.participants.participants(
  'conference_sid',
  { account_sid: 'account_sid' },
);

console.log(response.account_sid);
```

## Get conference participant resource

Gets conference participant resource

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}`

```javascript
const participant = await client.texml.accounts.conferences.participants.retrieve(
  'call_sid_or_participant_label',
  { account_sid: 'account_sid', conference_sid: 'conference_sid' },
);

console.log(participant.account_sid);
```

## Update a conference participant

Updates a conference participant

`POST /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}`

```javascript
const participant = await client.texml.accounts.conferences.participants.update(
  'call_sid_or_participant_label',
  { account_sid: 'account_sid', conference_sid: 'conference_sid' },
);

console.log(participant.account_sid);
```

## Delete a conference participant

Deletes a conference participant

`DELETE /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}`

```javascript
await client.texml.accounts.conferences.participants.delete('call_sid_or_participant_label', {
  account_sid: 'account_sid',
  conference_sid: 'conference_sid',
});
```

## List conference resources

Lists conference resources.

`GET /texml/Accounts/{account_sid}/Conferences`

```javascript
const response = await client.texml.accounts.conferences.retrieveConferences('account_sid');

console.log(response.conferences);
```

## Fetch a conference resource

Returns a conference resource.

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}`

```javascript
const conference = await client.texml.accounts.conferences.retrieve('conference_sid', {
  account_sid: 'account_sid',
});

console.log(conference.account_sid);
```

## Update a conference resource

Updates a conference resource.

`POST /texml/Accounts/{account_sid}/Conferences/{conference_sid}`

```javascript
const conference = await client.texml.accounts.conferences.update('conference_sid', {
  account_sid: 'account_sid',
});

console.log(conference.account_sid);
```

## List queue resources

Lists queue resources.

`GET /texml/Accounts/{account_sid}/Queues`

```javascript
// Automatically fetches more pages as needed.
for await (const queueListResponse of client.texml.accounts.queues.list('account_sid')) {
  console.log(queueListResponse.account_sid);
}
```

## Create a new queue

Creates a new queue resource.

`POST /texml/Accounts/{account_sid}/Queues`

```javascript
const queue = await client.texml.accounts.queues.create('account_sid');

console.log(queue.account_sid);
```

## Fetch a queue resource

Returns a queue resource.

`GET /texml/Accounts/{account_sid}/Queues/{queue_sid}`

```javascript
const queue = await client.texml.accounts.queues.retrieve('queue_sid', {
  account_sid: 'account_sid',
});

console.log(queue.account_sid);
```

## Update a queue resource

Updates a queue resource.

`POST /texml/Accounts/{account_sid}/Queues/{queue_sid}`

```javascript
const queue = await client.texml.accounts.queues.update('queue_sid', {
  account_sid: 'account_sid',
});

console.log(queue.account_sid);
```

## Delete a queue resource

Delete a queue resource.

`DELETE /texml/Accounts/{account_sid}/Queues/{queue_sid}`

```javascript
await client.texml.accounts.queues.delete('queue_sid', { account_sid: 'account_sid' });
```

## Fetch multiple recording resources

Returns multiple recording resources for an account.

`GET /texml/Accounts/{account_sid}/Recordings.json`

```javascript
const response = await client.texml.accounts.retrieveRecordingsJson('account_sid');

console.log(response.end);
```

## Fetch recording resource

Returns recording resource identified by recording id.

`GET /texml/Accounts/{account_sid}/Recordings/{recording_sid}.json`

```javascript
const texmlGetCallRecordingResponseBody =
  await client.texml.accounts.recordings.json.retrieveRecordingSidJson(
    '6a09cdc3-8948-47f0-aa62-74ac943d6c58',
    { account_sid: 'account_sid' },
  );

console.log(texmlGetCallRecordingResponseBody.account_sid);
```

## Delete recording resource

Deletes recording resource identified by recording id.

`DELETE /texml/Accounts/{account_sid}/Recordings/{recording_sid}.json`

```javascript
await client.texml.accounts.recordings.json.deleteRecordingSidJson(
  '6a09cdc3-8948-47f0-aa62-74ac943d6c58',
  { account_sid: 'account_sid' },
);
```

## Fetch recordings for a call

Returns recordings for a call identified by call_sid.

`GET /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json`

```javascript
const response = await client.texml.accounts.calls.recordingsJson.retrieveRecordingsJson(
  'call_sid',
  { account_sid: 'account_sid' },
);

console.log(response.end);
```

## Request recording for a call

Starts recording with specified parameters for call idientified by call_sid.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json`

```javascript
const response = await client.texml.accounts.calls.recordingsJson.recordingsJson('call_sid', {
  account_sid: 'account_sid',
});

console.log(response.account_sid);
```

## Update recording on a call

Updates recording resource for particular call.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{recording_sid}.json`

```javascript
const response = await client.texml.accounts.calls.recordings.recordingSidJson(
  '6a09cdc3-8948-47f0-aa62-74ac943d6c58',
  { account_sid: 'account_sid', call_sid: 'call_sid' },
);

console.log(response.account_sid);
```

## List conference recordings

Lists conference recordings

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings`

```javascript
const response = await client.texml.accounts.conferences.retrieveRecordings('conference_sid', {
  account_sid: 'account_sid',
});

console.log(response.end);
```

## Fetch recordings for a conference

Returns recordings for a conference identified by conference_sid.

`GET /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json`

```javascript
const response = await client.texml.accounts.conferences.retrieveRecordingsJson('conference_sid', {
  account_sid: 'account_sid',
});

console.log(response.end);
```

## Create a TeXML secret

Create a TeXML secret which can be later used as a Dynamic Parameter for TeXML when using Mustache Templates in your TeXML.

`POST /texml/secrets` — Required: `name`, `value`

```javascript
const response = await client.texml.secrets({ name: 'My Secret Name', value: 'My Secret Value' });

console.log(response.data);
```

## Request siprec session for a call

Starts siprec session with specified parameters for call idientified by call_sid.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json`

```javascript
const response = await client.texml.accounts.calls.siprecJson('call_sid', {
  account_sid: 'account_sid',
});

console.log(response.account_sid);
```

## Updates siprec session for a call

Updates siprec session identified by siprec_sid.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{siprec_sid}.json`

```javascript
const response = await client.texml.accounts.calls.siprec.siprecSidJson('siprec_sid', {
  account_sid: 'account_sid',
  call_sid: 'call_sid',
});

console.log(response.account_sid);
```

## Start streaming media from a call.

Starts streaming media from a call to a specific WebSocket address.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Streams.json`

```javascript
const response = await client.texml.accounts.calls.streamsJson('call_sid', {
  account_sid: 'account_sid',
});

console.log(response.account_sid);
```

## Update streaming on a call

Updates streaming resource for particular call.

`POST /texml/Accounts/{account_sid}/Calls/{call_sid}/Streams/{streaming_sid}.json`

```javascript
const response = await client.texml.accounts.calls.streams.streamingSidJson(
  '6a09cdc3-8948-47f0-aa62-74ac943d6c58',
  { account_sid: 'account_sid', call_sid: 'call_sid' },
);

console.log(response.account_sid);
```

## List recording transcriptions

Returns multiple recording transcription resources for an account.

`GET /texml/Accounts/{account_sid}/Transcriptions.json`

```javascript
const response = await client.texml.accounts.retrieveTranscriptionsJson('account_sid');

console.log(response.end);
```

## Fetch a recording transcription resource

Returns the recording transcription resource identified by its ID.

`GET /texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json`

```javascript
const response =
  await client.texml.accounts.transcriptions.json.retrieveRecordingTranscriptionSidJson(
    '6a09cdc3-8948-47f0-aa62-74ac943d6c58',
    { account_sid: 'account_sid' },
  );

console.log(response.account_sid);
```

## Delete a recording transcription

Permanently deletes a recording transcription.

`DELETE /texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json`

```javascript
await client.texml.accounts.transcriptions.json.deleteRecordingTranscriptionSidJson(
  '6a09cdc3-8948-47f0-aa62-74ac943d6c58',
  { account_sid: 'account_sid' },
);
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `TexmlCallAnsweredWebhook` | TeXML Call Answered. Webhook sent when a TeXML call is answered |
| `TexmlCallCompletedWebhook` | TeXML Call Completed. Webhook sent when a TeXML call is completed |
| `TexmlCallInitiatedWebhook` | TeXML Call Initiated. Webhook sent when a TeXML call is initiated |
| `TexmlCallRingingWebhook` | TeXML Call Ringing. Webhook sent when a TeXML call is ringing |
| `TexmlCallAmdWebhook` | TeXML Call AMD. Webhook sent when Answering Machine Detection (AMD) completes during a TeXML call |
| `TexmlCallDtmfWebhook` | TeXML Call DTMF. Webhook sent when a DTMF digit is received during a TeXML call |
| `TexmlGatherWebhook` | TeXML Gather. Webhook sent when a Gather command completes (sent to the action URL) |
| `TexmlHttpRequestWebhook` | TeXML HTTP Request. Webhook sent as response to an HTTP Request instruction |
| `TexmlAiGatherWebhook` | TeXML AI Gather. Webhook sent when AI Gather completes with transcription results |
| `TexmlConferenceJoinWebhook` | TeXML Conference Join. Webhook sent when a participant joins a TeXML conference |
| `TexmlConferenceLeaveWebhook` | TeXML Conference Leave. Webhook sent when a participant leaves a TeXML conference |
| `TexmlConferenceSpeakerWebhook` | TeXML Conference Speaker. Webhook sent when a participant starts or stops speaking in a TeXML conference |
| `TexmlConferenceEndWebhook` | TeXML Conference End. Webhook sent when a TeXML conference ends |
| `TexmlConferenceStartWebhook` | TeXML Conference Start. Webhook sent when a TeXML conference starts |
| `TexmlQueueWebhook` | TeXML Queue. Webhook sent for queue status events (triggered by Enqueue command waitUrl) |
| `TexmlRecordingCompletedWebhook` | TeXML Recording Completed. Webhook sent when a recording is completed during a TeXML call (triggered by recordingStatusCallbackEvent) |
| `TexmlRecordingInProgressWebhook` | TeXML Recording In-Progress. Webhook sent when a recording starts during a TeXML call (triggered by recordingStatusCallbackEvent) |
| `TexmlSiprecWebhook` | TeXML SIPREC. Webhook sent for SIPREC session status updates |
| `TexmlStreamWebhook` | TeXML Stream. Webhook sent for media streaming status updates |
| `TexmlTranscriptionWebhook` | TeXML Transcription. Webhook sent when a recording transcription is completed |
