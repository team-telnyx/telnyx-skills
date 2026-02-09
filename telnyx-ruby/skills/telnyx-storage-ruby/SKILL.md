---
name: telnyx-storage-ruby
description: >-
  Manage cloud storage buckets and objects using the S3-compatible Telnyx
  Storage API. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: storage
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Storage - Ruby

## Installation

```bash
gem install telnyx
```

## Setup

```ruby
require "telnyx"

client = Telnyx::Client.new(
  api_key: ENV["TELNYX_API_KEY"], # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Create Presigned Object URL

Returns a timed and authenticated URL to download (GET) or upload (PUT) an object.

`POST /storage/buckets/{bucketName}/{objectName}/presigned_url`

```ruby
response = client.storage.buckets.create_presigned_url("", bucket_name: "")

puts(response)
```

## Get Bucket SSL Certificate

Returns the stored certificate detail of a bucket, if applicable.

`GET /storage/buckets/{bucketName}/ssl_certificate`

```ruby
ssl_certificate = client.storage.buckets.ssl_certificate.retrieve("")

puts(ssl_certificate)
```

## Add SSL Certificate

Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN.

`PUT /storage/buckets/{bucketName}/ssl_certificate`

```ruby
ssl_certificate = client.storage.buckets.ssl_certificate.create("")

puts(ssl_certificate)
```

## Remove SSL Certificate

Deletes an SSL certificate and its matching secret.

`DELETE /storage/buckets/{bucketName}/ssl_certificate`

```ruby
ssl_certificate = client.storage.buckets.ssl_certificate.delete("")

puts(ssl_certificate)
```

## Get API Usage

Returns the detail on API usage on a bucket of a particular time period, group by method category.

`GET /storage/buckets/{bucketName}/usage/api`

```ruby
response = client.storage.buckets.usage.get_api_usage(
  "",
  filter: {end_time: "2019-12-27T18:11:19.117Z", start_time: "2019-12-27T18:11:19.117Z"}
)

puts(response)
```

## Get Bucket Usage

Returns the amount of storage space and number of files a bucket takes up.

`GET /storage/buckets/{bucketName}/usage/storage`

```ruby
response = client.storage.buckets.usage.get_bucket_usage("")

puts(response)
```

## List Migration Source coverage

`GET /storage/migration_source_coverage`

```ruby
response = client.storage.list_migration_source_coverage

puts(response)
```

## List all Migration Sources

`GET /storage/migration_sources`

```ruby
migration_sources = client.storage.migration_sources.list

puts(migration_sources)
```

## Create a Migration Source

Create a source from which data can be migrated from.

`POST /storage/migration_sources` — Required: `provider`, `provider_auth`, `bucket_name`

```ruby
migration_source = client.storage.migration_sources.create(bucket_name: "bucket_name", provider: :aws, provider_auth: {})

puts(migration_source)
```

## Get a Migration Source

`GET /storage/migration_sources/{id}`

```ruby
migration_source = client.storage.migration_sources.retrieve("")

puts(migration_source)
```

## Delete a Migration Source

`DELETE /storage/migration_sources/{id}`

```ruby
migration_source = client.storage.migration_sources.delete("")

puts(migration_source)
```

## List all Migrations

`GET /storage/migrations`

```ruby
migrations = client.storage.migrations.list

puts(migrations)
```

## Create a Migration

Initiate a migration of data from an external provider into Telnyx Cloud Storage.

`POST /storage/migrations` — Required: `source_id`, `target_bucket_name`, `target_region`

```ruby
migration = client.storage.migrations.create(
  source_id: "source_id",
  target_bucket_name: "target_bucket_name",
  target_region: "target_region"
)

puts(migration)
```

## Get a Migration

`GET /storage/migrations/{id}`

```ruby
migration = client.storage.migrations.retrieve("")

puts(migration)
```

## Stop a Migration

`POST /storage/migrations/{id}/actions/stop`

```ruby
response = client.storage.migrations.actions.stop("")

puts(response)
```
