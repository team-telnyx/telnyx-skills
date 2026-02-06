---
name: telnyx-networking-ruby
description: >-
  Configure private networks, WireGuard VPN gateways, internet gateways, and
  virtual cross connects. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: networking
  language: ruby
---

# Telnyx Networking - Ruby

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

## List all Regions

List all regions and the interfaces that region supports

`GET /regions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

regions = telnyx.regions.list

puts(regions)
```

## List all Networks

List all Networks.

`GET /networks`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.networks.list

puts(page)
```

## Create a Network

Create a new Network.

`POST /networks`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

network = telnyx.networks.create(name: "test network")

puts(network)
```

## Retrieve a Network

Retrieve a Network.

`GET /networks/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

network = telnyx.networks.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(network)
```

## Update a Network

Update a Network.

`PATCH /networks/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

network = telnyx.networks.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58", name: "test network")

puts(network)
```

## Delete a Network

Delete a Network.

`DELETE /networks/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

network = telnyx.networks.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(network)
```

## Get Default Gateway status.

`GET /networks/{id}/default_gateway`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

default_gateway = telnyx.networks.default_gateway.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(default_gateway)
```

## Create Default Gateway.

`POST /networks/{id}/default_gateway`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

default_gateway = telnyx.networks.default_gateway.create("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(default_gateway)
```

## Delete Default Gateway.

`DELETE /networks/{id}/default_gateway`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

default_gateway = telnyx.networks.default_gateway.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(default_gateway)
```

## List all Interfaces for a Network.

`GET /networks/{id}/network_interfaces`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.networks.list_interfaces("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(page)
```

## List all WireGuard Interfaces

List all WireGuard Interfaces.

`GET /wireguard_interfaces`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.wireguard_interfaces.list

puts(page)
```

## Create a WireGuard Interface

Create a new WireGuard Interface.

`POST /wireguard_interfaces`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_interface = telnyx.wireguard_interfaces.create(region_code: "ashburn-va")

puts(wireguard_interface)
```

## Retrieve a WireGuard Interfaces

Retrieve a WireGuard Interfaces.

`GET /wireguard_interfaces/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_interface = telnyx.wireguard_interfaces.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireguard_interface)
```

## Delete a WireGuard Interface

Delete a WireGuard Interface.

`DELETE /wireguard_interfaces/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_interface = telnyx.wireguard_interfaces.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireguard_interface)
```

## List all WireGuard Peers

List all WireGuard peers.

`GET /wireguard_peers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.wireguard_peers.list

puts(page)
```

## Create a WireGuard Peer

Create a new WireGuard Peer.

`POST /wireguard_peers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_peer = telnyx.wireguard_peers.create(wireguard_interface_id: "6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireguard_peer)
```

## Retrieve the WireGuard Peer

Retrieve the WireGuard peer.

`GET /wireguard_peers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_peer = telnyx.wireguard_peers.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireguard_peer)
```

## Update the WireGuard Peer

Update the WireGuard peer.

`PATCH /wireguard_peers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_peer = telnyx.wireguard_peers.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireguard_peer)
```

## Delete the WireGuard Peer

Delete the WireGuard peer.

`DELETE /wireguard_peers/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

wireguard_peer = telnyx.wireguard_peers.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireguard_peer)
```

## Retrieve Wireguard config template for Peer

