---
name: telnyx-twilio-migration
description: >-
  Migrate from Twilio to Telnyx. Orchestrates a complete 6-phase migration:
  discovery, planning, setup, code migration, validation, and cleanup.
  Covers voice (TwiML to TeXML, Call Control API), messaging, WebRTC,
  SIP trunking, verify, fax, video, IoT, number lookup, and porting.
  Includes automated scanners, validation scripts, and integration tests.
metadata:
  author: telnyx
  product: migration
---

# Twilio to Telnyx Migration

Orchestrate a complete migration from Twilio to Telnyx. This skill drives a 6-phase workflow: scan the user's codebase, plan the migration, swap SDKs and config, transform code file-by-file, validate the result, and generate a migration report.

> **Standalone skill**: Fully self-contained. For deeper SDK-specific code examples, install the relevant language plugin (`telnyx-python`, `telnyx-javascript`, `telnyx-go`, `telnyx-java`, `telnyx-ruby`, or `telnyx-curl`). For client-side WebRTC, install `telnyx-webrtc-client`.

> **SDK reference files**: This skill includes auto-extracted SDK reference docs for 27 products × 6 languages in `{baseDir}/sdk-reference/`. Regenerate with `bash {baseDir}/scripts/extract-sdk-reference.sh`.

## Quick Product Mapping

| Twilio Product | Telnyx Equivalent | Complexity | Reference File |
|---|---|---|---|
| Programmable Voice (TwiML) | TeXML | Low | `voice-migration.md` |
| Programmable Voice (REST) | Call Control API | Medium | `voice-migration.md` |
| Programmable Messaging | Messaging API | Medium | `messaging-migration.md` |
| Elastic SIP Trunking | SIP Connections | Low | `sip-trunking-migration.md` |
| Voice SDK (WebRTC) | WebRTC SDKs | Medium | `webrtc-migration.md` |
| Phone Numbers | Number Management | Low | *(SDK reference)* |
| Twilio Verify | Verify API | Medium | `verify-migration.md` |
| Twilio Lookup | Number Lookup | Low | `lookup-migration.md` |
| Twilio Video (retired) | Video Rooms API | Medium | `video-migration.md` |
| Twilio Fax (deprecated) | Programmable Fax | Low | `fax-migration.md` |
| Super SIM / IoT | IoT SIM Cards | Medium | `iot-migration.md` |
| 10DLC Registration | 10DLC Campaign Registry | Low | `messaging-migration.md` |
| Number Porting | FastPort | Low | `number-porting.md` |

Full mapping with Telnyx-only products and unsupported Twilio products: `{baseDir}/references/product-mapping.md`

## Universal Changes (All Migrations)

These changes apply regardless of which Twilio product you're migrating.

### 1. Authentication

```bash
# Twilio: Basic Auth (AccountSID:AuthToken)
curl -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" https://api.twilio.com/...

# Telnyx: Bearer Token (API Key v2)
curl -H "Authorization: Bearer $TELNYX_API_KEY" https://api.telnyx.com/v2/...
```

Get your API key at https://portal.telnyx.com/#/app/api-keys

### 2. Webhook Signatures: HMAC-SHA1 → Ed25519

Get your public key at https://portal.telnyx.com/#/app/account/public-key

### 3. Webhook Payloads: Flat → Nested

Twilio sends flat key-value pairs. Telnyx nests event data under `data.payload`:

```json
{"data": {"event_type": "message.received", "payload": {"from": {"phone_number": "+1..."}, "text": "Hello"}}}
```

### 4. Recording Defaults: Single → Dual Channel

Telnyx defaults to dual-channel. Set `channels="single"` to match Twilio behavior.

---

## Phase 1: Discovery

Scan the codebase and validate the Telnyx account is ready.

### Step 1.1: Preflight Check

```bash
bash {baseDir}/scripts/preflight-check.sh <project-root>
```

Validates: API key, account balance, phone number inventory, voice connections, messaging profiles, installed SDKs, git status. Use `--quick` to skip API calls.

### Step 1.2: Scan for Twilio Usage

```bash
bash {baseDir}/scripts/scan-twilio-usage.sh <project-root> > twilio-scan.json
```

Produces a JSON manifest with:
- `languages_detected` — which programming languages the project uses
- `products_used` — which Twilio products are in use (voice, messaging, verify, etc.)
- `files` — every file with Twilio references, with matched patterns and product mapping
- `env_vars` — Twilio environment variables found
- `config_files` — dependency files referencing Twilio
- `twiml_files` — XML files containing TwiML verbs
- `webhook_handlers` — files with Twilio webhook validation code

For deeper analysis (catches aliased imports, dynamic config):
```bash
python3 {baseDir}/scripts/scan-twilio-deep.py <project-root> > twilio-deep-scan.json
```

### Step 1.3: Review and Confirm Scope

