---
name: telnyx-account-management-curl
description: >-
  Manage sub-accounts for reseller and enterprise scenarios. This skill provides
  REST API (curl) examples.
metadata:
  author: telnyx
  product: account-management
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account Management - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Lists accounts managed by the current user.

Lists the accounts managed by the current user.

`GET /managed_accounts`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/managed_accounts?filter={'email': {'contains': 'john'}, 'organization_name': {'eq': 'Example Company LLC'}}&sort=email&include_cancelled_accounts=True"
```

## Create a new managed account.

Create a new managed account owned by the authenticated user.

`POST /managed_accounts` — Required: `business_name`

Optional: `email` (string), `managed_account_allow_custom_pricing` (boolean), `password` (string), `rollup_billing` (boolean)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "email": "new_managed_account@customer.org",
  "password": "3jVjLq!tMuWKyWx4NN*CvhnB",
  "business_name": "Larry's Cat Food Inc",
  "managed_account_allow_custom_pricing": false,
  "rollup_billing": false
}' \
  "https://api.telnyx.com/v2/managed_accounts"
```

## Display information about allocatable global outbound channels for the current user.

`GET /managed_accounts/allocatable_global_outbound_channels`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/managed_accounts/allocatable_global_outbound_channels"
```

## Retrieve a managed account

Retrieves the details of a single managed account.

`GET /managed_accounts/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/managed_accounts/{id}"
```

## Update a managed account

Update a single managed account.

`PATCH /managed_accounts/{id}`

Optional: `managed_account_allow_custom_pricing` (boolean)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "managed_account_allow_custom_pricing": false
}' \
  "https://api.telnyx.com/v2/managed_accounts/{id}"
```

## Disables a managed account

Disables a managed account, forbidding it to use Telnyx services, including sending or receiving phone calls and SMS messages.

`POST /managed_accounts/{id}/actions/disable`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/managed_accounts/{id}/actions/disable"
```

## Enables a managed account

Enables a managed account and its sub-users to use Telnyx services.

`POST /managed_accounts/{id}/actions/enable`

Optional: `reenable_all_connections` (boolean)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "reenable_all_connections": true
}' \
  "https://api.telnyx.com/v2/managed_accounts/{id}/actions/enable"
```

## Update the amount of allocatable global outbound channels allocated to a specific managed account.

`PATCH /managed_accounts/{id}/update_global_channel_limit`

Optional: `channel_limit` (integer)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "channel_limit": 30
}' \
  "https://api.telnyx.com/v2/managed_accounts/{id}/update_global_channel_limit"
```

## List organization users

Returns a list of the users in your organization.

`GET /organizations/users`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/organizations/users"
```

## Get organization users groups report

Returns a report of all users in your organization with their group memberships.

`GET /organizations/users/users_groups_report`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/organizations/users/users_groups_report"
```

## Get organization user

Returns a user in your organization.

`GET /organizations/users/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/organizations/users/{id}"
```

## Delete organization user

Deletes a user in your organization.

`POST /organizations/users/{id}/actions/remove`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/organizations/users/{id}/actions/remove"
```
