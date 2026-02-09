---
name: telnyx-ai-assistants-javascript
description: >-
  Create and manage AI voice assistants with custom personalities, knowledge
  bases, and tool integrations. This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: ai-assistants
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Ai Assistants - JavaScript

## Installation

```bash
npm install telnyx
```

## Setup

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'], // This is the default and can be omitted
});
```

All examples below assume `client` is already initialized as shown above.

## List assistants

Retrieve a list of all AI Assistants configured by the user.

`GET /ai/assistants`

```javascript
const assistantsList = await client.ai.assistants.list();

console.log(assistantsList.data);
```

## Create an assistant

Create a new AI Assistant.

`POST /ai/assistants` — Required: `name`, `model`, `instructions`

```javascript
const assistant = await client.ai.assistants.create({
  instructions: 'instructions',
  model: 'model',
  name: 'name',
});

console.log(assistant.id);
```

## Get an assistant

Retrieve an AI Assistant configuration by `assistant_id`.

`GET /ai/assistants/{assistant_id}`

```javascript
const assistant = await client.ai.assistants.retrieve('assistant_id');

console.log(assistant.id);
```

## Update an assistant

Update an AI Assistant's attributes.

`POST /ai/assistants/{assistant_id}`

```javascript
const assistant = await client.ai.assistants.update('assistant_id');

console.log(assistant.id);
```

## Delete an assistant

Delete an AI Assistant by `assistant_id`.

`DELETE /ai/assistants/{assistant_id}`

```javascript
const assistant = await client.ai.assistants.delete('assistant_id');

console.log(assistant.id);
```

## Assistant Chat (BETA)

This endpoint allows a client to send a chat message to a specific AI Assistant.

`POST /ai/assistants/{assistant_id}/chat` — Required: `content`, `conversation_id`

```javascript
const response = await client.ai.assistants.chat('assistant_id', {
  content: 'Tell me a joke about cats',
  conversation_id: '42b20469-1215-4a9a-8964-c36f66b406f4',
});

console.log(response.content);
```

## Assistant Sms Chat

Send an SMS message for an assistant.

`POST /ai/assistants/{assistant_id}/chat/sms` — Required: `from`, `to`

```javascript
const response = await client.ai.assistants.sendSMS('assistant_id', { from: 'from', to: 'to' });

console.log(response.conversation_id);
```

## Clone Assistant

Clone an existing assistant, excluding telephony and messaging settings.

`POST /ai/assistants/{assistant_id}/clone`

```javascript
const assistant = await client.ai.assistants.clone('assistant_id');

console.log(assistant.id);
```

## Import assistants from external provider

Import assistants from external providers.

`POST /ai/assistants/import` — Required: `provider`, `api_key_ref`

```javascript
const assistantsList = await client.ai.assistants.imports({
  api_key_ref: 'api_key_ref',
  provider: 'elevenlabs',
});

console.log(assistantsList.data);
```

## List scheduled events

Get scheduled events for an assistant with pagination and filtering

`GET /ai/assistants/{assistant_id}/scheduled_events`

```javascript
// Automatically fetches more pages as needed.
for await (const scheduledEventListResponse of client.ai.assistants.scheduledEvents.list(
  'assistant_id',
)) {
  console.log(scheduledEventListResponse);
}
```

## Create a scheduled event

Create a scheduled event for an assistant

`POST /ai/assistants/{assistant_id}/scheduled_events` — Required: `telnyx_conversation_channel`, `telnyx_end_user_target`, `telnyx_agent_target`, `scheduled_at_fixed_datetime`

```javascript
const scheduledEventResponse = await client.ai.assistants.scheduledEvents.create('assistant_id', {
  scheduled_at_fixed_datetime: '2025-04-15T13:07:28.764Z',
  telnyx_agent_target: 'telnyx_agent_target',
  telnyx_conversation_channel: 'phone_call',
  telnyx_end_user_target: 'telnyx_end_user_target',
});

console.log(scheduledEventResponse);
```

## Get a scheduled event

Retrieve a scheduled event by event ID

`GET /ai/assistants/{assistant_id}/scheduled_events/{event_id}`

```javascript
const scheduledEventResponse = await client.ai.assistants.scheduledEvents.retrieve('event_id', {
  assistant_id: 'assistant_id',
});

