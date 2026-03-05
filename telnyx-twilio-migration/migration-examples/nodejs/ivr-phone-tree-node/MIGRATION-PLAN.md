# Migration Plan: IVR Phone Tree (Twilio → Telnyx)

## Project Overview
- **Repository:** ivr-phone-tree-node
- **Language:** JavaScript (Node.js/Express)
- **Product:** Voice (TwiML-based IVR)
- **Migration Approach:** TeXML (drop-in replacement for TwiML)

## Migration Scope

### Files to Migrate
1. `src/ivr/handler.js` - Core IVR logic using VoiceResponse
2. `src/router.js` - Webhook middleware using twilio.webhook()
3. `package.json` - Dependencies

### Key Changes
1. **Voice Builder → Raw XML**: Replace `VoiceResponse` class with raw TeXML string generation
2. **Webhook Middleware**: Replace `twilio.webhook()` with Telnyx Ed25519 signature validation
3. **Polly Voices**: Update to use `Polly.Amy-Neural` (Neural variant preferred)
4. **Dependencies**: Add `telnyx` SDK alongside `twilio`

### Migration Strategy: Big-bang
- Only 2-3 files with Twilio code
- Single product (voice)
- Simple IVR flow

## Action Items
- [ ] Create migration branch
- [ ] Install Telnyx SDK
- [ ] Update environment variables
- [ ] Migrate handler.js (VoiceResponse → raw XML)
- [ ] Migrate router.js (remove twilio.webhook, add Telnyx signature validation)
- [ ] Update tests
- [ ] Validate migration
- [ ] Run integration tests
