---
name: telnyx-voice-advanced-javascript
description: >-
  Advanced call control features including DTMF sending, SIPREC recording, noise
  suppression, client state, and supervisor controls. This skill provides
  JavaScript SDK examples.
metadata:
  author: telnyx
  product: voice-advanced
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Advanced - JavaScript

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

## Update client state

Updates client state

`PUT /calls/{call_control_id}/actions/client_state_update` — Required: `client_state`

```javascript
const response = await client.calls.actions.updateClientState('call_control_id', {
  client_state: 'aGF2ZSBhIG5pY2UgZGF5ID1d',
});

console.log(response.data);
```

## SIP Refer a call

Initiate a SIP Refer on a Call Control call.

`POST /calls/{call_control_id}/actions/refer` — Required: `sip_address`

```javascript
const response = await client.calls.actions.refer('call_control_id', {
  sip_address: 'sip:username@sip.non-telnyx-address.com',
});

console.log(response.data);
```

## Send DTMF

Sends DTMF tones from this leg.

`POST /calls/{call_control_id}/actions/send_dtmf` — Required: `digits`

```javascript
const response = await client.calls.actions.sendDtmf('call_control_id', { digits: '1www2WABCDw9' });

console.log(response.data);
```

## SIPREC start

Start siprec session to configured in SIPREC connector SRS.

`POST /calls/{call_control_id}/actions/siprec_start`

```javascript
const response = await client.calls.actions.startSiprec('call_control_id');

console.log(response.data);
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

```javascript
const response = await client.calls.actions.stopSiprec('call_control_id');

console.log(response.data);
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

```javascript
const response = await client.calls.actions.startNoiseSuppression('call_control_id');

console.log(response.data);
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

```javascript
const response = await client.calls.actions.stopNoiseSuppression('call_control_id');

console.log(response.data);
```

## Switch supervisor role

Switch the supervisor role for a bridged call.

`POST /calls/{call_control_id}/actions/switch_supervisor_role` — Required: `role`

```javascript
const response = await client.calls.actions.switchSupervisorRole('call_control_id', {
  role: 'barge',
});

console.log(response.data);
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callReferStarted` | Call Refer Started |
| `callReferCompleted` | Call Refer Completed |
| `callReferFailed` | Call Refer Failed |
| `callSiprecStarted` | Call Siprec Started |
| `callSiprecStopped` | Call Siprec Stopped |
| `callSiprecFailed` | Call Siprec Failed |
