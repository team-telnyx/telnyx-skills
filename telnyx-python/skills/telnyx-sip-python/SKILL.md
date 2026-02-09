---
name: telnyx-sip-python
description: >-
  Configure SIP trunking connections and outbound voice profiles. Use when
  connecting PBX systems or managing SIP infrastructure. This skill provides
  Python SDK examples.
metadata:
  author: telnyx
  product: sip
  language: python
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Sip - Python

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

## Get all outbound voice profiles

Get all outbound voice profiles belonging to the user that match the given filters.

`GET /outbound_voice_profiles`

```python
page = client.outbound_voice_profiles.list()
page = page.data[0]
print(page.id)
```

## Create an outbound voice profile

Create an outbound voice profile.

`POST /outbound_voice_profiles` — Required: `name`

```python
outbound_voice_profile = client.outbound_voice_profiles.create(
    name="office",
)
print(outbound_voice_profile.data)
```

## Retrieve an outbound voice profile

Retrieves the details of an existing outbound voice profile.

`GET /outbound_voice_profiles/{id}`

```python
outbound_voice_profile = client.outbound_voice_profiles.retrieve(
    "1293384261075731499",
)
print(outbound_voice_profile.data)
```

## Updates an existing outbound voice profile.

`PATCH /outbound_voice_profiles/{id}` — Required: `name`

```python
outbound_voice_profile = client.outbound_voice_profiles.update(
    id="1293384261075731499",
    name="office",
)
print(outbound_voice_profile.data)
```

## Delete an outbound voice profile

Deletes an existing outbound voice profile.

`DELETE /outbound_voice_profiles/{id}`

```python
outbound_voice_profile = client.outbound_voice_profiles.delete(
    "1293384261075731499",
)
print(outbound_voice_profile.data)
```

## List connections

Returns a list of your connections irrespective of type.

`GET /connections`

```python
page = client.connections.list()
page = page.data[0]
print(page.id)
```

## Retrieve a connection

Retrieves the high-level details of an existing connection.

`GET /connections/{id}`

```python
connection = client.connections.retrieve(
    "id",
)
print(connection.data)
```

## List credential connections

Returns a list of your credential connections.

`GET /credential_connections`

```python
page = client.credential_connections.list()
page = page.data[0]
print(page.id)
```

## Create a credential connection

Creates a credential connection.

`POST /credential_connections` — Required: `user_name`, `password`, `connection_name`

```python
credential_connection = client.credential_connections.create(
    connection_name="my name",
    password="my123secure456password789",
    user_name="myusername123",
)
print(credential_connection.data)
```

## Retrieve a credential connection

Retrieves the details of an existing credential connection.

`GET /credential_connections/{id}`

```python
credential_connection = client.credential_connections.retrieve(
    "id",
)
print(credential_connection.data)
```

## Update a credential connection

Updates settings of an existing credential connection.

`PATCH /credential_connections/{id}`

```python
credential_connection = client.credential_connections.update(
    id="id",
)
print(credential_connection.data)
```

## Delete a credential connection

Deletes an existing credential connection.

`DELETE /credential_connections/{id}`

```python
credential_connection = client.credential_connections.delete(
    "id",
)
print(credential_connection.data)
```

## Check a Credential Connection Registration Status

Checks the registration_status for a credential connection, (`registration_status`) as well as the timestamp for the last SIP registration event (`registration_status_updated_at`)

`POST /credential_connections/{id}/actions/check_registration_status`

```python
response = client.credential_connections.actions.check_registration_status(
    "id",
)
print(response.data)
```

## List Ips

Get all IPs belonging to the user that match the given filters.

`GET /ips`

```python
page = client.ips.list()
page = page.data[0]
print(page.id)
```

## Create an Ip

Create a new IP object.

`POST /ips` — Required: `ip_address`

```python
ip = client.ips.create(
    ip_address="192.168.0.0",
)
print(ip.data)
```

## Retrieve an Ip

Return the details regarding a specific IP.

`GET /ips/{id}`

```python
ip = client.ips.retrieve(
    "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
)
print(ip.data)
```

## Update an Ip

Update the details of a specific IP.

`PATCH /ips/{id}` — Required: `ip_address`

```python
ip = client.ips.update(
    id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
    ip_address="192.168.0.0",
)
print(ip.data)
```

## Delete an Ip

Delete an IP.

