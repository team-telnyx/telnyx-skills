---
name: telnyx-oauth-ruby
description: >-
  Implement OAuth 2.0 authentication flows for Telnyx API access. This skill
  provides Ruby SDK examples.
metadata:
  author: telnyx
  product: oauth
  language: ruby
---

# Telnyx Oauth - Ruby

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

## Authorization server metadata

OAuth 2.0 Authorization Server Metadata (RFC 8414)

`GET /.well-known/oauth-authorization-server`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.well_known.retrieve_authorization_server_metadata

puts(response)
```

## Protected resource metadata

OAuth 2.0 Protected Resource Metadata for resource discovery

`GET /.well-known/oauth-protected-resource`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.well_known.retrieve_protected_resource_metadata

puts(response)
```

## OAuth authorization endpoint

OAuth 2.0 authorization endpoint for the authorization code flow

`GET /oauth/authorize`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.oauth.retrieve_authorize(
  client_id: "client_id",
  redirect_uri: "https://example.com",
  response_type: :code
)

puts(result)
```

## List OAuth clients

Retrieve a paginated list of OAuth clients for the authenticated user

`GET /oauth/clients`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.oauth_clients.list

puts(page)
```

## Create OAuth client

Create a new OAuth client

`POST /oauth/clients` — Required: `name`, `allowed_scopes`, `client_type`, `allowed_grant_types`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

oauth_client = telnyx.oauth_clients.create(
  allowed_grant_types: [:client_credentials],
  allowed_scopes: ["admin"],
  client_type: :public,
  name: "My OAuth client"
)

puts(oauth_client)
```

## Get OAuth client

Retrieve a single OAuth client by ID

`GET /oauth/clients/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

oauth_client = telnyx.oauth_clients.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(oauth_client)
```

## Update OAuth client

Update an existing OAuth client

`PUT /oauth/clients/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

oauth_client = telnyx.oauth_clients.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(oauth_client)
```

## Delete OAuth client

Delete an OAuth client

`DELETE /oauth/clients/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.oauth_clients.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(result)
```

## Get OAuth consent token

Retrieve details about an OAuth consent token

`GET /oauth/consent/{consent_token}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

oauth = telnyx.oauth.retrieve("consent_token")

puts(oauth)
```

## List OAuth grants

Retrieve a paginated list of OAuth grants for the authenticated user

`GET /oauth/grants`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.oauth_grants.list

puts(page)
```

## Get OAuth grant

Retrieve a single OAuth grant by ID

`GET /oauth/grants/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

oauth_grant = telnyx.oauth_grants.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(oauth_grant)
```

## Revoke OAuth grant

Revoke an OAuth grant

`DELETE /oauth/grants/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

oauth_grant = telnyx.oauth_grants.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(oauth_grant)
```

## Token introspection

Introspect an OAuth access token to check its validity and metadata

`POST /oauth/introspect` — Required: `token`

```ruby
telnyx = Telnyx::Client.new(client_id: "My Client ID", client_secret: "My Client Secret")

response = telnyx.oauth.introspect(token: "token")

puts(response)
```

## JSON Web Key Set

Retrieve the JSON Web Key Set for token verification

`GET /oauth/jwks`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.oauth.retrieve_jwks

puts(response)
```

## Dynamic client registration

Register a new OAuth client dynamically (RFC 7591)

`POST /oauth/register`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.oauth.register

puts(response)
```

## OAuth token endpoint

Exchange authorization code, client credentials, or refresh token for access token

`POST /oauth/token` — Required: `grant_type`

```ruby
telnyx = Telnyx::Client.new(client_id: "My Client ID", client_secret: "My Client Secret")

response = telnyx.oauth.token(grant_type: :client_credentials)

puts(response)
```
