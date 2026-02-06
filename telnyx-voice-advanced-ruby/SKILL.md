---
name: telnyx-voice-advanced-ruby
description: >-
  Advanced call control features including DTMF sending, SIPREC recording, noise
  suppression, client state, and supervisor controls. This skill provides Ruby
  SDK examples.
metadata:
  author: telnyx
  product: voice-advanced
  language: ruby
---

# Telnyx Voice Advanced - Ruby

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

## Update client state

Updates client state

`PUT /calls/{call_control_id}/actions/client_state_update` — Required: `client_state`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.update_client_state("call_control_id", client_state: "aGF2ZSBhIG5pY2UgZGF5ID1d")

puts(response)
```

## Send DTMF

Sends DTMF tones from this leg.

`POST /calls/{call_control_id}/actions/send_dtmf` — Required: `digits`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.send_dtmf("call_control_id", digits: "1www2WABCDw9")

puts(response)
```

## SIPREC start

Start siprec session to configured in SIPREC connector SRS.

`POST /calls/{call_control_id}/actions/siprec_start`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.start_siprec("call_control_id")

puts(response)
```

## SIPREC stop

Stop SIPREC session.

`POST /calls/{call_control_id}/actions/siprec_stop`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.stop_siprec("call_control_id")

puts(response)
```

## Noise Suppression Start (BETA)

`POST /calls/{call_control_id}/actions/suppression_start`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.start_noise_suppression("call_control_id")

puts(response)
```

## Noise Suppression Stop (BETA)

`POST /calls/{call_control_id}/actions/suppression_stop`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.stop_noise_suppression("call_control_id")

puts(response)
```

## Switch supervisor role

Switch the supervisor role for a bridged call.

`POST /calls/{call_control_id}/actions/switch_supervisor_role` — Required: `role`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.calls.actions.switch_supervisor_role("call_control_id", role: :barge)

puts(response)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `callSiprecStarted` | Call Siprec Started |
| `callSiprecStopped` | Call Siprec Stopped |
| `callSiprecFailed` | Call Siprec Failed |
