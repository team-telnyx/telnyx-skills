---
name: telnyx-sip-ruby
description: >-
  Configure SIP trunking connections and outbound voice profiles. Use when
  connecting PBX systems or managing SIP infrastructure. This skill provides
  Ruby SDK examples.
metadata:
  author: telnyx
  product: sip
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Sip - Ruby

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

## Get all outbound voice profiles

Get all outbound voice profiles belonging to the user that match the given filters.

`GET /outbound_voice_profiles`

```ruby
page = client.outbound_voice_profiles.list

puts(page)
```

## Create an outbound voice profile

Create an outbound voice profile.

`POST /outbound_voice_profiles` — Required: `name`

```ruby
outbound_voice_profile = client.outbound_voice_profiles.create(name: "office")

puts(outbound_voice_profile)
```

## Retrieve an outbound voice profile

Retrieves the details of an existing outbound voice profile.

`GET /outbound_voice_profiles/{id}`

```ruby
outbound_voice_profile = client.outbound_voice_profiles.retrieve("1293384261075731499")

puts(outbound_voice_profile)
```

## Updates an existing outbound voice profile.

`PATCH /outbound_voice_profiles/{id}` — Required: `name`

```ruby
outbound_voice_profile = client.outbound_voice_profiles.update("1293384261075731499", name: "office")

puts(outbound_voice_profile)
```

## Delete an outbound voice profile

Deletes an existing outbound voice profile.

`DELETE /outbound_voice_profiles/{id}`

```ruby
outbound_voice_profile = client.outbound_voice_profiles.delete("1293384261075731499")

puts(outbound_voice_profile)
```

## List connections

Returns a list of your connections irrespective of type.

`GET /connections`

```ruby
page = client.connections.list

puts(page)
```

## Retrieve a connection

Retrieves the high-level details of an existing connection.

`GET /connections/{id}`

```ruby
connection = client.connections.retrieve("id")

puts(connection)
```

## List credential connections

Returns a list of your credential connections.

`GET /credential_connections`

```ruby
page = client.credential_connections.list

puts(page)
```

## Create a credential connection

Creates a credential connection.

`POST /credential_connections` — Required: `user_name`, `password`, `connection_name`

```ruby
credential_connection = client.credential_connections.create(
  connection_name: "my name",
  password: "my123secure456password789",
  user_name: "myusername123"
)

puts(credential_connection)
```

## Retrieve a credential connection

Retrieves the details of an existing credential connection.

`GET /credential_connections/{id}`

```ruby
credential_connection = client.credential_connections.retrieve("id")

puts(credential_connection)
```

## Update a credential connection

Updates settings of an existing credential connection.

`PATCH /credential_connections/{id}`

```ruby
credential_connection = client.credential_connections.update("id")

puts(credential_connection)
```

## Delete a credential connection

Deletes an existing credential connection.

`DELETE /credential_connections/{id}`

```ruby
credential_connection = client.credential_connections.delete("id")

puts(credential_connection)
```

## Check a Credential Connection Registration Status

Checks the registration_status for a credential connection, (`registration_status`) as well as the timestamp for the last SIP registration event (`registration_status_updated_at`)

`POST /credential_connections/{id}/actions/check_registration_status`

```ruby
response = client.credential_connections.actions.check_registration_status("id")

puts(response)
```

## List Ips

Get all IPs belonging to the user that match the given filters.

`GET /ips`

```ruby
page = client.ips.list

puts(page)
```

## Create an Ip

Create a new IP object.

`POST /ips` — Required: `ip_address`

```ruby
ip = client.ips.create(ip_address: "192.168.0.0")

puts(ip)
```

## Retrieve an Ip

Return the details regarding a specific IP.

`GET /ips/{id}`

```ruby
ip = client.ips.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(ip)
```

## Update an Ip

Update the details of a specific IP.

`PATCH /ips/{id}` — Required: `ip_address`

```ruby
ip = client.ips.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58", ip_address: "192.168.0.0")

puts(ip)
```

## Delete an Ip

Delete an IP.

`DELETE /ips/{id}`

