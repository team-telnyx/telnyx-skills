---
name: telnyx-webrtc-react-native
description: >-
  Build cross-platform VoIP calling apps with React Native using Telnyx Voice SDK.
  High-level reactive API with automatic lifecycle management, CallKit/ConnectionService
  integration, and push notifications. Use for mobile VoIP apps with minimal setup.
metadata:
  author: telnyx
  product: webrtc
  language: typescript
  platform: react-native
---

# Telnyx WebRTC - React Native SDK

Build real-time voice communication into React Native apps (Android & iOS) using the `@telnyx/react-voice-commons-sdk` library.

> **Prerequisites**: Create WebRTC credentials and generate a login token using the Telnyx server-side SDK. See the `telnyx-webrtc-*` skill in your server language plugin (e.g., `telnyx-python`, `telnyx-javascript`).

## Features

- **Reactive Streams**: RxJS-based state management
- **Automatic Lifecycle**: Background/foreground handling
- **Native Call UI**: CallKit (iOS) and ConnectionService (Android)
- **Push Notifications**: FCM (Android) and APNs/PushKit (iOS)
- **TypeScript Support**: Full type definitions

## Installation

```bash
npm install @telnyx/react-voice-commons-sdk
```

---

## Basic Setup

```tsx
import { TelnyxVoiceApp, createTelnyxVoipClient } from '@telnyx/react-voice-commons-sdk';

// Create VoIP client instance
const voipClient = createTelnyxVoipClient({
  enableAppStateManagement: true,  // Auto background/foreground handling
  debug: true,                     // Enable logging
});

export default function App() {
  return (
    <TelnyxVoiceApp 
      voipClient={voipClient} 
      enableAutoReconnect={false} 
      debug={true}
    >
      <YourAppContent />
    </TelnyxVoiceApp>
  );
}
```

---

## Authentication

### Credential-Based Login

```tsx
import { createCredentialConfig } from '@telnyx/react-voice-commons-sdk';

const config = createCredentialConfig('sip_username', 'sip_password', {
  debug: true,
  pushNotificationDeviceToken: 'your_device_token',
});

await voipClient.login(config);
```

### Token-Based Login (JWT)

```tsx
import { createTokenConfig } from '@telnyx/react-voice-commons-sdk';

const config = createTokenConfig('your_jwt_token', {
  debug: true,
  pushNotificationDeviceToken: 'your_device_token',
});

await voipClient.loginWithToken(config);
```

### Auto-Reconnection

The library automatically stores credentials for seamless reconnection:

```tsx
// Automatically reconnects using stored credentials
const success = await voipClient.loginFromStoredConfig();

if (!success) {
  // No stored auth, show login UI
}
```

---

## Reactive State Management

```tsx
import { useEffect, useState } from 'react';

function CallScreen() {
  const [connectionState, setConnectionState] = useState(null);
  const [calls, setCalls] = useState([]);
  
  useEffect(() => {
    // Subscribe to connection state
    const connSub = voipClient.connectionState$.subscribe((state) => {
      setConnectionState(state);
    });
    
    // Subscribe to active calls
    const callsSub = voipClient.calls$.subscribe((activeCalls) => {
      setCalls(activeCalls);
    });
    
    return () => {
      connSub.unsubscribe();
      callsSub.unsubscribe();
    };
  }, []);
  
  return (/* UI */);
}
```

### Individual Call State

```tsx
useEffect(() => {
  if (call) {
    const sub = call.callState$.subscribe((state) => {
      console.log('Call state:', state);
    });
    return () => sub.unsubscribe();
  }
}, [call]);
```

---

## Making Calls

```tsx
const call = await voipClient.newCall('+18004377950');
```

---

## Receiving Calls

Incoming calls are handled automatically via push notifications and the `TelnyxVoiceApp` wrapper. The native call UI (CallKit/ConnectionService) is displayed automatically.

---

## Call Controls

