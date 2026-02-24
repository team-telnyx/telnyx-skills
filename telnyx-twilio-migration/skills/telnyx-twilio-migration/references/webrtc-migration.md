# WebRTC Migration: Twilio Voice SDK to Telnyx WebRTC

Migrate from Twilio's client-side Voice SDK to Telnyx WebRTC SDKs.

## Table of Contents

- [Architecture Differences](#architecture-differences)
- [Concept Mapping](#concept-mapping)
- [Migration Steps](#migration-steps)
- [Authentication Flow Comparison](#authentication-flow-comparison)
- [Client SDK Setup](#client-sdk-setup)
- [Call Management](#call-management)
- [Platform-Specific Guides](#platform-specific-guides)

## Architecture Differences

The most significant difference: **Telnyx simplifies the architecture by eliminating the mandatory backend token server.**

**Twilio architecture (required backend):**
```
Browser/App → Your Backend Server → Twilio API (get Access Token)
           ← Access Token ←
Browser/App → Twilio (connect with Access Token)
```

Your backend must generate short-lived Access Tokens using your Account SID and API Key. The client SDK cannot function without this backend.

**Telnyx architecture (optional backend):**
```
Browser/App → Telnyx (connect with SIP credentials or JWT)
```

Telnyx WebRTC supports direct authentication using SIP credentials (username/password) or JWT tokens. A backend server is optional — useful for dynamic credential management but not required.

## Concept Mapping

| Twilio Concept | Telnyx Concept | Notes |
|---|---|---|
| TwiML App | SIP Connection | Routes calls to your application logic |
| Access Token | SIP Credentials or JWT | Direct auth, no mandatory backend |
| Twilio.Device | TelnyxRTC.TelnyxRTC | Client SDK entry point |
| device.connect() | client.newCall() | Initiate outbound call |
| device.on('incoming') | client.on('telnyx.notification') | Receive inbound call |
| Call object | Call object | Active call with controls |
| call.mute() | call.muteAudio() | Mute microphone |
| call.disconnect() | call.hangup() | End call |
| device.register() | client.connect() | Register for inbound calls |
| device.unregister() | client.disconnect() | Unregister |

## Migration Steps

### 1. Create a SIP Connection (replaces TwiML App)

In Mission Control Portal → **SIP** → **SIP Connections**:
- Create a new connection
- Set the connection type to **Credentials**
- Note the connection ID

Or via API:
```bash
curl -X POST https://api.telnyx.com/v2/credential_connections \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_name": "my-webrtc-app",
    "active": true
  }'
```

### 2. Create SIP Credentials (replaces Access Token generation)

```bash
curl -X POST https://api.telnyx.com/v2/telephony_credentials \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_id": "YOUR_CONNECTION_ID",
    "name": "web-user-1"
  }'
```

Response includes `sip_username` and `sip_password`. These can be used directly by the client SDK — no backend token exchange required.

For JWT-based auth (optional, more secure):
```bash
curl -X POST "https://api.telnyx.com/v2/telephony_credentials/YOUR_CREDENTIAL_ID/token" \
  -H "Authorization: Bearer $TELNYX_API_KEY"
```

### 3. Swap the Client SDK

```bash
# Twilio (remove)
npm remove @twilio/voice-sdk

# Telnyx (add)
npm install @telnyx/webrtc
```

### 4. Update Client Code

See the side-by-side comparison in [Client SDK Setup](#client-sdk-setup) below.

### 5. Update Push Notification Configuration (Mobile)

If your mobile app uses VoIP push notifications:

| Platform | Twilio | Telnyx |
|---|---|---|
| iOS | Register with `device.register(accessToken)` | Upload APNs certificate in Mission Control Portal |
| Android | Use FCM with Twilio's `handleMessage()` | Use FCM with Telnyx's `handlePushNotification()` |

## Authentication Flow Comparison

### Twilio (requires backend)

```javascript
// Backend: generate Access Token
const AccessToken = require('twilio').jwt.AccessToken;
const VoiceGrant = new AccessToken.VoiceGrant({
  outgoingApplicationSid: 'AP...',
  incomingAllow: true
});
const token = new AccessToken('AC...', 'SK...', 'secret');
token.addGrant(voiceGrant);
token.identity = 'user-123';
return token.toJwt();
```

```javascript
// Client: connect with token from backend
const { Device } = require('@twilio/voice-sdk');
const response = await fetch('/api/token');
const { token } = await response.json();
const device = new Device(token);
await device.register();
```

### Telnyx (direct connection)

```javascript
// Client: connect directly with SIP credentials
const { TelnyxRTC } = require('@telnyx/webrtc');
const client = new TelnyxRTC({
  login: 'sip_username',
  password: 'sip_password'
});
client.connect();
```

Or with JWT:
```javascript
const client = new TelnyxRTC({
  login_token: 'jwt_token_from_api'
});
client.connect();
```

## Client SDK Setup

### JavaScript (Browser)

```javascript
// Twilio
import { Device } from '@twilio/voice-sdk';
const token = await fetchTokenFromBackend();
const device = new Device(token);
await device.register();

device.on('incoming', (call) => {
  call.accept();
});

const call = await device.connect({
  params: { To: '+15559876543' }
});

call.on('disconnect', () => console.log('Call ended'));
call.disconnect();
```

```javascript
// Telnyx
import { TelnyxRTC } from '@telnyx/webrtc';
const client = new TelnyxRTC({
  login: 'sip_username',
  password: 'sip_password'
});
client.connect();

client.on('telnyx.notification', (notification) => {
  const call = notification.call;
  call.answer();
});

const call = client.newCall({
  destinationNumber: '+15559876543',
  callerNumber: '+15551234567'
});

call.on('hangup', () => console.log('Call ended'));
call.hangup();
```

## Call Management

| Action | Twilio | Telnyx |
|---|---|---|
| Make call | `device.connect({params: {To: num}})` | `client.newCall({destinationNumber: num})` |
| Answer call | `call.accept()` | `call.answer()` |
| Hang up | `call.disconnect()` | `call.hangup()` |
| Mute | `call.mute(true)` | `call.muteAudio()` |
| Unmute | `call.mute(false)` | `call.unmuteAudio()` |
| Hold | Not built-in | `call.hold()` |
| Unhold | Not built-in | `call.unhold()` |
| Send DTMF | `call.sendDigits('1')` | `call.dtmf('1')` |
| Transfer | Not built-in | `call.transfer(destination)` |

Telnyx provides built-in hold, unhold, and transfer — features that require server-side logic with Twilio.

## Platform-Specific Guides

> **Enhanced coverage**: Install the `telnyx-webrtc-client` plugin for comprehensive platform-specific implementation guides:
>
> - **JavaScript/Browser**: `telnyx-webrtc-client-js` — Full browser WebRTC with media handling, codec configuration, quality metrics, debugging
> - **iOS/Swift**: `telnyx-webrtc-client-ios` — CallKit integration, APNs push notifications, background audio
> - **Android/Kotlin**: `telnyx-webrtc-client-android` — FCM push notifications, Telecom framework, foreground services
> - **Flutter/Dart**: `telnyx-webrtc-client-flutter` — Cross-platform with platform channel integration
> - **React Native/TypeScript**: `telnyx-webrtc-client-react-native` — Unified JS API with native modules

These skills cover authentication options, event handling, call controls, quality metrics, and debugging patterns for each platform.
