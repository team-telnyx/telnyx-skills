---
name: telnyx-account-javascript
description: >-
  Manage account balance, payments, invoices, webhooks, and view audit logs and
  detail records. This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: account
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Account - JavaScript

## Installation

```bash
npm install telnyx
```

## Setup

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'], // This is the default and can be omitted
});
```

All examples below assume `client` is already initialized as shown above.

## List Audit Logs

Retrieve a list of audit log entries.

`GET /audit_events`

```javascript
// Automatically fetches more pages as needed.
for await (const auditEventListResponse of client.auditEvents.list()) {
  console.log(auditEventListResponse.id);
}
```

## Get user balance details

`GET /balance`

```javascript
const balance = await client.balance.retrieve();

console.log(balance.data);
```

## Search detail records

Search for any detail record across the Telnyx Platform

`GET /detail_records`

```javascript
// Automatically fetches more pages as needed.
for await (const detailRecordListResponse of client.detailRecords.list()) {
  console.log(detailRecordListResponse);
}
```

## List invoices

Retrieve a paginated list of invoices.

`GET /invoices`

```javascript
// Automatically fetches more pages as needed.
for await (const invoiceListResponse of client.invoices.list()) {
  console.log(invoiceListResponse.file_id);
}
```

## Get invoice by ID

Retrieve a single invoice by its unique identifier.

`GET /invoices/{id}`

```javascript
const invoice = await client.invoices.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(invoice.data);
```

## List auto recharge preferences

Returns the payment auto recharge preferences.

`GET /payments/auto_recharge_prefs`

```javascript
const autoRechargePrefs = await client.payment.autoRechargePrefs.list();

console.log(autoRechargePrefs.data);
```

## Update auto recharge preferences

Update payment auto recharge preferences.

`PATCH /payments/auto_recharge_prefs`

```javascript
const autoRechargePref = await client.payment.autoRechargePrefs.update();

console.log(autoRechargePref.data);
```

## List User Tags

List all user tags.

`GET /user_tags`

```javascript
const userTags = await client.userTags.list();

console.log(userTags.data);
```

## List webhook deliveries

Lists webhook_deliveries for the authenticated user

`GET /webhook_deliveries`

```javascript
// Automatically fetches more pages as needed.
for await (const webhookDeliveryListResponse of client.webhookDeliveries.list()) {
  console.log(webhookDeliveryListResponse.id);
}
```

## Find webhook_delivery details by ID

Provides webhook_delivery debug data, such as timestamps, delivery status and attempts.

`GET /webhook_deliveries/{id}`

```javascript
const webhookDelivery = await client.webhookDeliveries.retrieve(
  'C9C0797E-901D-4349-A33C-C2C8F31A92C2',
);

console.log(webhookDelivery.data);
```
