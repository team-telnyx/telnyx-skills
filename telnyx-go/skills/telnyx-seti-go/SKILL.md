---
name: telnyx-seti-go
description: >-
  Access SETI (Space Exploration Telecommunications Infrastructure) APIs. This
  skill provides Go SDK examples.
metadata:
  author: telnyx
  product: seti
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Seti - Go

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
import (
  "context"
  "fmt"
  "os"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

client := telnyx.NewClient(
  option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
)
```

All examples below assume `client` is already initialized as shown above.

## Retrieve Black Box Test Results

Returns the results of the various black box tests

`GET /seti/black_box_test_results`

```go
	response, err := client.Seti.GetBlackBoxTestResults(context.TODO(), telnyx.SetiGetBlackBoxTestResultsParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```
