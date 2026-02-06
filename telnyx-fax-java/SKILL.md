---
name: telnyx-fax-java
description: >-
  Send and receive faxes programmatically. Manage fax applications and media.
  This skill provides Java SDK examples.
metadata:
  author: telnyx
  product: fax
  language: java
---

# Telnyx Fax - Java

## Installation

```bash
// Add to pom.xml or build.gradle - see https://github.com/team-telnyx/telnyx-java
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## List all Fax Applications

This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response.

`GET /fax_applications`

```java
import com.telnyx.sdk.models.faxapplications.FaxApplicationListPage;
import com.telnyx.sdk.models.faxapplications.FaxApplicationListParams;

FaxApplicationListPage page = client.faxApplications().list();
```

## Creates a Fax Application

Creates a new Fax Application based on the parameters sent in the request.

`POST /fax_applications` — Required: `application_name`, `webhook_event_url`

```java
import com.telnyx.sdk.models.faxapplications.FaxApplicationCreateParams;
import com.telnyx.sdk.models.faxapplications.FaxApplicationCreateResponse;

FaxApplicationCreateParams params = FaxApplicationCreateParams.builder()
    .applicationName("fax-router")
    .webhookEventUrl("https://example.com")
    .build();
FaxApplicationCreateResponse faxApplication = client.faxApplications().create(params);
```

## Retrieve a Fax Application

Return the details of an existing Fax Application inside the 'data' attribute of the response.

`GET /fax_applications/{id}`

```java
import com.telnyx.sdk.models.faxapplications.FaxApplicationRetrieveParams;
import com.telnyx.sdk.models.faxapplications.FaxApplicationRetrieveResponse;

FaxApplicationRetrieveResponse faxApplication = client.faxApplications().retrieve("1293384261075731499");
```

## Update a Fax Application

Updates settings of an existing Fax Application based on the parameters of the request.

`PATCH /fax_applications/{id}` — Required: `application_name`, `webhook_event_url`

```java
import com.telnyx.sdk.models.faxapplications.FaxApplicationUpdateParams;
import com.telnyx.sdk.models.faxapplications.FaxApplicationUpdateResponse;

FaxApplicationUpdateParams params = FaxApplicationUpdateParams.builder()
    .id("1293384261075731499")
    .applicationName("fax-router")
    .webhookEventUrl("https://example.com")
    .build();
FaxApplicationUpdateResponse faxApplication = client.faxApplications().update(params);
```

## Deletes a Fax Application

Permanently deletes a Fax Application.

`DELETE /fax_applications/{id}`

```java
import com.telnyx.sdk.models.faxapplications.FaxApplicationDeleteParams;
import com.telnyx.sdk.models.faxapplications.FaxApplicationDeleteResponse;

FaxApplicationDeleteResponse faxApplication = client.faxApplications().delete("1293384261075731499");
```

## View a list of faxes

`GET /faxes`

```java
import com.telnyx.sdk.models.faxes.FaxListPage;
import com.telnyx.sdk.models.faxes.FaxListParams;

FaxListPage page = client.faxes().list();
```

## Send a fax

Send a fax.

`POST /faxes` — Required: `connection_id`, `from`, `to`

```java
import com.telnyx.sdk.models.faxes.FaxCreateParams;
import com.telnyx.sdk.models.faxes.FaxCreateResponse;

FaxCreateParams params = FaxCreateParams.builder()
    .connectionId("234423")
    .from("+13125790015")
    .to("+13127367276")
    .build();
FaxCreateResponse fax = client.faxes().create(params);
```

## View a fax

`GET /faxes/{id}`

```java
import com.telnyx.sdk.models.faxes.FaxRetrieveParams;
import com.telnyx.sdk.models.faxes.FaxRetrieveResponse;

FaxRetrieveResponse fax = client.faxes().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Delete a fax

`DELETE /faxes/{id}`

```java
import com.telnyx.sdk.models.faxes.FaxDeleteParams;

client.faxes().delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Cancel a fax

Cancel the outbound fax that is in one of the following states: `queued`, `media.processed`, `originated` or `sending`

`POST /faxes/{id}/actions/cancel`

```java
import com.telnyx.sdk.models.faxes.actions.ActionCancelParams;
import com.telnyx.sdk.models.faxes.actions.ActionCancelResponse;

ActionCancelResponse response = client.faxes().actions().cancel("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Refresh a fax

Refreshes the inbound fax's media_url when it has expired

`POST /faxes/{id}/actions/refresh`

```java
import com.telnyx.sdk.models.faxes.actions.ActionRefreshParams;
import com.telnyx.sdk.models.faxes.actions.ActionRefreshResponse;

ActionRefreshResponse response = client.faxes().actions().refresh("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
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
