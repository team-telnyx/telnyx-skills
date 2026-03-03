---
name: telnyx-oauth-curl
description: >-
  Implement OAuth 2.0 authentication flows for Telnyx API access. This skill
  provides REST API (curl) examples.
metadata:
  author: telnyx
  product: oauth
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Oauth - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Authorization server metadata

OAuth 2.0 Authorization Server Metadata (RFC 8414)

`GET /.well-known/oauth-authorization-server`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/.well-known/oauth-authorization-server"
```

## Protected resource metadata

OAuth 2.0 Protected Resource Metadata for resource discovery

`GET /.well-known/oauth-protected-resource`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/.well-known/oauth-protected-resource"
```

## OAuth authorization endpoint

OAuth 2.0 authorization endpoint for the authorization code flow

`GET /oauth/authorize`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth/authorize?scope=admin"
```

## Get OAuth consent token

Retrieve details about an OAuth consent token

`GET /oauth/consent/{consent_token}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth/consent/{consent_token}"
```

## Create OAuth grant

Create an OAuth authorization grant

`POST /oauth/grants` — Required: `allowed`, `consent_token`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "allowed": true,
  "consent_token": "string"
}' \
  "https://api.telnyx.com/v2/oauth/grants"
```

## Token introspection

Introspect an OAuth access token to check its validity and metadata

`POST /oauth/introspect` — Required: `token`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "token": "string"
}' \
  "https://api.telnyx.com/v2/oauth/introspect"
```

## JSON Web Key Set

Retrieve the JSON Web Key Set for token verification

`GET /oauth/jwks`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth/jwks"
```

## Dynamic client registration

Register a new OAuth client dynamically (RFC 7591)

`POST /oauth/register`

Optional: `client_name` (string), `grant_types` (array[string]), `logo_uri` (uri), `policy_uri` (uri), `redirect_uris` (array[string]), `response_types` (array[string]), `scope` (string), `token_endpoint_auth_method` (enum), `tos_uri` (uri)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "redirect_uris": [
    "https://example.com/callback"
  ],
  "client_name": "My OAuth Application",
  "scope": "admin"
}' \
  "https://api.telnyx.com/v2/oauth/register"
```

## OAuth token endpoint

Exchange authorization code, client credentials, or refresh token for access token

`POST /oauth/token` — Required: `grant_type`

Optional: `client_id` (string), `client_secret` (string), `code` (string), `code_verifier` (string), `redirect_uri` (uri), `refresh_token` (string), `scope` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "grant_type": "client_credentials",
  "scope": "admin"
}' \
  "https://api.telnyx.com/v2/oauth/token"
```

## List OAuth clients

Retrieve a paginated list of OAuth clients for the authenticated user

`GET /oauth_clients`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth_clients"
```

## Create OAuth client

Create a new OAuth client

`POST /oauth_clients` — Required: `name`, `allowed_scopes`, `client_type`, `allowed_grant_types`

Optional: `logo_uri` (uri), `policy_uri` (uri), `redirect_uris` (array[string]), `require_pkce` (boolean), `tos_uri` (uri)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "My OAuth client",
  "allowed_scopes": [
    "admin"
  ],
  "client_type": "public",
  "allowed_grant_types": [
    "client_credentials"
  ]
}' \
  "https://api.telnyx.com/v2/oauth_clients"
```

## Get OAuth client

Retrieve a single OAuth client by ID

`GET /oauth_clients/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth_clients/{id}"
```

## Update OAuth client

Update an existing OAuth client

`PUT /oauth_clients/{id}`

Optional: `allowed_grant_types` (array[string]), `allowed_scopes` (array[string]), `logo_uri` (uri), `name` (string), `policy_uri` (uri), `redirect_uris` (array[string]), `require_pkce` (boolean), `tos_uri` (uri)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "allowed_scopes": [
    "admin"
  ]
}' \
  "https://api.telnyx.com/v2/oauth_clients/{id}"
```

## Delete OAuth client

Delete an OAuth client

`DELETE /oauth_clients/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/oauth_clients/{id}"
```

## List OAuth grants

Retrieve a paginated list of OAuth grants for the authenticated user

`GET /oauth_grants`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth_grants"
```

## Get OAuth grant

Retrieve a single OAuth grant by ID

`GET /oauth_grants/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/oauth_grants/{id}"
```

## Revoke OAuth grant

Revoke an OAuth grant

`DELETE /oauth_grants/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/oauth_grants/{id}"
```
