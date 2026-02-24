---
name: telnyx-twilio-migration
description: >-
  Migrate from Twilio to Telnyx. Covers voice (TwiML to TeXML with full verb
  reference), messaging, WebRTC, number porting via FastPort, and Verify.
  Includes product mapping, migration scripts, and key differences in auth,
  webhooks, and payload format.
metadata:
  author: telnyx
  product: migration
---

# Twilio to Telnyx Migration

One-stop guide for migrating from Twilio to Telnyx. This skill covers every product area with step-by-step migration paths, code examples, and validation scripts.

> **Standalone skill**: This skill is fully self-contained. For deeper SDK-specific code examples after migration, install the relevant language plugin (`telnyx-python`, `telnyx-javascript`, `telnyx-go`, `telnyx-java`, or `telnyx-ruby`). For client-side WebRTC, install `telnyx-webrtc-client`.

## Preflight Check

Before starting any migration, validate your environment:

```bash
bash {baseDir}/scripts/preflight-check.sh
```

This checks for a valid `TELNYX_API_KEY`, API connectivity, and detects any installed Twilio SDKs.

## Product Mapping (Quick Reference)

| Twilio Product | Telnyx Equivalent | Migration Path |
|---|---|---|
| Programmable Voice (TwiML) | TeXML | Near drop-in XML compatibility |
| Programmable Voice (REST) | Call Control API | Event-driven, WebSocket-based |
| Programmable Messaging | Messaging API | New SDK integration |
| Elastic SIP Trunking | SIP Trunking | Direct replacement |
| Voice SDK (WebRTC) | WebRTC SDKs (JS, iOS, Android, Flutter, RN) | Concept remapping |
| Phone Numbers | Number Management | FastPort for same-day porting |
| Twilio Verify | Verify API | Different API surface, same functionality |
| Twilio Lookup | Number Lookup | Direct replacement |
| Twilio Video (retired Dec 2024) | Video Rooms API | Telnyx still supports video |
| Twilio Fax (deprecated) | Programmable Fax | Telnyx still supports fax |
| Super SIM / IoT | IoT SIM Cards | 650+ networks, 180+ countries |

For the complete mapping including Telnyx-only products and unsupported Twilio products, read:
`{baseDir}/references/product-mapping.md`

## Universal Changes (All Migrations)

These four changes apply regardless of which Twilio product you are migrating.

### 1. Authentication

Twilio uses Basic Auth with Account SID + Auth Token. Telnyx uses Bearer Token with an API Key v2.

```bash
# Twilio
curl -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" \
  https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json

# Telnyx
curl -H "Authorization: Bearer $TELNYX_API_KEY" \
  https://api.telnyx.com/v2/messages
```

Get your API key at https://portal.telnyx.com/#/app/api-keys

### 2. Webhook Signature Validation

Twilio signs webhooks with HMAC-SHA1 (symmetric, uses auth token). Telnyx uses Ed25519 (asymmetric, uses a public key). This is the most common breaking change.

Get your public key at https://portal.telnyx.com/#/app/account/public-key

**Python:**
```python
import telnyx
# Set your public key for webhook validation
telnyx.public_key = "YOUR_TELNYX_PUBLIC_KEY"

# In your webhook handler:
from telnyx.webhook import WebhookSignatureVerifier
signature = request.headers.get("telnyx-signature-ed25519")
timestamp = request.headers.get("telnyx-timestamp")
WebhookSignatureVerifier.verify(request.body, signature, timestamp)
```

**Node.js:**
```javascript
const telnyx = require('telnyx')('YOUR_API_KEY');
telnyx.webhooks.signature.verifySignature(
  payload,
  request.headers['telnyx-signature-ed25519'],
  request.headers['telnyx-timestamp'],
  PUBLIC_KEY
);
```

### 3. Webhook Payload Structure

Twilio sends flat key-value pairs. Telnyx nests event data under a `data` object:

```json
// Twilio webhook payload
{ "MessageSid": "SM...", "From": "+1555...", "Body": "Hello" }

// Telnyx webhook payload
{
  "data": {
    "event_type": "message.received",
    "payload": {
      "id": "...",
      "from": { "phone_number": "+1555..." },
      "text": "Hello"
    }
  }
}
```

### 4. Recording Defaults

Twilio defaults to single-channel recordings. Telnyx defaults to **dual-channel** (each party on a separate channel). To match Twilio behavior, explicitly set `channels="single"` or `recordingChannels="single"` in your TeXML or API calls.

