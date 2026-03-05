# Migration Plan: Twilio to Telnyx

## Project Information
- **Project**: account-security-quickstart-spring
- **Language**: Java (Spring Boot)
- **Framework**: Gradle, Spring Boot 3.3.11
- **Migration Date**: 2026-03-05

## Products Detected

### 1. Twilio Verify (Primary)
- **Usage**: Phone number verification via SMS/Voice
- **Files**:
  - `src/main/java/com/twilio/accountsecurity/services/PhoneVerificationService.java`
  - `src/test/groovy/com/twilio/accountsecurity/services/PhoneVerificationServiceSpec.groovy`
- **Migration Strategy**: REST API (no official Telnyx Java SDK)

### 2. Authy (Account Security API)
- **Usage**: Two-factor authentication (2FA), push notifications, soft tokens
- **Files**:
  - `src/main/java/com/twilio/accountsecurity/config/SpringConfiguration.java`
  - `src/main/java/com/twilio/accountsecurity/filters/TwoFAFilter.java`
  - `src/main/java/com/twilio/accountsecurity/services/TokenService.java`
- **Migration Strategy**: Keep on Twilio (no Telnyx equivalent for Authy push/soft tokens)

## Migration Approach

### Strategy: Hybrid Deployment
- **Verify**: Migrate to Telnyx
- **Authy**: Keep on Twilio (unsupported product)

### Phase Order
1. Phase 0: Prerequisites (Complete)
2. Phase 1: Discovery (Complete)
3. Phase 2: Planning (Current)
4. Phase 3: Setup
5. Phase 4: Migration (Verify only)
6. Phase 5: Validation
7. Phase 6: Cleanup

## Environment Variables

| Current (Twilio) | New (Telnyx/Twilio) | Notes |
|------------------|---------------------|-------|
| TWILIO_ACCOUNT_SID | TWILIO_ACCOUNT_SID | Keep for Authy |
| TWILIO_AUTH_TOKEN | TWILIO_AUTH_TOKEN | Keep for Authy |
| TWILIO_VERIFICATION_SID | TELNYX_VERIFY_PROFILE_ID | Migrate to Telnyx |
| ACCOUNT_SECURITY_API_KEY | ACCOUNT_SECURITY_API_KEY | Keep for Authy |

## Code Changes Required

### PhoneVerificationService.java
Replace Twilio Verify SDK with Telnyx REST API calls:
- Remove: `com.twilio.Twilio`, `com.twilio.rest.verify.v2.service.*`
- Add: HTTP client (RestTemplate or WebClient)
- Change: `Verification.creator()` → POST /v2/verifications/sms or /call
- Change: `VerificationCheck.creator()` → POST /v2/verifications/by_phone_number/{phone}/actions/verify
- Change: Status check `approved` → `accepted`

### Settings.java
Add new getter for Telnyx environment variables:
- Add: `getTelnyxVerifyProfileId()`
- Keep: Existing Twilio/Authy getters

### build.gradle
No changes for Telnyx SDK (using REST API), keep Twilio for Authy.

## Testing Plan

1. Unit tests for PhoneVerificationService
2. Integration test with Telnyx Verify API
3. End-to-end verification flow test

## Rollback Plan

Maintain backward compatibility by:
1. Keeping Twilio SDK in dependencies
2. Feature flag for verification provider
3. Environment-based configuration
