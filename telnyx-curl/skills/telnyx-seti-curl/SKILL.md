---
name: telnyx-seti-curl
description: >-
  Access SETI (Space Exploration Telecommunications Infrastructure) APIs. This
  skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: seti
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Seti - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Get Enum

`GET /10dlc/enum/{endpoint}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/enum/{endpoint}"
```

## Retrieve Black Box Test Results

Returns the results of the various black box tests

`GET /seti/black_box_test_results`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/seti/black_box_test_results"
```