Present the scan results to the user. Confirm:
- Which products are in scope for migration
- Which files will be modified
- Any products that are out of scope (e.g., no Telnyx equivalent)

---

## Phase 2: Planning

Build a migration plan based on the scan results.

### Step 2.1: Read Relevant References

For each product detected in the scan, read the corresponding reference file:

| Detected Product | Read This Reference |
|---|---|
| `voice`, `texml` | `{baseDir}/references/voice-migration.md` and `{baseDir}/references/texml-verbs.md` |
| `messaging` | `{baseDir}/references/messaging-migration.md` |
| `webrtc` | `{baseDir}/references/webrtc-migration.md` |
| `verify` | `{baseDir}/references/verify-migration.md` |
| `sip`, `sip-integrations` | `{baseDir}/references/sip-trunking-migration.md` |
| `fax` | `{baseDir}/references/fax-migration.md` |
| `video` | `{baseDir}/references/video-migration.md` |
| `iot` | `{baseDir}/references/iot-migration.md` |
| `lookup` | `{baseDir}/references/lookup-migration.md` |
| `porting-in`, `porting-out` | `{baseDir}/references/number-porting.md` |

### Step 2.2: Present Decision Points

Ask the user to decide:
- **Voice approach**: TeXML (XML-compatible, lowest effort) vs Call Control API (imperative, more powerful) vs Both (incremental)
- **WebRTC auth**: Server-side credential management vs Direct client auth
- **Webhook validation**: Implement Ed25519 now (recommended) vs Skip for initial migration
- **Migration strategy**: Big-bang (all products at once) vs Product-by-product (incremental)

### Step 2.3: Generate Migration Plan

Fill in the template and save to the project:

```bash
cp {baseDir}/templates/MIGRATION-PLAN.md <project-root>/MIGRATION-PLAN.md
```

Populate: project overview, migration scope table, decision points, migration order, environment changes, webhook URL changes, risks/mitigations, rollback plan. Present to user for approval.

---

## Phase 3: Setup

Prepare the project for migration.

### Step 3.1: Create Migration Branch

```bash
cd <project-root>
git checkout -b migrate/twilio-to-telnyx
```

### Step 3.2: Update Dependencies

Install Telnyx SDK for the detected language(s):

```bash
# Python
pip install telnyx && pip freeze > requirements.txt

# Node.js
npm install telnyx

# Ruby
# Add to Gemfile: gem 'telnyx'
bundle install

# Go
go get github.com/telnyx/telnyx-go

# Java (Maven) — add to pom.xml:
# <dependency><groupId>com.telnyx</groupId><artifactId>telnyx-java</artifactId></dependency>

# PHP
composer require telnyx/telnyx-php
```

Remove Twilio SDK:

```bash
# Python
pip uninstall twilio -y && pip freeze > requirements.txt

# Node.js
npm uninstall twilio

# Ruby
# Remove from Gemfile: gem 'twilio-ruby'
bundle install

# Go
go get -u github.com/twilio/twilio-go@none && go mod tidy
```

### Step 3.3: Update Environment Variables

| Remove | Add | Notes |
|---|---|---|
| `TWILIO_ACCOUNT_SID` | `TELNYX_API_KEY` | Bearer token, get from portal |
| `TWILIO_AUTH_TOKEN` | `TELNYX_PUBLIC_KEY` | For webhook validation |
| `TWILIO_API_KEY` | — | Not needed |
| `TWILIO_API_KEY_SECRET` | — | Not needed |

Update `.env`, secrets manager, CI/CD variables, and deployment configs.

### Step 3.4: Commit Setup Changes

```bash
git add -A && git commit -m "chore: swap Twilio SDK for Telnyx SDK, update env vars"
```

---

## Phase 4: Migration

Transform code file-by-file, grouped by product area.

### Migration Loop

For each product area detected in the scan (in priority order: messaging first, then voice, then others):

1. **Read the user's file** from the scan manifest
2. **Read the conceptual mapping** from `{baseDir}/references/{product}-migration.md`
3. **Read the SDK reference** from `{baseDir}/sdk-reference/{language}/{product}.md` for exact Telnyx API syntax
4. **Transform the code**: Replace Twilio imports, client initialization, API calls, webhook handlers, and payload parsing with Telnyx equivalents
5. **Validate incrementally**: Run `bash {baseDir}/scripts/validate-migration.sh <project-root> --product {product}` after each product area
6. **Commit per product area**: `git commit -m "migrate: {product} — Twilio to Telnyx"`

### Product-Specific Transform Guidance

**Voice (TeXML path):**
- XML files: Usually no changes needed — `<Response>`, `<Say>`, `<Gather>`, etc. are compatible
- Validate with: `bash {baseDir}/scripts/validate-texml.sh <file>`
- API calls: Change base URL from `api.twilio.com/2010-04-01/Accounts/{SID}` to `api.telnyx.com/v2/texml`
- Auth: Basic Auth → Bearer Token
- Recording: Set `channels="single"` if expecting mono

