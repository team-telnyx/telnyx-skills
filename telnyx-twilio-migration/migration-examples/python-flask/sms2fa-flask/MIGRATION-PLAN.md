# Migration Plan: Twilio to Telnyx

## Summary

This project is a Flask-based SMS 2FA application. The migration involves moving from Twilio Programmable Messaging to Telnyx Messaging API for sending SMS verification codes.

## Scan Results

- **Languages**: Python
- **Products Detected**: Messaging (SMS)
- **Files with Twilio patterns**: 
  - `requirements.txt` - twilio==6.9.0 dependency
  - `.env.example` - TWILIO_* environment variables
  - `sms2fa_flask/config.py` - TWILIO_* configuration
  - `.travis.yml` - CI/CD environment variables

## Migration Strategy

**Approach**: Big-bang (single product, few files)
**Order**: messaging only

## Changes Required

### 1. Dependencies
- Remove: `twilio==6.9.0`
- Keep: `telnyx>=2.0,<3.0` (already present)

### 2. Environment Variables
| Twilio | Telnyx | Status |
|--------|--------|--------|
| TWILIO_ACCOUNT_SID | TELNYX_API_KEY | ✅ Already added |
| TWILIO_AUTH_TOKEN | TELNYX_PUBLIC_KEY | ⚠️ Add for webhook validation |
| TWILIO_NUMBER | TELNYX_PHONE_NUMBER | ✅ Already added |
| - | TELNYX_MESSAGING_PROFILE_ID | ⚠️ Add for messaging |

### 3. Code Changes
- `sms2fa_flask/confirmation_sender.py`: Already migrated to Telnyx
- `sms2fa_flask/config.py`: Already has Telnyx config
- Tests already updated for Telnyx

### 4. Post-Migration
- Remove Twilio from requirements.txt
- Update documentation
- Run integration tests
