---
name: telnyx-webrtc-ios
description: >-
  Build VoIP calling apps on iOS using Telnyx WebRTC SDK. Covers authentication,
  making/receiving calls, CallKit integration, PushKit/APNS push notifications,
  call quality metrics, and AI Agent integration. Use when implementing real-time
  voice communication on iOS.
metadata:
  author: telnyx
  product: webrtc
  language: swift
  platform: ios
---

# Telnyx WebRTC - iOS SDK

Build real-time voice communication into iOS applications using Telnyx WebRTC.

> **Prerequisites**: Create WebRTC credentials and generate a login token using the Telnyx server-side SDK. See the `telnyx-webrtc-*` skill in your server language plugin (e.g., `telnyx-python`, `telnyx-javascript`).

## Installation

### CocoaPods

```ruby
pod 'TelnyxRTC', '~> 0.1.0'
```

Then run:

```bash
pod install --repo-update
```

### Swift Package Manager

1. In Xcode: File → Add Packages
2. Enter: `https://github.com/team-telnyx/telnyx-webrtc-ios.git`
3. Select the `main` branch

## Project Configuration

1. **Disable Bitcode**: Build Settings → "Bitcode" → Set to "NO"

2. **Enable Background Modes**: Signing & Capabilities → +Capability → Background Modes:
   - Voice over IP
   - Audio, AirPlay, and Picture in Picture

3. **Microphone Permission**: Add to `Info.plist`:
   ```xml
   <key>NSMicrophoneUsageDescription</key>
   <string>Microphone access required for VoIP calls</string>
   ```

---

## Authentication

### Option 1: Credential-Based Login

```swift
import TelnyxRTC

let telnyxClient = TxClient()
telnyxClient.delegate = self

let txConfig = TxConfig(
    sipUser: "your_sip_username",
    password: "your_sip_password",
    pushDeviceToken: "DEVICE_APNS_TOKEN",
    ringtone: "incoming_call.mp3",
    ringBackTone: "ringback_tone.mp3",
    logLevel: .all
)

do {
    try telnyxClient.connect(txConfig: txConfig)
} catch {
    print("Connection error: \(error)")
}
```

### Option 2: Token-Based Login (JWT)

```swift
let txConfig = TxConfig(
    token: "your_jwt_token",
    pushDeviceToken: "DEVICE_APNS_TOKEN",
    ringtone: "incoming_call.mp3",
    ringBackTone: "ringback_tone.mp3",
    logLevel: .all
)

try telnyxClient.connect(txConfig: txConfig)
```

### Configuration Options

| Parameter | Type | Description |
|-----------|------|-------------|
| `sipUser` / `token` | String | Credentials from Telnyx Portal |
| `password` | String | SIP password (credential auth) |
| `pushDeviceToken` | String? | APNS VoIP push token |
| `ringtone` | String? | Audio file for incoming calls |
| `ringBackTone` | String? | Audio file for ringback |
| `logLevel` | LogLevel | .none, .error, .warning, .debug, .info, .all |
| `forceRelayCandidate` | Bool | Force TURN relay (avoid local network) |

### Region Selection

```swift
let serverConfig = TxServerConfiguration(
    environment: .production,
    region: .usEast  // .auto, .usEast, .usCentral, .usWest, .caCentral, .eu, .apac
)

try telnyxClient.connect(txConfig: txConfig, serverConfiguration: serverConfig)
```

---

## Client Delegate

Implement `TxClientDelegate` to receive events:

