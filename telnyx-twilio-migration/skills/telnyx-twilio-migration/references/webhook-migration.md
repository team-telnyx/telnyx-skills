# Webhook Migration: Twilio to Telnyx

Comprehensive guide for migrating webhook handlers from Twilio's flat form-encoded payloads to Telnyx's nested JSON event structure.

## Payload Structure

**Twilio** sends flat form-encoded key-value pairs (`application/x-www-form-urlencoded`):
```
MessageSid=SM123&From=%2B15551234567&To=%2B15559876543&Body=Hello
```

**Telnyx** sends nested JSON (`application/json`):
```json
{
  "data": {
    "event_type": "message.received",
    "id": "evt_abc123",
    "occurred_at": "2026-01-15T12:00:00Z",
    "payload": {
      "id": "msg_xyz789",
      "from": {"phone_number": "+15551234567"},
      "to": [{"phone_number": "+15559876543"}],
      "text": "Hello"
    }
  }
}
```

**Key change**: Your webhook handler must parse JSON body instead of form data, and access fields via `data.payload.*` instead of flat keys.

## Messaging Webhook Field Mapping

### Inbound Message (`message.received`)

| Twilio Field | Telnyx Field | Access Path |
|---|---|---|
| `MessageSid` | `id` | `data.payload.id` |
| `From` | `from.phone_number` | `data.payload.from.phone_number` |
| `To` | `to[0].phone_number` | `data.payload.to[0].phone_number` |
| `Body` | `text` | `data.payload.text` |
| `NumMedia` | `media.length` | `data.payload.media` (array length) |
| `MediaUrl0` | `media[0].url` | `data.payload.media[0].url` |
| `MediaContentType0` | `media[0].content_type` | `data.payload.media[0].content_type` |
| `AccountSid` | N/A | Not included |
| `ApiVersion` | N/A | Not included |

### Delivery Status (`message.sent`, `message.delivered`, `message.failed`)

| Twilio Field | Telnyx Field | Access Path |
|---|---|---|
| `MessageStatus` | `event_type` suffix | `data.event_type` (e.g., `message.delivered`) |
| `MessageSid` | `id` | `data.payload.id` |
| `ErrorCode` | `errors[0].code` | `data.payload.errors[0].code` |
| `ErrorMessage` | `errors[0].title` | `data.payload.errors[0].title` |

### Messaging Status Value Mapping

| Twilio Status | Telnyx Event Type | Notes |
|---|---|---|
| `queued` | `message.queued` | Message accepted |
| `sent` | `message.sent` | Sent to carrier |
| `delivered` | `message.delivered` | Carrier confirmed delivery |
| `undelivered` | `message.failed` | Delivery failed (check `errors`) |
| `failed` | `message.failed` | Send failed |
| `received` | `message.received` | Inbound message |

## Voice Webhook Field Mapping

### TeXML Callbacks (form-encoded, similar to Twilio)

TeXML callbacks use form-encoded params similar to Twilio, so the migration is simpler:

| Twilio Field | Telnyx Field | Notes |
|---|---|---|
| `CallSid` | `CallSid` | Telnyx call control ID |
| `AccountSid` | `AccountSid` | Telnyx connection ID |
| `From` | `From` | Caller number |
| `To` | `To` | Called number |
| `CallStatus` | `CallStatus` | Same values: `initiated`, `ringing`, `answered`, `completed` |
| `Direction` | `Direction` | `inbound` or `outbound` |
| `RecordingUrl` | `RecordingUrl` | **Expires after 10 minutes** — download promptly |

### Call Control Webhooks (JSON)

| Twilio Field | Telnyx Event | Access Path |
|---|---|---|
| `CallSid` | `call_control_id` | `data.payload.call_control_id` |
| `From` | `from` | `data.payload.from` |
| `To` | `to` | `data.payload.to` |
| `CallStatus=initiated` | `call.initiated` | `data.event_type` |
| `CallStatus=ringing` | `call.ringing` | `data.event_type` |
| `CallStatus=answered` | `call.answered` | `data.event_type` |
| `CallStatus=completed` | `call.hangup` | `data.event_type` |

### Voice Status Value Mapping

| Twilio CallStatus | Telnyx Event | Notes |
|---|---|---|
| `initiated` | `call.initiated` | Call created |
| `ringing` | `call.ringing` | Remote party ringing |
| `in-progress` / `answered` | `call.answered` | Call connected |
| `completed` | `call.hangup` | Call ended normally |
| `busy` | `call.hangup` (cause: `BUSY`) | Remote busy |
| `no-answer` | `call.hangup` (cause: `TIMEOUT`) | No answer |
| `failed` | `call.hangup` (cause: varies) | Call failed |
| `canceled` | `call.hangup` (cause: `ORIGINATOR_CANCEL`) | Caller hung up |

## Signature Verification

### Twilio (HMAC-SHA1) — Remove This

