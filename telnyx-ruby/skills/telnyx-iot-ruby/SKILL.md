---
name: telnyx-iot-ruby
description: >-
  Manage IoT SIM cards, eSIMs, data plans, and wireless connectivity. Use when
  building IoT/M2M solutions. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: iot
  language: ruby
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Iot - Ruby

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

## Get all wireless regions

Retrieve all wireless regions for the given product.

`GET /wireless/regions`

```ruby
response = client.wireless.retrieve_regions(product: "public_ips")

puts(response)
```

## Get all SIM cards

Get all SIM cards belonging to the user that match the given filters.

`GET /sim_cards`

```ruby
page = client.sim_cards.list

puts(page)
```

## Get SIM card

Returns the details regarding a specific SIM card.

`GET /sim_cards/{id}`

```ruby
sim_card = client.sim_cards.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card)
```

## Update a SIM card

Updates SIM card data

`PATCH /sim_cards/{id}`

```ruby
sim_card = client.sim_cards.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card)
```

## Deletes a SIM card

The SIM card will be decommissioned, removed from your account and you will stop being charged.<br />The SIM card won't be able to connect to the network after the deletion is completed, thus makin...

`DELETE /sim_cards/{id}`

```ruby
sim_card = client.sim_cards.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card)
```

## Get activation code for an eSIM

It returns the activation code for an eSIM.<br/><br/>
 This API is only available for eSIMs.

`GET /sim_cards/{id}/activation_code`

