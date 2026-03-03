---
name: telnyx-storage-curl
description: >-
  Manage cloud storage buckets and objects using the S3-compatible Telnyx
  Storage API. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: storage
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Storage - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Get Bucket SSL Certificate

Returns the stored certificate detail of a bucket, if applicable.

`GET /storage/buckets/{bucketName}/ssl_certificate`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/storage/buckets/{bucketName}/ssl_certificate"
```

## Add SSL Certificate

Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN.

`PUT /storage/buckets/{bucketName}/ssl_certificate`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "certificate=@/path/to/file" \
  -F "private_key=@/path/to/file" \
  "https://api.telnyx.com/v2/storage/buckets/{bucketName}/ssl_certificate"
```

## Remove SSL Certificate

Deletes an SSL certificate and its matching secret.

`DELETE /storage/buckets/{bucketName}/ssl_certificate`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/storage/buckets/{bucketName}/ssl_certificate"
```

## Get API Usage

Returns the detail on API usage on a bucket of a particular time period, group by method category.

`GET /storage/buckets/{bucketName}/usage/api`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/storage/buckets/{bucketName}/usage/api?filter={'start_time': '2020-01-01T00:00:00.000Z', 'end_time': '2020-01-01T00:00:00.000Z'}"
```

## Get Bucket Usage

Returns the amount of storage space and number of files a bucket takes up.

`GET /storage/buckets/{bucketName}/usage/storage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/storage/buckets/{bucketName}/usage/storage"
```

## Create Presigned Object URL

Returns a timed and authenticated URL to download (GET) or upload (PUT) an object.

`POST /storage/buckets/{bucketName}/{objectName}/presigned_url`

Optional: `ttl` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "ttl": 60
}' \
  "https://api.telnyx.com/v2/storage/buckets/{bucketName}/{objectName}/presigned_url"
```
