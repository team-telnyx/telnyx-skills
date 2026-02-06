---
name: telnyx-oauth-java
description: >-
  Implement OAuth 2.0 authentication flows for Telnyx API access. This skill
  provides Java SDK examples.
metadata:
  author: telnyx
  product: oauth
  language: java
---

# Telnyx Oauth - Java

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

## Authorization server metadata

OAuth 2.0 Authorization Server Metadata (RFC 8414)

`GET /.well-known/oauth-authorization-server`

```java
import com.telnyx.sdk.models.wellknown.WellKnownRetrieveAuthorizationServerMetadataParams;
import com.telnyx.sdk.models.wellknown.WellKnownRetrieveAuthorizationServerMetadataResponse;

WellKnownRetrieveAuthorizationServerMetadataResponse response = client.wellKnown().retrieveAuthorizationServerMetadata();
```

## Protected resource metadata

OAuth 2.0 Protected Resource Metadata for resource discovery

`GET /.well-known/oauth-protected-resource`

```java
import com.telnyx.sdk.models.wellknown.WellKnownRetrieveProtectedResourceMetadataParams;
import com.telnyx.sdk.models.wellknown.WellKnownRetrieveProtectedResourceMetadataResponse;

WellKnownRetrieveProtectedResourceMetadataResponse response = client.wellKnown().retrieveProtectedResourceMetadata();
```

## OAuth authorization endpoint

OAuth 2.0 authorization endpoint for the authorization code flow

`GET /oauth/authorize`

```java
import com.telnyx.sdk.models.oauth.OAuthRetrieveAuthorizeParams;

OAuthRetrieveAuthorizeParams params = OAuthRetrieveAuthorizeParams.builder()
    .clientId("client_id")
    .redirectUri("https://example.com")
    .responseType(OAuthRetrieveAuthorizeParams.ResponseType.CODE)
    .build();
client.oauth().retrieveAuthorize(params);
```

## List OAuth clients

Retrieve a paginated list of OAuth clients for the authenticated user

`GET /oauth/clients`

```java
import com.telnyx.sdk.models.oauthclients.OAuthClientListPage;
import com.telnyx.sdk.models.oauthclients.OAuthClientListParams;

OAuthClientListPage page = client.oauthClients().list();
```

## Create OAuth client

Create a new OAuth client

`POST /oauth/clients` — Required: `name`, `allowed_scopes`, `client_type`, `allowed_grant_types`

```java
import com.telnyx.sdk.models.oauthclients.OAuthClientCreateParams;
import com.telnyx.sdk.models.oauthclients.OAuthClientCreateResponse;

OAuthClientCreateParams params = OAuthClientCreateParams.builder()
    .addAllowedGrantType(OAuthClientCreateParams.AllowedGrantType.CLIENT_CREDENTIALS)
    .addAllowedScope("admin")
    .clientType(OAuthClientCreateParams.ClientType.PUBLIC)
    .name("My OAuth client")
    .build();
OAuthClientCreateResponse oauthClient = client.oauthClients().create(params);
```

## Get OAuth client

Retrieve a single OAuth client by ID

`GET /oauth/clients/{id}`

```java
import com.telnyx.sdk.models.oauthclients.OAuthClientRetrieveParams;
import com.telnyx.sdk.models.oauthclients.OAuthClientRetrieveResponse;

OAuthClientRetrieveResponse oauthClient = client.oauthClients().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Update OAuth client

Update an existing OAuth client

`PUT /oauth/clients/{id}`

```java
import com.telnyx.sdk.models.oauthclients.OAuthClientUpdateParams;
import com.telnyx.sdk.models.oauthclients.OAuthClientUpdateResponse;

OAuthClientUpdateResponse oauthClient = client.oauthClients().update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Delete OAuth client

Delete an OAuth client

`DELETE /oauth/clients/{id}`

```java
import com.telnyx.sdk.models.oauthclients.OAuthClientDeleteParams;

client.oauthClients().delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Get OAuth consent token

Retrieve details about an OAuth consent token

`GET /oauth/consent/{consent_token}`

```java
import com.telnyx.sdk.models.oauth.OAuthRetrieveParams;
import com.telnyx.sdk.models.oauth.OAuthRetrieveResponse;

OAuthRetrieveResponse oauth = client.oauth().retrieve("consent_token");
```

## List OAuth grants

Retrieve a paginated list of OAuth grants for the authenticated user

`GET /oauth/grants`

```java
import com.telnyx.sdk.models.oauthgrants.OAuthGrantListPage;
import com.telnyx.sdk.models.oauthgrants.OAuthGrantListParams;

OAuthGrantListPage page = client.oauthGrants().list();
```

## Get OAuth grant

Retrieve a single OAuth grant by ID

`GET /oauth/grants/{id}`

```java
import com.telnyx.sdk.models.oauthgrants.OAuthGrantRetrieveParams;
import com.telnyx.sdk.models.oauthgrants.OAuthGrantRetrieveResponse;

OAuthGrantRetrieveResponse oauthGrant = client.oauthGrants().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Revoke OAuth grant

Revoke an OAuth grant

`DELETE /oauth/grants/{id}`

```java
import com.telnyx.sdk.models.oauthgrants.OAuthGrantDeleteParams;
import com.telnyx.sdk.models.oauthgrants.OAuthGrantDeleteResponse;

OAuthGrantDeleteResponse oauthGrant = client.oauthGrants().delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Token introspection

Introspect an OAuth access token to check its validity and metadata

`POST /oauth/introspect` — Required: `token`

```java
import com.telnyx.sdk.models.oauth.OAuthIntrospectParams;
import com.telnyx.sdk.models.oauth.OAuthIntrospectResponse;

OAuthIntrospectParams params = OAuthIntrospectParams.builder()
    .token("token")
    .build();
OAuthIntrospectResponse response = client.oauth().introspect(params);
```

## JSON Web Key Set

Retrieve the JSON Web Key Set for token verification

`GET /oauth/jwks`

```java
import com.telnyx.sdk.models.oauth.OAuthRetrieveJwksParams;
import com.telnyx.sdk.models.oauth.OAuthRetrieveJwksResponse;

OAuthRetrieveJwksResponse response = client.oauth().retrieveJwks();
```

## Dynamic client registration

Register a new OAuth client dynamically (RFC 7591)

`POST /oauth/register`

```java
import com.telnyx.sdk.models.oauth.OAuthRegisterParams;
import com.telnyx.sdk.models.oauth.OAuthRegisterResponse;

OAuthRegisterResponse response = client.oauth().register();
```

## OAuth token endpoint

Exchange authorization code, client credentials, or refresh token for access token

`POST /oauth/token` — Required: `grant_type`

```java
import com.telnyx.sdk.models.oauth.OAuthTokenParams;
import com.telnyx.sdk.models.oauth.OAuthTokenResponse;

OAuthTokenParams params = OAuthTokenParams.builder()
    .grantType(OAuthTokenParams.GrantType.CLIENT_CREDENTIALS)
    .build();
OAuthTokenResponse response = client.oauth().token(params);
```
