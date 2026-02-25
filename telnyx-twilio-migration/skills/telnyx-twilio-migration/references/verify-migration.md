# Verify Migration: Twilio Verify to Telnyx Verify

Migrate from Twilio Verify to the Telnyx Verify API for phone number verification and 2FA.

## Table of Contents

- [Overview](#overview)
- [Verification Methods](#verification-methods)
- [Setup](#setup)
- [Sending Verification Codes](#sending-verification-codes)
- [Checking Verification Codes](#checking-verification-codes)
- [Flash Calling](#flash-calling)
- [Concept Mapping](#concept-mapping)
- [Webhook Differences](#webhook-differences)

## Overview

Telnyx Verify is not a drop-in replacement for Twilio Verify. The API surface is different, but the functionality is equivalent. Key differences:

- Telnyx uses a **Verify Profile** (analogous to Twilio's Verify Service)
- Different endpoint structure and parameter names
- Telnyx supports flash calling (missed-call verification) which Twilio does not offer on Verify
- PSD2 (Payment Services Directive 2) compliance built-in

## Verification Methods

| Method | Twilio Verify | Telnyx Verify |
|---|---|---|
| SMS OTP | Yes | Yes |
| Voice call OTP | Yes | Yes (`call` channel) |
| Email OTP | Yes | No |
| Push notification | Yes (Authy) | No |
| TOTP | Yes (Authy) | No |
| Flash calling | No | Yes — verification via missed call (caller ID matching) |
| vSMS (templated) | No | Yes — SMS with pre-approved carrier templates |
| PSD2 | No native support | Yes — built-in PSD2-compliant verification |

## Setup

### Create a Verify Profile

```bash
curl -X POST https://api.telnyx.com/v2/verify_profiles \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My App Verification",
    "messaging_enabled": true,
    "rcs_enabled": false,
    "default_timeout_secs": 300
  }'
```

Note the `id` in the response — this is your Verify Profile ID.

### Twilio Setup (for comparison)

```javascript
// Twilio: create Verify Service
const service = await client.verify.v2.services.create({
  friendlyName: 'My App Verification'
});
// service.sid = 'VA...'
```

## Sending Verification Codes

### SMS Verification

```python
# Twilio
verification = client.verify.v2 \
    .services('VA...') \
    .verifications \
    .create(to='+15559876543', channel='sms')

# Telnyx
import telnyx
telnyx.api_key = "YOUR_API_KEY"
verification = telnyx.Verification.create(
    phone_number="+15559876543",
    verify_profile_id="YOUR_PROFILE_ID",
    type="sms"
)
```

```javascript
// Twilio
const verification = await client.verify.v2
  .services('VA...')
  .verifications
  .create({ to: '+15559876543', channel: 'sms' });

// Telnyx
const telnyx = require('telnyx')('YOUR_API_KEY');
const verification = await telnyx.verifications.create({
  phone_number: '+15559876543',
  verify_profile_id: 'YOUR_PROFILE_ID',
  type: 'sms'
});
```

```bash
# Twilio
curl -X POST "https://verify.twilio.com/v2/Services/$SERVICE_SID/Verifications" \
  -u "$SID:$AUTH_TOKEN" \
  -d "To=+15559876543" -d "Channel=sms"

# Telnyx
curl -X POST https://api.telnyx.com/v2/verifications \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "+15559876543",
    "verify_profile_id": "YOUR_PROFILE_ID",
    "type": "sms"
  }'
```

### Voice Call Verification

```python
# Twilio
verification = client.verify.v2 \
    .services('VA...') \
    .verifications \
    .create(to='+15559876543', channel='call')

# Telnyx
verification = telnyx.Verification.create(
    phone_number="+15559876543",
    verify_profile_id="YOUR_PROFILE_ID",
    type="call"
)
```

### Parameter Mapping

| Twilio | Telnyx | Notes |
|---|---|---|
| `to` | `phone_number` | E.164 format |
| `channel` | `type` | `sms`, `call`, `flash_call`, `psd2` |
| Service SID (`VA...`) | `verify_profile_id` | Profile ID from setup |
| `locale` | Not specified | Language determined by phone number region |
| `customCode` | `custom_code` | Use your own code (optional) |
| `amount` + `payee` | `amount` + `payee` | For PSD2 verification |

## Checking Verification Codes

```python
# Twilio
check = client.verify.v2 \
    .services('VA...') \
    .verification_checks \
    .create(to='+15559876543', code='123456')
# check.status == 'approved' or 'pending'

# Telnyx
verification = telnyx.Verification.verify_by_phone_number(
    phone_number="+15559876543",
    code="123456"
)
# verification.response_code == 'accepted' or 'rejected'
```

```javascript
// Twilio
const check = await client.verify.v2
  .services('VA...')
  .verificationChecks
  .create({ to: '+15559876543', code: '123456' });
// check.status === 'approved'

// Telnyx
const result = await telnyx.verifications.verify_by_phone_number({
  phone_number: '+15559876543',
  code: '123456'
});
// result.data.response_code === 'accepted'
```

```bash
# Twilio
curl -X POST "https://verify.twilio.com/v2/Services/$SERVICE_SID/VerificationChecks" \
  -u "$SID:$AUTH_TOKEN" \
  -d "To=+15559876543" -d "Code=123456"

# Telnyx
curl -X POST https://api.telnyx.com/v2/verifications/by_phone_number \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "+15559876543",
    "code": "123456"
  }'
```

### Status Mapping

| Twilio Status | Telnyx Response Code | Meaning |
|---|---|---|
| `approved` | `accepted` | Code is correct |
| `pending` | `rejected` | Code is incorrect or expired |
| `canceled` | N/A | Verification was canceled |

## Flash Calling

Telnyx-only feature. Verification via a missed call — the user's phone displays a caller ID, and the last N digits of that number are the verification code. No SMS charges, faster in some markets.

```python
verification = telnyx.Verification.create(
    phone_number="+15559876543",
    verify_profile_id="YOUR_PROFILE_ID",
    type="flash_call"
)
```

The user sees an incoming call that auto-disconnects. Your app reads the caller ID and extracts the code automatically (or prompts the user to enter it).

## Concept Mapping

| Twilio Concept | Telnyx Concept |
|---|---|
| Verify Service (`VA...`) | Verify Profile |
| Verification SID | Verification ID |
| Channel (`sms`, `call`, `email`) | Type (`sms`, `call`, `flash_call`, `psd2`) |
| `approved` / `pending` | `accepted` / `rejected` |
| Rate limits (per Service) | Rate limits (per Profile) |
| Fraud Guard | Built-in fraud detection |

## Webhook Differences

Twilio Verify does not use webhooks for verification results — you poll with VerificationChecks.

Telnyx Verify also primarily uses a request/response pattern (create verification → check code). However, Telnyx sends webhook events for verification status changes if configured on your Verify Profile:

- `verification.sent` — code was sent
- `verification.accepted` — code was correctly verified
- `verification.rejected` — incorrect code submitted
- `verification.expired` — code expired without verification
