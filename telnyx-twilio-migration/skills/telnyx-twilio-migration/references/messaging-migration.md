# Messaging Migration: Twilio to Telnyx

Migrate from Twilio Programmable Messaging to the Telnyx Messaging API.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Sending Messages](#sending-messages)
- [Receiving Messages (Webhooks)](#receiving-messages-webhooks)
- [MMS and Media](#mms-and-media)
- [Messaging Profiles](#messaging-profiles)
- [10DLC Registration](#10dlc-registration)
- [Short Codes and Toll-Free](#short-codes-and-toll-free)
- [Webhook Payload Mapping](#webhook-payload-mapping)
- [Error Code Mapping](#error-code-mapping)

## Overview

Telnyx Messaging is a new SDK integration, not a drop-in replacement. The core changes:

1. Different SDK and client initialization
2. Different parameter names (`body` → `text`, flat params → structured objects)
3. Webhook payloads use Telnyx's event structure (nested under `data`)
4. Webhook signatures use Ed25519 instead of HMAC-SHA1
5. Numbers must be assigned to a **Messaging Profile** (analogous to Twilio's Messaging Service)

## Setup

### Install the Telnyx SDK

```bash
# Python
pip install telnyx

# Node.js
npm install telnyx

# Ruby
gem install telnyx

# Go
go get github.com/telnyx/telnyx-go
```

### Configure Authentication

```python
# Python
import telnyx
telnyx.api_key = "YOUR_TELNYX_API_KEY"
```

```javascript
// Node.js
const Telnyx = require('telnyx');
const telnyx = Telnyx('YOUR_TELNYX_API_KEY');
```

```bash
# curl
export TELNYX_API_KEY="YOUR_API_KEY"
```

## Sending Messages

### SMS

```python
# Twilio
from twilio.rest import Client
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+15559876543",
    from_="+15551234567",
    body="Hello from Twilio"
)
print(message.sid)

# Telnyx
import telnyx
telnyx.api_key = "YOUR_API_KEY"
message = telnyx.Message.create(
    to="+15559876543",
    from_="+15551234567",
    text="Hello from Telnyx"
)
print(message.id)
```

```javascript
// Twilio
const client = require('twilio')(accountSid, authToken);
const message = await client.messages.create({
  to: '+15559876543',
  from: '+15551234567',
  body: 'Hello from Twilio'
});

// Telnyx
const telnyx = require('telnyx')('YOUR_API_KEY');
const message = await telnyx.messages.create({
  to: '+15559876543',
  from: '+15551234567',
  text: 'Hello from Telnyx'
});
```

```bash
# Twilio
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/$SID/Messages.json" \
  -u "$SID:$AUTH_TOKEN" \
  -d "To=+15559876543" -d "From=+15551234567" -d "Body=Hello"

# Telnyx
curl -X POST "https://api.telnyx.com/v2/messages" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"to":"+15559876543","from":"+15551234567","text":"Hello"}'
```

### Key Parameter Differences

| Twilio | Telnyx | Notes |
|---|---|---|
| `body` | `text` | Message content |
| `from_` / `From` | `from` | Sender number (E.164) |
| `to` / `To` | `to` | Recipient number (E.164) |
| `StatusCallback` | Configured on Messaging Profile | Per-message callbacks not supported; set on the profile |
| `MessagingServiceSid` | `messaging_profile_id` | Message routing profile |
| `MediaUrl` | `media_urls` | Array of media URLs (for MMS) |

## Receiving Messages (Webhooks)

Configure your webhook URL on a **Messaging Profile** in the Mission Control Portal (not per-number like Twilio).

### Webhook Payload Comparison

**Twilio incoming message webhook:**
```json
{
  "MessageSid": "SM...",
  "AccountSid": "AC...",
  "From": "+15559876543",
  "To": "+15551234567",
  "Body": "Hello",
  "NumMedia": "0"
}
```

**Telnyx incoming message webhook:**
```json
{
  "data": {
    "event_type": "message.received",
    "id": "evt_...",
    "occurred_at": "2026-01-15T12:00:00Z",
    "payload": {
      "id": "msg_...",
      "from": {
        "phone_number": "+15559876543",
        "carrier": "T-Mobile"
      },
      "to": [{
        "phone_number": "+15551234567"
      }],
      "text": "Hello",
      "media": [],
      "direction": "inbound",
      "type": "SMS"
    }
  }
}
```

### Webhook Handler Example

```python
# Twilio
@app.route('/sms', methods=['POST'])
def handle_sms():
    from_number = request.form['From']
    body = request.form['Body']
    # Process message...

# Telnyx
@app.route('/sms', methods=['POST'])
def handle_sms():
    event = request.json['data']
    payload = event['payload']
    from_number = payload['from']['phone_number']
    body = payload['text']
    # Process message...
```

```javascript
// Twilio
app.post('/sms', (req, res) => {
  const from = req.body.From;
  const body = req.body.Body;
  // Process message...
});

// Telnyx
app.post('/sms', (req, res) => {
  const { payload } = req.body.data;
  const from = payload.from.phone_number;
  const body = payload.text;
  // Process message...
  res.sendStatus(200);
});
```

## MMS and Media

```python
# Twilio MMS
message = client.messages.create(
    to="+15559876543",
    from_="+15551234567",
    body="Check this out",
    media_url=["https://example.com/image.jpg"]
)

# Telnyx MMS
message = telnyx.Message.create(
    to="+15559876543",
    from_="+15551234567",
    text="Check this out",
    media_urls=["https://example.com/image.jpg"]
)
```

Telnyx MMS supports images (JPEG, PNG, GIF), audio, video, and vCard. Maximum media size: 1 MB for most carriers.

## Messaging Profiles

Telnyx uses **Messaging Profiles** to configure message routing, webhooks, and features. This is analogous to Twilio's Messaging Service.

Create a profile in the portal or via API:

```bash
curl -X POST https://api.telnyx.com/v2/messaging_profiles \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My App",
    "webhook_url": "https://example.com/webhooks/messaging",
    "webhook_failover_url": "https://example.com/webhooks/messaging-backup"
  }'
```

Then assign numbers to the profile. All messages to/from those numbers use the profile's webhook configuration.

## 10DLC Registration

Both Twilio and Telnyx use The Campaign Registry (TCR) for 10DLC compliance. The process is the same:

1. **Register your brand** (business identity)
2. **Create a campaign** (use case: marketing, 2FA, customer care, etc.)
3. **Assign numbers** to the campaign

Telnyx provides 10DLC registration via the Mission Control Portal (**Messaging** → **10DLC**) or via API.

> **Enhanced coverage**: Install a language plugin and reference the `telnyx-10dlc-*` skill for complete API examples.

## Short Codes and Toll-Free

| Feature | Twilio | Telnyx |
|---|---|---|
| Dedicated short codes | Supported | Supported |
| Shared short codes | Deprecated | Not available |
| Toll-free SMS | Supported | Supported |
| Toll-free verification | Required | Required (via portal or API) |
| Alphanumeric sender ID | Supported (select countries) | Supported (select countries) |

## Webhook Payload Mapping

| Twilio Field | Telnyx Field | Location in Telnyx Payload |
|---|---|---|
| `MessageSid` | `id` | `data.payload.id` |
| `From` | `from.phone_number` | `data.payload.from.phone_number` |
| `To` | `to[0].phone_number` | `data.payload.to[0].phone_number` |
| `Body` | `text` | `data.payload.text` |
| `NumMedia` | `media.length` | `data.payload.media` (array) |
| `MediaUrl0` | `media[0].url` | `data.payload.media[0].url` |
| `MessageStatus` | `event_type` | `data.event_type` (e.g., `message.sent`, `message.delivered`) |
| `ErrorCode` | `errors` | `data.payload.errors` (array) |

## Error Code Mapping

| Scenario | Twilio Error | Telnyx Error |
|---|---|---|
| Invalid destination | 21211 | `40300` — Invalid destination |
| Unsubscribed recipient | 21610 | `40008` — Number opted out |
| Rate limit exceeded | 14107 | `40009` — Rate limit exceeded |
| Carrier rejected | 30007 | `40300` — Carrier rejected |
| Number not provisioned | 21606 | `40004` — Number not associated with messaging profile |

Telnyx error details are included in webhook delivery-status events and in API error responses.
