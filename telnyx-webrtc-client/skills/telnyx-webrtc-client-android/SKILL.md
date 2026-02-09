---
name: telnyx-webrtc-client-android
description: >-
  Build VoIP calling apps on Android using Telnyx WebRTC SDK. Covers authentication,
  making/receiving calls, push notifications (FCM), call quality metrics, and AI Agent
  integration. Use when implementing real-time voice communication on Android.
metadata:
  author: telnyx
  product: webrtc
  language: kotlin
  platform: android
---

# Telnyx WebRTC - Android SDK

Build real-time voice communication into Android applications using Telnyx WebRTC.

> **Prerequisites**: Create WebRTC credentials and generate a login token using the Telnyx server-side SDK. See the `telnyx-webrtc-*` skill in your server language plugin (e.g., `telnyx-python`, `telnyx-javascript`).

## Installation

Add JitPack repository to your project's `build.gradle`:

```gradle
allprojects {
    repositories {
        maven { url 'https://jitpack.io' }
    }
}
```

Add the dependency:

```gradle
dependencies {
    implementation 'com.github.team-telnyx:telnyx-webrtc-android:latest-version'
}
```

## Required Permissions

Add to `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<!-- For push notifications (Android 14+) -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_PHONE_CALL"/>
```

---

## Authentication

### Option 1: Credential-Based Login

```kotlin
val telnyxClient = TelnyxClient(context)
telnyxClient.connect()

val credentialConfig = CredentialConfig(
    sipUser = "your_sip_username",
    sipPassword = "your_sip_password",
    sipCallerIDName = "Display Name",
    sipCallerIDNumber = "+15551234567",
    fcmToken = fcmToken,  // Optional: for push notifications
    logLevel = LogLevel.DEBUG,
    autoReconnect = true
)

telnyxClient.credentialLogin(credentialConfig)
```

### Option 2: Token-Based Login (JWT)

```kotlin
val tokenConfig = TokenConfig(
    sipToken = "your_jwt_token",
    sipCallerIDName = "Display Name",
    sipCallerIDNumber = "+15551234567",
    fcmToken = fcmToken,
    logLevel = LogLevel.DEBUG,
    autoReconnect = true
)

telnyxClient.tokenLogin(tokenConfig)
```

### Configuration Options

| Parameter | Type | Description |
|-----------|------|-------------|
| `sipUser` / `sipToken` | String | Credentials from Telnyx Portal |
| `sipCallerIDName` | String? | Caller ID name displayed to recipients |
| `sipCallerIDNumber` | String? | Caller ID number |
| `fcmToken` | String? | Firebase Cloud Messaging token for push |
| `ringtone` | Any? | Raw resource ID or URI for ringtone |
| `ringBackTone` | Int? | Raw resource ID for ringback tone |
| `logLevel` | LogLevel | NONE, ERROR, WARNING, DEBUG, INFO, ALL |
| `autoReconnect` | Boolean | Auto-retry login on failure (3 attempts) |
| `region` | Region | AUTO, US_EAST, US_WEST, EU_WEST |

---

## Making Outbound Calls

```kotlin
// Create a new outbound call
telnyxClient.call.newInvite(
    callerName = "John Doe",
    callerNumber = "+15551234567",
    destinationNumber = "+15559876543",
    clientState = "my-custom-state"
)
```

---

## Receiving Inbound Calls

Listen for socket events using SharedFlow (recommended):

```kotlin
lifecycleScope.launch {
    telnyxClient.socketResponseFlow.collect { response ->
        when (response.status) {
            SocketStatus.ESTABLISHED -> {
                // Socket connected
            }
            SocketStatus.MESSAGERECEIVED -> {
                response.data?.let { data ->
                    when (data.method) {
                        SocketMethod.CLIENT_READY.methodName -> {
                            // Ready to make/receive calls
                        }
                        SocketMethod.LOGIN.methodName -> {
                            // Successfully logged in
                        }
                        SocketMethod.INVITE.methodName -> {
                            // Incoming call!
                            val invite = data.result as InviteResponse
                            // Show incoming call UI, then accept:
                            telnyxClient.acceptCall(
                                invite.callId,
                                invite.callerIdNumber
                            )
                        }
                        SocketMethod.ANSWER.methodName -> {
                            // Call was answered
                        }
                        SocketMethod.BYE.methodName -> {
                            // Call ended
                        }
                        SocketMethod.RINGING.methodName -> {
                            // Remote party is ringing
                        }
                    }
                }
            }
            SocketStatus.ERROR -> {
                // Handle error: response.errorCode
            }
            SocketStatus.DISCONNECT -> {
                // Socket disconnected
            }
        }
    }
}
```

---

## Call Controls

```kotlin
// Get current call
val currentCall: Call? = telnyxClient.calls[callId]

// End call
currentCall?.endCall(callId)

// Mute/Unmute
currentCall?.onMuteUnmutePressed()

// Hold/Unhold
currentCall?.onHoldUnholdPressed(callId)

// Send DTMF tone
currentCall?.dtmf(callId, "1")
```