`DELETE /ips/{id}`

```python
ip = client.ips.delete(
    "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
)
print(ip.data)
```

## List Ip connections

Returns a list of your IP connections.

`GET /ip_connections`

```python
page = client.ip_connections.list()
page = page.data[0]
print(page.id)
```

## Create an Ip connection

Creates an IP connection.

`POST /ip_connections`

```python
ip_connection = client.ip_connections.create()
print(ip_connection.data)
```

## Retrieve an Ip connection

Retrieves the details of an existing ip connection.

`GET /ip_connections/{id}`

```python
ip_connection = client.ip_connections.retrieve(
    "id",
)
print(ip_connection.data)
```

## Update an Ip connection

Updates settings of an existing IP connection.

`PATCH /ip_connections/{id}`

```python
ip_connection = client.ip_connections.update(
    id="id",
)
print(ip_connection.data)
```

## Delete an Ip connection

Deletes an existing IP connection.

`DELETE /ip_connections/{id}`

```python
ip_connection = client.ip_connections.delete(
    "id",
)
print(ip_connection.data)
```

## List FQDNs

Get all FQDNs belonging to the user that match the given filters.

`GET /fqdns`

```python
page = client.fqdns.list()
page = page.data[0]
print(page.id)
```

## Create an FQDN

Create a new FQDN object.

`POST /fqdns` — Required: `fqdn`, `dns_record_type`, `connection_id`

```python
fqdn = client.fqdns.create(
    connection_id="1516447646313612565",
    dns_record_type="a",
    fqdn="example.com",
)
print(fqdn.data)
```

## Retrieve an FQDN

Return the details regarding a specific FQDN.

`GET /fqdns/{id}`

```python
fqdn = client.fqdns.retrieve(
    "id",
)
print(fqdn.data)
```

## Update an FQDN

Update the details of a specific FQDN.

`PATCH /fqdns/{id}`

```python
fqdn = client.fqdns.update(
    id="id",
)
print(fqdn.data)
```

## Delete an FQDN

Delete an FQDN.

`DELETE /fqdns/{id}`

```python
fqdn = client.fqdns.delete(
    "id",
)
print(fqdn.data)
```

## List FQDN connections

Returns a list of your FQDN connections.

`GET /fqdn_connections`

```python
page = client.fqdn_connections.list()
page = page.data[0]
print(page.id)
```

## Create an FQDN connection

Creates a FQDN connection.

`POST /fqdn_connections` — Required: `connection_name`

```python
fqdn_connection = client.fqdn_connections.create(
    connection_name="string",
)
print(fqdn_connection.data)
```

## Retrieve an FQDN connection

Retrieves the details of an existing FQDN connection.

`GET /fqdn_connections/{id}`

```python
fqdn_connection = client.fqdn_connections.retrieve(
    "id",
)
print(fqdn_connection.data)
```

## Update an FQDN connection

Updates settings of an existing FQDN connection.

`PATCH /fqdn_connections/{id}`

```python
fqdn_connection = client.fqdn_connections.update(
    id="id",
)
print(fqdn_connection.data)
```

## Delete an FQDN connection

Deletes an FQDN connection.

`DELETE /fqdn_connections/{id}`

```python
fqdn_connection = client.fqdn_connections.delete(
    "id",
)
print(fqdn_connection.data)
```

## List Mobile Voice Connections

`GET /v2/mobile_voice_connections`

```python
page = client.mobile_voice_connections.list()
page = page.data[0]
print(page.id)
```

## Create a Mobile Voice Connection

`POST /v2/mobile_voice_connections`

```python
mobile_voice_connection = client.mobile_voice_connections.create()
print(mobile_voice_connection.data)
```

## Retrieve a Mobile Voice Connection

`GET /v2/mobile_voice_connections/{id}`

```python
mobile_voice_connection = client.mobile_voice_connections.retrieve(
    "id",
)
print(mobile_voice_connection.data)
```

## Update a Mobile Voice Connection

`PATCH /v2/mobile_voice_connections/{id}`

```python
mobile_voice_connection = client.mobile_voice_connections.update(
    id="id",
)
print(mobile_voice_connection.data)
```

## Delete a Mobile Voice Connection

`DELETE /v2/mobile_voice_connections/{id}`

```python
mobile_voice_connection = client.mobile_voice_connections.delete(
    "id",
)
print(mobile_voice_connection.data)
```
