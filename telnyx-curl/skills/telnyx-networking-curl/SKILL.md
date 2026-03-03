---
name: telnyx-networking-curl
description: >-
  Configure private networks, WireGuard VPN gateways, internet gateways, and
  virtual cross connects. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: networking
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Networking - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List all clusters

`GET /ai/clusters`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/clusters"
```

## Compute new clusters

Starts a background task to compute how the data in an [embedded storage bucket](https://developers.telnyx.com/api-reference/embeddings/embed-documents) is clustered.

`POST /ai/clusters` — Required: `bucket`

Optional: `files` (array[string]), `min_cluster_size` (integer), `min_subcluster_size` (integer), `prefix` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "bucket": "string"
}' \
  "https://api.telnyx.com/v2/ai/clusters"
```

## Fetch a cluster

`GET /ai/clusters/{task_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/clusters/{task_id}"
```

## Delete a cluster

`DELETE /ai/clusters/{task_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/clusters/{task_id}"
```

## Fetch a cluster visualization

`GET /ai/clusters/{task_id}/graph`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/clusters/{task_id}/graph"
```

## List Integrations

List all available integrations.

`GET /ai/integrations`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/integrations"
```

## List User Integrations

List user setup integrations

`GET /ai/integrations/connections`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/integrations/connections"
```

## Get User Integration connection By Id

Get user setup integrations

`GET /ai/integrations/connections/{user_connection_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/integrations/connections/{user_connection_id}"
```

## Delete Integration Connection

Delete a specific integration connection.

`DELETE /ai/integrations/connections/{user_connection_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/integrations/connections/{user_connection_id}"
```

## List Integration By Id

Retrieve integration details

`GET /ai/integrations/{integration_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/integrations/{integration_id}"
```

## List all Global IP Allowed Ports

`GET /global_ip_allowed_ports`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_allowed_ports"
```

## Global IP Assignment Health Check Metrics

`GET /global_ip_assignment_health`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_assignment_health"
```

## List all Global IP assignments

List all Global IP assignments.

`GET /global_ip_assignments`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_assignments"
```

## Create a Global IP assignment

Create a Global IP assignment.

`POST /global_ip_assignments`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/global_ip_assignments"
```

## Retrieve a Global IP

Retrieve a Global IP assignment.

`GET /global_ip_assignments/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_assignments/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Update a Global IP assignment

Update a Global IP assignment.

`PATCH /global_ip_assignments/{id}`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/global_ip_assignments/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Global IP assignment

Delete a Global IP assignment.

`DELETE /global_ip_assignments/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/global_ip_assignments/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Global IP Assignment Usage Metrics

`GET /global_ip_assignments_usage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_assignments_usage"
```

## List all Global IP Health check types

List all Global IP Health check types.

`GET /global_ip_health_check_types`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_health_check_types"
```

## List all Global IP health checks

List all Global IP health checks.

`GET /global_ip_health_checks`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_health_checks"
```

## Create a Global IP health check

Create a Global IP health check.

`POST /global_ip_health_checks`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/global_ip_health_checks"
```

## Retrieve a Global IP health check

Retrieve a Global IP health check.

`GET /global_ip_health_checks/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_health_checks/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Global IP health check

Delete a Global IP health check.

`DELETE /global_ip_health_checks/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/global_ip_health_checks/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Global IP Latency Metrics

`GET /global_ip_latency`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_latency"
```

## List all Global IP Protocols

`GET /global_ip_protocols`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_protocols"
```

## Global IP Usage Metrics

`GET /global_ip_usage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ip_usage"
```

## List all Global IPs

List all Global IPs.

`GET /global_ips`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ips"
```

## Create a Global IP

Create a Global IP.

`POST /global_ips`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/global_ips"
```

## Retrieve a Global IP

Retrieve a Global IP.

`GET /global_ips/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/global_ips/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Global IP

Delete a Global IP.

`DELETE /global_ips/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/global_ips/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## List all Networks

List all Networks.

`GET /networks`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/networks"
```

## Create a Network

Create a new Network.

`POST /networks`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/networks"
```

## Retrieve a Network

Retrieve a Network.

`GET /networks/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Update a Network

Update a Network.

`PATCH /networks/{id}`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Network

Delete a Network.

`DELETE /networks/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Get Default Gateway status.

`GET /networks/{id}/default_gateway`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58/default_gateway"
```

## Create Default Gateway.

`POST /networks/{id}/default_gateway`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58/default_gateway"
```

## Delete Default Gateway.

`DELETE /networks/{id}/default_gateway`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58/default_gateway"
```

## List all Interfaces for a Network.

`GET /networks/{id}/network_interfaces`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/networks/6a09cdc3-8948-47f0-aa62-74ac943d6c58/network_interfaces"
```

## Get all Private Wireless Gateways

Get all Private Wireless Gateways belonging to the user.

`GET /private_wireless_gateways`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/private_wireless_gateways?filter[name]=my private gateway&filter[ip_range]=192.168.0.0/24&filter[region_code]=dc2&filter[created_at]=2018-02-02T22:25:27.521Z&filter[updated_at]=2018-02-02T22:25:27.521Z"
```

## Create a Private Wireless Gateway

Asynchronously create a Private Wireless Gateway for SIM cards for a previously created network.

`POST /private_wireless_gateways` — Required: `network_id`, `name`

Optional: `region_code` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "network_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
  "name": "My private wireless gateway",
  "region_code": "dc2"
}' \
  "https://api.telnyx.com/v2/private_wireless_gateways"
```

## Get a Private Wireless Gateway

Retrieve information about a Private Wireless Gateway.

`GET /private_wireless_gateways/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/private_wireless_gateways/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Private Wireless Gateway

Deletes the Private Wireless Gateway.

`DELETE /private_wireless_gateways/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/private_wireless_gateways/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## List all Public Internet Gateways

List all Public Internet Gateways.

`GET /public_internet_gateways`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/public_internet_gateways"
```

## Create a Public Internet Gateway

Create a new Public Internet Gateway.

`POST /public_internet_gateways`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/public_internet_gateways"
```

## Retrieve a Public Internet Gateway

Retrieve a Public Internet Gateway.

`GET /public_internet_gateways/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/public_internet_gateways/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Public Internet Gateway

Delete a Public Internet Gateway.

`DELETE /public_internet_gateways/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/public_internet_gateways/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## List all Regions

List all regions and the interfaces that region supports

`GET /regions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/regions"
```

## List all Virtual Cross Connects

List all Virtual Cross Connects.

`GET /virtual_cross_connects`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/virtual_cross_connects"
```

## Create a Virtual Cross Connect

Create a new Virtual Cross Connect.<br /><br />For AWS and GCE, you have the option of creating the primary connection first and the secondary connection later.

`POST /virtual_cross_connects`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/virtual_cross_connects"
```

## Retrieve a Virtual Cross Connect

Retrieve a Virtual Cross Connect.

`GET /virtual_cross_connects/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/virtual_cross_connects/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Update the Virtual Cross Connect

Update the Virtual Cross Connect.<br /><br />Cloud IPs can only be patched during the `created` state, as GCE will only inform you of your generated IP once the pending connection requested has bee...

`PATCH /virtual_cross_connects/{id}`

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/virtual_cross_connects/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Virtual Cross Connect

Delete a Virtual Cross Connect.

`DELETE /virtual_cross_connects/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/virtual_cross_connects/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## List Virtual Cross Connect Cloud Coverage

List Virtual Cross Connects Cloud Coverage.<br /><br />This endpoint shows which cloud regions are available for the `location_code` your Virtual Cross Connect will be provisioned in.

`GET /virtual_cross_connects_coverage`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/virtual_cross_connects_coverage"
```

## List all WireGuard Interfaces

List all WireGuard Interfaces.

`GET /wireguard_interfaces`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireguard_interfaces"
```

## Create a WireGuard Interface

Create a new WireGuard Interface.

`POST /wireguard_interfaces`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/wireguard_interfaces"
```

## Retrieve a WireGuard Interfaces

Retrieve a WireGuard Interfaces.

`GET /wireguard_interfaces/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireguard_interfaces/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a WireGuard Interface

Delete a WireGuard Interface.

`DELETE /wireguard_interfaces/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/wireguard_interfaces/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## List all WireGuard Peers

List all WireGuard peers.

`GET /wireguard_peers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireguard_peers"
```

## Create a WireGuard Peer

Create a new WireGuard Peer.

`POST /wireguard_peers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/wireguard_peers"
```

## Retrieve the WireGuard Peer

Retrieve the WireGuard peer.

`GET /wireguard_peers/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireguard_peers/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Update the WireGuard Peer

Update the WireGuard peer.

`PATCH /wireguard_peers/{id}`

Optional: `public_key` (string)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "public_key": "qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU="
}' \
  "https://api.telnyx.com/v2/wireguard_peers/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete the WireGuard Peer

Delete the WireGuard peer.

`DELETE /wireguard_peers/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/wireguard_peers/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Retrieve Wireguard config template for Peer

`GET /wireguard_peers/{id}/config`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireguard_peers/6a09cdc3-8948-47f0-aa62-74ac943d6c58/config"
```