**Voice (Call Control path):**
- Replace TwiML response generation with Call Control API commands
- Use `client_state` (base64 JSON) for stateless server architecture
- See `{baseDir}/references/voice-migration.md` → "Advanced Voice Patterns"

**Messaging:**
- `body` → `text` parameter name change
- `from_` → `from` (same in most SDKs)
- `StatusCallback` per-message → configure on Messaging Profile
- `MessagingServiceSid` → `messaging_profile_id`
- Webhook payload: flat `{From, Body}` → nested `{data.payload.from.phone_number, data.payload.text}`

**WebRTC:**
- Delete simple dial TwiML endpoints (use `client.newCall()` instead)
- Convert complex TwiML endpoints to TeXML
- Replace Access Token generation with SIP credentials
- Update client SDK: `@twilio/voice-sdk` → `@telnyx/webrtc`
- See `{baseDir}/references/webrtc-migration.md` → "TwiML Endpoint Analysis"

**Verify:**
- Verify Service SID → Verify Profile ID
- `channel` → `type` parameter
- `to` → `phone_number`
- Check response: `approved` → `accepted`, `pending` → `rejected`

**Webhook Signature Validation (all products):**
- Replace HMAC-SHA1 (`RequestValidator`) with Ed25519 (`WebhookSignatureVerifier`)
- Replace `X-Twilio-Signature` header check with `telnyx-signature-ed25519` + `telnyx-timestamp`

---

## Phase 5: Validation

Verify the migration is complete and working.

### Step 5.1: Full Validation Scan

```bash
bash {baseDir}/scripts/validate-migration.sh <project-root>
```

Checks for: residual Twilio imports, API URLs, env vars, signature patterns, Telnyx SDK presence, Bearer auth, Ed25519 validation code, config cleanup.

Use `--json` for machine-readable output. Exit code 0 = fully migrated.

### Step 5.2: TeXML Validation (if applicable)

```bash
# For each XML file that was migrated or left as-is
bash {baseDir}/scripts/validate-texml.sh <file.xml>
```

### Step 5.3: Smoke Test (Free)

```bash
bash {baseDir}/scripts/test-migration/smoke-test.sh
```

Validates: SDK imports, API key, account balance, number inventory, connections, messaging profiles, webhook URL reachability. No cost.

### Step 5.4: Webhook Mock Test (Free)

```bash
# Terminal 1: Start local webhook receiver
python3 {baseDir}/scripts/test-migration/webhook-receiver.py --port 8080

# Terminal 2: Send mock Telnyx webhooks
python3 {baseDir}/scripts/test-migration/test-webhooks-local.py --url http://localhost:8080/webhooks
```

Tests that your webhook handlers correctly parse Telnyx event payloads for voice, messaging, verify, and fax events.

### Step 5.5: Integration Tests (Opt-in, Real API Calls)

These tests make real API calls and incur small charges. Each requires `--confirm` to execute.

```bash
# Voice: outbound call with TTS (~$0.01)
bash {baseDir}/scripts/test-migration/test-voice.sh --confirm

# Messaging: send SMS (~$0.004)
bash {baseDir}/scripts/test-migration/test-messaging.sh --confirm

# Verify: send OTP (~$0.05)
bash {baseDir}/scripts/test-migration/test-verify.sh --confirm
```

Use `--dry-run` to validate setup without making real calls.

### Step 5.6: Fix Issues

If validation fails, review the specific check output, fix the issue, re-run validation, and commit:

```bash
git commit -m "fix: resolve migration validation issues"
```

---

## Phase 6: Cleanup & Handoff

### Step 6.1: Generate Migration Report

```bash
cp {baseDir}/templates/MIGRATION-REPORT.md <project-root>/MIGRATION-REPORT.md
```

Fill in: summary metrics, changes by product, validation results, environment changes, dependency changes, remaining manual steps.

### Step 6.2: Post-Migration Checklist

Present to the user:

- [ ] **Number porting**: Submit porting order for Twilio numbers → Telnyx via FastPort (see `{baseDir}/references/number-porting.md`)
- [ ] **DNS/webhook URLs**: Update any hardcoded webhook URLs in load balancers, DNS, or external services
- [ ] **Secrets manager**: Update environment variables in production secrets (AWS Secrets Manager, Vault, etc.)
- [ ] **CI/CD**: Update pipeline environment variables
- [ ] **Monitoring**: Update alerts for Telnyx error codes and webhook formats
- [ ] **Documentation**: Update internal docs referencing Twilio APIs
- [ ] **Run existing test suite**: Ensure unit/integration tests pass with the new SDK
- [ ] **Staging deployment**: Deploy to staging and run end-to-end tests before production
- [ ] **Cancel Twilio**: After validation period, cancel Twilio account (keep porting active first)