```swift
extension ViewController: TxClientDelegate {
    
    func onSocketConnected() {
        // Connected to Telnyx backend
    }
    
    func onSocketDisconnected() {
        // Disconnected from backend
    }
    
    func onClientReady() {
        // Ready to make/receive calls
    }
    
    func onClientError(error: Error) {
        // Handle error
    }
    
    func onIncomingCall(call: Call) {
        // Incoming call while app is in foreground
        self.currentCall = call
    }
    
    func onPushCall(call: Call) {
        // Incoming call from push notification
        self.currentCall = call
    }
    
    func onCallStateUpdated(callState: CallState, callId: UUID) {
        switch callState {
        case .CONNECTING:
            break
        case .RINGING:
            break
        case .ACTIVE:
            break
        case .HELD:
            break
        case .DONE(let reason):
            if let reason = reason {
                print("Call ended: \(reason.cause ?? "Unknown")")
                print("SIP: \(reason.sipCode ?? 0) \(reason.sipReason ?? "")")
            }
        case .RECONNECTING(let reason):
            print("Reconnecting: \(reason.rawValue)")
        case .DROPPED(let reason):
            print("Dropped: \(reason.rawValue)")
        }
    }
}
```

---

## Making Outbound Calls

```swift
let call = try telnyxClient.newCall(
    callerName: "John Doe",
    callerNumber: "+15551234567",
    destinationNumber: "+18004377950",
    callId: UUID()
)
```

---

## Receiving Inbound Calls

```swift
func onIncomingCall(call: Call) {
    // Store reference and show UI
    self.currentCall = call
    
    // Answer the call
    call.answer()
}
```

---

## Call Controls

```swift
// End call
call.hangup()

// Mute/Unmute
call.muteAudio()
call.unmuteAudio()

// Hold/Unhold
call.hold()
call.unhold()

// Send DTMF
call.dtmf(digit: "1")

// Toggle speaker
// (Use AVAudioSession for speaker routing)
```

---

## Push Notifications (PushKit + CallKit)

### 1. Configure PushKit

```swift
import PushKit

class AppDelegate: UIResponder, UIApplicationDelegate, PKPushRegistryDelegate {
    
    private var pushRegistry = PKPushRegistry(queue: .main)
    
    func initPushKit() {
        pushRegistry.delegate = self
        pushRegistry.desiredPushTypes = [.voIP]
    }
    
    func pushRegistry(_ registry: PKPushRegistry, 
                      didUpdate credentials: PKPushCredentials, 
                      for type: PKPushType) {
        if type == .voIP {
            let token = credentials.token.map { String(format: "%02X", $0) }.joined()
            // Save token for use in TxConfig
        }
    }
    
    func pushRegistry(_ registry: PKPushRegistry, 
                      didReceiveIncomingPushWith payload: PKPushPayload, 
                      for type: PKPushType, 
                      completion: @escaping () -> Void) {
        if type == .voIP {
            handleVoIPPush(payload: payload)
        }
        completion()
    }
}
```

### 2. Handle VoIP Push

```swift
func handleVoIPPush(payload: PKPushPayload) {
    guard let metadata = payload.dictionaryPayload["metadata"] as? [String: Any] else { return }
    
    let callId = metadata["call_id"] as? String ?? UUID().uuidString
    let callerName = (metadata["caller_name"] as? String) ?? ""
    let callerNumber = (metadata["caller_number"] as? String) ?? ""
    
    // Reconnect client and process push
    let txConfig = TxConfig(sipUser: sipUser, password: password, pushDeviceToken: token)
    try? telnyxClient.processVoIPNotification(
        txConfig: txConfig, 
        serverConfiguration: serverConfig,
        pushMetaData: metadata
    )
    
    // Report to CallKit (REQUIRED on iOS 13+)
    let callHandle = CXHandle(type: .generic, value: callerNumber)
    let callUpdate = CXCallUpdate()
    callUpdate.remoteHandle = callHandle
    
    provider.reportNewIncomingCall(with: UUID(uuidString: callId)!, update: callUpdate) { error in
        if let error = error {
            print("Failed to report call: \(error)")
        }
    }
}
```

### 3. CallKit Integration

