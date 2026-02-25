# WebRTC Migration: Twilio Voice SDK to Telnyx WebRTC

Migrate from Twilio's client-side Voice SDK to Telnyx WebRTC SDKs.

## Table of Contents

- [Architecture Differences](#architecture-differences)
- [TwiML Endpoint Analysis (DELETE vs CONVERT)](#twiml-endpoint-analysis-delete-vs-convert)
- [Concept Mapping](#concept-mapping)
- [Migration Steps](#migration-steps)
- [Authentication Flow Comparison](#authentication-flow-comparison)
- [Client SDK Setup](#client-sdk-setup)
- [Call Management](#call-management)
- [Token and Credential Management](#token-and-credential-management)
- [Platform-Specific Guides](#platform-specific-guides)
- [Contact Center / PBX Patterns](#contact-center--pbx-patterns)

## Architecture Differences

The most significant difference: **Telnyx WebRTC can dial PSTN directly from the browser without a server webhook.**

**Twilio architecture (mandatory backend):**
```
Browser/App → Your Backend Server → Twilio API (get Access Token)
           ← Access Token ←
Browser/App → Twilio (connect with Access Token)
           → Twilio calls your TwiML App webhook → Server returns <Dial> → Call connects
```

Every outbound call requires a round-trip to your server to get TwiML instructions, even for a simple dial.

**Telnyx architecture (optional backend):**
```
Browser/App → Telnyx (connect with SIP credentials or JWT)
Browser/App → client.newCall({destinationNumber}) → Call connects directly to PSTN
```

A backend server is only needed for:
- Dynamic credential management
- Complex call flows (IVR, recording, conferencing)
- Business logic that can't live in the client

## TwiML Endpoint Analysis (DELETE vs CONVERT)

Before migrating each TwiML endpoint, determine if it's still needed:

```
TwiML ENDPOINT DECISION TREE
─────────────────────────────
Does it ONLY do simple dial?
(Returns <Dial><Number>{param}</Number></Dial>)
├── YES → DELETE endpoint, use client.newCall() instead
└── NO → Does it use <Gather>, <Record>, <Say>, <Play>, <Conference>, or conditional logic?
    ├── YES → CONVERT to TeXML (keep server endpoint, XML is compatible)
    └── NO → Likely DELETE (analyze further)
```

| TwiML Pattern | Action | Telnyx Replacement |
|---|---|---|
| `<Dial><Number>{To}</Number></Dial>` | **DELETE** | `client.newCall({destinationNumber: to})` |
| `<Dial callerId="+1...">{To}</Dial>` | **DELETE** | `client.newCall({destinationNumber, callerNumber})` |
| `<Gather><Say>Press 1...</Say></Gather>` | **CONVERT** | Same XML, point to TeXML Application |
| `<Record action="/handle">` | **CONVERT** | Same XML, point to TeXML Application |
| `<Dial><Conference>room</Conference></Dial>` | **CONVERT** | Same XML, point to TeXML Application |
| Conditional routing (if/else) | **CONVERT** | Same server logic, return TeXML |

**Benefits of deleting endpoints:** Lower latency (no server round-trip), less code to maintain, reduced server costs.

## Concept Mapping

| Twilio Concept | Telnyx Concept | Notes |
|---|---|---|
| TwiML App | SIP Connection | Routes calls to your application logic |
| Access Token | SIP Credentials or JWT | Direct auth, no mandatory backend |
| Twilio.Device | TelnyxRTC.TelnyxRTC | Client SDK entry point |
| device.connect() | client.newCall() | Initiate outbound call |
| device.on('incoming') | client.on('telnyx.notification') | Receive inbound call |
| Call object | Call object | Active call with controls |
| call.accept() | call.answer() | Answer incoming call |
| call.mute(true/false) | call.muteAudio() / call.unmuteAudio() | No `isMuted()` — track state manually |
| call.disconnect() | call.hangup() | End call |
| call.sendDigits() | call.dtmf() | Send DTMF tones |
| device.register() | client.connect() | Register for inbound calls |
| device.unregister() | client.disconnect() | Unregister |
| device.on('registered') | client.on('telnyx.ready') | Client connected |
| device.on('error') | client.on('telnyx.error') | Error handler |
| device.on('tokenWillExpire') | *None — use timer* | See [Token Management](#token-and-credential-management) |
| Not built-in | call.hold() / call.unhold() | Telnyx has native hold |
| Not built-in | call.transfer() | Telnyx has native transfer |

### Telnyx Call States

Telnyx calls pass through these states: `new` → `trying` → `requesting` → `recovering` → `ringing` → `answering` → `early` → `active` → `held` → `hangup` → `destroy` → `purge`

## Migration Steps

### 1. Create a SIP Connection (replaces TwiML App)

In Mission Control Portal → **SIP** → **SIP Connections**:
- Create a new connection
- Set the connection type to **Credentials**
- **Enable URI dialing** if your app dials SIP URIs (not just PSTN)
- Note the connection ID

Or via API:
```bash
curl -X POST https://api.telnyx.com/v2/credential_connections \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_name": "my-webrtc-app",
    "active": true,
    "webrtc_enabled": true,
    "sip_uri_calling_preference": "disabled",
    "inbound": {
      "sip_subdomain": "my-app",
      "sip_subdomain_receive_settings": "only_my_connections"
    },
    "outbound": {
      "outbound_voice_profile_id": "YOUR_OVP_ID"
    }
  }'
```

Key SIP connection parameters:
| Parameter | Purpose |
|---|---|
| `webrtc_enabled` | Must be `true` for browser/app clients |
| `sip_uri_calling_preference` | `"disabled"` (default), `"unrestricted"`, or `"internal"` — controls URI dialing |
| `sip_subdomain` | Unique subdomain for SIP registration (e.g., `my-app.sip.telnyx.com`) |
| `sip_subdomain_receive_settings` | `"from_anyone"` or `"only_my_connections"` |
| `outbound_voice_profile_id` | Controls caller ID policy for outbound calls |

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

**CDN vs npm — critical pitfall:**

| Method | Import |
|---|---|
| npm/bundler | `import { TelnyxRTC } from '@telnyx/webrtc'` — use `TelnyxRTC` directly |
| CDN script | `<script src="...bundle.js">` — use `TelnyxWebRTC.TelnyxRTC` (double namespace!) |

```javascript
// CDN: INCORRECT (throws "TelnyxRTC is not defined")
const client = new TelnyxRTC({ login_token: token });

// CDN: CORRECT
const client = new TelnyxWebRTC.TelnyxRTC({ login_token: token });
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

// IMPORTANT: Set audio element for remote audio playback
client.remoteElement = document.getElementById('remoteAudio');

client.connect();

client.on('telnyx.notification', (notification) => {
  if (notification.type === 'callUpdate' &&
      notification.call.state === 'ringing' &&
      notification.call.direction === 'inbound') {
    notification.call.answer();
  }
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
| Check mute | `call.isMuted()` | *Track manually* — no built-in method |
| Hold | Not built-in | `call.hold()` |
| Unhold | Not built-in | `call.unhold()` |
| Send DTMF | `call.sendDigits('1')` | `call.dtmf('1')` |
| Transfer | Not built-in | `call.transfer(destination)` |

Telnyx provides built-in hold, unhold, and transfer — features that require server-side logic with Twilio.

## Token and Credential Management

### Credential Lifecycle: Per-Session, Not Per-Call

**Twilio pattern** (per-call): Twilio documentation suggests creating a new Access Token for each call or short session. Tokens expire quickly (typically 1 hour).

**Telnyx pattern** (per-session): Generate credentials once per user session and reuse them for the session duration. Do NOT create new credentials for every call.

```javascript
// RECOMMENDED: Generate credentials once per session
class TelnyxSession {
  constructor() {
    this.client = null;
    this.tokenRefreshTimer = null;
  }

  async initialize() {
    // Create credential (do this ONCE per session, not per call)
    const credential = await fetch('/api/telnyx/credential', { method: 'POST' });
    const { token } = await credential.json();

    this.client = new TelnyxRTC({ login_token: token });
    this.client.remoteElement = document.getElementById('remoteAudio');
    this.client.connect();

    // Store client in your app's state management (React state, Redux, etc.)
    // so it persists across component renders
    this.scheduleTokenRefresh();
  }

  scheduleTokenRefresh() {
    // JWT tokens expire after 24 hours — refresh at 23 hours
    // Telnyx has NO tokenWillExpire event (unlike Twilio)
    this.tokenRefreshTimer = setTimeout(async () => {
      const { token } = await fetch('/api/telnyx/credential', { method: 'POST' })
        .then(r => r.json());
      // Must disconnect and reconnect with new token (no updateToken method)
      this.client.disconnect();
      this.client = new TelnyxRTC({ login_token: token });
      this.client.remoteElement = document.getElementById('remoteAudio');
      this.client.connect();
      this.scheduleTokenRefresh();
    }, 23 * 60 * 60 * 1000); // 23 hours
  }
}
```

**Server-side credential generation (recommended: dynamic credentials):**
```javascript
// Express.js endpoint
app.post('/api/telnyx/credential', async (req, res) => {
  const telnyx = require('telnyx')(process.env.TELNYX_API_KEY);

  // Create a dynamic credential for this session
  const credential = await telnyx.telephonyCredentials.create({
    connection_id: process.env.TELNYX_CONNECTION_ID,
    name: `session-${req.user.id}-${Date.now()}`
  });

  // Generate JWT token from the credential
  const tokenResponse = await telnyx.telephonyCredentials.createToken(
    credential.data.id
  );

  // CRITICAL: return .data, not the raw response
  res.json({ token: tokenResponse.data });
});
```

### Environment Variables Mapping

| Twilio | Telnyx | Notes |
|---|---|---|
| `TWILIO_ACCOUNT_SID` | `TELNYX_API_KEY` | Bearer token, not Basic Auth |
| `TWILIO_API_SECRET` | *(not needed)* | Single key for auth |
| `TWILIO_TWIML_APP_SID` | `TELNYX_CONNECTION_ID` | SIP Connection ID |
| `TWILIO_CALLER_ID` | `TELNYX_PHONE_NUMBER` | Must be in Outbound Voice Profile |
| *(none)* | `TELNYX_CREDENTIAL_ID` | For SIP credential auth |

> **Enhanced coverage**: The `telnyx-webrtc-*` skills (in language plugins) and `telnyx-oauth-*` skills provide complete credential CRUD examples.

## Platform-Specific Guides

> **Enhanced coverage**: Install the `telnyx-webrtc-client` plugin for comprehensive platform-specific implementation guides:
>
> - **JavaScript/Browser**: `telnyx-webrtc-client-js` — Full browser WebRTC with media handling, codec configuration, quality metrics, debugging
> - **iOS/Swift**: `telnyx-webrtc-client-ios` — CallKit integration, APNs push notifications, background audio
> - **Android/Kotlin**: `telnyx-webrtc-client-android` — FCM push notifications, Telecom framework, foreground services, custom SIP headers
> - **Flutter/Dart**: `telnyx-webrtc-client-flutter` — Cross-platform with platform channel integration, custom headers
> - **React Native/TypeScript**: `telnyx-webrtc-client-react-native` — Unified JS API with native modules

These skills cover authentication options, event handling, call controls, quality metrics, and debugging patterns for each platform.

## Contact Center / PBX Patterns

These patterns apply when migrating Twilio-based contact centers, PBX systems, or multi-party call applications. They address architectural differences that are unique to Telnyx.

### Conferences Are Not Always Necessary

**Twilio pattern**: Conferences are required for any scenario with more than 2 call legs or where you need supervisor features (listen, whisper, barge). Even simple call transfers often use conferences.

**Telnyx pattern**: Conferences are only needed for true multi-party audio (3+ participants). For two-party calls with supervisor features, use `<Dial>` with `supervisorRole`:

```javascript
// Twilio: requires conference for supervisor
// Supervisor joins a conference room where the agent and customer are already connected

// Telnyx: supervisor via Dial — no conference needed for 2-party monitoring
await telnyx.calls.update(supervisorCallId, {
  supervisor_role: 'barge'  // 'whisper' | 'barge' | 'monitor'
});
```

**When you DO need conferences on Telnyx:**
- 3+ participants need to hear each other
- Dynamic participant management (add/remove callers)
- Conference recording with mixed audio

**When you DON'T need conferences (use bridge/dial instead):**
- Simple call transfers
- Two-party calls with supervisor monitoring
- Warm transfers (bridge, then drop the transferring agent)

> **Enhanced coverage**: The `telnyx-voice-conferencing-*` skills cover conference CRUD, participant management (with `supervisor_role`, `whisper_call_control_ids`, `mute`, `hold`), recording, and all webhook payload schemas. The `telnyx-voice-advanced-*` skills cover `switchSupervisorRole()` and `client_state` on all commands.

### Passing Data from WebRTC Client to Voice API Backend

**Problem**: The WebRTC SDK's `client_state` parameter on `newCall()` does NOT propagate to the Call Control API webhook. This is a common surprise for Twilio migrants who expect data set on the client to appear in server webhooks.

**Solution**: Use custom SIP headers to pass data from the WebRTC client to your backend:

```javascript
// Client-side: pass custom data via SIP headers
const call = client.newCall({
  destinationNumber: '+15559876543',
  callerNumber: '+15551234567',
  customHeaders: [
    { name: 'X-Account-Id', value: '12345' },
    { name: 'X-User-Tier', value: 'premium' },
    { name: 'X-Department', value: 'sales' }
  ]
});
```

```javascript
// Server-side: read custom headers from the webhook
app.post('/webhook', (req, res) => {
  const event = req.body.data;
  const sipHeaders = event.payload.sip_headers || [];

  // Headers arrive as array of {name, value} objects
  const accountId = sipHeaders.find(h => h.name === 'X-Account-Id')?.value;
  const userTier = sipHeaders.find(h => h.name === 'X-User-Tier')?.value;

  // Route based on custom data
  if (userTier === 'premium') {
    // Priority routing
  }
});
```

Custom headers prefixed with `X-` are passed through to Call Control webhooks. This enables:
- Account/user identification without a database lookup
- Priority routing based on client-side context
- Department-based call routing
- Custom metadata for analytics

> **Enhanced coverage**: The `telnyx-webrtc-client-android` and `telnyx-webrtc-client-flutter` skills show custom header examples with template variable mapping (`{{variable_name}}`).

### URI Dialing

To enable dialing SIP URIs (not just PSTN numbers) from WebRTC clients, enable URI dialing on the SIP connection:

```bash
curl -X PATCH "https://api.telnyx.com/v2/credential_connections/YOUR_CONN_ID" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sip_uri_calling_preference": "unrestricted"}'
```

Then dial SIP URIs from the client:
```javascript
const call = client.newCall({
  destinationNumber: 'sip:agent@my-company.sip.telnyx.com'
});
```

Settings for `sip_uri_calling_preference`:
- `disabled` — only PSTN dialing allowed (default)
- `unrestricted` — dial any SIP URI
- `internal` — only dial URIs within your Telnyx connections

### Call Parking and Outbound Call Handling

**Call parking** on Telnyx works through the Call Control API `park` command, not through conferences:

```javascript
// Park a call (puts caller on hold music)
await telnyx.calls.park(callControlId, {
  park_timeout: 300  // seconds before auto-hangup
});

// Retrieve (unpark) by bridging to the parked call
await telnyx.calls.bridge(newCallControlId, {
  call_control_id: parkedCallControlId
});
```

**Outbound call handling** — for progressive/predictive dialer patterns:
```javascript
// Initiate outbound call
const { data: call } = await telnyx.calls.create({
  connection_id: process.env.TELNYX_CONNECTION_ID,
  to: '+15559876543',
  from: '+15551234567',
  webhook_url: 'https://your-server.com/outbound-events'
});

// When answered, bridge to the waiting agent's WebRTC call
// Use bridge_on_answer for automatic bridging (see voice-migration.md)
```

> **Enhanced coverage**: The `telnyx-voice-conferencing-*` skills document `leave()` (returns to parked state), `join()` (with `supervisor_role`, `whisper_call_control_ids`), and all conference actions with optional params and webhook payload schemas. The `telnyx-voice-*` skills cover dial (with `bridge_on_answer`, `link_to`, `park_after_unbridge`, `supervisor_role`, `sip_headers`, `custom_headers`) and bridge operations — all with complete optional parameter lists and webhook field tables.
