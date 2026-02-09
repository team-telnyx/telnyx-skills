---
name: telnyx-fax-go
description: >-
  Send and receive faxes programmatically. Manage fax applications and media.
  This skill provides Go SDK examples.
metadata:
  author: telnyx
  product: fax
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Fax - Go

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

## List all Fax Applications

This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response.

`GET /fax_applications`

```go
	page, err := client.FaxApplications.List(context.TODO(), telnyx.FaxApplicationListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Creates a Fax Application

Creates a new Fax Application based on the parameters sent in the request.

`POST /fax_applications` — Required: `application_name`, `webhook_event_url`

```go
	faxApplication, err := client.FaxApplications.New(context.TODO(), telnyx.FaxApplicationNewParams{
		ApplicationName: "fax-router",
		WebhookEventURL: "https://example.com",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", faxApplication.Data)
```

## Retrieve a Fax Application

Return the details of an existing Fax Application inside the 'data' attribute of the response.

`GET /fax_applications/{id}`

```go
	faxApplication, err := client.FaxApplications.Get(context.TODO(), "1293384261075731499")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", faxApplication.Data)
```

## Update a Fax Application

Updates settings of an existing Fax Application based on the parameters of the request.

`PATCH /fax_applications/{id}` — Required: `application_name`, `webhook_event_url`

```go
	faxApplication, err := client.FaxApplications.Update(
		context.TODO(),
		"1293384261075731499",
		telnyx.FaxApplicationUpdateParams{
			ApplicationName: "fax-router",
			WebhookEventURL: "https://example.com",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", faxApplication.Data)
```

## Deletes a Fax Application

Permanently deletes a Fax Application.

`DELETE /fax_applications/{id}`

```go
	faxApplication, err := client.FaxApplications.Delete(context.TODO(), "1293384261075731499")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", faxApplication.Data)
```

## View a list of faxes

`GET /faxes`

```go
	page, err := client.Faxes.List(context.TODO(), telnyx.FaxListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Send a fax

Send a fax.

`POST /faxes` — Required: `connection_id`, `from`, `to`

```go
	fax, err := client.Faxes.New(context.TODO(), telnyx.FaxNewParams{
		ConnectionID: "234423",
		From:         "+13125790015",
		To:           "+13127367276",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", fax.Data)
```

## View a fax

`GET /faxes/{id}`

```go
	fax, err := client.Faxes.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", fax.Data)
```

## Delete a fax

`DELETE /faxes/{id}`

```go
	err := client.Faxes.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
```

## Cancel a fax

Cancel the outbound fax that is in one of the following states: `queued`, `media.processed`, `originated` or `sending`

`POST /faxes/{id}/actions/cancel`

```go
	response, err := client.Faxes.Actions.Cancel(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Refresh a fax

Refreshes the inbound fax's media_url when it has expired

`POST /faxes/{id}/actions/refresh`

```go
	response, err := client.Faxes.Actions.Refresh(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `fax.delivered` | Fax Delivered |
| `fax.failed` | Fax Failed |
| `fax.media.processed` | Fax Media Processed |
| `fax.queued` | Fax Queued |
| `fax.sending.started` | Fax Sending Started |
