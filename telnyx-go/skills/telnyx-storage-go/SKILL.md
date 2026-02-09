---
name: telnyx-storage-go
description: >-
  Manage cloud storage buckets and objects using the S3-compatible Telnyx
  Storage API. This skill provides Go SDK examples.
metadata:
  author: telnyx
  product: storage
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Storage - Go

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
import (
  "context"
  "fmt"
  "os"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

client := telnyx.NewClient(
  option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
)
```

All examples below assume `client` is already initialized as shown above.

## Create Presigned Object URL

Returns a timed and authenticated URL to download (GET) or upload (PUT) an object.

`POST /storage/buckets/{bucketName}/{objectName}/presigned_url`

```go
	response, err := client.Storage.Buckets.NewPresignedURL(
		context.TODO(),
		"",
		telnyx.StorageBucketNewPresignedURLParams{
			BucketName: "",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Content)
```

## Get Bucket SSL Certificate

Returns the stored certificate detail of a bucket, if applicable.

`GET /storage/buckets/{bucketName}/ssl_certificate`

```go
	sslCertificate, err := client.Storage.Buckets.SslCertificate.Get(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", sslCertificate.Data)
```

## Add SSL Certificate

Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN.

`PUT /storage/buckets/{bucketName}/ssl_certificate`

```go
	sslCertificate, err := client.Storage.Buckets.SslCertificate.New(
		context.TODO(),
		"",
		telnyx.StorageBucketSslCertificateNewParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", sslCertificate.Data)
```

## Remove SSL Certificate

Deletes an SSL certificate and its matching secret.

`DELETE /storage/buckets/{bucketName}/ssl_certificate`

```go
	sslCertificate, err := client.Storage.Buckets.SslCertificate.Delete(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", sslCertificate.Data)
```

## Get API Usage

Returns the detail on API usage on a bucket of a particular time period, group by method category.

`GET /storage/buckets/{bucketName}/usage/api`

```go
	response, err := client.Storage.Buckets.Usage.GetAPIUsage(
		context.TODO(),
		"",
		telnyx.StorageBucketUsageGetAPIUsageParams{
			Filter: telnyx.StorageBucketUsageGetAPIUsageParamsFilter{
				EndTime:   time.Now(),
				StartTime: time.Now(),
			},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Get Bucket Usage

Returns the amount of storage space and number of files a bucket takes up.

`GET /storage/buckets/{bucketName}/usage/storage`

```go
	response, err := client.Storage.Buckets.Usage.GetBucketUsage(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List Migration Source coverage

`GET /storage/migration_source_coverage`

```go
	response, err := client.Storage.ListMigrationSourceCoverage(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List all Migration Sources

`GET /storage/migration_sources`

```go
	migrationSources, err := client.Storage.MigrationSources.List(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migrationSources.Data)
```

## Create a Migration Source

Create a source from which data can be migrated from.

`POST /storage/migration_sources` — Required: `provider`, `provider_auth`, `bucket_name`

```go
	migrationSource, err := client.Storage.MigrationSources.New(context.TODO(), telnyx.StorageMigrationSourceNewParams{
		MigrationSourceParams: telnyx.MigrationSourceParams{
			BucketName:   "bucket_name",
			Provider:     telnyx.MigrationSourceParamsProviderAws,
			ProviderAuth: telnyx.MigrationSourceParamsProviderAuth{},
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migrationSource.Data)
```

## Get a Migration Source

`GET /storage/migration_sources/{id}`

```go
	migrationSource, err := client.Storage.MigrationSources.Get(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migrationSource.Data)
```

## Delete a Migration Source

`DELETE /storage/migration_sources/{id}`

```go
	migrationSource, err := client.Storage.MigrationSources.Delete(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migrationSource.Data)
```

## List all Migrations

`GET /storage/migrations`

```go
	migrations, err := client.Storage.Migrations.List(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migrations.Data)
```

## Create a Migration

Initiate a migration of data from an external provider into Telnyx Cloud Storage.

`POST /storage/migrations` — Required: `source_id`, `target_bucket_name`, `target_region`

```go
	migration, err := client.Storage.Migrations.New(context.TODO(), telnyx.StorageMigrationNewParams{
		MigrationParams: telnyx.MigrationParams{
			SourceID:         "source_id",
			TargetBucketName: "target_bucket_name",
			TargetRegion:     "target_region",
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migration.Data)
```

## Get a Migration

`GET /storage/migrations/{id}`

```go
	migration, err := client.Storage.Migrations.Get(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", migration.Data)
```

## Stop a Migration

`POST /storage/migrations/{id}/actions/stop`

```go
	response, err := client.Storage.Migrations.Actions.Stop(context.TODO(), "")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```
