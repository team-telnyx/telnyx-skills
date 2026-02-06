---
name: telnyx-seti-java
description: >-
  Access SETI (Space Exploration Telecommunications Infrastructure) APIs. This
  skill provides Java SDK examples.
metadata:
  author: telnyx
  product: seti
  language: java
---

# Telnyx Seti - Java

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

## Retrieve Black Box Test Results

Returns the results of the various black box tests

`GET /seti/black_box_test_results`

```java
import com.telnyx.sdk.models.seti.SetiRetrieveBlackBoxTestResultsParams;
import com.telnyx.sdk.models.seti.SetiRetrieveBlackBoxTestResultsResponse;

SetiRetrieveBlackBoxTestResultsResponse response = client.seti().retrieveBlackBoxTestResults();
```
