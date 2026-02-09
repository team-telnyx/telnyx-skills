---
name: telnyx-voice-conferencing-java
description: >-
  Create and manage conference calls, queues, and multi-party sessions. Use when
  building call centers or conferencing applications. This skill provides Java
  SDK examples.
metadata:
  author: telnyx
  product: voice-conferencing
  language: java
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Conferencing - Java

## Installation

```text
// See https://github.com/team-telnyx/telnyx-java for Maven/Gradle setup
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## Enqueue call

Put the call in a queue.

`POST /calls/{call_control_id}/actions/enqueue` — Required: `queue_name`

```java
import com.telnyx.sdk.models.calls.actions.ActionEnqueueParams;
import com.telnyx.sdk.models.calls.actions.ActionEnqueueResponse;

ActionEnqueueParams params = ActionEnqueueParams.builder()
    .callControlId("call_control_id")
    .queueName("support")
    .build();
ActionEnqueueResponse response = client.calls().actions().enqueue(params);
```

## Remove call from a queue

Removes the call from a queue.

`POST /calls/{call_control_id}/actions/leave_queue`

```java
import com.telnyx.sdk.models.calls.actions.ActionLeaveQueueParams;
import com.telnyx.sdk.models.calls.actions.ActionLeaveQueueResponse;

ActionLeaveQueueResponse response = client.calls().actions().leaveQueue("call_control_id");
```

## List conferences

Lists conferences.

`GET /conferences`

```java
import com.telnyx.sdk.models.conferences.ConferenceListPage;
import com.telnyx.sdk.models.conferences.ConferenceListParams;

ConferenceListPage page = client.conferences().list();
```

## Create conference

Create a conference from an existing call leg using a `call_control_id` and a conference name.

`POST /conferences` — Required: `call_control_id`, `name`

```java
import com.telnyx.sdk.models.conferences.ConferenceCreateParams;
import com.telnyx.sdk.models.conferences.ConferenceCreateResponse;

ConferenceCreateParams params = ConferenceCreateParams.builder()
    .callControlId("v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg")
    .name("Business")
    .build();
ConferenceCreateResponse conference = client.conferences().create(params);
```

## Retrieve a conference

Retrieve an existing conference

`GET /conferences/{id}`

```java
import com.telnyx.sdk.models.conferences.ConferenceRetrieveParams;
import com.telnyx.sdk.models.conferences.ConferenceRetrieveResponse;

ConferenceRetrieveResponse conference = client.conferences().retrieve("id");
```

## Hold conference participants

Hold a list of participants in a conference call

`POST /conferences/{id}/actions/hold`

```java
import com.telnyx.sdk.models.conferences.actions.ActionHoldParams;
import com.telnyx.sdk.models.conferences.actions.ActionHoldResponse;

ActionHoldResponse response = client.conferences().actions().hold("id");
```

## Join a conference

Join an existing call leg to a conference.

`POST /conferences/{id}/actions/join` — Required: `call_control_id`

```java
import com.telnyx.sdk.models.conferences.actions.ActionJoinParams;
import com.telnyx.sdk.models.conferences.actions.ActionJoinResponse;

ActionJoinParams params = ActionJoinParams.builder()
    .id("id")
    .callControlId("v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg")
    .build();
ActionJoinResponse response = client.conferences().actions().join(params);
```

## Leave a conference

Removes a call leg from a conference and moves it back to parked state.

`POST /conferences/{id}/actions/leave` — Required: `call_control_id`

```java
import com.telnyx.sdk.models.conferences.actions.ActionLeaveParams;
import com.telnyx.sdk.models.conferences.actions.ActionLeaveResponse;

ActionLeaveParams params = ActionLeaveParams.builder()
    .id("id")
    .callControlId("c46e06d7-b78f-4b13-96b6-c576af9640ff")
    .build();
ActionLeaveResponse response = client.conferences().actions().leave(params);
```

## Mute conference participants

Mute a list of participants in a conference call

`POST /conferences/{id}/actions/mute`

```java
import com.telnyx.sdk.models.conferences.actions.ActionMuteParams;
import com.telnyx.sdk.models.conferences.actions.ActionMuteResponse;

ActionMuteResponse response = client.conferences().actions().mute("id");
```

## Play audio to conference participants

Play audio to all or some participants on a conference call.

`POST /conferences/{id}/actions/play`

```java
import com.telnyx.sdk.models.conferences.actions.ActionPlayParams;
import com.telnyx.sdk.models.conferences.actions.ActionPlayResponse;

ActionPlayResponse response = client.conferences().actions().play("id");
```

## Conference recording pause

Pause conference recording.

`POST /conferences/{id}/actions/record_pause`

```java
import com.telnyx.sdk.models.conferences.actions.ActionRecordPauseParams;
import com.telnyx.sdk.models.conferences.actions.ActionRecordPauseResponse;

