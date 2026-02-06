---
name: telnyx-voice-python
description: >-
  Make and receive calls, transfer, bridge, and manage call lifecycle with Call
  Control. Includes application management and call events. This skill provides
  Python SDK examples.
metadata:
  author: telnyx
  product: voice
  language: python
---

# Telnyx Voice - Python

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

## Answer call

Answer an incoming call.

`POST /calls/{call_control_id}/actions/answer`

```python
response = client.calls.actions.answer(
    call_control_id="call_control_id",
)
print(response.data)
```

## Bridge calls

Bridge two call control calls.

`POST /calls/{call_control_id}/actions/bridge` — Required: `call_control_id`

```python
response = client.calls.actions.bridge(
    call_control_id_to_bridge="call_control_id",
    call_control_id_to_bridge_with="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
)
print(response.data)
```

## Dial

Dial a number or SIP URI from a given connection.

`POST /calls` — Required: `connection_id`, `to`, `from`

```python
response = client.calls.dial(
    connection_id="7267xxxxxxxxxxxxxx",
    from_="+18005550101",
    to="+18005550100 or sip:username@sip.telnyx.com",
)
print(response.data)
```

## Hangup call

Hang up the call.

`POST /calls/{call_control_id}/actions/hangup`

```python
response = client.calls.actions.hangup(
    call_control_id="call_control_id",
)
print(response.data)
```

## Transfer call

Transfer a call to a new destination.

`POST /calls/{call_control_id}/actions/transfer` — Required: `to`

```python
response = client.calls.actions.transfer(
    call_control_id="call_control_id",
    to="+18005550100 or sip:username@sip.telnyx.com",
)
print(response.data)
```

## List all active calls for given connection

Lists all active calls for given connection.

`GET /connections/{connection_id}/active_calls`

```python
page = client.connections.list_active_calls(
    connection_id="1293384261075731461",
)
page = page.data[0]
print(page.call_control_id)
```

## List call control applications

Return a list of call control applications.

`GET /call_control_applications`

```python
page = client.call_control_applications.list()
page = page.data[0]
print(page.id)
```

## Create a call control application

Create a call control application.

`POST /call_control_applications` — Required: `application_name`, `webhook_event_url`

```python
call_control_application = client.call_control_applications.create(
    application_name="call-router",
    webhook_event_url="https://example.com",
)
print(call_control_application.data)
```

## Retrieve a call control application

Retrieves the details of an existing call control application.

`GET /call_control_applications/{id}`

```python
call_control_application = client.call_control_applications.retrieve(
    "id",
)
print(call_control_application.data)
```

## Update a call control application

Updates settings of an existing call control application.

`PATCH /call_control_applications/{id}` — Required: `application_name`, `webhook_event_url`

```python
call_control_application = client.call_control_applications.update(
    id="id",
    application_name="call-router",
    webhook_event_url="https://example.com",
)
print(call_control_application.data)
```

## Delete a call control application

Deletes a call control application.

`DELETE /call_control_applications/{id}`

```python
call_control_application = client.call_control_applications.delete(
    "id",
)
print(call_control_application.data)
```

## List call events

Filters call events by given filter parameters.

`GET /call_events`

```python
page = client.call_events.list()
page = page.data[0]
print(page.call_leg_id)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callAnswered` | Call Answered |
| `callStreamingStarted` | Call Streaming Started |
| `callStreamingStopped` | Call Streaming Stopped |
| `callStreamingFailed` | Call Streaming Failed |
| `callBridged` | Call Bridged |
| `callInitiated` | Call Initiated |
| `callHangup` | Call Hangup |
| `callRecordingSaved` | Call Recording Saved |
| `callMachineDetectionEnded` | Call Machine Detection Ended |
| `callMachineGreetingEnded` | Call Machine Greeting Ended |
| `callMachinePremiumDetectionEnded` | Call Machine Premium Detection Ended |
| `callMachinePremiumGreetingEnded` | Call Machine Premium Greeting Ended |
