---
name: telnyx-webrtc-client-js
description: >-
  Build browser-based VoIP calling apps using Telnyx WebRTC JavaScript SDK.
  Covers authentication, voice calls, events, debugging, call quality
  metrics, and AI Agent integration. Use for web-based real-time communication.
metadata:
  author: telnyx
  product: webrtc
  language: javascript
  platform: browser
---

# Telnyx WebRTC - JavaScript SDK

Build real-time voice communication into browser applications.

> **Prerequisites**: Create WebRTC credentials and generate a login token using the Telnyx server-side SDK. See the `telnyx-webrtc-*` skill in your server language plugin (e.g., `telnyx-python`, `telnyx-javascript`).

## Installation

```bash
npm install @telnyx/webrtc --save
```

Import the client:

```js
import { TelnyxRTC } from '@telnyx/webrtc';
```

---

## Authentication

### Option 1: Token-Based (Recommended)

```js
const client = new TelnyxRTC({
  login_token: 'your_jwt_token',
});

client.connect();
```

### Option 2: Credential-Based

```js
const client = new TelnyxRTC({
  login: 'sip_username',
  password: 'sip_password',
});

client.connect();
```

> **Important**: Never hardcode credentials in frontend code. Use environment variables or prompt users.

### Disconnect

```js
// When done, disconnect and remove listeners
client.disconnect();
client.off('telnyx.ready');
client.off('telnyx.notification');
```

---

## Media Elements

Specify an HTML element to play remote audio:

```js
client.remoteElement = 'remoteMedia';
```

HTML:

```html
<audio id="remoteMedia" autoplay="true" />
```

---

## Events

```js
let activeCall;

client
  .on('telnyx.ready', () => {
    console.log('Ready to make calls');
  })
  .on('telnyx.error', (error) => {
    console.error('Error:', error);
  })
  .on('telnyx.notification', (notification) => {
    if (notification.type === 'callUpdate') {
      activeCall = notification.call;
      
      // Handle incoming call
      if (activeCall.state === 'ringing') {
        // Show incoming call UI
        // Call activeCall.answer() to accept
      }
    }
  });
```

### Event Types

| Event | Description |
|-------|-------------|
| `telnyx.ready` | Client connected and ready |
| `telnyx.error` | Error occurred |
| `telnyx.notification` | Call updates, incoming calls |
| `telnyx.stats.frame` | In-call quality metrics (when debug enabled) |

---

## Making Calls

```js
const call = client.newCall({
  destinationNumber: '+18004377950',
  callerNumber: '+15551234567',
});
```

---

## Receiving Calls

```js
client.on('telnyx.notification', (notification) => {
  const call = notification.call;
  
  if (notification.type === 'callUpdate' && call.state === 'ringing') {
    // Incoming call - show UI and answer
    call.answer();
  }
});
```

---

## Call Controls

```js
// End call
call.hangup();

// Send DTMF tones
call.dtmf('1234');

// Mute audio
call.muteAudio();
call.unmuteAudio();

// Hold
call.hold();
call.unhold();
```

---

## Debugging & Call Quality

### Enable Debug Logging

```js
const call = client.newCall({
  destinationNumber: '+18004377950',
  debug: true,
  debugOutput: 'socket',  // 'socket' (send to Telnyx) or 'file' (save locally)
});
```

### In-Call Quality Metrics

```js
const call = client.newCall({
  destinationNumber: '+18004377950',
  debug: true,  // Required for metrics
});

client.on('telnyx.stats.frame', (stats) => {
  console.log('Quality stats:', stats);
  // Contains jitter, RTT, packet loss, etc.
});
```

---

## Pre-Call Diagnosis

Test connectivity before making calls:

```js
import { PreCallDiagnosis } from '@telnyx/webrtc';

PreCallDiagnosis.run({
  credentials: {
    login: 'sip_username',
    password: 'sip_password',
    // or: loginToken: 'jwt_token'
  },
  texMLApplicationNumber: '+12407758982',
})
  .then((report) => {
    console.log('Diagnosis report:', report);
  })
  .catch((error) => {
    console.error('Diagnosis failed:', error);
  });
```

---

## Preferred Codecs

Set codec preference for calls:

```js
const allCodecs = RTCRtpReceiver.getCapabilities('audio').codecs;

// Prefer Opus for AI/high quality
const opusCodec = allCodecs.find(c => 
  c.mimeType.toLowerCase().includes('opus')
);

// Or PCMA for telephony compatibility
const pcmaCodec = allCodecs.find(c => 
  c.mimeType.toLowerCase().includes('pcma')
);

client.newCall({
  destinationNumber: '+18004377950',
  preferred_codecs: [opusCodec],
});
```

---

## Registration State

Check if client is registered:

```js
const isRegistered = await client.getIsRegistered();
console.log('Registered:', isRegistered);
```

---

## AI Agent Integration

### Anonymous Login

Connect to an AI assistant without SIP credentials:

```js
const client = new TelnyxRTC({
  anonymous_login: {
    target_id: 'your-ai-assistant-id',
    target_type: 'ai_assistant',
  },
});

client.connect();
```

> **Note**: The AI assistant must have `telephony_settings.supports_unauthenticated_web_calls` set to `true`.

### Make Call to AI Assistant

```js
// After anonymous login, destinationNumber is ignored
const call = client.newCall({
  destinationNumber: '',  // Can be empty
  remoteElement: 'remoteMedia',
});
```

### Recommended Codec for AI

```js
const allCodecs = RTCRtpReceiver.getCapabilities('audio').codecs;
const opusCodec = allCodecs.find(c => 
  c.mimeType.toLowerCase().includes('opus')
);

client.newCall({
  destinationNumber: '',
  preferred_codecs: [opusCodec],  // Opus recommended for AI
});
```

---

## Browser Support

| Platform | Chrome | Firefox | Safari | Edge |
|----------|--------|---------|--------|------|
| Android | ✓ | ✓ | - | - |
| iOS | - | - | ✓ | - |
| Linux | ✓ | ✓ | - | - |
| macOS | ✓ | ✓ | ✓ | ✓ |
| Windows | ✓ | ✓ | - | ✓ |

### Check Browser Support

```js
const webRTCInfo = TelnyxRTC.webRTCInfo;
console.log('WebRTC supported:', webRTCInfo.supportWebRTC);
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No audio | Check microphone permissions in browser |
| Echo/feedback | Use headphones or enable echo cancellation |
| Connection fails | Check network, firewall, or use TURN relay |
| Quality issues | Enable `debug: true` and check `telnyx.stats.frame` events |

---

## Resources

- [Official Documentation](https://developers.telnyx.com/development/webrtc/js-sdk/quickstart)
- [npm Package](https://www.npmjs.com/package/@telnyx/webrtc)
- [GitHub Repository](https://github.com/team-telnyx/webrtc)
- [Demo App](https://github.com/team-telnyx/webrtc-demo-js)
