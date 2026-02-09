---
name: telnyx-fax-javascript
description: >-
  Send and receive faxes programmatically. Manage fax applications and media.
  This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: fax
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Fax - JavaScript

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

## List all Fax Applications

This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response.

`GET /fax_applications`

```javascript
// Automatically fetches more pages as needed.
for await (const faxApplication of client.faxApplications.list()) {
  console.log(faxApplication.id);
}
```

## Creates a Fax Application

Creates a new Fax Application based on the parameters sent in the request.

`POST /fax_applications` — Required: `application_name`, `webhook_event_url`

```javascript
const faxApplication = await client.faxApplications.create({
  application_name: 'fax-router',
  webhook_event_url: 'https://example.com',
});

console.log(faxApplication.data);
```

## Retrieve a Fax Application

Return the details of an existing Fax Application inside the 'data' attribute of the response.

`GET /fax_applications/{id}`

```javascript
const faxApplication = await client.faxApplications.retrieve('1293384261075731499');

console.log(faxApplication.data);
```

## Update a Fax Application

Updates settings of an existing Fax Application based on the parameters of the request.

`PATCH /fax_applications/{id}` — Required: `application_name`, `webhook_event_url`

```javascript
const faxApplication = await client.faxApplications.update('1293384261075731499', {
  application_name: 'fax-router',
  webhook_event_url: 'https://example.com',
});

console.log(faxApplication.data);
```

## Deletes a Fax Application

Permanently deletes a Fax Application.

`DELETE /fax_applications/{id}`

```javascript
const faxApplication = await client.faxApplications.delete('1293384261075731499');

console.log(faxApplication.data);
```

## View a list of faxes

`GET /faxes`

```javascript
// Automatically fetches more pages as needed.
for await (const fax of client.faxes.list()) {
  console.log(fax.id);
}
```

## Send a fax

Send a fax.

`POST /faxes` — Required: `connection_id`, `from`, `to`

```javascript
const fax = await client.faxes.create({
  connection_id: '234423',
  from: '+13125790015',
  to: '+13127367276',
});

console.log(fax.data);
```

## View a fax

`GET /faxes/{id}`

```javascript
const fax = await client.faxes.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(fax.data);
```

## Delete a fax

`DELETE /faxes/{id}`

```javascript
await client.faxes.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```

## Cancel a fax

Cancel the outbound fax that is in one of the following states: `queued`, `media.processed`, `originated` or `sending`

`POST /faxes/{id}/actions/cancel`

```javascript
const response = await client.faxes.actions.cancel('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(response.data);
```

## Refresh a fax

Refreshes the inbound fax's media_url when it has expired

`POST /faxes/{id}/actions/refresh`

```javascript
const response = await client.faxes.actions.refresh('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(response.data);
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
