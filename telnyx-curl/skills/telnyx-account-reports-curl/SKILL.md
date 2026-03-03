---
name: telnyx-account-reports-curl
description: >-
  Generate and retrieve usage reports for billing, analytics, and
  reconciliation. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: account-reports
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Reports - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List call events

Filters call events by given filter parameters.

`GET /call_events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/call_events"
```

## Create a ledger billing group report

`POST /ledger_billing_group_reports`

Optional: `month` (integer), `year` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "year": 2019,
  "month": 10
}' \
  "https://api.telnyx.com/v2/ledger_billing_group_reports"
```

## Get a ledger billing group report

`GET /ledger_billing_group_reports/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ledger_billing_group_reports/f5586561-8ff0-4291-a0ac-84fe544797bd"
```

## Get all MDR detailed report requests

Retrieves all MDR detailed report requests for the authenticated user

`GET /legacy/reporting/batch_detail_records/messaging`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/messaging"
```

## Create a new MDR detailed report request

Creates a new MDR detailed report request with the specified filters

`POST /legacy/reporting/batch_detail_records/messaging` — Required: `start_time`, `end_time`

Optional: `connections` (array[integer]), `directions` (array[integer]), `filters` (array[object]), `include_message_body` (boolean), `managed_accounts` (array[string]), `profiles` (array[string]), `record_types` (array[integer]), `report_name` (string), `select_all_managed_accounts` (boolean), `timezone` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "start_time": "2024-02-01T00:00:00Z",
  "end_time": "2024-02-12T23:59:59Z",
  "timezone": "UTC",
  "directions": [
    1,
    2
  ],
  "record_types": [
    1,
    2
  ],
  "connections": [
    123,
    456
  ],
  "report_name": "My MDR Report",
  "include_message_body": true,
  "profiles": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "7d4e3f8a-9b2c-4e1d-8f5a-1a2b3c4d5e6f"
  ],
  "managed_accounts": [
    "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
  ],
  "select_all_managed_accounts": false
}' \
  "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/messaging"
```

## Get a specific MDR detailed report request

Retrieves a specific MDR detailed report request by ID

`GET /legacy/reporting/batch_detail_records/messaging/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/messaging/{id}"
```

## Delete a MDR detailed report request

Deletes a specific MDR detailed report request by ID

`DELETE /legacy/reporting/batch_detail_records/messaging/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/messaging/{id}"
```

## Get all CDR report requests

Retrieves all CDR report requests for the authenticated user

`GET /legacy/reporting/batch_detail_records/voice`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/voice"
```

## Create a new CDR report request

Creates a new CDR report request with the specified filters

`POST /legacy/reporting/batch_detail_records/voice` — Required: `start_time`, `end_time`

Optional: `call_types` (array[integer]), `connections` (array[integer]), `fields` (array[string]), `filters` (array[object]), `include_all_metadata` (boolean), `managed_accounts` (array[string]), `record_types` (array[integer]), `report_name` (string), `select_all_managed_accounts` (boolean), `source` (string), `timezone` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "start_time": "2024-02-01T00:00:00Z",
  "end_time": "2024-02-12T23:59:59Z",
  "timezone": "UTC",
  "call_types": [
    1,
    2
  ],
  "record_types": [
    1,
    2
  ],
  "connections": [
    123,
    456
  ],
  "report_name": "My CDR Report",
  "source": "calls",
  "include_all_metadata": true,
  "fields": [
    "call_leg_id",
    "start_time",
    "end_time"
  ],
  "managed_accounts": [
    "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
  ],
  "select_all_managed_accounts": false
}' \
  "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/voice"
```

## Get available CDR report fields

Retrieves all available fields that can be used in CDR reports

`GET /legacy/reporting/batch_detail_records/voice/fields`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/voice/fields"
```

## Get a specific CDR report request

Retrieves a specific CDR report request by ID

`GET /legacy/reporting/batch_detail_records/voice/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/voice/{id}"
```

## Delete a CDR report request

Deletes a specific CDR report request by ID

`DELETE /legacy/reporting/batch_detail_records/voice/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/voice/{id}"
```

## List MDR usage reports

Fetch all previous requests for MDR usage reports.

`GET /legacy/reporting/usage_reports/messaging`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/messaging"
```

## Create a new legacy usage V2 MDR report request

Creates a new legacy usage V2 MDR report request with the specified filters

`POST /legacy/reporting/usage_reports/messaging`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/legacy/reporting/usage_reports/messaging"
```

## Get an MDR usage report

Fetch single MDR usage report by id.

`GET /legacy/reporting/usage_reports/messaging/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/messaging/{id}"
```

## Delete a V2 legacy usage MDR report request

