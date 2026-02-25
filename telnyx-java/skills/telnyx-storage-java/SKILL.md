---
name: telnyx-storage-java
description: >-
  Manage cloud storage buckets and objects using the S3-compatible Telnyx
  Storage API. This skill provides Java SDK examples.
metadata:
  author: telnyx
  product: storage
  language: java
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Storage - Java

## Installation

```text
// See https://github.com/team-telnyx/telnyx-java for Maven/Gradle setup
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## Create Presigned Object URL

Returns a timed and authenticated URL to download (GET) or upload (PUT) an object.

`POST /storage/buckets/{bucketName}/{objectName}/presigned_url`

Optional: `ttl` (integer)

```java
import com.telnyx.sdk.models.storage.buckets.BucketCreatePresignedUrlParams;
import com.telnyx.sdk.models.storage.buckets.BucketCreatePresignedUrlResponse;

BucketCreatePresignedUrlParams params = BucketCreatePresignedUrlParams.builder()
    .bucketName("")
    .objectName("")
    .build();
BucketCreatePresignedUrlResponse response = client.storage().buckets().createPresignedUrl(params);
```

## Get Bucket SSL Certificate

Returns the stored certificate detail of a bucket, if applicable.

`GET /storage/buckets/{bucketName}/ssl_certificate`

```java
import com.telnyx.sdk.models.storage.buckets.sslcertificate.SslCertificateRetrieveParams;
import com.telnyx.sdk.models.storage.buckets.sslcertificate.SslCertificateRetrieveResponse;

SslCertificateRetrieveResponse sslCertificate = client.storage().buckets().sslCertificate().retrieve("");
```

## Add SSL Certificate

Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN.

`PUT /storage/buckets/{bucketName}/ssl_certificate`

```java
import com.telnyx.sdk.models.storage.buckets.sslcertificate.SslCertificateCreateParams;
import com.telnyx.sdk.models.storage.buckets.sslcertificate.SslCertificateCreateResponse;

SslCertificateCreateResponse sslCertificate = client.storage().buckets().sslCertificate().create("");
```

## Remove SSL Certificate

Deletes an SSL certificate and its matching secret.

`DELETE /storage/buckets/{bucketName}/ssl_certificate`

```java
import com.telnyx.sdk.models.storage.buckets.sslcertificate.SslCertificateDeleteParams;
import com.telnyx.sdk.models.storage.buckets.sslcertificate.SslCertificateDeleteResponse;

SslCertificateDeleteResponse sslCertificate = client.storage().buckets().sslCertificate().delete("");
```

## Get API Usage

Returns the detail on API usage on a bucket of a particular time period, group by method category.

`GET /storage/buckets/{bucketName}/usage/api`

```java
import com.telnyx.sdk.models.storage.buckets.usage.UsageGetApiUsageParams;
import com.telnyx.sdk.models.storage.buckets.usage.UsageGetApiUsageResponse;
import java.time.OffsetDateTime;

UsageGetApiUsageParams params = UsageGetApiUsageParams.builder()
    .bucketName("")
    .filter(UsageGetApiUsageParams.Filter.builder()
        .endTime(OffsetDateTime.parse("2019-12-27T18:11:19.117Z"))
        .startTime(OffsetDateTime.parse("2019-12-27T18:11:19.117Z"))
        .build())
    .build();
UsageGetApiUsageResponse response = client.storage().buckets().usage().getApiUsage(params);
```

## Get Bucket Usage

Returns the amount of storage space and number of files a bucket takes up.

`GET /storage/buckets/{bucketName}/usage/storage`

```java
import com.telnyx.sdk.models.storage.buckets.usage.UsageGetBucketUsageParams;
import com.telnyx.sdk.models.storage.buckets.usage.UsageGetBucketUsageResponse;

UsageGetBucketUsageResponse response = client.storage().buckets().usage().getBucketUsage("");
```

## List Migration Source coverage

`GET /storage/migration_source_coverage`

```java
import com.telnyx.sdk.models.storage.StorageListMigrationSourceCoverageParams;
import com.telnyx.sdk.models.storage.StorageListMigrationSourceCoverageResponse;

StorageListMigrationSourceCoverageResponse response = client.storage().listMigrationSourceCoverage();
```

## List all Migration Sources

`GET /storage/migration_sources`

```java
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceListParams;
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceListResponse;

MigrationSourceListResponse migrationSources = client.storage().migrationSources().list();
```

## Create a Migration Source

Create a source from which data can be migrated from.

`POST /storage/migration_sources` — Required: `provider`, `provider_auth`, `bucket_name`

Optional: `id` (string), `source_region` (string)

```java
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceCreateParams;
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceCreateResponse;
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceParams;

MigrationSourceParams params = MigrationSourceParams.builder()
    .bucketName("bucket_name")
    .provider(MigrationSourceParams.Provider.AWS)
    .providerAuth(MigrationSourceParams.ProviderAuth.builder().build())
    .build();
MigrationSourceCreateResponse migrationSource = client.storage().migrationSources().create(params);
```

## Get a Migration Source

`GET /storage/migration_sources/{id}`

```java
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceRetrieveParams;
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceRetrieveResponse;

MigrationSourceRetrieveResponse migrationSource = client.storage().migrationSources().retrieve("");
```

## Delete a Migration Source

`DELETE /storage/migration_sources/{id}`

```java
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceDeleteParams;
import com.telnyx.sdk.models.storage.migrationsources.MigrationSourceDeleteResponse;

MigrationSourceDeleteResponse migrationSource = client.storage().migrationSources().delete("");
```

## List all Migrations

`GET /storage/migrations`

```java
import com.telnyx.sdk.models.storage.migrations.MigrationListParams;
import com.telnyx.sdk.models.storage.migrations.MigrationListResponse;

MigrationListResponse migrations = client.storage().migrations().list();
```

## Create a Migration

Initiate a migration of data from an external provider into Telnyx Cloud Storage.

`POST /storage/migrations` — Required: `source_id`, `target_bucket_name`, `target_region`

Optional: `bytes_migrated` (integer), `bytes_to_migrate` (integer), `created_at` (date-time), `eta` (date-time), `id` (string), `last_copy` (date-time), `refresh` (boolean), `speed` (integer), `status` (enum)

```java
import com.telnyx.sdk.models.storage.migrations.MigrationCreateParams;
import com.telnyx.sdk.models.storage.migrations.MigrationCreateResponse;
import com.telnyx.sdk.models.storage.migrations.MigrationParams;

MigrationParams params = MigrationParams.builder()
    .sourceId("source_id")
    .targetBucketName("target_bucket_name")
    .targetRegion("target_region")
    .build();
MigrationCreateResponse migration = client.storage().migrations().create(params);
```

## Get a Migration

`GET /storage/migrations/{id}`

```java
import com.telnyx.sdk.models.storage.migrations.MigrationRetrieveParams;
import com.telnyx.sdk.models.storage.migrations.MigrationRetrieveResponse;

MigrationRetrieveResponse migration = client.storage().migrations().retrieve("");
```

## Stop a Migration

`POST /storage/migrations/{id}/actions/stop`

```java
import com.telnyx.sdk.models.storage.migrations.actions.ActionStopParams;
import com.telnyx.sdk.models.storage.migrations.actions.ActionStopResponse;

ActionStopResponse response = client.storage().migrations().actions().stop("");
```