### Step 6.3: Explore Telnyx-Only Features

Now that you're on Telnyx, highlight capabilities unavailable on Twilio:

- **AI Assistants**: Voice/chat AI agents with built-in LLM orchestration
- **Inference API**: OpenAI-compatible LLM hosting on Telnyx GPUs
- **Embeddings**: Vector search and RAG pipelines
- **Cloud Storage**: S3-compatible object storage
- **Multiple STT Engines**: Google, Deepgram, Telnyx, Azure (in TeXML `<Gather>`)
- **ElevenLabs TTS**: Premium voice synthesis (in TeXML `<Say>`)
- **FastPort**: Same-day number porting with on-demand activation windows
- **Private Wireless Gateway**: IoT connectivity with private networking

---

## Scripts Reference

| Script | Purpose | Cost |
|---|---|---|
| `scripts/preflight-check.sh [<root>] [--quick]` | Environment readiness validation | Free |
| `scripts/scan-twilio-usage.sh <root>` | Grep-based Twilio codebase scanner → JSON | Free |
| `scripts/scan-twilio-deep.py <root>` | AST-level deep scanner (Python/JS) → JSON | Free |
| `scripts/validate-migration.sh <root> [--product X] [--json]` | Post-migration validation | Free |
| `scripts/validate-texml.sh <file>` | TwiML/TeXML XML compatibility check | Free |
| `scripts/extract-sdk-reference.sh [--dry-run]` | Populate sdk-reference/ from sibling plugins | Free |
| `scripts/test-migration/smoke-test.sh` | Free API validation checks | Free |
| `scripts/test-migration/test-webhooks-local.py` | Mock webhook payload sender | Free |
| `scripts/test-migration/webhook-receiver.py` | Local webhook receiver + optional ngrok | Free |
| `scripts/test-migration/test-voice.sh [--confirm]` | Real outbound call test | ~$0.01 |
| `scripts/test-migration/test-messaging.sh [--confirm]` | Real SMS send test | ~$0.004 |
| `scripts/test-migration/test-verify.sh [--confirm]` | Real OTP verification test | ~$0.05 |

## Related Skills

After migration, these skills provide deeper coverage for ongoing development:

| Migration Area | Related Skills | Coverage |
|---|---|---|
| Voice (Call Control) | `telnyx-voice-*` | dial, bridge, transfer, answer, hangup with all optional params |
| Voice (Advanced) | `telnyx-voice-advanced-*` | client_state, SIP Refer, DTMF, SIPREC, noise suppression |
| Voice (Conferencing) | `telnyx-voice-conferencing-*` | conference CRUD, supervisor roles, recording |
| Voice (Gather/IVR) | `telnyx-voice-gather-*` | DTMF gathering, AI gather, speech recognition |
| Voice (Media) | `telnyx-voice-media-*` | audio playback, recording, streaming |
| Voice (TeXML REST) | `telnyx-texml-*` | TeXML API operations |
| Voice (Streaming) | `telnyx-voice-streaming-*` | WebSocket audio streaming |
| WebRTC (Backend) | `telnyx-webrtc-*` | credential CRUD, SIP connection setup |
| WebRTC (Client) | `telnyx-webrtc-client-*` | JS, iOS, Android, Flutter, React Native SDKs |
| SIP / Trunking | `telnyx-sip-*` | outbound voice profiles, credential/IP connections |
| Messaging | `telnyx-messaging-*` | SMS/MMS send/receive, webhooks |
| Messaging (Profiles) | `telnyx-messaging-profiles-*` | profile CRUD, number pool config |
| Numbers | `telnyx-numbers-*` | number search, purchase, configuration |
| Porting | `telnyx-porting-in-*`, `telnyx-porting-out-*` | porting orders, requirements, activation |
| Verify | `telnyx-verify-*` | SMS/voice/flash call verification |
| Video | `telnyx-video-*` | video rooms, participants, tokens |
| Fax | `telnyx-fax-*` | send/receive fax |
| IoT | `telnyx-iot-*` | SIM management, data plans |
| 10DLC | `telnyx-10dlc-*` | brand/campaign registration |
| AI | `telnyx-ai-assistants-*`, `telnyx-ai-inference-*` | LLM orchestration, inference |
| Storage | `telnyx-storage-*` | S3-compatible object storage |

Install the relevant language plugin to access these skills.

## Resources

- Telnyx Mission Control Portal: https://portal.telnyx.com
- Telnyx Developer Docs: https://developers.telnyx.com
- Telnyx API Reference: https://developers.telnyx.com/api/overview
- Telnyx Status Page: https://status.telnyx.com
- Telnyx Support: https://support.telnyx.com