Deletes a specific V2 legacy usage MDR report request by ID

`DELETE /legacy/reporting/usage_reports/messaging/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/legacy/reporting/usage_reports/messaging/{id}"
```

## List telco data usage reports

Retrieve a paginated list of telco data usage reports

`GET /legacy/reporting/usage_reports/number_lookup`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/number_lookup"
```

## Submit telco data usage report

Submit a new telco data usage report

`POST /legacy/reporting/usage_reports/number_lookup`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/legacy/reporting/usage_reports/number_lookup"
```

## Get telco data usage report by ID

Retrieve a specific telco data usage report by its ID

`GET /legacy/reporting/usage_reports/number_lookup/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/number_lookup/{id}"
```

## Delete telco data usage report

Delete a specific telco data usage report by its ID

`DELETE /legacy/reporting/usage_reports/number_lookup/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/legacy/reporting/usage_reports/number_lookup/{id}"
```

## List CDR usage reports

Fetch all previous requests for cdr usage reports.

`GET /legacy/reporting/usage_reports/voice`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/voice"
```

## Create a new legacy usage V2 CDR report request

Creates a new legacy usage V2 CDR report request with the specified filters

`POST /legacy/reporting/usage_reports/voice`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/legacy/reporting/usage_reports/voice"
```

## Get a CDR usage report

Fetch single cdr usage report by id.

`GET /legacy/reporting/usage_reports/voice/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/voice/{id}"
```

## Delete a V2 legacy usage CDR report request

Deletes a specific V2 legacy usage CDR report request by ID

`DELETE /legacy/reporting/usage_reports/voice/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/legacy/reporting/usage_reports/voice/{id}"
```

## List CSV downloads

`GET /phone_numbers/csv_downloads`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/csv_downloads"
```

## Create a CSV download

`POST /phone_numbers/csv_downloads`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/phone_numbers/csv_downloads"
```

## Retrieve a CSV download

`GET /phone_numbers/csv_downloads/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/phone_numbers/csv_downloads/{id}"
```

## Generates and fetches CDR Usage Reports

Generate and fetch voice usage report synchronously.

`GET /reports/cdr_usage_reports/sync`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/reports/cdr_usage_reports/sync?start_date=2020-07-01T00:00:00-06:00&end_date=2020-07-01T00:00:00-06:00&aggregation_type=NO_AGGREGATION&product_breakdown=NO_BREAKDOWN&connections=[1234567890123]"
```

## Fetch all Messaging usage reports

Fetch all messaging usage reports.

`GET /reports/mdr_usage_reports`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/reports/mdr_usage_reports"
```

## Create MDR Usage Report

Submit request for new new messaging usage report.

`POST /reports/mdr_usage_reports`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/reports/mdr_usage_reports"
```

## Generate and fetch MDR Usage Report

Generate and fetch messaging usage report synchronously.

`GET /reports/mdr_usage_reports/sync`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/reports/mdr_usage_reports/sync?start_date=2020-07-01T00:00:00-06:00&end_date=2020-07-01T00:00:00-06:00&aggregation_type=PROFILE&profiles=['My profile']"
```

## Retrieve messaging report

Fetch a single messaging usage report by id

`GET /reports/mdr_usage_reports/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/reports/mdr_usage_reports/{id}"
```

## Delete MDR Usage Report

Delete messaging usage report by id

`DELETE /reports/mdr_usage_reports/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/reports/mdr_usage_reports/{id}"
```

## Fetch all Mdr records

`GET /reports/mdrs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/reports/mdrs?id=e093fbe0-5bde-11eb-ae93-0242ac130002&direction=INBOUND&profile=My profile&cld=+15551237654&cli=+15551237654&status=DELIVERED&message_type=SMS"
```

## Fetches all Wdr records

Fetch all Wdr records

`GET /reports/wdrs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/reports/wdrs?start_date=2021-05-01T00:00:00Z&end_date=2021-06-01T00:00:00Z&id=e093fbe0-5bde-11eb-ae93-0242ac130002&mcc=204&mnc=01&imsi=123456&sim_group_name=sim name&sim_group_id=f05a189f-7c46-4531-ac56-1460dc465a42&sim_card_id=877f80a6-e5b2-4687-9a04-88076265720f&phone_number=+12345678910&sort=['created_at']"
```

## Get Telnyx product usage data (BETA)

Get Telnyx usage data by product, broken out by the specified dimensions

`GET /usage_reports`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/usage_reports"
```

## Get Usage Reports query options (BETA)

Get the Usage Reports options for querying usage, including the products available and their respective metrics and dimensions

`GET /usage_reports/options`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/usage_reports/options"
```
