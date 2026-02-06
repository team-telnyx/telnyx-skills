---
name: telnyx-ai-assistants-ruby
description: >-
  Create and manage AI voice assistants with custom personalities, knowledge
  bases, and tool integrations. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: ai-assistants
  language: ruby
---

# Telnyx Ai Assistants - Ruby

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

## List assistants

Retrieve a list of all AI Assistants configured by the user.

`GET /ai/assistants`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistants_list = telnyx.ai.assistants.list

puts(assistants_list)
```

## Create an assistant

Create a new AI Assistant.

`POST /ai/assistants` — Required: `name`, `model`, `instructions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.create(instructions: "instructions", model: "model", name: "name")

puts(inference_embedding)
```

## Get an assistant

Retrieve an AI Assistant configuration by `assistant_id`.

`GET /ai/assistants/{assistant_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.retrieve("assistant_id")

puts(inference_embedding)
```

## Update an assistant

Update an AI Assistant's attributes.

`POST /ai/assistants/{assistant_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.update("assistant_id")

puts(inference_embedding)
```

## Delete an assistant

Delete an AI Assistant by `assistant_id`.

`DELETE /ai/assistants/{assistant_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistant = telnyx.ai.assistants.delete("assistant_id")

puts(assistant)
```

## Assistant Chat (BETA)

This endpoint allows a client to send a chat message to a specific AI Assistant.

`POST /ai/assistants/{assistant_id}/chat` — Required: `content`, `conversation_id`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.assistants.chat(
  "assistant_id",
  content: "Tell me a joke about cats",
  conversation_id: "42b20469-1215-4a9a-8964-c36f66b406f4"
)

puts(response)
```

## Assistant Sms Chat

Send an SMS message for an assistant.

`POST /ai/assistants/{assistant_id}/chat/sms` — Required: `from`, `to`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.assistants.send_sms("assistant_id", from: "from", to: "to")

puts(response)
```

## Clone Assistant

Clone an existing assistant, excluding telephony and messaging settings.

`POST /ai/assistants/{assistant_id}/clone`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.clone_("assistant_id")

puts(inference_embedding)
```

## Import assistants from external provider

Import assistants from external providers.

`POST /ai/assistants/import` — Required: `provider`, `api_key_ref`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistants_list = telnyx.ai.assistants.imports(api_key_ref: "api_key_ref", provider: :elevenlabs)

puts(assistants_list)
```

## List scheduled events

Get scheduled events for an assistant with pagination and filtering

`GET /ai/assistants/{assistant_id}/scheduled_events`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.assistants.scheduled_events.list("assistant_id")

puts(page)
```

## Create a scheduled event

Create a scheduled event for an assistant

`POST /ai/assistants/{assistant_id}/scheduled_events` — Required: `telnyx_conversation_channel`, `telnyx_end_user_target`, `telnyx_agent_target`, `scheduled_at_fixed_datetime`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

scheduled_event_response = telnyx.ai.assistants.scheduled_events.create(
  "assistant_id",
  scheduled_at_fixed_datetime: "2025-04-15T13:07:28.764Z",
  telnyx_agent_target: "telnyx_agent_target",
  telnyx_conversation_channel: :phone_call,
  telnyx_end_user_target: "telnyx_end_user_target"
)

puts(scheduled_event_response)
```

## Get a scheduled event

Retrieve a scheduled event by event ID

`GET /ai/assistants/{assistant_id}/scheduled_events/{event_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

scheduled_event_response = telnyx.ai.assistants.scheduled_events.retrieve("event_id", assistant_id: "assistant_id")

puts(scheduled_event_response)
```

## Delete a scheduled event

If the event is pending, this will cancel the event.

`DELETE /ai/assistants/{assistant_id}/scheduled_events/{event_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.assistants.scheduled_events.delete("event_id", assistant_id: "assistant_id")

puts(result)
```

## List assistant tests with pagination

Retrieves a paginated list of assistant tests with optional filtering capabilities

`GET /ai/assistants/tests`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.assistants.tests.list

puts(page)
```

## Create a new assistant test

Creates a comprehensive test configuration for evaluating AI assistant performance

`POST /ai/assistants/tests` — Required: `name`, `destination`, `instructions`, `rubric`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistant_test = telnyx.ai.assistants.tests.create(
  destination: "+15551234567",
  instructions: "Act as a frustrated customer who received a damaged product. Ask for a refund and escalate if not satisfied with the initial response.",
  name: "Customer Support Bot Test",
  rubric: [
    {criteria: "Assistant responds within 30 seconds", name: "Response Time"},
    {criteria: "Provides correct product information", name: "Accuracy"}
  ]
)

puts(assistant_test)
```

## Get all test suite names

Retrieves a list of all distinct test suite names available to the current user

`GET /ai/assistants/tests/test-suites`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

test_suites = telnyx.ai.assistants.tests.test_suites.list

puts(test_suites)
```

## Get test suite run history

Retrieves paginated history of test runs for a specific test suite with filtering options

`GET /ai/assistants/tests/test-suites/{suite_name}/runs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.assistants.tests.test_suites.runs.list("suite_name")

puts(page)
```

## Trigger test suite execution

Executes all tests within a specific test suite as a batch operation

`POST /ai/assistants/tests/test-suites/{suite_name}/runs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

test_run_responses = telnyx.ai.assistants.tests.test_suites.runs.trigger("suite_name")

puts(test_run_responses)
```

## Get assistant test by ID

Retrieves detailed information about a specific assistant test

`GET /ai/assistants/tests/{test_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistant_test = telnyx.ai.assistants.tests.retrieve("test_id")

puts(assistant_test)
```

## Update an assistant test

Updates an existing assistant test configuration with new settings

`PUT /ai/assistants/tests/{test_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistant_test = telnyx.ai.assistants.tests.update("test_id")

puts(assistant_test)
```

## Delete an assistant test

Permanently removes an assistant test and all associated data

`DELETE /ai/assistants/tests/{test_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.assistants.tests.delete("test_id")

puts(result)
```

## Get test run history for a specific test

Retrieves paginated execution history for a specific assistant test with filtering options

`GET /ai/assistants/tests/{test_id}/runs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.assistants.tests.runs.list("test_id")

puts(page)
```

## Trigger a manual test run

Initiates immediate execution of a specific assistant test

`POST /ai/assistants/tests/{test_id}/runs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

test_run_response = telnyx.ai.assistants.tests.runs.trigger("test_id")

puts(test_run_response)
```

## Get specific test run details

Retrieves detailed information about a specific test run execution

`GET /ai/assistants/tests/{test_id}/runs/{run_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

test_run_response = telnyx.ai.assistants.tests.runs.retrieve("run_id", test_id: "test_id")

puts(test_run_response)
```

## Get all versions of an assistant

Retrieves all versions of a specific assistant with complete configuration and metadata

`GET /ai/assistants/{assistant_id}/versions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

assistants_list = telnyx.ai.assistants.versions.list("assistant_id")

puts(assistants_list)
```

## Get a specific assistant version

Retrieves a specific version of an assistant by assistant_id and version_id

`GET /ai/assistants/{assistant_id}/versions/{version_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.versions.retrieve("version_id", assistant_id: "assistant_id")

puts(inference_embedding)
```

## Update a specific assistant version

Updates the configuration of a specific assistant version.

`POST /ai/assistants/{assistant_id}/versions/{version_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.versions.update("version_id", assistant_id: "assistant_id")

puts(inference_embedding)
```

## Delete a specific assistant version

Permanently removes a specific version of an assistant.

`DELETE /ai/assistants/{assistant_id}/versions/{version_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.assistants.versions.delete("version_id", assistant_id: "assistant_id")

puts(result)
```

## Promote an assistant version to main

Promotes a specific version to be the main/current version of the assistant.

`POST /ai/assistants/{assistant_id}/versions/{version_id}/promote`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

inference_embedding = telnyx.ai.assistants.versions.promote("version_id", assistant_id: "assistant_id")

puts(inference_embedding)
```

## Get Canary Deploy

Endpoint to get a canary deploy configuration for an assistant.

`GET /ai/assistants/{assistant_id}/canary-deploys`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

canary_deploy_response = telnyx.ai.assistants.canary_deploys.retrieve("assistant_id")

puts(canary_deploy_response)
```

## Create Canary Deploy

Endpoint to create a canary deploy configuration for an assistant.

`POST /ai/assistants/{assistant_id}/canary-deploys` — Required: `versions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

canary_deploy_response = telnyx.ai.assistants.canary_deploys.create(
  "assistant_id",
  versions: [{percentage: 1, version_id: "version_id"}]
)

puts(canary_deploy_response)
```

## Update Canary Deploy

Endpoint to update a canary deploy configuration for an assistant.

`PUT /ai/assistants/{assistant_id}/canary-deploys` — Required: `versions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

canary_deploy_response = telnyx.ai.assistants.canary_deploys.update(
  "assistant_id",
  versions: [{percentage: 1, version_id: "version_id"}]
)

puts(canary_deploy_response)
```

## Delete Canary Deploy

Endpoint to delete a canary deploy configuration for an assistant.

`DELETE /ai/assistants/{assistant_id}/canary-deploys`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.assistants.canary_deploys.delete("assistant_id")

puts(result)
```

## Get assistant texml

Get an assistant texml by `assistant_id`.

`GET /ai/assistants/{assistant_id}/texml`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.assistants.get_texml("assistant_id")

puts(response)
```

## Test Assistant Tool

Test a webhook tool for an assistant

`POST /ai/assistants/{assistant_id}/tools/{tool_id}/test`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.assistants.tools.test_("tool_id", assistant_id: "assistant_id")

puts(response)
```

## List Integrations

List all available integrations.

`GET /ai/integrations`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

integrations = telnyx.ai.integrations.list

puts(integrations)
```

## List User Integrations

List user setup integrations

`GET /ai/integrations/connections`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

connections = telnyx.ai.integrations.connections.list

puts(connections)
```

## Get User Integration connection By Id

Get user setup integrations

`GET /ai/integrations/connections/{user_connection_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

connection = telnyx.ai.integrations.connections.retrieve("user_connection_id")

puts(connection)
```

## Delete Integration Connection

Delete a specific integration connection.

`DELETE /ai/integrations/connections/{user_connection_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.integrations.connections.delete("user_connection_id")

puts(result)
```

## List Integration By Id

Retrieve integration details

`GET /ai/integrations/{integration_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

integration = telnyx.ai.integrations.retrieve("integration_id")

puts(integration)
```

## List MCP Servers

Retrieve a list of MCP servers.

`GET /ai/mcp_servers`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.mcp_servers.list

puts(page)
```

## Create MCP Server

Create a new MCP server.

`POST /ai/mcp_servers` — Required: `name`, `type`, `url`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

mcp_server = telnyx.ai.mcp_servers.create(name: "name", type: "type", url: "url")

puts(mcp_server)
```

## Get MCP Server

Retrieve details for a specific MCP server.

`GET /ai/mcp_servers/{mcp_server_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

mcp_server = telnyx.ai.mcp_servers.retrieve("mcp_server_id")

puts(mcp_server)
```

## Update MCP Server

Update an existing MCP server.

`PUT /ai/mcp_servers/{mcp_server_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

mcp_server = telnyx.ai.mcp_servers.update("mcp_server_id")

puts(mcp_server)
```

## Delete MCP Server

Delete a specific MCP server.

`DELETE /ai/mcp_servers/{mcp_server_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.mcp_servers.delete("mcp_server_id")

puts(result)
```