ActionRecordPauseResponse response = client.conferences().actions().recordPause("id");
```

## Conference recording resume

Resume conference recording.

`POST /conferences/{id}/actions/record_resume`

```java
import com.telnyx.sdk.models.conferences.actions.ActionRecordResumeParams;
import com.telnyx.sdk.models.conferences.actions.ActionRecordResumeResponse;

ActionRecordResumeResponse response = client.conferences().actions().recordResume("id");
```

## Conference recording start

Start recording the conference.

`POST /conferences/{id}/actions/record_start` — Required: `format`

```java
import com.telnyx.sdk.models.conferences.actions.ActionRecordStartParams;
import com.telnyx.sdk.models.conferences.actions.ActionRecordStartResponse;

ActionRecordStartParams params = ActionRecordStartParams.builder()
    .id("id")
    .format(ActionRecordStartParams.Format.WAV)
    .build();
ActionRecordStartResponse response = client.conferences().actions().recordStart(params);
```

## Conference recording stop

Stop recording the conference.

`POST /conferences/{id}/actions/record_stop`

```java
import com.telnyx.sdk.models.conferences.actions.ActionRecordStopParams;
import com.telnyx.sdk.models.conferences.actions.ActionRecordStopResponse;

ActionRecordStopResponse response = client.conferences().actions().recordStop("id");
```

## Speak text to conference participants

Convert text to speech and play it to all or some participants.

`POST /conferences/{id}/actions/speak` — Required: `payload`, `voice`

```java
import com.telnyx.sdk.models.conferences.actions.ActionSpeakParams;
import com.telnyx.sdk.models.conferences.actions.ActionSpeakResponse;

ActionSpeakParams params = ActionSpeakParams.builder()
    .id("id")
    .payload("Say this to participants")
    .voice("female")
    .build();
ActionSpeakResponse response = client.conferences().actions().speak(params);
```

## Stop audio being played on the conference

Stop audio being played to all or some participants on a conference call.

`POST /conferences/{id}/actions/stop`

```java
import com.telnyx.sdk.models.conferences.actions.ActionStopParams;
import com.telnyx.sdk.models.conferences.actions.ActionStopResponse;

ActionStopResponse response = client.conferences().actions().stop("id");
```

## Unhold conference participants

Unhold a list of participants in a conference call

`POST /conferences/{id}/actions/unhold` — Required: `call_control_ids`

```java
import com.telnyx.sdk.models.conferences.actions.ActionUnholdParams;
import com.telnyx.sdk.models.conferences.actions.ActionUnholdResponse;

ActionUnholdParams params = ActionUnholdParams.builder()
    .id("id")
    .addCallControlId("v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg")
    .build();
ActionUnholdResponse response = client.conferences().actions().unhold(params);
```

## Unmute conference participants

Unmute a list of participants in a conference call

`POST /conferences/{id}/actions/unmute`

```java
import com.telnyx.sdk.models.conferences.actions.ActionUnmuteParams;
import com.telnyx.sdk.models.conferences.actions.ActionUnmuteResponse;

ActionUnmuteResponse response = client.conferences().actions().unmute("id");
```

## Update conference participant

Update conference participant supervisor_role

`POST /conferences/{id}/actions/update` — Required: `call_control_id`, `supervisor_role`

```java
import com.telnyx.sdk.models.conferences.actions.ActionUpdateParams;
import com.telnyx.sdk.models.conferences.actions.ActionUpdateResponse;
import com.telnyx.sdk.models.conferences.actions.UpdateConference;

ActionUpdateParams params = ActionUpdateParams.builder()
    .id("id")
    .updateConference(UpdateConference.builder()
        .callControlId("v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg")
        .supervisorRole(UpdateConference.SupervisorRole.WHISPER)
        .build())
    .build();
ActionUpdateResponse action = client.conferences().actions().update(params);
```

## List conference participants

Lists conference participants

`GET /conferences/{conference_id}/participants`

```java
import com.telnyx.sdk.models.conferences.ConferenceListParticipantsPage;
import com.telnyx.sdk.models.conferences.ConferenceListParticipantsParams;

ConferenceListParticipantsPage page = client.conferences().listParticipants("conference_id");
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callEnqueued` | Call Enqueued |
| `callLeftQueue` | Call Left Queue |
| `conferenceCreated` | Conference Created |
| `conferenceEnded` | Conference Ended |
| `conferenceFloorChanged` | Conference Floor Changed |
| `conferenceParticipantJoined` | Conference Participant Joined |
| `conferenceParticipantLeft` | Conference Participant Left |
| `conferenceParticipantPlaybackEnded` | Conference Participant Playback Ended |
| `conferenceParticipantPlaybackStarted` | Conference Participant Playback Started |
| `conferenceParticipantSpeakEnded` | Conference Participant Speak Ended |
| `conferenceParticipantSpeakStarted` | Conference Participant Speak Started |
| `conferencePlaybackEnded` | Conference Playback Ended |
| `conferencePlaybackStarted` | Conference Playback Started |
| `conferenceRecordingSaved` | Conference Recording Saved |
| `conferenceSpeakEnded` | Conference Speak Ended |
| `conferenceSpeakStarted` | Conference Speak Started |