## Migration Guides by Product

### Voice: TwiML to TeXML

TeXML is Telnyx's TwiML-compatible XML markup for voice applications. Most TwiML documents work with minimal changes.

**Quick validation** -- check your existing TwiML files for compatibility:
```bash
bash {baseDir}/scripts/validate-texml.sh /path/to/your/twiml.xml
```

The script reports unsupported verbs, attribute differences, and Telnyx-only features you can adopt.

**Step-by-step migration process:**
Read `{baseDir}/references/voice-migration.md`

**Complete TeXML verb reference** (all 15 verbs + 8 nouns with attributes, nesting rules, and examples):
Read `{baseDir}/references/texml-verbs.md`

**Key facts:**
- TeXML supports all standard TwiML verbs: `<Say>`, `<Play>`, `<Gather>`, `<Dial>`, `<Record>`, `<Hangup>`, `<Pause>`, `<Redirect>`, `<Reject>`, `<Refer>`, `<Enqueue>`, `<Leave>`
- Telnyx adds: `<Start>`, `<Stop>`, `<Connect>` (for async services)
- Telnyx-only nouns: `<Transcription>` (real-time STT), `<Suppression>` (audio suppression), `<Siprec>` (SIPREC recording)
- `<Gather>` supports multiple STT engines: Google, Telnyx, Deepgram, Azure
- `<Say>` supports ElevenLabs voices alongside Polly
- `<Pay>` has no TeXML equivalent

### Messaging

Migrate from Twilio Programmable Messaging to the Telnyx Messaging API. This is a new SDK integration, not a drop-in replacement.

Read `{baseDir}/references/messaging-migration.md`

**Quick comparison:**
```python
# Twilio
from twilio.rest import Client
client = Client(account_sid, auth_token)
message = client.messages.create(to="+1555...", from_="+1666...", body="Hello")

# Telnyx
import telnyx
telnyx.api_key = "YOUR_API_KEY"
message = telnyx.Message.create(to="+1555...", from_="+1666...", text="Hello")
```

### WebRTC / Voice SDK

Migrate from Twilio Voice SDK to Telnyx WebRTC SDKs. Key architectural difference: Telnyx eliminates the mandatory backend server for token generation.

Read `{baseDir}/references/webrtc-migration.md`

> **Enhanced coverage**: Install the `telnyx-webrtc-client` plugin for platform-specific implementation guides (JavaScript, iOS, Android, Flutter, React Native).

### Number Porting (FastPort)

Move your phone numbers from Twilio to Telnyx programmatically. FastPort provides real-time LOA validation and on-demand activation for US/Canada numbers.

Read `{baseDir}/references/number-porting.md`

### Verify / 2FA

Migrate from Twilio Verify to Telnyx Verify API. Supports SMS, voice, flash calling, and PSD2 verification methods.

Read `{baseDir}/references/verify-migration.md`

## Scripts

### validate-texml.sh

Analyzes TwiML/TeXML XML files for compatibility issues:

```bash
bash {baseDir}/scripts/validate-texml.sh /path/to/file.xml
```

Reports:
- **Errors**: Unsupported verbs with no TeXML equivalent
- **Warnings**: Attributes with different defaults or behavior
- **Info**: Telnyx-only features you could adopt

### preflight-check.sh

Validates migration environment readiness:

```bash
bash {baseDir}/scripts/preflight-check.sh
```

Checks:
- `TELNYX_API_KEY` environment variable
- API connectivity to `api.telnyx.com`
- Installed Twilio/Telnyx SDKs (Python, Node.js, Ruby, Go, Java)

## Post-Migration Checklist

After completing migration for any product:

1. Update all webhook URLs to point to your Telnyx-configured endpoints
2. Replace all Twilio signature validation with Telnyx Ed25519 validation
3. Update credential storage (API keys, public keys)
4. Test webhook delivery in the Telnyx Mission Control Portal
5. Verify number assignments (each number must be assigned to a connection or messaging profile)
6. Update monitoring/alerting for Telnyx-specific status codes and error formats
7. Update any Twilio status callback URLs to Telnyx webhook format

## Resources

- Telnyx Mission Control Portal: https://portal.telnyx.com
- Telnyx Developer Docs: https://developers.telnyx.com
- Telnyx API Reference: https://developers.telnyx.com/api/overview
- Telnyx Status Page: https://status.telnyx.com
- Telnyx Support: https://support.telnyx.com
