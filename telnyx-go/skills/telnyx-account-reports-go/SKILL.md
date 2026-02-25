---
name: telnyx-account-reports-go
description: >-
  Generate and retrieve usage reports for billing, analytics, and
  reconciliation. This skill provides Go SDK examples.
metadata:
  author: telnyx
  product: account-reports
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Reports - Go

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

## Get all MDR detailed report requests

Retrieves all MDR detailed report requests for the authenticated user

`GET /legacy_reporting/batch_detail_records/messaging`

```go
	messagings, err := client.Legacy.Reporting.BatchDetailRecords.Messaging.List(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messagings.Data)
```

## Create a new MDR detailed report request

Creates a new MDR detailed report request with the specified filters

`POST /legacy_reporting/batch_detail_records/messaging` — Required: `start_time`, `end_time`

Optional: `connections` (array[integer]), `directions` (array[integer]), `filters` (array[object]), `include_message_body` (boolean), `managed_accounts` (array[string]), `profiles` (array[string]), `record_types` (array[integer]), `report_name` (string), `select_all_managed_accounts` (boolean), `timezone` (string)

```go
	messaging, err := client.Legacy.Reporting.BatchDetailRecords.Messaging.New(context.TODO(), telnyx.LegacyReportingBatchDetailRecordMessagingNewParams{
		EndTime:   time.Now(),
		StartTime: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messaging.Data)
```

## Get a specific MDR detailed report request

Retrieves a specific MDR detailed report request by ID

`GET /legacy_reporting/batch_detail_records/messaging/{id}`

```go
	messaging, err := client.Legacy.Reporting.BatchDetailRecords.Messaging.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messaging.Data)
```

## Delete a MDR detailed report request

Deletes a specific MDR detailed report request by ID

`DELETE /legacy_reporting/batch_detail_records/messaging/{id}`

```go
	messaging, err := client.Legacy.Reporting.BatchDetailRecords.Messaging.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messaging.Data)
```

## Get all CDR report requests

Retrieves all CDR report requests for the authenticated user

`GET /legacy_reporting/batch_detail_records/voice`

```go
	voices, err := client.Legacy.Reporting.BatchDetailRecords.Voice.List(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voices.Data)
```

## Create a new CDR report request

Creates a new CDR report request with the specified filters

`POST /legacy_reporting/batch_detail_records/voice` — Required: `start_time`, `end_time`

Optional: `call_types` (array[integer]), `connections` (array[integer]), `fields` (array[string]), `filters` (array[object]), `include_all_metadata` (boolean), `managed_accounts` (array[string]), `record_types` (array[integer]), `report_name` (string), `select_all_managed_accounts` (boolean), `source` (string), `timezone` (string)

```go
	voice, err := client.Legacy.Reporting.BatchDetailRecords.Voice.New(context.TODO(), telnyx.LegacyReportingBatchDetailRecordVoiceNewParams{
		EndTime:   time.Now(),
		StartTime: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Get a specific CDR report request

Retrieves a specific CDR report request by ID

`GET /legacy_reporting/batch_detail_records/voice/{id}`

```go
	voice, err := client.Legacy.Reporting.BatchDetailRecords.Voice.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Delete a CDR report request

Deletes a specific CDR report request by ID

`DELETE /legacy_reporting/batch_detail_records/voice/{id}`

```go
	voice, err := client.Legacy.Reporting.BatchDetailRecords.Voice.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Get available CDR report fields

Retrieves all available fields that can be used in CDR reports

`GET /legacy_reporting/batch_detail_records/voice/fields`

```go
	response, err := client.Legacy.Reporting.BatchDetailRecords.Voice.GetFields(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Billing)
