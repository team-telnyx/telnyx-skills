---
name: telnyx-go
description: >-
  Broad Telnyx Go SDK entrypoint. Use when starting a Go integration and you
  need the main setup pattern plus a map of the available Telnyx product
  skills.
metadata:
  author: telnyx
  product: telnyx
  language: go
---

# Telnyx Go SDK

Use this wrapper when you want broad Telnyx Go SDK guidance before narrowing to a specific product area.

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
package main

import (
    "github.com/team-telnyx/telnyx-go/v4"
)

func main() {
    client := telnyx.NewClient()
    _ = client
}
```

## Choose The Right Product Skill

- Messaging: `telnyx-messaging-go`, `telnyx-messaging-profiles-go`, `telnyx-messaging-hosted-go`, `telnyx-10dlc-go`
- Voice: `telnyx-voice-go`, `telnyx-voice-media-go`, `telnyx-voice-gather-go`, `telnyx-voice-streaming-go`, `telnyx-voice-conferencing-go`, `telnyx-voice-advanced-go`, `telnyx-texml-go`, `telnyx-sip-go`, `telnyx-sip-integrations-go`, `telnyx-webrtc-go`
- Numbers: `telnyx-numbers-go`, `telnyx-numbers-config-go`, `telnyx-numbers-compliance-go`, `telnyx-numbers-services-go`, `telnyx-porting-in-go`, `telnyx-porting-out-go`, `telnyx-verify-go`
- AI: `telnyx-ai-assistants-go`, `telnyx-ai-inference-go`, `telnyx-missions-go`
- Account and platform services: `telnyx-account-go`, `telnyx-account-access-go`, `telnyx-account-management-go`, `telnyx-account-notifications-go`, `telnyx-account-reports-go`, `telnyx-storage-go`, `telnyx-video-go`, `telnyx-fax-go`, `telnyx-networking-go`, `telnyx-iot-go`, `telnyx-oauth-go`, `telnyx-seti-go`

## Usage Guidance

- Use this skill to start a Telnyx Go integration with the standard SDK setup and a map of the main product areas.
- For implementation details, install the product skill that matches the workflow you are building.
- Keep this skill focused on choosing the right Telnyx area; use the linked product skills for endpoint- and workflow-level guidance.
