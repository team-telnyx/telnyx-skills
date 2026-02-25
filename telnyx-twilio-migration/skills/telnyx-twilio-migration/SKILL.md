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

**Step-by-step migration process** (includes Call Control API as an alternative, client state patterns, bridge/link_to, caller ID policy, and subdomains):
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
- Telnyx also offers the **Call Control API** — an imperative, event-driven alternative to XML. Use it for complex conditional logic, real-time call manipulation, or state-machine workflows

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

Migrate from Twilio Voice SDK to Telnyx WebRTC SDKs. Key architectural difference: Telnyx allows direct browser-to-PSTN dialing without a server webhook.

Read `{baseDir}/references/webrtc-migration.md`

Covers: SDK mapping, TwiML endpoint analysis (DELETE vs CONVERT decision tree), credential lifecycle (per-session, not per-call), token refresh, CDN vs npm pitfalls, contact center patterns (conferences not always needed, SIP headers for passing data, URI dialing, call parking).

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

## Related Skills in This Repo

After migration, these skills provide deeper coverage for ongoing development:

| Migration Area | Related Skills | What They Cover |
|---|---|---|
| Voice (Call Control) | `telnyx-voice-*` | dial (with `bridge_on_answer`, `bridge_intent`, `link_to`, `supervisor_role`, `sip_headers`, `custom_headers`, `park_after_unbridge`), bridge, transfer, answer, hangup — all with optional params and webhook payload schemas |
| Voice (Advanced) | `telnyx-voice-advanced-*` | `client_state` on all commands, `updateClientState`, SIP Refer with `custom_headers`/`sip_headers`, DTMF send, SIPREC, noise suppression — with webhook payload field tables |
| Voice (Conferencing) | `telnyx-voice-conferencing-*` | conference create (with `max_participants`, `hold_audio_url`, `region`), join (with `supervisor_role`, `whisper_call_control_ids`, `mute`, `hold`), leave (returns to parked state), recording, speak, play — with webhook payload schemas |
| Voice (Gather/IVR) | `telnyx-voice-gather-*` | DTMF gathering, AI gather, gather using speak/audio — with webhook payload schemas for `call.gather.ended` |
| Voice (Media) | `telnyx-voice-media-*` | play audio, start/stop recording, streaming — with optional params for recording format, channels, track |
| Voice (TeXML REST) | `telnyx-texml-*` | TeXML API CRUD (JS only — other langs use Call Control) |
| WebRTC (Backend) | `telnyx-webrtc-*` | telephony credential create/token, SIP connection setup |
| WebRTC (Client) | `telnyx-webrtc-client-*` | platform SDKs (JS, iOS, Android, Flutter, React Native) — custom SIP headers, push notifications |
| SIP / Trunking | `telnyx-sip-*` | outbound voice profiles (with `whitelisted_destinations`, `traffic_type`, `calling_window`, `concurrent_call_limit`), credential connections (with `sip_uri_calling_preference`, `inbound`/`outbound` objects, `encrypted_media`), IP/FQDN connections |
| Messaging | `telnyx-messaging-*` | send/receive SMS/MMS with optional params and webhook payload schemas |
| Numbers | `telnyx-numbers-*`, `telnyx-porting-in-*` | number management, porting |
| Verify | `telnyx-verify-*` | verification API (SMS, voice, flash calling) |

Install the relevant language plugin (`telnyx-python`, `telnyx-javascript`, `telnyx-go`, `telnyx-java`, or `telnyx-ruby`) to access these skills.

## Resources

- Telnyx Mission Control Portal: https://portal.telnyx.com
- Telnyx Developer Docs: https://developers.telnyx.com
- Telnyx API Reference: https://developers.telnyx.com/api/overview
- Telnyx Status Page: https://status.telnyx.com
- Telnyx Support: https://support.telnyx.com