```ruby
ip = client.ips.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(ip)
```

## List Ip connections

Returns a list of your IP connections.

`GET /ip_connections`

```ruby
page = client.ip_connections.list

puts(page)
```

## Create an Ip connection

Creates an IP connection.

`POST /ip_connections`

```ruby
ip_connection = client.ip_connections.create

puts(ip_connection)
```

## Retrieve an Ip connection

Retrieves the details of an existing ip connection.

`GET /ip_connections/{id}`

```ruby
ip_connection = client.ip_connections.retrieve("id")

puts(ip_connection)
```

## Update an Ip connection

Updates settings of an existing IP connection.

`PATCH /ip_connections/{id}`

```ruby
ip_connection = client.ip_connections.update("id")

puts(ip_connection)
```

## Delete an Ip connection

Deletes an existing IP connection.

`DELETE /ip_connections/{id}`

```ruby
ip_connection = client.ip_connections.delete("id")

puts(ip_connection)
```

## List FQDNs

Get all FQDNs belonging to the user that match the given filters.

`GET /fqdns`

```ruby
page = client.fqdns.list

puts(page)
```

## Create an FQDN

Create a new FQDN object.

`POST /fqdns` — Required: `fqdn`, `dns_record_type`, `connection_id`

```ruby
fqdn = client.fqdns.create(connection_id: "1516447646313612565", dns_record_type: "a", fqdn: "example.com")

puts(fqdn)
```

## Retrieve an FQDN

Return the details regarding a specific FQDN.

`GET /fqdns/{id}`

```ruby
fqdn = client.fqdns.retrieve("id")

puts(fqdn)
```

## Update an FQDN

Update the details of a specific FQDN.

`PATCH /fqdns/{id}`

```ruby
fqdn = client.fqdns.update("id")

puts(fqdn)
```

## Delete an FQDN

Delete an FQDN.

`DELETE /fqdns/{id}`

```ruby
fqdn = client.fqdns.delete("id")

puts(fqdn)
```

## List FQDN connections

Returns a list of your FQDN connections.

`GET /fqdn_connections`

```ruby
page = client.fqdn_connections.list

puts(page)
```

## Create an FQDN connection

Creates a FQDN connection.

`POST /fqdn_connections` — Required: `connection_name`

```ruby
fqdn_connection = client.fqdn_connections.create(connection_name: "string")

puts(fqdn_connection)
```

## Retrieve an FQDN connection

Retrieves the details of an existing FQDN connection.

`GET /fqdn_connections/{id}`

```ruby
fqdn_connection = client.fqdn_connections.retrieve("id")

puts(fqdn_connection)
```

## Update an FQDN connection

Updates settings of an existing FQDN connection.

`PATCH /fqdn_connections/{id}`

```ruby
fqdn_connection = client.fqdn_connections.update("id")

puts(fqdn_connection)
```

## Delete an FQDN connection

Deletes an FQDN connection.

`DELETE /fqdn_connections/{id}`

```ruby
fqdn_connection = client.fqdn_connections.delete("id")

puts(fqdn_connection)
```

## List Mobile Voice Connections

`GET /v2/mobile_voice_connections`

```ruby
page = client.mobile_voice_connections.list

puts(page)
```

## Create a Mobile Voice Connection

`POST /v2/mobile_voice_connections`

```ruby
mobile_voice_connection = client.mobile_voice_connections.create

puts(mobile_voice_connection)
```

## Retrieve a Mobile Voice Connection

`GET /v2/mobile_voice_connections/{id}`

```ruby
mobile_voice_connection = client.mobile_voice_connections.retrieve("id")

puts(mobile_voice_connection)
```

## Update a Mobile Voice Connection

`PATCH /v2/mobile_voice_connections/{id}`

```ruby
mobile_voice_connection = client.mobile_voice_connections.update("id")

puts(mobile_voice_connection)
```

## Delete a Mobile Voice Connection

`DELETE /v2/mobile_voice_connections/{id}`

```ruby
mobile_voice_connection = client.mobile_voice_connections.delete("id")

puts(mobile_voice_connection)
```