```tsx
// Answer incoming call
await call.answer();

// Mute/Unmute
await call.mute();
await call.unmute();

// Hold/Unhold
await call.hold();
await call.unhold();

// End call
await call.hangup();

// Send DTMF
await call.dtmf('1');
```

---

## Push Notifications - Android (FCM)

### 1. Place `google-services.json` in project root

### 2. MainActivity Setup

```kotlin
// MainActivity.kt
import com.telnyx.react_voice_commons.TelnyxMainActivity

class MainActivity : TelnyxMainActivity() {
    override fun onHandleIntent(intent: Intent) {
        super.onHandleIntent(intent)
        // Additional intent processing
    }
}
```

### 3. Background Message Handler

```tsx
// index.js or App.tsx
import messaging from '@react-native-firebase/messaging';
import { TelnyxVoiceApp } from '@telnyx/react-voice-commons-sdk';

messaging().setBackgroundMessageHandler(async (remoteMessage) => {
  await TelnyxVoiceApp.handleBackgroundPush(remoteMessage.data);
});
```

---

## Push Notifications - iOS (PushKit)

### AppDelegate Setup

```swift
// AppDelegate.swift
import PushKit
import TelnyxVoiceCommons

@UIApplicationMain
public class AppDelegate: ExpoAppDelegate, PKPushRegistryDelegate {
  
  public override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Initialize VoIP push registration
    TelnyxVoipPushHandler.initializeVoipRegistration()
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
  
  // VoIP Push Token Update
  public func pushRegistry(_ registry: PKPushRegistry, 
                           didUpdate pushCredentials: PKPushCredentials, 
                           for type: PKPushType) {
    TelnyxVoipPushHandler.shared.handleVoipTokenUpdate(pushCredentials, type: type)
  }
  
  // VoIP Push Received
  public func pushRegistry(_ registry: PKPushRegistry, 
                           didReceiveIncomingPushWith payload: PKPushPayload, 
                           for type: PKPushType, 
                           completion: @escaping () -> Void) {
    TelnyxVoipPushHandler.shared.handleVoipPush(payload, type: type, completion: completion)
  }
}
```

> **Note**: CallKit integration is automatically handled by the internal CallBridge component.

---

## Configuration Options

### createTelnyxVoipClient Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `enableAppStateManagement` | boolean | true | Auto background/foreground handling |
| `debug` | boolean | false | Enable debug logging |

### TelnyxVoiceApp Props

| Prop | Type | Description |
|------|------|-------------|
| `voipClient` | TelnyxVoipClient | The VoIP client instance |
| `enableAutoReconnect` | boolean | Auto-reconnect on disconnect |
| `debug` | boolean | Enable debug logging |

---

## Storage Keys (Managed Automatically)

The library manages these AsyncStorage keys internally:

- `@telnyx_username` - SIP username
- `@telnyx_password` - SIP password
- `@credential_token` - JWT token
- `@push_token` - Push notification token

> You don't need to manage these manually.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Double login | Don't call `login()` manually when using `TelnyxVoiceApp` with auto-reconnect |
| Background disconnect | Check `enableAutoReconnect` setting |
| Android push not working | Verify `google-services.json` and MainActivity extends `TelnyxMainActivity` |
| iOS push not working | Ensure AppDelegate implements `PKPushRegistryDelegate` and calls `TelnyxVoipPushHandler` |
| Memory leaks | Unsubscribe from RxJS observables in useEffect cleanup |
| Audio issues | iOS audio handled by CallBridge; Android check ConnectionService |

### Clear Stored Auth (Advanced)

```tsx
import AsyncStorage from '@react-native-async-storage/async-storage';

await AsyncStorage.multiRemove([
  '@telnyx_username',
  '@telnyx_password', 
  '@credential_token',
  '@push_token',
]);
```

---

## Resources

- [Official Documentation](https://developers.telnyx.com/development/webrtc/react-native-sdk)
- [GitHub Repository](https://github.com/team-telnyx/react-native-voice-commons)
- [npm Package](https://www.npmjs.com/package/@telnyx/react-voice-commons-sdk)
