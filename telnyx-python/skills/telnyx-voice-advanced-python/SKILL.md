---
name: telnyx-voice-advanced-python
description: >-
  Advanced call control features including DTMF sending, SIPREC recording, noise
  suppression, client state, and supervisor controls. This skill provides Python
  SDK examples.
metadata:
  author: telnyx
  product: voice-advanced
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Voice Advanced - Python

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

## Update client state

Updates client state

`PUT /calls/{call_control_id}/actions/client_state_update` — Required: `client_state`

```python
response = client.calls.actions.update_client_state(
    call_control_id="call_control_id",
    client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
)
print(response.data)
```

## SIP Refer a call

Initiate a SIP Refer on a Call Control call.

`POST /calls/{call_control_id}/actions/refer` — Required: `sip_address`

```python
response = client.calls.actions.refer(
    call_control_id="call_control_id",
    sip_address="sip:username@sip.non-telnyx-address.com",
)
print(response.data)
```

## Send DTMF

Sends DTMF tones from this leg.

`POST /calls/{call_control_id}/actions/send_dtmf` — Required: `digits`

```python
response = client.calls.actions.send_dtmf(
    call_control_id="call_control_id",
    digits="1www2WABCDw9",
)
print(response.data)
```

## SIPREC start

Start siprec session to configured in SIPREC connector SRS.

`POST /calls/{call_control_id}/actions/siprec_start`

```python
response = client.calls.actions.start_siprec(
    call_control_id="call_control_id",
)
print(response.data)
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

```python
response = client.calls.actions.stop_siprec(
    call_control_id="call_control_id",
)
print(response.data)
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

```python
response = client.calls.actions.start_noise_suppression(
    call_control_id="call_control_id",
)
print(response.data)
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

```python
response = client.calls.actions.stop_noise_suppression(
    call_control_id="call_control_id",
)
print(response.data)
```

## Switch supervisor role

Switch the supervisor role for a bridged call.

`POST /calls/{call_control_id}/actions/switch_supervisor_role` — Required: `role`

```python
response = client.calls.actions.switch_supervisor_role(
    call_control_id="call_control_id",
    role="barge",
)
print(response.data)
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