```python
from twilio.request_validator import RequestValidator
validator = RequestValidator(auth_token)
is_valid = validator.validate(url, params, request.headers.get('X-Twilio-Signature'))
```

### Telnyx (Ed25519) — Add This

**Python:**
```python
from telnyx import Telnyx
client = Telnyx(api_key="YOUR_API_KEY")

from telnyx.webhooks import verify_signature
verify_signature(
    payload=request.data.decode("utf-8"),
    signature=request.headers.get("telnyx-signature-ed25519"),
    timestamp=request.headers.get("telnyx-timestamp"),
    public_key="YOUR_PUBLIC_KEY"
)
```

**Node.js:**
```javascript
const Telnyx = require('telnyx');
const client = new Telnyx({ apiKey: 'YOUR_API_KEY' });

client.webhooks.signature.verifySignature(
  JSON.stringify(req.body),
  req.headers['telnyx-signature-ed25519'],
  req.headers['telnyx-timestamp'],
  'YOUR_PUBLIC_KEY'
);
```

**Go (manual Ed25519):**
```go
import (
    "crypto/ed25519"
    "encoding/base64"
)

func verifyWebhook(payload, signature, timestamp, publicKeyBase64 string) bool {
    pubKey, _ := base64.StdEncoding.DecodeString(publicKeyBase64)
    sig, _ := base64.StdEncoding.DecodeString(signature)
    message := []byte(timestamp + "|" + payload)
    return ed25519.Verify(ed25519.PublicKey(pubKey), message, sig)
}
```

**Ruby:**
```ruby
require 'telnyx'
client = Telnyx::Client.new(api_key: 'YOUR_API_KEY')
Telnyx::Webhook.construct_event(payload, signature, timestamp, public_key: 'YOUR_PUBLIC_KEY')
```

## Framework-Specific Examples

### Flask (Python)

```python
from flask import Flask, request, jsonify
from telnyx import Telnyx
from telnyx.webhooks import verify_signature

app = Flask(__name__)
client = Telnyx(api_key="YOUR_API_KEY")
PUBLIC_KEY = "YOUR_PUBLIC_KEY"

@app.route('/webhooks/messaging', methods=['POST'])
def messaging_webhook():
    # Verify signature
    try:
        verify_signature(
            payload=request.data.decode("utf-8"),
            signature=request.headers.get("telnyx-signature-ed25519"),
            timestamp=request.headers.get("telnyx-timestamp"),
            public_key=PUBLIC_KEY
        )
    except Exception:
        return "Forbidden", 403

    event = request.json['data']
    event_type = event['event_type']
    payload = event['payload']

    if event_type == 'message.received':
        from_number = payload['from']['phone_number']
        text = payload['text']
        # Process inbound message...
    elif event_type == 'message.delivered':
        msg_id = payload['id']
        # Handle delivery confirmation...
    elif event_type == 'message.failed':
        errors = payload.get('errors', [])
        # Handle failure...

    return jsonify({"status": "ok"}), 200
```

### Express (Node.js)

```javascript
const express = require('express');
const Telnyx = require('telnyx');
const client = new Telnyx({ apiKey: 'YOUR_API_KEY' });
const app = express();
app.use(express.json());

app.post('/webhooks/messaging', (req, res) => {
  // Verify signature
  try {
    client.webhooks.signature.verifySignature(
      JSON.stringify(req.body),
      req.headers['telnyx-signature-ed25519'],
      req.headers['telnyx-timestamp'],
      'YOUR_PUBLIC_KEY'
    );
  } catch (e) {
    return res.status(403).send('Forbidden');
  }

  const { event_type, payload } = req.body.data;

  if (event_type === 'message.received') {
    const from = payload.from.phone_number;
    const text = payload.text;
    // Process inbound message...
  } else if (event_type === 'message.delivered') {
    // Handle delivery confirmation...
  } else if (event_type === 'message.failed') {
    const errors = payload.errors || [];
    // Handle failure...
  }

  res.sendStatus(200);
});
```

## Common Webhook Migration Mistakes

1. **Still parsing form data** — Telnyx sends JSON, not form-encoded. Use `request.json` (Flask) or `req.body` with JSON middleware (Express), not `request.form`.

2. **Missing `data` wrapper** — Telnyx nests everything under `data`. The event type is at `data.event_type`, not at the top level.

3. **Flat vs nested `from`** — Twilio: `From` is a string. Telnyx: `from` is an object with `phone_number` (and optionally `carrier`, `line_type`).

4. **`to` is an array** — Telnyx `to` is always an array (supports group messaging). Use `to[0].phone_number` for the primary recipient.

5. **No `200 OK` response** — Telnyx expects a `200` response within the timeout. If your handler doesn't respond, Telnyx retries (up to the configured retry count).

6. **Signature header names** — Twilio: `X-Twilio-Signature`. Telnyx: `telnyx-signature-ed25519` + `telnyx-timestamp` (two headers).

7. **Recording URLs expire** — Telnyx voice recording URLs expire after 10 minutes. Download or store them immediately in the webhook handler.