`GET /wireguard_peers/{id}/config`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.wireguard_peers.retrieve_config("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Get all Private Wireless Gateways

Get all Private Wireless Gateways belonging to the user.

`GET /private_wireless_gateways`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.private_wireless_gateways.list

puts(page)
```

## Create a Private Wireless Gateway

Asynchronously create a Private Wireless Gateway for SIM cards for a previously created network.

`POST /private_wireless_gateways` — Required: `network_id`, `name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

private_wireless_gateway = telnyx.private_wireless_gateways.create(
  name: "My private wireless gateway",
  network_id: "6a09cdc3-8948-47f0-aa62-74ac943d6c58"
)

puts(private_wireless_gateway)
```

## Get a Private Wireless Gateway

Retrieve information about a Private Wireless Gateway.

`GET /private_wireless_gateways/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

private_wireless_gateway = telnyx.private_wireless_gateways.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(private_wireless_gateway)
```

## Delete a Private Wireless Gateway

Deletes the Private Wireless Gateway.

`DELETE /private_wireless_gateways/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

private_wireless_gateway = telnyx.private_wireless_gateways.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(private_wireless_gateway)
```

## List all Public Internet Gateways

List all Public Internet Gateways.

`GET /public_internet_gateways`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.public_internet_gateways.list

puts(page)
```

## Create a Public Internet Gateway

Create a new Public Internet Gateway.

`POST /public_internet_gateways`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

public_internet_gateway = telnyx.public_internet_gateways.create

puts(public_internet_gateway)
```

## Retrieve a Public Internet Gateway

Retrieve a Public Internet Gateway.

`GET /public_internet_gateways/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

public_internet_gateway = telnyx.public_internet_gateways.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(public_internet_gateway)
```

## Delete a Public Internet Gateway

Delete a Public Internet Gateway.

`DELETE /public_internet_gateways/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

public_internet_gateway = telnyx.public_internet_gateways.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(public_internet_gateway)
```

## List all Virtual Cross Connects

List all Virtual Cross Connects.

`GET /virtual_cross_connects`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.virtual_cross_connects.list

puts(page)
```

## Create a Virtual Cross Connect

Create a new Virtual Cross Connect.<br /><br />For AWS and GCE, you have the option of creating the primary connection first and the secondary connection later.

`POST /virtual_cross_connects`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

virtual_cross_connect = telnyx.virtual_cross_connects.create(region_code: "ashburn-va")

puts(virtual_cross_connect)
```

## Retrieve a Virtual Cross Connect

Retrieve a Virtual Cross Connect.

`GET /virtual_cross_connects/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

virtual_cross_connect = telnyx.virtual_cross_connects.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(virtual_cross_connect)
```

## Update the Virtual Cross Connect

Update the Virtual Cross Connect.<br /><br />Cloud IPs can only be patched during the `created` state, as GCE will only inform you of your generated IP once the pending connection requested has bee...

`PATCH /virtual_cross_connects/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

virtual_cross_connect = telnyx.virtual_cross_connects.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(virtual_cross_connect)
```

## Delete a Virtual Cross Connect

Delete a Virtual Cross Connect.

`DELETE /virtual_cross_connects/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

virtual_cross_connect = telnyx.virtual_cross_connects.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(virtual_cross_connect)
```

## List Virtual Cross Connect Cloud Coverage

List Virtual Cross Connects Cloud Coverage.<br /><br />This endpoint shows which cloud regions are available for the `location_code` your Virtual Cross Connect will be provisioned in.

`GET /virtual_cross_connects/coverage`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.virtual_cross_connects_coverage.list

puts(page)
```

## List all Global IPs

List all Global IPs.

`GET /global_ips`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.global_ips.list

puts(page)
```

## Create a Global IP

Create a Global IP.

`POST /global_ips`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip = telnyx.global_ips.create

puts(global_ip)
```

## Retrieve a Global IP

Retrieve a Global IP.

`GET /global_ips/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip = telnyx.global_ips.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(global_ip)
```

## Delete a Global IP

Delete a Global IP.

`DELETE /global_ips/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip = telnyx.global_ips.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(global_ip)
```

## List all Global IP Allowed Ports

`GET /global_ip_allowed_ports`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_allowed_ports = telnyx.global_ip_allowed_ports.list

puts(global_ip_allowed_ports)
```

## Global IP Assignment Health Check Metrics

`GET /global_ip_assignment_health`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_assignment_health = telnyx.global_ip_assignment_health.retrieve

puts(global_ip_assignment_health)
```

## List all Global IP assignments

List all Global IP assignments.

`GET /global_ip_assignments`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.global_ip_assignments.list

puts(page)
```

## Create a Global IP assignment

Create a Global IP assignment.

`POST /global_ip_assignments`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_assignment = telnyx.global_ip_assignments.create

puts(global_ip_assignment)
```

## Retrieve a Global IP

Retrieve a Global IP assignment.

`GET /global_ip_assignments/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_assignment = telnyx.global_ip_assignments.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(global_ip_assignment)
```

## Update a Global IP assignment

Update a Global IP assignment.

`PATCH /global_ip_assignments/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_assignment = telnyx.global_ip_assignments.update(
  "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
  global_ip_assignment_update_request: {}
)

puts(global_ip_assignment)
```

## Delete a Global IP assignment

Delete a Global IP assignment.

`DELETE /global_ip_assignments/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_assignment = telnyx.global_ip_assignments.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(global_ip_assignment)
```

## Global IP Assignment Usage Metrics

`GET /global_ip_assignments/usage`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_assignments_usage = telnyx.global_ip_assignments_usage.retrieve

puts(global_ip_assignments_usage)
```

## List all Global IP Health check types

List all Global IP Health check types.

`GET /global_ip_health_check_types`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_health_check_types = telnyx.global_ip_health_check_types.list

puts(global_ip_health_check_types)
```

## List all Global IP health checks

List all Global IP health checks.

`GET /global_ip_health_checks`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.global_ip_health_checks.list

puts(page)
```

## Create a Global IP health check

Create a Global IP health check.

`POST /global_ip_health_checks`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_health_check = telnyx.global_ip_health_checks.create

puts(global_ip_health_check)
```

## Retrieve a Global IP health check

Retrieve a Global IP health check.

`GET /global_ip_health_checks/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_health_check = telnyx.global_ip_health_checks.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(global_ip_health_check)
```

## Delete a Global IP health check

Delete a Global IP health check.

`DELETE /global_ip_health_checks/{id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_health_check = telnyx.global_ip_health_checks.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(global_ip_health_check)
```

## Global IP Latency Metrics

`GET /global_ip_latency`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_latency = telnyx.global_ip_latency.retrieve

puts(global_ip_latency)
```

## List all Global IP Protocols

`GET /global_ip_protocols`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_protocols = telnyx.global_ip_protocols.list

puts(global_ip_protocols)
```

## Global IP Usage Metrics

`GET /global_ip_usage`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

global_ip_usage = telnyx.global_ip_usage.retrieve

puts(global_ip_usage)
```