### Handling Multiple Calls

```kotlin
// Get all active calls
val calls: Map<UUID, Call> = telnyxClient.calls

// Iterate through calls
calls.forEach { (callId, call) ->
    // Handle each call
}
```

---

## Push Notifications (FCM)

### 1. Setup Firebase

Add Firebase to your project and get an FCM token:

```kotlin
FirebaseMessaging.getInstance().token.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        val fcmToken = task.result
        // Use this token in your login config
    }
}
```

### 2. Handle Incoming Push

In your `FirebaseMessagingService`:

```kotlin
class MyFirebaseService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        val params = remoteMessage.data
        val metadata = JSONObject(params as Map<*, *>).getString("metadata")
        
        // Check for missed call
        if (params["message"] == "Missed call!") {
            // Show missed call notification
            return
        }
        
        // Show incoming call notification (use Foreground Service)
        showIncomingCallNotification(metadata)
    }
}
```

### 3. Decline Push Call (Simplified)

```kotlin
// The SDK now handles decline automatically
telnyxClient.connectWithDeclinePush(
    txPushMetaData = pushMetaData,
    credentialConfig = credentialConfig
)
// SDK connects, sends decline, and disconnects automatically
```

### Android 14+ Requirements

```xml
<service
    android:name=".YourForegroundService"
    android:foregroundServiceType="phoneCall"
    android:exported="true" />
```

---

## Call Quality Metrics

Enable metrics to monitor call quality in real-time:

```kotlin
val credentialConfig = CredentialConfig(
    // ... other config
    debug = true  // Enables call quality metrics
)

// Listen for quality updates
lifecycleScope.launch {
    currentCall?.callQualityFlow?.collect { metrics ->
        println("MOS: ${metrics.mos}")
        println("Jitter: ${metrics.jitter * 1000} ms")
        println("RTT: ${metrics.rtt * 1000} ms")
        println("Quality: ${metrics.quality}")  // EXCELLENT, GOOD, FAIR, POOR, BAD
    }
}
```

| Quality Level | MOS Range |
|---------------|-----------|
| EXCELLENT | > 4.2 |
| GOOD | 4.1 - 4.2 |
| FAIR | 3.7 - 4.0 |
| POOR | 3.1 - 3.6 |
| BAD | ≤ 3.0 |

---

## AI Agent Integration

Connect to a Telnyx Voice AI Agent without traditional SIP credentials:

### 1. Anonymous Login

```kotlin
telnyxClient.connectAnonymously(
    targetId = "your_ai_assistant_id",
    targetType = "ai_assistant",  // Default
    targetVersionId = "optional_version_id",
    userVariables = mapOf("user_id" to "12345")
)
```

### 2. Start Conversation

```kotlin
// After anonymous login, call the AI Agent
telnyxClient.newInvite(
    callerName = "User Name",
    callerNumber = "+15551234567",
    destinationNumber = "",  // Ignored for AI Agent
    clientState = "state",
    customHeaders = mapOf(
        "X-Account-Number" to "123",  // Maps to {{account_number}}
        "X-User-Tier" to "premium"    // Maps to {{user_tier}}
    )
)
```

### 3. Receive Transcripts

```kotlin
lifecycleScope.launch {
    telnyxClient.transcriptUpdateFlow.collect { transcript ->
        transcript.forEach { item ->
            println("${item.role}: ${item.content}")
            // role: "user" or "assistant"
        }
    }
}
```

### 4. Send Text to AI Agent

```kotlin
// Send text message during active call
telnyxClient.sendAIAssistantMessage("Hello, I need help with my account")
```

---

## Custom Logging

Implement your own logger:

```kotlin
class MyLogger : TxLogger {
    override fun log(level: LogLevel, tag: String?, message: String, throwable: Throwable?) {
        // Send to your logging service
        MyAnalytics.log(level.name, tag ?: "Telnyx", message)
    }
}

val config = CredentialConfig(
    // ... other config
    logLevel = LogLevel.ALL,
    customLogger = MyLogger()
)
```

---

## ProGuard Rules

If using code obfuscation, add to `proguard-rules.pro`:

```proguard
-keep class com.telnyx.webrtc.** { *; }
-dontwarn kotlin.Experimental$Level
-dontwarn kotlin.Experimental
-dontwarn kotlinx.coroutines.scheduling.ExperimentalCoroutineDispatcher
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No audio | Check RECORD_AUDIO permission is granted |
| Push not received | Verify FCM token is passed in config |
| Login fails | Verify SIP credentials in Telnyx Portal |
| Call drops | Check network stability, enable `autoReconnect` |
| sender_id_mismatch (push) | FCM project mismatch - ensure app's `google-services.json` matches server credentials |

## Resources

- [Official Documentation](https://developers.telnyx.com/docs/voice/webrtc/android-sdk/quickstart)
- [Push Notification Setup](https://developers.telnyx.com/docs/voice/webrtc/android-sdk/push-notification/portal-setup)
- [GitHub Repository](https://github.com/team-telnyx/telnyx-webrtc-android)