```swift
import CallKit

class AppDelegate: CXProviderDelegate {
    
    var callKitProvider: CXProvider!
    
    func initCallKit() {
        let config = CXProviderConfiguration(localizedName: "TelnyxRTC")
        config.maximumCallGroups = 1
        config.maximumCallsPerCallGroup = 1
        callKitProvider = CXProvider(configuration: config)
        callKitProvider.setDelegate(self, queue: nil)
    }
    
    // CRITICAL: Audio session handling for WebRTC + CallKit
    func provider(_ provider: CXProvider, didActivate audioSession: AVAudioSession) {
        telnyxClient.enableAudioSession(audioSession: audioSession)
    }
    
    func provider(_ provider: CXProvider, didDeactivate audioSession: AVAudioSession) {
        telnyxClient.disableAudioSession(audioSession: audioSession)
    }
    
    func provider(_ provider: CXProvider, perform action: CXAnswerCallAction) {
        // Use SDK method to handle race conditions
        telnyxClient.answerFromCallkit(answerAction: action)
    }
    
    func provider(_ provider: CXProvider, perform action: CXEndCallAction) {
        telnyxClient.endCallFromCallkit(endAction: action)
    }
}
```

---

## Call Quality Metrics

Enable with `debug: true`:

```swift
let call = try telnyxClient.newCall(
    callerName: "John",
    callerNumber: "+15551234567",
    destinationNumber: "+18004377950",
    callId: UUID(),
    debug: true
)

call.onCallQualityChange = { metrics in
    print("MOS: \(metrics.mos)")
    print("Jitter: \(metrics.jitter * 1000) ms")
    print("RTT: \(metrics.rtt * 1000) ms")
    print("Quality: \(metrics.quality.rawValue)")
    
    switch metrics.quality {
    case .excellent, .good:
        // Green indicator
    case .fair:
        // Yellow indicator
    case .poor, .bad:
        // Red indicator
    case .unknown:
        // Gray indicator
    }
}
```

| Quality Level | MOS Range |
|---------------|-----------|
| .excellent | > 4.2 |
| .good | 4.1 - 4.2 |
| .fair | 3.7 - 4.0 |
| .poor | 3.1 - 3.6 |
| .bad | ≤ 3.0 |

---

## AI Agent Integration

### 1. Anonymous Login

```swift
client.anonymousLogin(
    targetId: "your-ai-assistant-id",
    targetType: "ai_assistant"
)
```

### 2. Start Conversation

```swift
// After anonymous login, destination is ignored
let call = client.newInvite(
    callerName: "User",
    callerNumber: "user",
    destinationNumber: "ai-assistant",  // Ignored
    callId: UUID()
)
```

### 3. Receive Transcripts

```swift
let cancellable = client.aiAssistantManager.subscribeToTranscriptUpdates { transcripts in
    for item in transcripts {
        print("\(item.role): \(item.content)")
        // role: "user" or "assistant"
    }
}
```

### 4. Send Text Message

```swift
let success = client.sendAIAssistantMessage("Hello, can you help me?")
```

---

## Custom Logging

```swift
class MyLogger: TxLogger {
    func log(level: LogLevel, message: String) {
        // Send to your logging service
        MyAnalytics.log(level: level, message: message)
    }
}

let txConfig = TxConfig(
    sipUser: sipUser,
    password: password,
    logLevel: .all,
    customLogger: MyLogger()
)
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No audio | Ensure microphone permission granted |
| Push not working | Verify APNS certificate in Telnyx Portal |
| CallKit crash on iOS 13+ | Must report incoming call to CallKit |
| Audio routing issues | Use `enableAudioSession`/`disableAudioSession` in CXProviderDelegate |
| Login fails | Verify SIP credentials in Telnyx Portal |

## Resources

- [Official Documentation](https://developers.telnyx.com/docs/voice/webrtc/ios-sdk)
- [Push Notification Setup](https://developers.telnyx.com/docs/voice/webrtc/ios-sdk/push-notification/portal-setup)
- [GitHub Repository](https://github.com/team-telnyx/telnyx-webrtc-ios)
