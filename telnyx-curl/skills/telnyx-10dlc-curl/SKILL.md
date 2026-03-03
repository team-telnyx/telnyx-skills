---
name: telnyx-10dlc-curl
description: >-
  Register brands and campaigns for 10DLC (10-digit long code) A2P messaging
  compliance in the US. Manage campaign assignments to phone numbers. This skill
  provides REST API (curl) examples.
metadata:
  author: telnyx
  product: 10dlc
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx 10Dlc - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List Brands

This endpoint is used to list all brands associated with your organization.

`GET /10dlc/brand`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/brand?sort=-identityStatus&brandId=826ef77a-348c-445b-81a5-a9b13c68fbfe&tcrBrandId=BBAND1"
```

## Create Brand

This endpoint is used to create a new brand.

`POST /10dlc/brand` — Required: `entityType`, `displayName`, `country`, `email`, `vertical`

Optional: `businessContactEmail` (string), `city` (string), `companyName` (string), `ein` (string), `firstName` (string), `ipAddress` (string), `isReseller` (boolean), `lastName` (string), `mobilePhone` (string), `mock` (boolean), `phone` (string), `postalCode` (string), `state` (string), `stockExchange` (object), `stockSymbol` (string), `street` (string), `webhookFailoverURL` (string), `webhookURL` (string), `website` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entityType": "string",
  "displayName": "ABC Mobile",
  "companyName": "ABC Inc.",
  "firstName": "John",
  "lastName": "Smith",
  "ein": "111111111",
  "phone": "+12024567890",
  "street": "123",
  "city": "New York",
  "state": "NY",
  "postalCode": "10001",
  "country": "US",
  "email": "string",
  "stockSymbol": "ABC",
  "stockExchange": "NASDAQ",
  "website": "http://www.abcmobile.com",
  "vertical": "string",
  "mobilePhone": "+12024567890",
  "businessContactEmail": "name@example.com",
  "webhookURL": "https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
  "webhookFailoverURL": "https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6"
}' \
  "https://api.telnyx.com/v2/10dlc/brand"
```

## Get Brand Feedback By Id

Get feedback about a brand by ID.

`GET /10dlc/brand/feedback/{brandId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/brand/feedback/{brandId}"
```

## Get Brand SMS OTP Status

Query the status of an SMS OTP (One-Time Password) for Sole Proprietor brand verification.

`GET /10dlc/brand/smsOtp/{referenceId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/brand/smsOtp/OTP4B2001?brandId=B123ABC"
```

## Get Brand

Retrieve a brand by `brandId`.

`GET /10dlc/brand/{brandId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/brand/{brandId}"
```

## Update Brand

Update a brand's attributes by `brandId`.

`PUT /10dlc/brand/{brandId}` — Required: `entityType`, `displayName`, `country`, `email`, `vertical`

Optional: `altBusinessId` (string), `altBusinessIdType` (enum), `businessContactEmail` (string), `city` (string), `companyName` (string), `ein` (string), `firstName` (string), `identityStatus` (enum), `ipAddress` (string), `isReseller` (boolean), `lastName` (string), `phone` (string), `postalCode` (string), `state` (string), `stockExchange` (object), `stockSymbol` (string), `street` (string), `webhookFailoverURL` (string), `webhookURL` (string), `website` (string)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entityType": "string",
  "displayName": "ABC Mobile",
  "companyName": "ABC Inc.",
  "firstName": "John",
  "lastName": "Smith",
  "ein": "111111111",
  "phone": "+12024567890",
  "street": "123",
  "city": "New York",
  "state": "NY",
  "postalCode": "10001",
  "country": "US",
  "email": "string",
  "stockSymbol": "ABC",
  "stockExchange": "NASDAQ",
  "website": "http://www.abcmobile.com",
  "vertical": "string",
  "businessContactEmail": "name@example.com",
  "webhookURL": "https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
  "webhookFailoverURL": "https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6"
}' \
  "https://api.telnyx.com/v2/10dlc/brand/{brandId}"
```

## Delete Brand

Delete Brand.

`DELETE /10dlc/brand/{brandId}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/10dlc/brand/{brandId}"
```

## Resend brand 2FA email

`POST /10dlc/brand/{brandId}/2faEmail`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/10dlc/brand/{brandId}/2faEmail"
```

## List External Vettings

Get list of valid external vetting record for a given brand

`GET /10dlc/brand/{brandId}/externalVetting`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/brand/{brandId}/externalVetting"
```

## Order Brand External Vetting

Order new external vetting for a brand

`POST /10dlc/brand/{brandId}/externalVetting` — Required: `evpId`, `vettingClass`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "evpId": "string",
  "vettingClass": "string"
}' \
  "https://api.telnyx.com/v2/10dlc/brand/{brandId}/externalVetting"
```

## Import External Vetting Record

This operation can be used to import an external vetting record from a TCR-approved
vetting provider.

`PUT /10dlc/brand/{brandId}/externalVetting` — Required: `evpId`, `vettingId`

Optional: `vettingToken` (string)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "evpId": "string",
  "vettingId": "string"
}' \
  "https://api.telnyx.com/v2/10dlc/brand/{brandId}/externalVetting"
