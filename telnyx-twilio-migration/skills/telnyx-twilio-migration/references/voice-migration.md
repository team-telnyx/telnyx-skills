# Voice Migration: TwiML to TeXML

Step-by-step guide for migrating Twilio TwiML-based voice applications to Telnyx TeXML.

## Table of Contents

- [Overview](#overview)
- [Step 1: Create a Telnyx Account](#step-1-create-a-telnyx-account)
- [Step 2: Create a TeXML Application](#step-2-create-a-texml-application)
- [Step 3: Configure Webhook URLs](#step-3-configure-webhook-urls)
- [Step 4: Purchase or Port Phone Numbers](#step-4-purchase-or-port-phone-numbers)
- [Step 5: Update API Endpoints](#step-5-update-api-endpoints)
- [Step 6: Update Authentication](#step-6-update-authentication)
- [Step 7: Update Webhook Signature Validation](#step-7-update-webhook-signature-validation)
- [TeXML Bins](#texml-bins)
- [Testing Your Migration](#testing-your-migration)
- [Webhook Differences](#webhook-differences)
- [REST API Mapping](#rest-api-mapping)

## Overview

TeXML is Telnyx's TwiML-compatible markup language. Most TwiML documents work with Telnyx with these changes:

1. API base URL: `api.twilio.com` → `api.telnyx.com/v2/texml`
2. Authentication: Basic Auth → Bearer Token
3. Webhook signatures: HMAC-SHA1 → Ed25519
4. Webhook payloads: same top-level structure for TeXML callbacks

Your XML voice documents (`<Response>`, `<Say>`, `<Gather>`, etc.) generally require **no changes**.

## Step 1: Create a Telnyx Account

1. Sign up at https://telnyx.com/sign-up
2. Complete identity verification
3. Generate an API Key v2 at https://portal.telnyx.com/#/app/api-keys
4. Note your public key at https://portal.telnyx.com/#/app/account/public-key (needed for webhook validation)

## Step 2: Create a TeXML Application

In the Mission Control Portal:

1. Navigate to **Voice** → **TeXML Applications**
2. Click **Add New App**
3. Set a friendly name (e.g., `my-ivr-app`)
4. Configure voice webhook URLs (see Step 3)

Or via API:

```bash
curl -X POST https://api.telnyx.com/v2/texml_applications \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "friendly_name": "my-ivr-app",
    "voice_url": "https://example.com/voice",
    "voice_method": "POST",
    "status_callback": "https://example.com/status",
    "status_callback_method": "POST"
  }'
```

## Step 3: Configure Webhook URLs

Point your TeXML application to the same webhook server that currently serves your TwiML responses. Your server returns XML in the `<Response>` format — this does not change.

| Setting | Description |
|---|---|
| Voice URL | Your server endpoint that returns TeXML/TwiML XML for incoming calls |
| Voice Fallback URL | Backup URL if the primary fails |
| Voice Method | `POST` (recommended) or `GET` |
| Status Callback | URL for call status events (initiated, ringing, answered, completed) |

## Step 4: Purchase or Port Phone Numbers

**Purchase new numbers:**

```bash
curl -X POST https://api.telnyx.com/v2/number_orders \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": [{"phone_number": "+15551234567"}],
    "connection_id": "YOUR_TEXML_APP_ID"
  }'
```

**Port existing numbers from Twilio:** See `{baseDir}/references/number-porting.md` for the full FastPort guide.

Assign each number to your TeXML Application in the portal or via API.

## Step 5: Update API Endpoints

Replace Twilio REST API endpoints with Telnyx TeXML endpoints:

| Operation | Twilio | Telnyx |
|---|---|---|
| **Base URL** | `https://api.twilio.com/2010-04-01/Accounts/{SID}` | `https://api.telnyx.com/v2/texml` |
| List calls | `GET /Calls.json` | `GET /Calls` |
| Make a call | `POST /Calls.json` | `POST /Calls` |
| Get call | `GET /Calls/{SID}.json` | `GET /Calls/{SID}` |
| Update call | `POST /Calls/{SID}.json` | `POST /Calls/{SID}` |
| List recordings | `GET /Recordings.json` | `GET /Recordings` |
| List conferences | `GET /Conferences.json` | `GET /Conferences` |

Example — initiate an outbound call:

```bash
# Twilio
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_SID/Calls.json" \
  -u "$TWILIO_SID:$TWILIO_AUTH_TOKEN" \
  -d "To=+15559876543" \
  -d "From=+15551234567" \
  -d "Url=https://example.com/outbound-call"

# Telnyx
curl -X POST "https://api.telnyx.com/v2/texml/Calls" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "To=+15559876543" \
  -d "From=+15551234567" \
  -d "Url=https://example.com/outbound-call"
```

## Step 6: Update Authentication

Replace Twilio's Basic Auth with Telnyx Bearer Token in all API calls:

```python
# Twilio
from twilio.rest import Client
client = Client("ACCOUNT_SID", "AUTH_TOKEN")

# Telnyx — using native SDK
import telnyx
telnyx.api_key = "YOUR_TELNYX_API_KEY"
```

```javascript
// Twilio
const twilio = require('twilio');
const client = twilio('ACCOUNT_SID', 'AUTH_TOKEN');

// Telnyx — using native SDK
const Telnyx = require('telnyx');
const telnyx = Telnyx('YOUR_TELNYX_API_KEY');
```

```bash
# Twilio
curl -u "$TWILIO_SID:$TWILIO_AUTH_TOKEN" ...

# Telnyx
curl -H "Authorization: Bearer $TELNYX_API_KEY" ...
```

## Step 7: Update Webhook Signature Validation

This is the most important code change. Twilio uses HMAC-SHA1 with your auth token. Telnyx uses Ed25519 with a public key.

**Python:**
```python
# Twilio (remove this)
from twilio.request_validator import RequestValidator
validator = RequestValidator(auth_token)
is_valid = validator.validate(url, params, request.headers.get('X-Twilio-Signature'))

# Telnyx (add this)
import telnyx
telnyx.public_key = "YOUR_PUBLIC_KEY"  # from portal.telnyx.com

from telnyx.webhook import WebhookSignatureVerifier
try:
    WebhookSignatureVerifier.verify(
        payload=request.data.decode("utf-8"),
        signature=request.headers.get("telnyx-signature-ed25519"),
        timestamp=request.headers.get("telnyx-timestamp")
    )
    # Signature valid
except Exception:
    # Signature invalid — reject the request
    return "Forbidden", 403
```

**Node.js:**
```javascript
// Twilio (remove this)
const twilio = require('twilio');
const isValid = twilio.validateRequest(authToken, signature, url, params);

// Telnyx (add this)
const telnyx = require('telnyx')('YOUR_API_KEY');
const PUBLIC_KEY = "YOUR_PUBLIC_KEY";

try {
  telnyx.webhooks.signature.verifySignature(
    JSON.stringify(req.body),
    req.headers['telnyx-signature-ed25519'],
    req.headers['telnyx-timestamp'],
    PUBLIC_KEY
  );
  // Signature valid
} catch (e) {
  // Signature invalid
  res.status(403).send('Forbidden');
}
```

## TeXML Bins

Twilio has TwiML Bins — static TwiML documents hosted by Twilio. Telnyx has an equivalent: **TeXML Bins**.

Create a TeXML Bin in the Mission Control Portal under **Voice** → **TeXML Applications** → **TeXML Bins**. Paste your static XML and get a hosted URL you can use as a Voice URL or waitUrl.

## Testing Your Migration

1. **Validate your XML first:**
   ```bash
   bash {baseDir}/scripts/validate-texml.sh /path/to/your/twiml.xml
   ```

2. **Test with a single number:** Assign one number to your TeXML Application and make a test call.

3. **Check webhook delivery:** In the Mission Control Portal, navigate to **Debugging** → **API Logs** to see webhook deliveries and responses.

4. **Verify recordings:** If your app uses recording, confirm that dual-channel is acceptable or explicitly set `channels="single"` / `recordingChannels="single"`.

5. **Test answering machine detection (AMD):** If you use AMD, verify `machineDetection` attribute behavior. Telnyx supports `Regular` and `Premium` detection modes.

## Webhook Differences

TeXML callbacks use the same parameter names as TwiML for most fields. Key differences:

| Parameter | Notes |
|---|---|
| `AccountSid` | Your Telnyx Connection ID (not the same as Twilio Account SID) |
| `CallSid` | Telnyx call control ID |
| `RecordingUrl` | Valid for 10 minutes after call ends (Twilio URLs persist longer) |

Status callback events match Twilio's: `initiated`, `ringing`, `answered`, `completed`.

## REST API Mapping

For REST API operations (managing calls, conferences, recordings programmatically), the existing TeXML skills in this repo provide complete SDK examples:

> **Enhanced coverage**: Install the language plugin for your stack (`telnyx-python`, `telnyx-javascript`, `telnyx-go`, `telnyx-java`, `telnyx-ruby`) and reference the `telnyx-texml-*` skill for complete REST API examples.
