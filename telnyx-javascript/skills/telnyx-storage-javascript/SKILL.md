---
name: telnyx-storage-javascript
description: >-
  Manage cloud storage buckets and objects using the S3-compatible Telnyx
  Storage API. This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: storage
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Storage - JavaScript

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

## Create Presigned Object URL

Returns a timed and authenticated URL to download (GET) or upload (PUT) an object.

`POST /storage/buckets/{bucketName}/{objectName}/presigned_url`

Optional: `ttl` (integer)

```javascript
const response = await client.storage.buckets.createPresignedURL('', { bucketName: '' });

console.log(response.content);
```

## Get Bucket SSL Certificate

Returns the stored certificate detail of a bucket, if applicable.

`GET /storage/buckets/{bucketName}/ssl_certificate`

```javascript
const sslCertificate = await client.storage.buckets.sslCertificate.retrieve('');

console.log(sslCertificate.data);
```

## Add SSL Certificate

Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN.

`PUT /storage/buckets/{bucketName}/ssl_certificate`

```javascript
const sslCertificate = await client.storage.buckets.sslCertificate.create('');

console.log(sslCertificate.data);
```

## Remove SSL Certificate

Deletes an SSL certificate and its matching secret.

`DELETE /storage/buckets/{bucketName}/ssl_certificate`

```javascript
const sslCertificate = await client.storage.buckets.sslCertificate.delete('');

console.log(sslCertificate.data);
```

## Get API Usage

Returns the detail on API usage on a bucket of a particular time period, group by method category.

`GET /storage/buckets/{bucketName}/usage/api`

```javascript
const response = await client.storage.buckets.usage.getAPIUsage('', {
  filter: { end_time: '2019-12-27T18:11:19.117Z', start_time: '2019-12-27T18:11:19.117Z' },
});

console.log(response.data);
```

## Get Bucket Usage

Returns the amount of storage space and number of files a bucket takes up.

`GET /storage/buckets/{bucketName}/usage/storage`

```javascript
const response = await client.storage.buckets.usage.getBucketUsage('');

console.log(response.data);
```

## List Migration Source coverage

`GET /storage/migration_source_coverage`

```javascript
const response = await client.storage.listMigrationSourceCoverage();

console.log(response.data);
```

## List all Migration Sources

`GET /storage/migration_sources`

```javascript
const migrationSources = await client.storage.migrationSources.list();

console.log(migrationSources.data);
```

## Create a Migration Source

Create a source from which data can be migrated from.

`POST /storage/migration_sources` — Required: `provider`, `provider_auth`, `bucket_name`

Optional: `id` (string), `source_region` (string)

```javascript
const migrationSource = await client.storage.migrationSources.create({
  bucket_name: 'bucket_name',
  provider: 'aws',
  provider_auth: {},
});

console.log(migrationSource.data);
```

## Get a Migration Source

`GET /storage/migration_sources/{id}`

```javascript
const migrationSource = await client.storage.migrationSources.retrieve('');

console.log(migrationSource.data);
```

## Delete a Migration Source

`DELETE /storage/migration_sources/{id}`

```javascript
const migrationSource = await client.storage.migrationSources.delete('');

console.log(migrationSource.data);
```

## List all Migrations

`GET /storage/migrations`

```javascript
const migrations = await client.storage.migrations.list();

console.log(migrations.data);
```

## Create a Migration

Initiate a migration of data from an external provider into Telnyx Cloud Storage.

`POST /storage/migrations` — Required: `source_id`, `target_bucket_name`, `target_region`

Optional: `bytes_migrated` (integer), `bytes_to_migrate` (integer), `created_at` (date-time), `eta` (date-time), `id` (string), `last_copy` (date-time), `refresh` (boolean), `speed` (integer), `status` (enum)

```javascript
const migration = await client.storage.migrations.create({
  source_id: 'source_id',
  target_bucket_name: 'target_bucket_name',
  target_region: 'target_region',
});

console.log(migration.data);
```

## Get a Migration

`GET /storage/migrations/{id}`

```javascript
const migration = await client.storage.migrations.retrieve('');

console.log(migration.data);
```

## Stop a Migration

`POST /storage/migrations/{id}/actions/stop`

```javascript
const response = await client.storage.migrations.actions.stop('');

console.log(response.data);
```
