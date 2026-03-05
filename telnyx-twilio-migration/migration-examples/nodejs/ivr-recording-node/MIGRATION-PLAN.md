# Migration Plan: Twilio to Telnyx

## Project: ivr-recording-node

### Scope
- **Product**: Voice/IVR with Recording
- **Framework**: Node.js/Express
- **Migration Strategy**: TeXML (TwiML-compatible)

### Files Migrated
1. `routes/ivr.js` - Welcome IVR handler
2. `routes/menu.js` - Menu selection handler
3. `routes/extension.js` - Extension connection handler
4. `routes/agents.js` - Agent call handling and recording
5. `routes/recordings.js` - Recording webhook handler (updated for Telnyx format)
6. `README.md` - Documentation updated
7. `.env.example` - Environment variables updated

### Key Changes
- `twilio` SDK → `telnyx` SDK
- `twilio.twiml.VoiceResponse` → `Telnyx.TeXML.VoiceResponse`
- `twilio.webhook({validate: false})` middleware removed (signature validation optional)
- Voice attribute: `'Polly.Amy'` → `'Polly.Amy-Neural'`
- Added `channels: 'single'` to `<Record>` verb

### Environment Variables
| Old (Twilio) | New (Telnyx) |
|--------------|--------------|
| TWILIO_ACCOUNT_SID | TELNYX_API_KEY |
| TWILIO_AUTH_TOKEN | Not needed |
| TWILIO_PHONE_NUMBER | TELNYX_PHONE_NUMBER |
| - | TELNYX_CONNECTION_ID |

### Testing Plan
1. Unit tests in `spec/` need updating (remove Twilio signature headers)
2. Integration tests: Place actual call to test IVR flow and recording

### Deployment Checklist
- [ ] Set up TeXML Application in Telnyx Mission Control
- [ ] Configure phone number webhook URL
- [ ] Update environment variables in production
- [ ] Test recording download (URLs expire in 10 minutes)