```ruby
response = client.sim_cards.get_activation_code("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Get SIM card device details

It returns the device details where a SIM card is currently being used.

`GET /sim_cards/{id}/device_details`

```ruby
response = client.sim_cards.get_device_details("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Get SIM card public IP definition

It returns the public IP requested for a SIM card.

`GET /sim_cards/{id}/public_ip`

```ruby
response = client.sim_cards.get_public_ip("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## List wireless connectivity logs

This API allows listing a paginated collection of Wireless Connectivity Logs associated with a SIM Card, for troubleshooting purposes.

`GET /sim_cards/{id}/wireless_connectivity_logs`

```ruby
page = client.sim_cards.list_wireless_connectivity_logs("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(page)
```

## Request a SIM card disable

This API disables a SIM card, disconnecting it from the network and making it impossible to consume data.<br/>
The API will trigger an asynchronous operation called a SIM Card Action.

`POST /sim_cards/{id}/actions/disable`

```ruby
response = client.sim_cards.actions.disable("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request a SIM card enable

This API enables a SIM card, connecting it to the network and making it possible to consume data.<br/>
To enable a SIM card, it must be associated with a SIM card group.<br/>
The API will trigger a...

`POST /sim_cards/{id}/actions/enable`

```ruby
response = client.sim_cards.actions.enable("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request removing a SIM card public IP

This API removes an existing public IP from a SIM card.

`POST /sim_cards/{id}/actions/remove_public_ip`

```ruby
response = client.sim_cards.actions.remove_public_ip("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request setting a SIM card public IP

This API makes a SIM card reachable on the public internet by mapping a random public IP to the SIM card.

`POST /sim_cards/{id}/actions/set_public_ip`

```ruby
response = client.sim_cards.actions.set_public_ip("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request setting a SIM card to standby

The SIM card will be able to connect to the network once the process to set it to standby has been completed, thus making it possible to consume data.<br/>
To set a SIM card to standby, it must be ...

`POST /sim_cards/{id}/actions/set_standby`

```ruby
response = client.sim_cards.actions.set_standby("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request bulk setting SIM card public IPs.

This API triggers an asynchronous operation to set a public IP for each of the specified SIM cards.<br/>
For each SIM Card a SIM Card Action will be generated.

`POST /sim_cards/actions/bulk_set_public_ips` — Required: `sim_card_ids`

```ruby
response = client.sim_cards.actions.bulk_set_public_ips(sim_card_ids: ["6b14e151-8493-4fa1-8664-1cc4e6d14158"])

puts(response)
```

## Validate SIM cards registration codes

It validates whether SIM card registration codes are valid or not.

`POST /sim_cards/actions/validate_registration_codes`

```ruby
response = client.sim_cards.actions.validate_registration_codes

puts(response)
```

## List SIM card actions

This API lists a paginated collection of SIM card actions.

`GET /sim_card_actions`

```ruby
page = client.sim_cards.actions.list

puts(page)
```

## Get SIM card action details

This API fetches detailed information about a SIM card action to follow-up on an existing asynchronous operation.

`GET /sim_card_actions/{id}`

```ruby
action = client.sim_cards.actions.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(action)
```

## List bulk SIM card actions

This API lists a paginated collection of bulk SIM card actions.

`GET /bulk_sim_card_actions`

```ruby
page = client.bulk_sim_card_actions.list

puts(page)
```

## Get bulk SIM card action details

This API fetches information about a bulk SIM card action.

`GET /bulk_sim_card_actions/{id}`

```ruby
bulk_sim_card_action = client.bulk_sim_card_actions.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(bulk_sim_card_action)
```

## Get all SIM card groups

Get all SIM card groups belonging to the user that match the given filters.

`GET /sim_card_groups`

```ruby
page = client.sim_card_groups.list

puts(page)
```

## Create a SIM card group

Creates a new SIM card group object

`POST /sim_card_groups` — Required: `name`

```ruby
sim_card_group = client.sim_card_groups.create(name: "My Test Group")

puts(sim_card_group)
```

## Get SIM card group

Returns the details regarding a specific SIM card group

`GET /sim_card_groups/{id}`

```ruby
sim_card_group = client.sim_card_groups.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_group)
```

## Update a SIM card group

Updates a SIM card group

`PATCH /sim_card_groups/{id}`

```ruby
sim_card_group = client.sim_card_groups.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_group)
```

## Delete a SIM card group

Permanently deletes a SIM card group

`DELETE /sim_card_groups/{id}`

```ruby
sim_card_group = client.sim_card_groups.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_group)
```

## Request Private Wireless Gateway removal from SIM card group

This action will asynchronously remove an existing Private Wireless Gateway definition from a SIM card group.

`POST /sim_card_groups/{id}/actions/remove_private_wireless_gateway`

```ruby
response = client.sim_card_groups.actions.remove_private_wireless_gateway("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request Wireless Blocklist removal from SIM card group

This action will asynchronously remove an existing Wireless Blocklist to all the SIMs in the SIM card group.

`POST /sim_card_groups/{id}/actions/remove_wireless_blocklist`

```ruby
response = client.sim_card_groups.actions.remove_wireless_blocklist("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(response)
```

## Request Private Wireless Gateway assignment for SIM card group

This action will asynchronously assign a provisioned Private Wireless Gateway to the SIM card group.

`POST /sim_card_groups/{id}/actions/set_private_wireless_gateway` — Required: `private_wireless_gateway_id`

```ruby
response = client.sim_card_groups.actions.set_private_wireless_gateway(
  "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
  private_wireless_gateway_id: "6a09cdc3-8948-47f0-aa62-74ac943d6c58"
)

puts(response)
```

## Request Wireless Blocklist assignment for SIM card group

This action will asynchronously assign a Wireless Blocklist to all the SIMs in the SIM card group.

`POST /sim_card_groups/{id}/actions/set_wireless_blocklist` — Required: `wireless_blocklist_id`

```ruby
response = client.sim_card_groups.actions.set_wireless_blocklist(
  "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
  wireless_blocklist_id: "6a09cdc3-8948-47f0-aa62-74ac943d6c58"
)

puts(response)
```

## List SIM card group actions

This API allows listing a paginated collection a SIM card group actions.

`GET /sim_card_group_actions`

```ruby
page = client.sim_card_groups.actions.list

puts(page)
```

## Get SIM card group action details

This API allows fetching detailed information about a SIM card group action resource to make follow-ups in an existing asynchronous operation.

`GET /sim_card_group_actions/{id}`

```ruby
action = client.sim_card_groups.actions.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(action)
```

## Get all SIM card orders

Get all SIM card orders according to filters.

`GET /sim_card_orders`

```ruby
page = client.sim_card_orders.list

puts(page)
```

## Create a SIM card order

Creates a new order for SIM cards.

`POST /sim_card_orders` — Required: `address_id`, `quantity`

```ruby
sim_card_order = client.sim_card_orders.create(address_id: "1293384261075731499", quantity: 23)

puts(sim_card_order)
```

## Get a single SIM card order

Get a single SIM card order by its ID.

`GET /sim_card_orders/{id}`

```ruby
sim_card_order = client.sim_card_orders.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_order)
```

## Preview SIM card orders

Preview SIM card order purchases.

`POST /sim_card_order_preview` — Required: `quantity`, `address_id`

```ruby
response = client.sim_card_order_preview.preview(address_id: "1293384261075731499", quantity: 21)

puts(response)
```

## List SIM card data usage notifications

Lists a paginated collection of SIM card data usage notifications.

`GET /sim_card_data_usage_notifications`

```ruby
page = client.sim_card_data_usage_notifications.list

puts(page)
```

## Create a new SIM card data usage notification

Creates a new SIM card data usage notification.

`POST /sim_card_data_usage_notifications` — Required: `sim_card_id`, `threshold`

```ruby
sim_card_data_usage_notification = client.sim_card_data_usage_notifications.create(
  sim_card_id: "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
  threshold: {}
)

puts(sim_card_data_usage_notification)
```

## Get a single SIM card data usage notification

Get a single SIM Card Data Usage Notification.

`GET /sim_card_data_usage_notifications/{id}`

```ruby
sim_card_data_usage_notification = client.sim_card_data_usage_notifications.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_data_usage_notification)
```

## Updates information for a SIM Card Data Usage Notification

Updates information for a SIM Card Data Usage Notification.

`PATCH /sim_card_data_usage_notifications/{id}`

```ruby
sim_card_data_usage_notification = client.sim_card_data_usage_notifications.update("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_data_usage_notification)
```

## Delete SIM card data usage notifications

Delete the SIM Card Data Usage Notification.

`DELETE /sim_card_data_usage_notifications/{id}`

```ruby
sim_card_data_usage_notification = client.sim_card_data_usage_notifications.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(sim_card_data_usage_notification)
```

## Purchase eSIMs

Purchases and registers the specified amount of eSIMs to the current user's account.<br/><br/>
If <code>sim_card_group_id</code> is provided, the eSIMs will be associated with that group.

`POST /actions/purchase/esims` — Required: `amount`

```ruby
purchase = client.actions.purchase.create(amount: 10)

puts(purchase)
```

## Register SIM cards

Register the SIM cards associated with the provided registration codes to the current user's account.<br/><br/>
If <code>sim_card_group_id</code> is provided, the SIM cards will be associated with ...

`POST /actions/register/sim_cards` — Required: `registration_codes`

```ruby
register = client.actions.register.create(registration_codes: ["0000000001", "0000000002", "0000000003"])

puts(register)
```

## List OTA updates

`GET /ota_updates`

```ruby
page = client.ota_updates.list

puts(page)
```

## Get OTA update

This API returns the details of an Over the Air (OTA) update.

`GET /ota_updates/{id}`

```ruby
ota_update = client.ota_updates.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(ota_update)
```

## Get all Private Wireless Gateways

Get all Private Wireless Gateways belonging to the user.

`GET /private_wireless_gateways`

```ruby
page = client.private_wireless_gateways.list

puts(page)
```

## Create a Private Wireless Gateway

Asynchronously create a Private Wireless Gateway for SIM cards for a previously created network.

`POST /private_wireless_gateways` — Required: `network_id`, `name`

```ruby
private_wireless_gateway = client.private_wireless_gateways.create(
  name: "My private wireless gateway",
  network_id: "6a09cdc3-8948-47f0-aa62-74ac943d6c58"
)

puts(private_wireless_gateway)
```

## Get a Private Wireless Gateway

Retrieve information about a Private Wireless Gateway.

`GET /private_wireless_gateways/{id}`

```ruby
private_wireless_gateway = client.private_wireless_gateways.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(private_wireless_gateway)
```

## Delete a Private Wireless Gateway

Deletes the Private Wireless Gateway.

`DELETE /private_wireless_gateways/{id}`

```ruby
private_wireless_gateway = client.private_wireless_gateways.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(private_wireless_gateway)
```

## Get all Wireless Blocklists

Get all Wireless Blocklists belonging to the user.

`GET /wireless_blocklists`

```ruby
page = client.wireless_blocklists.list

puts(page)
```

## Create a Wireless Blocklist

Create a Wireless Blocklist to prevent SIMs from connecting to certain networks.

`POST /wireless_blocklists` — Required: `name`, `type`, `values`

```ruby
wireless_blocklist = client.wireless_blocklists.create(name: "My Wireless Blocklist", type: :country, values: ["CA", "US"])

puts(wireless_blocklist)
```

## Update a Wireless Blocklist

Update a Wireless Blocklist.

`PATCH /wireless_blocklists`

```ruby
wireless_blocklist = client.wireless_blocklists.update

puts(wireless_blocklist)
```

## Get a Wireless Blocklist

Retrieve information about a Wireless Blocklist.

`GET /wireless_blocklists/{id}`

```ruby
wireless_blocklist = client.wireless_blocklists.retrieve("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireless_blocklist)
```

## Delete a Wireless Blocklist

Deletes the Wireless Blocklist.

`DELETE /wireless_blocklists/{id}`

```ruby
wireless_blocklist = client.wireless_blocklists.delete("6a09cdc3-8948-47f0-aa62-74ac943d6c58")

puts(wireless_blocklist)
```

## Get all possible wireless blocklist values

Retrieve all wireless blocklist values for a given blocklist type.

`GET /wireless_blocklist_values`

```ruby
wireless_blocklist_values = client.wireless_blocklist_values.list(type: :country)

puts(wireless_blocklist_values)
```