console.log(scheduledEventResponse);
```

## Delete a scheduled event

If the event is pending, this will cancel the event.

`DELETE /ai/assistants/{assistant_id}/scheduled_events/{event_id}`

```javascript
await client.ai.assistants.scheduledEvents.delete('event_id', { assistant_id: 'assistant_id' });
```

## List assistant tests with pagination

Retrieves a paginated list of assistant tests with optional filtering capabilities

`GET /ai/assistants/tests`

```javascript
// Automatically fetches more pages as needed.
for await (const assistantTest of client.ai.assistants.tests.list()) {
  console.log(assistantTest.test_id);
}
```

## Create a new assistant test

Creates a comprehensive test configuration for evaluating AI assistant performance

`POST /ai/assistants/tests` — Required: `name`, `destination`, `instructions`, `rubric`

```javascript
const assistantTest = await client.ai.assistants.tests.create({
  destination: '+15551234567',
  instructions:
    'Act as a frustrated customer who received a damaged product. Ask for a refund and escalate if not satisfied with the initial response.',
  name: 'Customer Support Bot Test',
  rubric: [
    { criteria: 'Assistant responds within 30 seconds', name: 'Response Time' },
    { criteria: 'Provides correct product information', name: 'Accuracy' },
  ],
});

console.log(assistantTest.test_id);
```

## Get all test suite names

Retrieves a list of all distinct test suite names available to the current user

`GET /ai/assistants/tests/test-suites`

```javascript
const testSuites = await client.ai.assistants.tests.testSuites.list();

console.log(testSuites.data);
```

## Get test suite run history

Retrieves paginated history of test runs for a specific test suite with filtering options

`GET /ai/assistants/tests/test-suites/{suite_name}/runs`

```javascript
// Automatically fetches more pages as needed.
for await (const testRunResponse of client.ai.assistants.tests.testSuites.runs.list('suite_name')) {
  console.log(testRunResponse.run_id);
}
```

## Trigger test suite execution

Executes all tests within a specific test suite as a batch operation

`POST /ai/assistants/tests/test-suites/{suite_name}/runs`

```javascript
const testRunResponses = await client.ai.assistants.tests.testSuites.runs.trigger('suite_name');

console.log(testRunResponses);
```

## Get assistant test by ID

Retrieves detailed information about a specific assistant test

`GET /ai/assistants/tests/{test_id}`

```javascript
const assistantTest = await client.ai.assistants.tests.retrieve('test_id');

console.log(assistantTest.test_id);
```

## Update an assistant test

Updates an existing assistant test configuration with new settings

`PUT /ai/assistants/tests/{test_id}`

```javascript
const assistantTest = await client.ai.assistants.tests.update('test_id');

console.log(assistantTest.test_id);
```

## Delete an assistant test

Permanently removes an assistant test and all associated data

`DELETE /ai/assistants/tests/{test_id}`

```javascript
await client.ai.assistants.tests.delete('test_id');
```

## Get test run history for a specific test

Retrieves paginated execution history for a specific assistant test with filtering options

`GET /ai/assistants/tests/{test_id}/runs`

```javascript
// Automatically fetches more pages as needed.
for await (const testRunResponse of client.ai.assistants.tests.runs.list('test_id')) {
  console.log(testRunResponse.run_id);
}
```

## Trigger a manual test run

Initiates immediate execution of a specific assistant test

`POST /ai/assistants/tests/{test_id}/runs`

```javascript
const testRunResponse = await client.ai.assistants.tests.runs.trigger('test_id');

console.log(testRunResponse.run_id);
```

## Get specific test run details

Retrieves detailed information about a specific test run execution

`GET /ai/assistants/tests/{test_id}/runs/{run_id}`

```javascript
const testRunResponse = await client.ai.assistants.tests.runs.retrieve('run_id', {
  test_id: 'test_id',
});

console.log(testRunResponse.run_id);
```

## Get all versions of an assistant

Retrieves all versions of a specific assistant with complete configuration and metadata

`GET /ai/assistants/{assistant_id}/versions`

```javascript
const assistantsList = await client.ai.assistants.versions.list('assistant_id');

console.log(assistantsList.data);
```

## Get a specific assistant version

Retrieves a specific version of an assistant by assistant_id and version_id

`GET /ai/assistants/{assistant_id}/versions/{version_id}`

```javascript
const assistant = await client.ai.assistants.versions.retrieve('version_id', {
  assistant_id: 'assistant_id',
});

console.log(assistant.id);
```

## Update a specific assistant version

Updates the configuration of a specific assistant version.

`POST /ai/assistants/{assistant_id}/versions/{version_id}`

```javascript
const assistant = await client.ai.assistants.versions.update('version_id', {
  assistant_id: 'assistant_id',
});

