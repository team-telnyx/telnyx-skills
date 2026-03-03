---
name: telnyx-messaging-hosted-curl
description: >-
  Set up hosted SMS numbers, toll-free verification, and RCS messaging. Use when
  migrating numbers or enabling rich messaging features. This skill provides
  REST API (curl) examples.
metadata:
  author: telnyx
  product: messaging-hosted
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Messaging Hosted - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Send an RCS message

`POST /messages/rcs` — Required: `agent_id`, `to`, `messaging_profile_id`, `agent_message`

Optional: `mms_fallback` (object), `sms_fallback` (object), `type` (enum), `webhook_url` (url)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "agent_id": "Agent007",
  "to": "+13125551234",
  "messaging_profile_id": "string",
  "type": "RCS",
  "agent_message": {}
}' \
  "https://api.telnyx.com/v2/messages/rcs"
```

## Generate RCS deeplink

Generate a deeplink URL that can be used to start an RCS conversation with a specific agent.

`GET /messages/rcs/deeplinks/{agent_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}?phone_number=%2B18445550001&body=hello%20world"
```

## List all RCS agents

`GET /messaging/rcs/agents`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging/rcs/agents"
```

## Retrieve an RCS agent

`GET /messaging/rcs/agents/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging/rcs/agents/{id}"
```

## Modify an RCS agent

`PATCH /messaging/rcs/agents/{id}`

Optional: `profile_id` (uuid), `webhook_failover_url` (url), `webhook_url` (url)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "profile_id": "4001932a-b8a3-42fc-9389-021be6388909",
  "webhook_url": "http://example.com",
  "webhook_failover_url": "http://example.com"
}' \
  "https://api.telnyx.com/v2/messaging/rcs/agents/{id}"
```

## Check RCS capabilities (batch)

`POST /messaging/rcs/bulk_capabilities` — Required: `agent_id`, `phone_numbers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "agent_id": "TestAgent",
  "phone_numbers": [
    "+13125551234"
  ]
}' \
  "https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities"
```

## Check RCS capabilities

`GET /messaging/rcs/capabilities/{agent_id}/{phone_number}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging/rcs/capabilities/{agent_id}/{phone_number}"
```

## Add RCS test number

Adds a test phone number to an RCS agent for testing purposes.

`PUT /messaging/rcs/test_number_invite/{id}/{phone_number}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/messaging/rcs/test_number_invite/{id}/{phone_number}"
```

## List messaging hosted number orders

`GET /messaging_hosted_number_orders`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_hosted_number_orders"
```

## Create a messaging hosted number order

`POST /messaging_hosted_number_orders`

Optional: `messaging_profile_id` (string), `phone_numbers` (array[string])

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders"
```

## Check hosted messaging eligibility

`POST /messaging_hosted_number_orders/eligibility_numbers_check` — Required: `phone_numbers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check"
```

## Retrieve a messaging hosted number order

`GET /messaging_hosted_number_orders/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_hosted_number_orders/{id}"
```

## Delete a messaging hosted number order

Delete a messaging hosted number order and all associated phone numbers.

`DELETE /messaging_hosted_number_orders/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{id}"
```

## Upload hosted number document

`POST /messaging_hosted_number_orders/{id}/actions/file_upload`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "loa=@/path/to/file" \
  -F "bill=@/path/to/file" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{id}/actions/file_upload"
```

## Validate hosted number codes

Validate the verification codes sent to the numbers of the hosted order.

`POST /messaging_hosted_number_orders/{id}/validation_codes` — Required: `verification_codes`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "verification_codes": [
    {}
  ]
}' \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{id}/validation_codes"
```

## Create hosted number verification codes

Create verification codes to validate numbers of the hosted order.

`POST /messaging_hosted_number_orders/{id}/verification_codes` — Required: `phone_numbers`, `verification_method`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "phone_numbers": [
    "string"
  ],
  "verification_method": "sms"
}' \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{id}/verification_codes"
```

## Delete a messaging hosted number

`DELETE /messaging_hosted_numbers/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/messaging_hosted_numbers/{id}"
```

## List Verification Requests

Get a list of previously-submitted tollfree verification requests