```

## List MDR usage reports

Fetch all previous requests for MDR usage reports.

`GET /legacy_reporting/usage_reports/messaging`

```go
	page, err := client.Legacy.Reporting.UsageReports.Messaging.List(context.TODO(), telnyx.LegacyReportingUsageReportMessagingListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create a new legacy usage V2 MDR report request

Creates a new legacy usage V2 MDR report request with the specified filters

`POST /legacy_reporting/usage_reports/messaging`

```go
	messaging, err := client.Legacy.Reporting.UsageReports.Messaging.New(context.TODO(), telnyx.LegacyReportingUsageReportMessagingNewParams{
		AggregationType: 0,
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messaging.Data)
```

## Get an MDR usage report

Fetch single MDR usage report by id.

`GET /legacy_reporting/usage_reports/messaging/{id}`

```go
	messaging, err := client.Legacy.Reporting.UsageReports.Messaging.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messaging.Data)
```

## Delete a V2 legacy usage MDR report request

Deletes a specific V2 legacy usage MDR report request by ID

`DELETE /legacy_reporting/usage_reports/messaging/{id}`

```go
	messaging, err := client.Legacy.Reporting.UsageReports.Messaging.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messaging.Data)
```

## List telco data usage reports

Retrieve a paginated list of telco data usage reports

`GET /legacy_reporting/usage_reports/number_lookup`

```go
	numberLookups, err := client.Legacy.Reporting.UsageReports.NumberLookup.List(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", numberLookups.Data)
```

## Submit telco data usage report

Submit a new telco data usage report

`POST /legacy_reporting/usage_reports/number_lookup`

```go
	numberLookup, err := client.Legacy.Reporting.UsageReports.NumberLookup.New(context.TODO(), telnyx.LegacyReportingUsageReportNumberLookupNewParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", numberLookup.Data)
```

## Get telco data usage report by ID

Retrieve a specific telco data usage report by its ID

`GET /legacy_reporting/usage_reports/number_lookup/{id}`

```go
	numberLookup, err := client.Legacy.Reporting.UsageReports.NumberLookup.Get(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", numberLookup.Data)
```

## Delete telco data usage report

Delete a specific telco data usage report by its ID

`DELETE /legacy_reporting/usage_reports/number_lookup/{id}`

```go
	err := client.Legacy.Reporting.UsageReports.NumberLookup.Delete(context.TODO(), "id")
	if err != nil {
		panic(err.Error())
	}
```

## Get speech to text usage report

Generate and fetch speech to text usage report synchronously.

`GET /legacy_reporting/usage_reports/speech_to_text`

```go
	response, err := client.Legacy.Reporting.UsageReports.GetSpeechToText(context.TODO(), telnyx.LegacyReportingUsageReportGetSpeechToTextParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List CDR usage reports

Fetch all previous requests for cdr usage reports.

`GET /legacy_reporting/usage_reports/voice`

```go
	page, err := client.Legacy.Reporting.UsageReports.Voice.List(context.TODO(), telnyx.LegacyReportingUsageReportVoiceListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create a new legacy usage V2 CDR report request

Creates a new legacy usage V2 CDR report request with the specified filters

`POST /legacy_reporting/usage_reports/voice`

```go
	voice, err := client.Legacy.Reporting.UsageReports.Voice.New(context.TODO(), telnyx.LegacyReportingUsageReportVoiceNewParams{
		EndTime:   time.Now(),
		StartTime: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Get a CDR usage report

Fetch single cdr usage report by id.

`GET /legacy_reporting/usage_reports/voice/{id}`

```go
	voice, err := client.Legacy.Reporting.UsageReports.Voice.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Delete a V2 legacy usage CDR report request

Deletes a specific V2 legacy usage CDR report request by ID

`DELETE /legacy_reporting/usage_reports/voice/{id}`

```go
	voice, err := client.Legacy.Reporting.UsageReports.Voice.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", voice.Data)
```

## Fetch all Messaging usage reports

Fetch all messaging usage reports.

`GET /reports/mdr_usage_reports`

```go
	page, err := client.Reports.MdrUsageReports.List(context.TODO(), telnyx.ReportMdrUsageReportListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create MDR Usage Report

Submit request for new new messaging usage report.

`POST /reports/mdr_usage_reports`

```go
	mdrUsageReport, err := client.Reports.MdrUsageReports.New(context.TODO(), telnyx.ReportMdrUsageReportNewParams{
		AggregationType: telnyx.ReportMdrUsageReportNewParamsAggregationTypeNoAggregation,
		EndDate:         time.Now(),
		StartDate:       time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mdrUsageReport.Data)
```

## Retrieve messaging report

Fetch a single messaging usage report by id

`GET /reports/mdr_usage_reports/{id}`

```go
	mdrUsageReport, err := client.Reports.MdrUsageReports.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mdrUsageReport.Data)
```

## Delete MDR Usage Report

Delete messaging usage report by id

`DELETE /reports/mdr_usage_reports/{id}`

```go
	mdrUsageReport, err := client.Reports.MdrUsageReports.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mdrUsageReport.Data)
```

## Generate and fetch MDR Usage Report

Generate and fetch messaging usage report synchronously.

`GET /reports/mdr_usage_reports/sync`

```go
	response, err := client.Reports.MdrUsageReports.FetchSync(context.TODO(), telnyx.ReportMdrUsageReportFetchSyncParams{
		AggregationType: telnyx.ReportMdrUsageReportFetchSyncParamsAggregationTypeProfile,
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Generates and fetches CDR Usage Reports

Generate and fetch voice usage report synchronously.

`GET /reports/cdr_usage_reports/sync`

```go
	response, err := client.Reports.CdrUsageReports.FetchSync(context.TODO(), telnyx.ReportCdrUsageReportFetchSyncParams{
		AggregationType:  telnyx.ReportCdrUsageReportFetchSyncParamsAggregationTypeNoAggregation,
		ProductBreakdown: telnyx.ReportCdrUsageReportFetchSyncParamsProductBreakdownNoBreakdown,
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Get Telnyx product usage data (BETA)

Get Telnyx usage data by product, broken out by the specified dimensions

`GET /usage_reports`

```go
	page, err := client.UsageReports.List(context.TODO(), telnyx.UsageReportListParams{
		Dimensions: []string{"string"},
		Metrics:    []string{"string"},
		Product:    "product",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Get Usage Reports query options (BETA)

Get the Usage Reports options for querying usage, including the products available and their respective metrics and dimensions

`GET /usage_reports/options`

```go
	response, err := client.UsageReports.GetOptions(context.TODO(), telnyx.UsageReportGetOptionsParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```
