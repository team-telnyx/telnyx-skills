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
go get github.com/team-telnyx/telnyx-go
```

### Configure Authentication

```python
# Python
from telnyx import Telnyx
client = Telnyx(api_key="YOUR_TELNYX_API_KEY")
```

```javascript
// Node.js
const Telnyx = require('telnyx');
const client = new Telnyx({ apiKey: 'YOUR_TELNYX_API_KEY' });
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
from telnyx import Telnyx
client = Telnyx(api_key="YOUR_API_KEY")
message = client.messages.send(
    to="+15559876543",
    from_="+15551234567",
    text="Hello from Telnyx",
    messaging_profile_id="YOUR_MESSAGING_PROFILE_ID"
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
const Telnyx = require('telnyx');
const client = new Telnyx({ apiKey: 'YOUR_API_KEY' });
const message = await client.messages.send({
  to: '+15559876543',
  from: '+15551234567',
  text: 'Hello from Telnyx',
  messaging_profile_id: 'YOUR_MESSAGING_PROFILE_ID'
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
  -d '{"to":"+15559876543","from":"+15551234567","text":"Hello","messaging_profile_id":"YOUR_MESSAGING_PROFILE_ID"}'
```

```go
// Go
// Twilio
import "github.com/twilio/twilio-go"
import twilioApi "github.com/twilio/twilio-go/rest/api/v2010"

client := twilio.NewRestClient()
params := &twilioApi.CreateMessageParams{}
params.SetTo("+15559876543")
params.SetFrom("+15551234567")
params.SetBody("Hello from Twilio")
resp, _ := client.Api.CreateMessage(params)

// Telnyx
import (
	"context"
	"os"
	"github.com/team-telnyx/telnyx-go"
	"github.com/team-telnyx/telnyx-go/option"
)
client := telnyx.NewClient(option.WithAPIKey(os.Getenv("TELNYX_API_KEY")))
message, _ := client.Messages.Send(context.TODO(), telnyx.MessageSendParams{
	To:                  telnyx.String("+15559876543"),
	From:                telnyx.String("+15551234567"),
	Text:                telnyx.String("Hello from Telnyx"),
	MessagingProfileID:  telnyx.String("YOUR_MESSAGING_PROFILE_ID"),
})
```

```ruby
# Twilio
require 'twilio-ruby'
client = Twilio::REST::Client.new(account_sid, auth_token)
message = client.messages.create(
  to: '+15559876543', from: '+15551234567', body: 'Hello from Twilio'
)

# Telnyx
require 'telnyx'
client = Telnyx::Client.new(api_key: 'YOUR_API_KEY')
message = client.messages.send_(
  to: '+15559876543', from: '+15551234567', text: 'Hello from Telnyx',
  messaging_profile_id: 'YOUR_MESSAGING_PROFILE_ID'
)
```

```java
// Twilio
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

Message message = Message.creator(
    new PhoneNumber("+15559876543"),
    new PhoneNumber("+15551234567"),
    "Hello from Twilio"
).create();

// Telnyx — use REST API with OkHttp or HttpClient
// POST https://api.telnyx.com/v2/messages
// Body: {"to":"+15559876543","from":"+15551234567","text":"Hello from Telnyx","messaging_profile_id":"YOUR_PROFILE_ID"}
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
message = client.messages.send(
    to="+15559876543",
    from_="+15551234567",
    text="Check this out",
    media_urls=["https://example.com/image.jpg"],
    messaging_profile_id="YOUR_MESSAGING_PROFILE_ID"
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

## Messaging Service → Messaging Profile Migration

If you're using Twilio Messaging Services, here's how to map them to Telnyx Messaging Profiles:

| Twilio Messaging Service Feature | Telnyx Messaging Profile Feature |
|---|---|
| Friendly name | `name` |
| Webhook URL (StatusCallback) | `webhook_url` |
| Fallback URL | `webhook_failover_url` |
| Sticky Sender | Not needed — Telnyx routes optimally per-message |
| Validity Period | `v1_secret` (not a direct mapping — configure per-message) |
| Smart Encoding | Automatic |
| MMS Converter | Automatic |
| Area Code Geomatch | Supported via number pool configuration |
| Copilot Features | Configure on the Messaging Profile |

**Steps to migrate:**

1. Create a Messaging Profile for each Messaging Service:
   ```bash
   curl -X POST https://api.telnyx.com/v2/messaging_profiles \
     -H "Authorization: Bearer $TELNYX_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "My Messaging Service Replacement",
       "webhook_url": "https://example.com/webhooks/messaging",
       "webhook_failover_url": "https://example.com/webhooks/messaging-backup",
       "number_pool_settings": {
         "geomatch": true,
         "sticky_sender": true
       }
     }'
   ```
2. Assign phone numbers to the profile
3. Update your code to use `messaging_profile_id` instead of `MessagingServiceSid`

## Alphanumeric Sender ID & Toll-Free Verification

### Alphanumeric Sender ID

Both Twilio and Telnyx support alphanumeric sender IDs in supported countries. On Telnyx:

- Register your sender ID via the Mission Control Portal or API
- Sender IDs must be 3-11 characters, alphanumeric
- Country-specific registration may be required (e.g., UK, Germany)
- Not available in the US or Canada (carrier restriction, not Telnyx-specific)

### Toll-Free Verification

US toll-free numbers require verification for SMS/MMS. Both carriers use the same TCR process:

1. Submit your use case (marketing, 2FA, customer care, etc.)
2. Provide sample messages
3. Verification typically takes 1-5 business days
4. Unverified toll-free numbers have reduced throughput

On Telnyx, manage toll-free verification through the Mission Control Portal under **Messaging** → **Toll-Free Verification**.

## 10DLC Registration

Both Twilio and Telnyx use The Campaign Registry (TCR) for 10DLC compliance. The process is the same:

1. **Register your brand** (business identity)
2. **Create a campaign** (use case: marketing, 2FA, customer care, etc.)
3. **Assign numbers** to the campaign

Telnyx provides 10DLC registration via the Mission Control Portal (**Messaging** → **10DLC**) or via API.

> **Complete 10DLC API examples** with all parameters are in the sdk-reference files: `sdk-reference/{language}/10dlc.md`.

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
