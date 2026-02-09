---
name: telnyx-storage-python
description: >-
  Manage cloud storage buckets and objects using the S3-compatible Telnyx
  Storage API. This skill provides Python SDK examples.
metadata:
  author: telnyx
  product: storage
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Storage - Python

## Installation

```bash
pip install telnyx
```

## Setup

```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),  # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Create Presigned Object URL

Returns a timed and authenticated URL to download (GET) or upload (PUT) an object.

`POST /storage/buckets/{bucketName}/{objectName}/presigned_url`

```python
response = client.storage.buckets.create_presigned_url(
    object_name="",
    bucket_name="",
)
print(response.content)
```

## Get Bucket SSL Certificate

Returns the stored certificate detail of a bucket, if applicable.

`GET /storage/buckets/{bucketName}/ssl_certificate`

```python
ssl_certificate = client.storage.buckets.ssl_certificate.retrieve(
    "",
)
print(ssl_certificate.data)
```

## Add SSL Certificate

Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN.

`PUT /storage/buckets/{bucketName}/ssl_certificate`

```python
ssl_certificate = client.storage.buckets.ssl_certificate.create(
    bucket_name="",
)
print(ssl_certificate.data)
```

## Remove SSL Certificate

Deletes an SSL certificate and its matching secret.

`DELETE /storage/buckets/{bucketName}/ssl_certificate`

```python
ssl_certificate = client.storage.buckets.ssl_certificate.delete(
    "",
)
print(ssl_certificate.data)
```

## Get API Usage

Returns the detail on API usage on a bucket of a particular time period, group by method category.

`GET /storage/buckets/{bucketName}/usage/api`

```python
from datetime import datetime

response = client.storage.buckets.usage.get_api_usage(
    bucket_name="",
    filter={
        "end_time": datetime.fromisoformat("2019-12-27T18:11:19.117"),
        "start_time": datetime.fromisoformat("2019-12-27T18:11:19.117"),
    },
)
print(response.data)
```

## Get Bucket Usage

Returns the amount of storage space and number of files a bucket takes up.

`GET /storage/buckets/{bucketName}/usage/storage`

```python
response = client.storage.buckets.usage.get_bucket_usage(
    "",
)
print(response.data)
```

## List Migration Source coverage

`GET /storage/migration_source_coverage`

```python
response = client.storage.list_migration_source_coverage()
print(response.data)
```

## List all Migration Sources

`GET /storage/migration_sources`

```python
migration_sources = client.storage.migration_sources.list()
print(migration_sources.data)
```

## Create a Migration Source

Create a source from which data can be migrated from.

`POST /storage/migration_sources` — Required: `provider`, `provider_auth`, `bucket_name`

```python
migration_source = client.storage.migration_sources.create(
    bucket_name="bucket_name",
    provider="aws",
    provider_auth={},
)
print(migration_source.data)
```

## Get a Migration Source

`GET /storage/migration_sources/{id}`

```python
migration_source = client.storage.migration_sources.retrieve(
    "",
)
print(migration_source.data)
```

## Delete a Migration Source

`DELETE /storage/migration_sources/{id}`

```python
migration_source = client.storage.migration_sources.delete(
    "",
)
print(migration_source.data)
```

## List all Migrations

`GET /storage/migrations`

```python
migrations = client.storage.migrations.list()
print(migrations.data)
```

## Create a Migration

Initiate a migration of data from an external provider into Telnyx Cloud Storage.

`POST /storage/migrations` — Required: `source_id`, `target_bucket_name`, `target_region`

```python
migration = client.storage.migrations.create(
    source_id="source_id",
    target_bucket_name="target_bucket_name",
    target_region="target_region",
)
print(migration.data)
```

## Get a Migration

`GET /storage/migrations/{id}`

```python
migration = client.storage.migrations.retrieve(
    "",
)
print(migration.data)
```

## Stop a Migration

`POST /storage/migrations/{id}/actions/stop`

```python
response = client.storage.migrations.actions.stop(
    "",
)
print(response.data)
```
