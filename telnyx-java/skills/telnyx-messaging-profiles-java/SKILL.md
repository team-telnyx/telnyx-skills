---
name: telnyx-messaging-profiles-java
description: >-
  Create and manage messaging profiles with number pools, sticky sender, and
  geomatch features. Configure short codes for high-volume messaging. This skill
  provides Java SDK examples.
metadata:
  author: telnyx
  product: messaging-profiles
  language: java
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Messaging Profiles - Java

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

## List messaging profiles

`GET /messaging_profiles`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileListPage;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileListParams;

MessagingProfileListPage page = client.messagingProfiles().list();
```

## Create a messaging profile

`POST /messaging_profiles` — Required: `name`, `whitelisted_destinations`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileCreateParams;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileCreateResponse;

MessagingProfileCreateParams params = MessagingProfileCreateParams.builder()
    .name("My name")
    .addWhitelistedDestination("US")
    .build();
MessagingProfileCreateResponse messagingProfile = client.messagingProfiles().create(params);
```

## Retrieve a messaging profile

`GET /messaging_profiles/{id}`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileRetrieveParams;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileRetrieveResponse;

MessagingProfileRetrieveResponse messagingProfile = client.messagingProfiles().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Update a messaging profile

`PATCH /messaging_profiles/{id}`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileUpdateParams;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileUpdateResponse;

MessagingProfileUpdateResponse messagingProfile = client.messagingProfiles().update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Delete a messaging profile

`DELETE /messaging_profiles/{id}`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileDeleteParams;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileDeleteResponse;

MessagingProfileDeleteResponse messagingProfile = client.messagingProfiles().delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## List phone numbers associated with a messaging profile

`GET /messaging_profiles/{id}/phone_numbers`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileListPhoneNumbersPage;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileListPhoneNumbersParams;

MessagingProfileListPhoneNumbersPage page = client.messagingProfiles().listPhoneNumbers("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## List short codes associated with a messaging profile

`GET /messaging_profiles/{id}/short_codes`

```java
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileListShortCodesPage;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileListShortCodesParams;

MessagingProfileListShortCodesPage page = client.messagingProfiles().listShortCodes("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## List Auto-Response Settings

`GET /messaging_profiles/{profile_id}/autoresp_configs`

```java
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutorespConfigListParams;
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutorespConfigListResponse;

AutorespConfigListResponse autorespConfigs = client.messagingProfiles().autorespConfigs().list("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Create auto-response setting

`POST /messaging_profiles/{profile_id}/autoresp_configs` — Required: `op`, `keywords`, `country_code`

```java
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutoRespConfigCreate;
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutoRespConfigResponse;
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutorespConfigCreateParams;

AutorespConfigCreateParams params = AutorespConfigCreateParams.builder()
    .profileId("profile_id")
    .autoRespConfigCreate(AutoRespConfigCreate.builder()
        .countryCode("US")
        .addKeyword("keyword1")
        .addKeyword("keyword2")
        .op(AutoRespConfigCreate.Op.START)
        .build())
    .build();
AutoRespConfigResponse autoRespConfigResponse = client.messagingProfiles().autorespConfigs().create(params);
```

## Get Auto-Response Setting

`GET /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}`

```java
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutoRespConfigResponse;
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutorespConfigRetrieveParams;

AutorespConfigRetrieveParams params = AutorespConfigRetrieveParams.builder()
    .profileId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .autorespCfgId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .build();
AutoRespConfigResponse autoRespConfigResponse = client.messagingProfiles().autorespConfigs().retrieve(params);
```

## Update Auto-Response Setting

`PUT /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}` — Required: `op`, `keywords`, `country_code`

```java
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutoRespConfigCreate;
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutoRespConfigResponse;
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutorespConfigUpdateParams;

AutorespConfigUpdateParams params = AutorespConfigUpdateParams.builder()
    .profileId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .autorespCfgId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .autoRespConfigCreate(AutoRespConfigCreate.builder()
        .countryCode("US")
        .addKeyword("keyword1")
        .addKeyword("keyword2")
        .op(AutoRespConfigCreate.Op.START)
        .build())
    .build();
AutoRespConfigResponse autoRespConfigResponse = client.messagingProfiles().autorespConfigs().update(params);
```

## Delete Auto-Response Setting

`DELETE /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}`

```java
import com.telnyx.sdk.models.messagingprofiles.autorespconfigs.AutorespConfigDeleteParams;

AutorespConfigDeleteParams params = AutorespConfigDeleteParams.builder()
    .profileId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .autorespCfgId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .build();
String autorespConfig = client.messagingProfiles().autorespConfigs().delete(params);
```

## List short codes

`GET /short_codes`

```java
import com.telnyx.sdk.models.shortcodes.ShortCodeListPage;
import com.telnyx.sdk.models.shortcodes.ShortCodeListParams;

ShortCodeListPage page = client.shortCodes().list();
```

## Retrieve a short code

`GET /short_codes/{id}`

```java
import com.telnyx.sdk.models.shortcodes.ShortCodeRetrieveParams;
import com.telnyx.sdk.models.shortcodes.ShortCodeRetrieveResponse;

ShortCodeRetrieveResponse shortCode = client.shortCodes().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Update short code

Update the settings for a specific short code.

`PATCH /short_codes/{id}` — Required: `messaging_profile_id`

```java
import com.telnyx.sdk.models.shortcodes.ShortCodeUpdateParams;
import com.telnyx.sdk.models.shortcodes.ShortCodeUpdateResponse;

ShortCodeUpdateParams params = ShortCodeUpdateParams.builder()
    .id("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .messagingProfileId("abc85f64-5717-4562-b3fc-2c9600000000")
    .build();
ShortCodeUpdateResponse shortCode = client.shortCodes().update(params);
```
