---
name: telnyx-numbers-config-go
description: >-
  Configure phone number settings including caller ID, call forwarding,
  messaging enablement, and connection assignments. This skill provides Go SDK
  examples.
metadata:
  author: telnyx
  product: numbers-config
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Numbers Config - Go

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

## Lists the phone number blocks jobs

`GET /phone_number_blocks/jobs`

```go
	page, err := client.PhoneNumberBlocks.Jobs.List(context.TODO(), telnyx.PhoneNumberBlockJobListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Retrieves a phone number blocks job

`GET /phone_number_blocks/jobs/{id}`

```go
	job, err := client.PhoneNumberBlocks.Jobs.Get(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", job.Data)
```

## Deletes all numbers associated with a phone number block

Creates a new background job to delete all the phone numbers associated with the given block.

`POST /phone_number_blocks/jobs/delete_phone_number_block` — Required: `phone_number_block_id`

```go
	response, err := client.PhoneNumberBlocks.Jobs.DeletePhoneNumberBlock(context.TODO(), telnyx.PhoneNumberBlockJobDeletePhoneNumberBlockParams{
		PhoneNumberBlockID: "f3946371-7199-4261-9c3d-81a0d7935146",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List phone numbers

`GET /phone_numbers`

```go
	page, err := client.PhoneNumbers.List(context.TODO(), telnyx.PhoneNumberListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Retrieve a phone number

`GET /phone_numbers/{id}`

```go
	phoneNumber, err := client.PhoneNumbers.Get(context.TODO(), "1293384261075731499")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", phoneNumber.Data)
```

## Update a phone number

`PATCH /phone_numbers/{id}`

Optional: `address_id` (string), `billing_group_id` (string), `connection_id` (string), `customer_reference` (string), `external_pin` (string), `hd_voice_enabled` (boolean), `id` (string), `tags` (array[string])

```go
	phoneNumber, err := client.PhoneNumbers.Update(
		context.TODO(),
		"1293384261075731499",
		telnyx.PhoneNumberUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", phoneNumber.Data)
```

## Delete a phone number

`DELETE /phone_numbers/{id}`

```go
	phoneNumber, err := client.PhoneNumbers.Delete(context.TODO(), "1293384261075731499")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", phoneNumber.Data)
```

## Change the bundle status for a phone number (set to being in a bundle or remove from a bundle)

`PATCH /phone_numbers/{id}/actions/bundle_status_change` — Required: `bundle_id`

```go
	response, err := client.PhoneNumbers.Actions.ChangeBundleStatus(
		context.TODO(),
		"1293384261075731499",
		telnyx.PhoneNumberActionChangeBundleStatusParams{
			BundleID: "5194d8fc-87e6-4188-baa9-1c434bbe861b",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Enable emergency for a phone number

`POST /phone_numbers/{id}/actions/enable_emergency` — Required: `emergency_enabled`, `emergency_address_id`

```go
	response, err := client.PhoneNumbers.Actions.EnableEmergency(
		context.TODO(),
		"1293384261075731499",
		telnyx.PhoneNumberActionEnableEmergencyParams{
			EmergencyAddressID: "53829456729313",
			EmergencyEnabled:   true,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Retrieve a phone number with voice settings

`GET /phone_numbers/{id}/voice`

```go
	voice, err := client.PhoneNumbers.Voice.Get(context.TODO(), "1293384261075731499")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Update a phone number with voice settings

`PATCH /phone_numbers/{id}/voice`

Optional: `call_forwarding` (object), `call_recording` (object), `caller_id_name_enabled` (boolean), `cnam_listing` (object), `inbound_call_screening` (enum), `media_features` (object), `tech_prefix_enabled` (boolean), `translated_number` (string), `usage_payment_method` (enum)

```go
	voice, err := client.PhoneNumbers.Voice.Update(
		context.TODO(),
		"1293384261075731499",
		telnyx.PhoneNumberVoiceUpdateParams{
			UpdateVoiceSettings: telnyx.UpdateVoiceSettingsParam{},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Verify ownership of phone numbers

Verifies ownership of the provided phone numbers and returns a mapping of numbers to their IDs, plus a list of numbers not found in the account.

`POST /phone_numbers/actions/verify_ownership` — Required: `phone_numbers`

```go
	response, err := client.PhoneNumbers.Actions.VerifyOwnership(context.TODO(), telnyx.PhoneNumberActionVerifyOwnershipParams{
		PhoneNumbers: []string{"+15551234567"},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List CSV downloads

`GET /phone_numbers/csv_downloads`

```go
	page, err := client.PhoneNumbers.CsvDownloads.List(context.TODO(), telnyx.PhoneNumberCsvDownloadListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create a CSV download

`POST /phone_numbers/csv_downloads`

```go
	csvDownload, err := client.PhoneNumbers.CsvDownloads.New(context.TODO(), telnyx.PhoneNumberCsvDownloadNewParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", csvDownload.Data)
```

## Retrieve a CSV download

`GET /phone_numbers/csv_downloads/{id}`

```go
	csvDownload, err := client.PhoneNumbers.CsvDownloads.Get(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", csvDownload.Data)
```

## Lists the phone numbers jobs

`GET /phone_numbers/jobs`

```go
	page, err := client.PhoneNumbers.Jobs.List(context.TODO(), telnyx.PhoneNumberJobListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Retrieve a phone numbers job

`GET /phone_numbers/jobs/{id}`

```go
	job, err := client.PhoneNumbers.Jobs.Get(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", job.Data)
```

## Delete a batch of numbers

Creates a new background job to delete a batch of numbers.

`POST /phone_numbers/jobs/delete_phone_numbers` — Required: `phone_numbers`

```go
	response, err := client.PhoneNumbers.Jobs.DeleteBatch(context.TODO(), telnyx.PhoneNumberJobDeleteBatchParams{
		PhoneNumbers: []string{"+19705555098", "+19715555098", "32873127836"},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Update the emergency settings from a batch of numbers

Creates a background job to update the emergency settings of a collection of phone numbers.

`POST /phone_numbers/jobs/update_emergency_settings` — Required: `emergency_enabled`, `phone_numbers`

Optional: `emergency_address_id` (['string', 'null'])

```go
	response, err := client.PhoneNumbers.Jobs.UpdateEmergencySettingsBatch(context.TODO(), telnyx.PhoneNumberJobUpdateEmergencySettingsBatchParams{
		EmergencyEnabled: true,
		PhoneNumbers:     []string{"+19705555098", "+19715555098", "32873127836"},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Update a batch of numbers

Creates a new background job to update a batch of numbers.

`POST /phone_numbers/jobs/update_phone_numbers` — Required: `phone_numbers`

Optional: `billing_group_id` (string), `connection_id` (string), `customer_reference` (string), `deletion_lock_enabled` (boolean), `external_pin` (string), `hd_voice_enabled` (boolean), `tags` (array[string]), `voice` (object)

```go
	response, err := client.PhoneNumbers.Jobs.UpdateBatch(context.TODO(), telnyx.PhoneNumberJobUpdateBatchParams{
		PhoneNumbers: []string{"1583466971586889004", "+13127367254"},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Retrieve regulatory requirements for a list of phone numbers

`GET /phone_numbers/regulatory_requirements`

```go
	phoneNumbersRegulatoryRequirement, err := client.PhoneNumbersRegulatoryRequirements.Get(context.TODO(), telnyx.PhoneNumbersRegulatoryRequirementGetParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", phoneNumbersRegulatoryRequirement.Data)
```

## Slim List phone numbers

List phone numbers, This endpoint is a lighter version of the /phone_numbers endpoint having higher performance and rate limit.

`GET /phone_numbers/slim`

```go
	page, err := client.PhoneNumbers.SlimList(context.TODO(), telnyx.PhoneNumberSlimListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## List phone numbers with voice settings

`GET /phone_numbers/voice`

```go
	page, err := client.PhoneNumbers.Voice.List(context.TODO(), telnyx.PhoneNumberVoiceListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## List Mobile Phone Numbers

`GET /v2/mobile_phone_numbers`

```go
	page, err := client.MobilePhoneNumbers.List(context.TODO(), telnyx.MobilePhoneNumberListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Retrieve a Mobile Phone Number

`GET /v2/mobile_phone_numbers/{id}`

```go
	mobilePhoneNumber, err := client.MobilePhoneNumbers.Get(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mobilePhoneNumber.Data)
```

## Update a Mobile Phone Number

`PATCH /v2/mobile_phone_numbers/{id}`

Optional: `call_forwarding` (object), `call_recording` (object), `caller_id_name_enabled` (boolean), `cnam_listing` (object), `connection_id` (['string', 'null']), `customer_reference` (['string', 'null']), `inbound` (object), `inbound_call_screening` (enum), `noise_suppression` (boolean), `outbound` (object), `tags` (array[string])

```go
	mobilePhoneNumber, err := client.MobilePhoneNumbers.Update(
		context.TODO(),
		"id",
		telnyx.MobilePhoneNumberUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mobilePhoneNumber.Data)
```
