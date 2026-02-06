---
name: telnyx-voice-ruby
description: >-
  Make and receive calls, transfer, bridge, and manage call lifecycle with Call
  Control. Includes application management and call events. This skill provides
  Ruby SDK examples.
metadata:
  author: telnyx
  product: voice
  language: ruby
---

# Telnyx Voice - Ruby

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

## Answer call

Answer an incoming call.

`POST /calls/{call_control_id}/actions/answer`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.answer("call_control_id")

puts(response)
```

## Bridge calls

Bridge two call control calls.

`POST /calls/{call_control_id}/actions/bridge` — Required: `call_control_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.bridge(
  "call_control_id",
  call_control_id_to_bridge_with: "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"
)

puts(response)
```

## Dial

Dial a number or SIP URI from a given connection.

`POST /calls` — Required: `connection_id`, `to`, `from`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.dial(
  connection_id: "7267xxxxxxxxxxxxxx",
  from: "+18005550101",
  to: "+18005550100 or sip:username@sip.telnyx.com"
)

puts(response)
```

## Hangup call

Hang up the call.

`POST /calls/{call_control_id}/actions/hangup`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.hangup("call_control_id")

puts(response)
```

## Transfer call

Transfer a call to a new destination.

`POST /calls/{call_control_id}/actions/transfer` — Required: `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.transfer("call_control_id", to: "+18005550100 or sip:username@sip.telnyx.com")

puts(response)
```

## List all active calls for given connection

Lists all active calls for given connection.

`GET /connections/{connection_id}/active_calls`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.connections.list_active_calls("1293384261075731461")

puts(page)
```

## List call control applications

Return a list of call control applications.

`GET /call_control_applications`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.call_control_applications.list

puts(page)
```

## Create a call control application

Create a call control application.

`POST /call_control_applications` — Required: `application_name`, `webhook_event_url`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

call_control_application = telnyx.call_control_applications.create(
  application_name: "call-router",
  webhook_event_url: "https://example.com"
)

puts(call_control_application)
```

## Retrieve a call control application

Retrieves the details of an existing call control application.

`GET /call_control_applications/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

call_control_application = telnyx.call_control_applications.retrieve("id")

puts(call_control_application)
```

## Update a call control application

Updates settings of an existing call control application.

`PATCH /call_control_applications/{id}` — Required: `application_name`, `webhook_event_url`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

call_control_application = telnyx.call_control_applications.update(
  "id",
  application_name: "call-router",
  webhook_event_url: "https://example.com"
)

puts(call_control_application)
```

## Delete a call control application

Deletes a call control application.

`DELETE /call_control_applications/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

call_control_application = telnyx.call_control_applications.delete("id")

puts(call_control_application)
```

## List call events

Filters call events by given filter parameters.

`GET /call_events`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.call_events.list

puts(page)
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