```

## Revet Brand

This operation allows you to revet the brand.

`PUT /10dlc/brand/{brandId}/revet`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/10dlc/brand/{brandId}/revet"
```

## Get Brand SMS OTP Status by Brand ID

Query the status of an SMS OTP (One-Time Password) for Sole Proprietor brand verification using the Brand ID.

`GET /10dlc/brand/{brandId}/smsOtp`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/brand/4b20019b-043a-78f8-0657-b3be3f4b4002/smsOtp"
```

## Trigger Brand SMS OTP

Trigger or re-trigger an SMS OTP (One-Time Password) for Sole Proprietor brand verification.

`POST /10dlc/brand/{brandId}/smsOtp` — Required: `pinSms`, `successSms`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "pinSms": "Your PIN is @OTP_PIN@",
  "successSms": "Verification successful!"
}' \
  "https://api.telnyx.com/v2/10dlc/brand/4b20019b-043a-78f8-0657-b3be3f4b4002/smsOtp"
```

## Verify Brand SMS OTP

Verify the SMS OTP (One-Time Password) for Sole Proprietor brand verification.

`PUT /10dlc/brand/{brandId}/smsOtp` — Required: `otpPin`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "otpPin": "123456"
}' \
  "https://api.telnyx.com/v2/10dlc/brand/4b20019b-043a-78f8-0657-b3be3f4b4002/smsOtp"
```

## List Campaigns

Retrieve a list of campaigns associated with a supplied `brandId`.

`GET /10dlc/campaign`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign?sort=-assignedPhoneNumbersCount"
```

## Accept Shared Campaign

Manually accept a campaign shared with Telnyx

`POST /10dlc/campaign/acceptSharing/{campaignId}`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/10dlc/campaign/acceptSharing/{campaignId}"
```

## Get Campaign Cost

`GET /10dlc/campaign/usecase/cost`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign/usecase/cost"
```

## Get campaign

Retrieve campaign details by `campaignId`.

`GET /10dlc/campaign/{campaignId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}"
```

## Update campaign

Update a campaign's properties by `campaignId`.

`PUT /10dlc/campaign/{campaignId}`

Optional: `autoRenewal` (boolean), `helpMessage` (string), `messageFlow` (string), `resellerId` (string), `sample1` (string), `sample2` (string), `sample3` (string), `sample4` (string), `sample5` (string), `webhookFailoverURL` (string), `webhookURL` (string)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}"
```

## Deactivate campaign

Terminate a campaign.

`DELETE /10dlc/campaign/{campaignId}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}"
```

## Submit campaign appeal for manual review

Submits an appeal for rejected native campaigns in TELNYX_FAILED or MNO_REJECTED status.

`POST /10dlc/campaign/{campaignId}/appeal` — Required: `appeal_reason`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "appeal_reason": "The website has been updated to include the required privacy policy and terms of service."
}' \
  "https://api.telnyx.com/v2/10dlc/campaign/5eb13888-32b7-4cab-95e6-d834dde21d64/appeal"
```

## Get Campaign Mno Metadata

Get the campaign metadata for each MNO it was submitted to.

`GET /10dlc/campaign/{campaignId}/mnoMetadata`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}/mnoMetadata"
```

## Get campaign operation status

Retrieve campaign's operation status at MNO level.

`GET /10dlc/campaign/{campaignId}/operationStatus`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}/operationStatus"
```

## Get OSR campaign attributes

`GET /10dlc/campaign/{campaignId}/osr/attributes`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}/osr/attributes"
```

## Get Sharing Status

`GET /10dlc/campaign/{campaignId}/sharing`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaign/{campaignId}/sharing"
```

## Submit Campaign

Before creating a campaign, use the [Qualify By Usecase endpoint](https://developers.telnyx.com/api-reference/campaign/qualify-by-usecase) to ensure that the brand you want to assign a new campaign...

`POST /10dlc/campaignBuilder` — Required: `brandId`, `description`, `usecase`

Optional: `ageGated` (boolean), `autoRenewal` (boolean), `directLending` (boolean), `embeddedLink` (boolean), `embeddedLinkSample` (string), `embeddedPhone` (boolean), `helpKeywords` (string), `helpMessage` (string), `messageFlow` (string), `mnoIds` (array[integer]), `numberPool` (boolean), `optinKeywords` (string), `optinMessage` (string), `optoutKeywords` (string), `optoutMessage` (string), `privacyPolicyLink` (string), `referenceId` (string), `resellerId` (string), `sample1` (string), `sample2` (string), `sample3` (string), `sample4` (string), `sample5` (string), `subUsecases` (array[string]), `subscriberHelp` (boolean), `subscriberOptin` (boolean), `subscriberOptout` (boolean), `tag` (array[string]), `termsAndConditions` (boolean), `termsAndConditionsLink` (string), `webhookFailoverURL` (string), `webhookURL` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "brandId": "string",
  "description": "string",
  "usecase": "string",
  "webhookURL": "https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
  "webhookFailoverURL": "https://webhook.com/93711262-23e5-4048-a966-c0b2a16d5963"
}' \
  "https://api.telnyx.com/v2/10dlc/campaignBuilder"