console.log(assistant.id);
```

## Delete a specific assistant version

Permanently removes a specific version of an assistant.

`DELETE /ai/assistants/{assistant_id}/versions/{version_id}`

```javascript
await client.ai.assistants.versions.delete('version_id', { assistant_id: 'assistant_id' });
```

## Promote an assistant version to main

Promotes a specific version to be the main/current version of the assistant.

`POST /ai/assistants/{assistant_id}/versions/{version_id}/promote`

```javascript
const assistant = await client.ai.assistants.versions.promote('version_id', {
  assistant_id: 'assistant_id',
});

console.log(assistant.id);
```

## Get Canary Deploy

Endpoint to get a canary deploy configuration for an assistant.

`GET /ai/assistants/{assistant_id}/canary-deploys`

```javascript
const canaryDeployResponse = await client.ai.assistants.canaryDeploys.retrieve('assistant_id');

console.log(canaryDeployResponse.assistant_id);
```

## Create Canary Deploy

Endpoint to create a canary deploy configuration for an assistant.

`POST /ai/assistants/{assistant_id}/canary-deploys` — Required: `versions`

```javascript
const canaryDeployResponse = await client.ai.assistants.canaryDeploys.create('assistant_id', {
  versions: [{ percentage: 1, version_id: 'version_id' }],
});

console.log(canaryDeployResponse.assistant_id);
```

## Update Canary Deploy

Endpoint to update a canary deploy configuration for an assistant.

`PUT /ai/assistants/{assistant_id}/canary-deploys` — Required: `versions`

```javascript
const canaryDeployResponse = await client.ai.assistants.canaryDeploys.update('assistant_id', {
  versions: [{ percentage: 1, version_id: 'version_id' }],
});

console.log(canaryDeployResponse.assistant_id);
```

## Delete Canary Deploy

Endpoint to delete a canary deploy configuration for an assistant.

`DELETE /ai/assistants/{assistant_id}/canary-deploys`

```javascript
await client.ai.assistants.canaryDeploys.delete('assistant_id');
```

## Get assistant texml

Get an assistant texml by `assistant_id`.

`GET /ai/assistants/{assistant_id}/texml`

```javascript
const response = await client.ai.assistants.getTexml('assistant_id');

console.log(response);
```

## Test Assistant Tool

Test a webhook tool for an assistant

`POST /ai/assistants/{assistant_id}/tools/{tool_id}/test`

```javascript
const response = await client.ai.assistants.tools.test('tool_id', { assistant_id: 'assistant_id' });

console.log(response.data);
```

## List Integrations

List all available integrations.

`GET /ai/integrations`

```javascript
const integrations = await client.ai.integrations.list();

console.log(integrations.data);
```

## List User Integrations

List user setup integrations

`GET /ai/integrations/connections`

```javascript
const connections = await client.ai.integrations.connections.list();

console.log(connections.data);
```

## Get User Integration connection By Id

Get user setup integrations

`GET /ai/integrations/connections/{user_connection_id}`

```javascript
const connection = await client.ai.integrations.connections.retrieve('user_connection_id');

console.log(connection.data);
```

## Delete Integration Connection

Delete a specific integration connection.

`DELETE /ai/integrations/connections/{user_connection_id}`

```javascript
await client.ai.integrations.connections.delete('user_connection_id');
```

## List Integration By Id

Retrieve integration details

`GET /ai/integrations/{integration_id}`

```javascript
const integration = await client.ai.integrations.retrieve('integration_id');

console.log(integration.id);
```

## List MCP Servers

Retrieve a list of MCP servers.

`GET /ai/mcp_servers`

```javascript
// Automatically fetches more pages as needed.
for await (const mcpServerListResponse of client.ai.mcpServers.list()) {
  console.log(mcpServerListResponse.id);
}
```

## Create MCP Server

Create a new MCP server.

`POST /ai/mcp_servers` — Required: `name`, `type`, `url`

```javascript
const mcpServer = await client.ai.mcpServers.create({
  name: 'name',
  type: 'type',
  url: 'url',
});

console.log(mcpServer.id);
```

## Get MCP Server

Retrieve details for a specific MCP server.

`GET /ai/mcp_servers/{mcp_server_id}`

```javascript
const mcpServer = await client.ai.mcpServers.retrieve('mcp_server_id');

console.log(mcpServer.id);
```

## Update MCP Server

Update an existing MCP server.

`PUT /ai/mcp_servers/{mcp_server_id}`

```javascript
const mcpServer = await client.ai.mcpServers.update('mcp_server_id');

console.log(mcpServer.id);
```

## Delete MCP Server

Delete a specific MCP server.

`DELETE /ai/mcp_servers/{mcp_server_id}`

```javascript
await client.ai.mcpServers.delete('mcp_server_id');
```