`GET /messaging_tollfree/verification/requests`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_tollfree/verification/requests"
```

## Submit Verification Request

Submit a new tollfree verification request

`POST /messaging_tollfree/verification/requests` — Required: `businessName`, `corporateWebsite`, `businessAddr1`, `businessCity`, `businessState`, `businessZip`, `businessContactFirstName`, `businessContactLastName`, `businessContactEmail`, `businessContactPhone`, `messageVolume`, `phoneNumbers`, `useCase`, `useCaseSummary`, `productionMessageContent`, `optInWorkflow`, `optInWorkflowImageURLs`, `additionalInformation`

Optional: `ageGatedContent` (boolean), `businessAddr2` (string), `businessRegistrationCountry` (['string', 'null']), `businessRegistrationNumber` (['string', 'null']), `businessRegistrationType` (['string', 'null']), `campaignVerifyAuthorizationToken` (['string', 'null']), `doingBusinessAs` (['string', 'null']), `entityType` (object), `helpMessageResponse` (['string', 'null']), `isvReseller` (['string', 'null']), `optInConfirmationResponse` (['string', 'null']), `optInKeywords` (['string', 'null']), `privacyPolicyURL` (['string', 'null']), `termsAndConditionURL` (['string', 'null']), `webhookUrl` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "businessName": "Telnyx LLC",
  "corporateWebsite": "http://example.com",
  "businessAddr1": "600 Congress Avenue",
  "businessAddr2": "14th Floor",
  "businessCity": "Austin",
  "businessState": "Texas",
  "businessZip": "78701",
  "businessContactFirstName": "John",
  "businessContactLastName": "Doe",
  "businessContactEmail": "email@example.com",
  "businessContactPhone": "+18005550100",
  "messageVolume": "100,000",
  "phoneNumbers": [
    {
      "phoneNumber": "+18773554398"
    },
    {
      "phoneNumber": "+18773554399"
    }
  ],
  "useCase": "2FA",
  "useCaseSummary": "This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
  "productionMessageContent": "Your Telnyx OTP is XXXX",
  "optInWorkflow": "User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
  "optInWorkflowImageURLs": [
    {
      "url": "https://telnyx.com/sign-up"
    },
    {
      "url": "https://telnyx.com/company/data-privacy"
    }
  ],
  "additionalInformation": "string",
  "webhookUrl": "http://example-webhook.com",
  "businessRegistrationNumber": "12-3456789",
  "businessRegistrationType": "EIN",
  "businessRegistrationCountry": "US",
  "doingBusinessAs": "Acme Services",
  "optInConfirmationResponse": "You have successfully opted in to receive messages from Acme Corp",
  "helpMessageResponse": "Reply HELP for assistance or STOP to unsubscribe. Contact: support@example.com",
  "privacyPolicyURL": "https://example.com/privacy",
  "termsAndConditionURL": "https://example.com/terms",
  "optInKeywords": "START, YES, SUBSCRIBE",
  "campaignVerifyAuthorizationToken": "cv_token_abc123xyz"
}' \
  "https://api.telnyx.com/v2/messaging_tollfree/verification/requests"
```

## Get Verification Request

Get a single verification request by its ID.

`GET /messaging_tollfree/verification/requests/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_tollfree/verification/requests/{id}"
```

## Update Verification Request

Update an existing tollfree verification request.

`PATCH /messaging_tollfree/verification/requests/{id}` — Required: `businessName`, `corporateWebsite`, `businessAddr1`, `businessCity`, `businessState`, `businessZip`, `businessContactFirstName`, `businessContactLastName`, `businessContactEmail`, `businessContactPhone`, `messageVolume`, `phoneNumbers`, `useCase`, `useCaseSummary`, `productionMessageContent`, `optInWorkflow`, `optInWorkflowImageURLs`, `additionalInformation`

Optional: `ageGatedContent` (boolean), `businessAddr2` (string), `businessRegistrationCountry` (['string', 'null']), `businessRegistrationNumber` (['string', 'null']), `businessRegistrationType` (['string', 'null']), `campaignVerifyAuthorizationToken` (['string', 'null']), `doingBusinessAs` (['string', 'null']), `entityType` (object), `helpMessageResponse` (['string', 'null']), `isvReseller` (['string', 'null']), `optInConfirmationResponse` (['string', 'null']), `optInKeywords` (['string', 'null']), `privacyPolicyURL` (['string', 'null']), `termsAndConditionURL` (['string', 'null']), `webhookUrl` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "businessName": "Telnyx LLC",
  "corporateWebsite": "http://example.com",
  "businessAddr1": "600 Congress Avenue",
  "businessAddr2": "14th Floor",
  "businessCity": "Austin",
  "businessState": "Texas",
  "businessZip": "78701",
  "businessContactFirstName": "John",
  "businessContactLastName": "Doe",
  "businessContactEmail": "email@example.com",
  "businessContactPhone": "+18005550100",
  "messageVolume": "100,000",
  "phoneNumbers": [
    {
      "phoneNumber": "+18773554398"
    },
    {
      "phoneNumber": "+18773554399"
    }
  ],
  "useCase": "2FA",
  "useCaseSummary": "This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
  "productionMessageContent": "Your Telnyx OTP is XXXX",
  "optInWorkflow": "User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
  "optInWorkflowImageURLs": [
    {
      "url": "https://telnyx.com/sign-up"
    },
    {
      "url": "https://telnyx.com/company/data-privacy"
    }
  ],
  "additionalInformation": "string",
  "webhookUrl": "http://example-webhook.com",
  "businessRegistrationNumber": "12-3456789",
  "businessRegistrationType": "EIN",
  "businessRegistrationCountry": "US",
  "doingBusinessAs": "Acme Services",
  "optInConfirmationResponse": "You have successfully opted in to receive messages from Acme Corp",
  "helpMessageResponse": "Reply HELP for assistance or STOP to unsubscribe. Contact: support@example.com",
  "privacyPolicyURL": "https://example.com/privacy",
  "termsAndConditionURL": "https://example.com/terms",
  "optInKeywords": "START, YES, SUBSCRIBE",
  "campaignVerifyAuthorizationToken": "cv_token_abc123xyz"
}' \
  "https://api.telnyx.com/v2/messaging_tollfree/verification/requests/{id}"
```

## Delete Verification Request

Delete a verification request

A request may only be deleted when when the request is in the "rejected" state.

`DELETE /messaging_tollfree/verification/requests/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/messaging_tollfree/verification/requests/{id}"
```

## Get Verification Request Status History

Get the history of status changes for a verification request.

`GET /messaging_tollfree/verification/requests/{id}/status_history`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_tollfree/verification/requests/{id}/status_history"
```

## List messaging URL domains

`GET /messaging_url_domains`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/messaging_url_domains"
```