```

## Qualify By Usecase

This endpoint allows you to see whether or not the supplied brand is suitable for your desired campaign use case.

`GET /10dlc/campaignBuilder/brand/{brandId}/usecase/{usecase}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/campaignBuilder/brand/{brandId}/usecase/{usecase}"
```

## List shared partner campaigns

Get all partner campaigns you have shared to Telnyx in a paginated fashion

This endpoint is currently limited to only returning shared campaigns that Telnyx
has accepted.

`GET /10dlc/partnerCampaign/sharedByMe`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/partnerCampaign/sharedByMe"
```

## Get Sharing Status

`GET /10dlc/partnerCampaign/{campaignId}/sharing`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/partnerCampaign/{campaignId}/sharing"
```

## List Shared Campaigns

Retrieve all partner campaigns you have shared to Telnyx in a paginated fashion.

`GET /10dlc/partner_campaigns`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/partner_campaigns?sort=-assignedPhoneNumbersCount"
```

## Get Single Shared Campaign

Retrieve campaign details by `campaignId`.

`GET /10dlc/partner_campaigns/{campaignId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/partner_campaigns/{campaignId}"
```

## Update Single Shared Campaign

Update campaign details by `campaignId`.

`PATCH /10dlc/partner_campaigns/{campaignId}`

Optional: `webhookFailoverURL` (string), `webhookURL` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "webhookURL": "https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
  "webhookFailoverURL": "https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6"
}' \
  "https://api.telnyx.com/v2/10dlc/partner_campaigns/{campaignId}"
```

## Assign Messaging Profile To Campaign

This endpoint allows you to link all phone numbers associated with a Messaging Profile to a campaign.

`POST /10dlc/phoneNumberAssignmentByProfile` — Required: `messagingProfileId`

Optional: `campaignId` (string), `tcrCampaignId` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messagingProfileId": "4001767e-ce0f-4cae-9d5f-0d5e636e7809",
  "tcrCampaignId": "CWZTFH1",
  "campaignId": "4b300178-131c-d902-d54e-72d90ba1620j"
}' \
  "https://api.telnyx.com/v2/10dlc/phoneNumberAssignmentByProfile"
```

## Get Assignment Task Status

Check the status of the task associated with assigning all phone numbers on a messaging profile to a campaign by `taskId`.

`GET /10dlc/phoneNumberAssignmentByProfile/{taskId}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/phoneNumberAssignmentByProfile/{taskId}"
```

## Get Phone Number Status

Check the status of the individual phone number/campaign assignments associated with the supplied `taskId`.

`GET /10dlc/phoneNumberAssignmentByProfile/{taskId}/phoneNumbers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/phoneNumberAssignmentByProfile/{taskId}/phoneNumbers"
```

## List phone number campaigns

`GET /10dlc/phone_number_campaigns`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/phone_number_campaigns?sort=-phoneNumber"
```

## Create New Phone Number Campaign

`POST /10dlc/phone_number_campaigns` — Required: `phoneNumber`, `campaignId`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phoneNumber": "+18005550199",
  "campaignId": "4b300178-131c-d902-d54e-72d90ba1620j"
}' \
  "https://api.telnyx.com/v2/10dlc/phone_number_campaigns"
```

## Get Single Phone Number Campaign

Retrieve an individual phone number/campaign assignment by `phoneNumber`.

`GET /10dlc/phone_number_campaigns/{phoneNumber}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/10dlc/phone_number_campaigns/{phoneNumber}"
```

## Create New Phone Number Campaign

`PUT /10dlc/phone_number_campaigns/{phoneNumber}` — Required: `phoneNumber`, `campaignId`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phoneNumber": "+18005550199",
  "campaignId": "4b300178-131c-d902-d54e-72d90ba1620j"
}' \
  "https://api.telnyx.com/v2/10dlc/phone_number_campaigns/{phoneNumber}"
```

## Delete Phone Number Campaign

This endpoint allows you to remove a campaign assignment from the supplied `phoneNumber`.

`DELETE /10dlc/phone_number_campaigns/{phoneNumber}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/10dlc/phone_number_campaigns/{phoneNumber}"
```

---

## Webhooks

The following webhook events are sent to your configured webhook URL.
All webhooks include `telnyx-timestamp` and `telnyx-signature-ed25519` headers for verification (Standard Webhooks compatible).

| Event | Description |
|-------|-------------|
| `campaignStatusUpdate` | Campaign Status Update |

### Webhook payload fields

**`campaignStatusUpdate`**

| Field | Type | Description |
|-------|------|-------------|
| `brandId` | string | Brand ID associated with the campaign. |
| `campaignId` | string | The ID of the campaign. |
| `createDate` | string | Unix timestamp when campaign was created. |
| `cspId` | string | Alphanumeric identifier of the CSP associated with this campaign. |
| `isTMobileRegistered` | boolean | Indicates whether the campaign is registered with T-Mobile. |
| `type` | enum |  |
| `description` | string | Description of the event. |
| `status` | enum | The status of the campaign. |
