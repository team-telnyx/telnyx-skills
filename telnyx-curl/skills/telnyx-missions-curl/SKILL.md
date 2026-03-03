---
name: telnyx-missions-curl
description: >-
  Create and manage Telnyx Missions — automated workflows, tasks, and
  sub-resources for AI-driven telecom operations. This skill provides REST API
  (curl) examples.
metadata:
  author: telnyx
  product: missions
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Missions - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## List missions

List all missions for the organization

`GET /ai/missions`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions"
```

## Create mission

Create a new mission definition

`POST /ai/missions` — Required: `name`

Optional: `description` (string), `execution_mode` (enum), `instructions` (string), `metadata` (object), `model` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}' \
  "https://api.telnyx.com/v2/ai/missions"
```

## List recent events

List recent events across all missions

`GET /ai/missions/events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/events"
```

## List recent runs

List recent runs across all missions

`GET /ai/missions/runs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/runs"
```

## Get mission

Get a mission by ID (includes tools, knowledge_bases, mcp_servers)

`GET /ai/missions/{mission_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}"
```

## Update mission

Update a mission definition

`PUT /ai/missions/{mission_id}`

Optional: `description` (string), `execution_mode` (enum), `instructions` (string), `metadata` (object), `model` (string), `name` (string)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}"
```

## Delete mission

Delete a mission

`DELETE /ai/missions/{mission_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}"
```

## Clone mission

Clone an existing mission

`POST /ai/missions/{mission_id}/clone`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/clone"
```

## List knowledge bases

List all knowledge bases for a mission

`GET /ai/missions/{mission_id}/knowledge-bases`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/knowledge-bases"
```

## Create knowledge base

Create a new knowledge base for a mission

`POST /ai/missions/{mission_id}/knowledge-bases`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/knowledge-bases"
```

## Get knowledge base

Get a specific knowledge base by ID

`GET /ai/missions/{mission_id}/knowledge-bases/{knowledge_base_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/knowledge-bases/{knowledge_base_id}"
```

## Update knowledge base

Update a knowledge base definition

`PUT /ai/missions/{mission_id}/knowledge-bases/{knowledge_base_id}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/knowledge-bases/{knowledge_base_id}"
```

## Delete knowledge base

Delete a knowledge base from a mission

`DELETE /ai/missions/{mission_id}/knowledge-bases/{knowledge_base_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/knowledge-bases/{knowledge_base_id}"
```

## List MCP servers

List all MCP servers for a mission

`GET /ai/missions/{mission_id}/mcp-servers`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/mcp-servers"
```

## Create MCP server

Create a new MCP server for a mission

`POST /ai/missions/{mission_id}/mcp-servers`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/mcp-servers"
```

## Get MCP server

Get a specific MCP server by ID

`GET /ai/missions/{mission_id}/mcp-servers/{mcp_server_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/mcp-servers/{mcp_server_id}"
```

## Update MCP server

Update an MCP server definition

`PUT /ai/missions/{mission_id}/mcp-servers/{mcp_server_id}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/mcp-servers/{mcp_server_id}"
```

## Delete MCP server

Delete an MCP server from a mission

`DELETE /ai/missions/{mission_id}/mcp-servers/{mcp_server_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/mcp-servers/{mcp_server_id}"
```

## List runs for mission

List all runs for a specific mission

`GET /ai/missions/{mission_id}/runs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs"
```

## Start a run

Start a new run for a mission

`POST /ai/missions/{mission_id}/runs`

Optional: `input` (object), `metadata` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs"
```

## Get run details

Get details of a specific run

`GET /ai/missions/{mission_id}/runs/{run_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}"
```

## Update run

Update run status and/or result

`PATCH /ai/missions/{mission_id}/runs/{run_id}`

Optional: `error` (string), `metadata` (object), `result_payload` (object), `result_summary` (string), `status` (enum)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}"
```

## Cancel run

Cancel a running or paused run

`POST /ai/missions/{mission_id}/runs/{run_id}/cancel`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/cancel"
```

## List events

List events for a run (paginated)

`GET /ai/missions/{mission_id}/runs/{run_id}/events`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/events"
```

## Log event

Log an event for a run

`POST /ai/missions/{mission_id}/runs/{run_id}/events` — Required: `type`, `summary`

Optional: `agent_id` (string), `idempotency_key` (string), `payload` (object), `step_id` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "type": "status_change",
  "summary": "string"
}' \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/events"
```

## Get event details

Get details of a specific event

`GET /ai/missions/{mission_id}/runs/{run_id}/events/{event_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/events/{event_id}"
```

## Pause run

Pause a running run

`POST /ai/missions/{mission_id}/runs/{run_id}/pause`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/pause"
```

## Get plan

Get the plan (all steps) for a run

`GET /ai/missions/{mission_id}/runs/{run_id}/plan`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/plan"
```

## Create initial plan

Create the initial plan for a run

`POST /ai/missions/{mission_id}/runs/{run_id}/plan` — Required: `steps`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "steps": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/plan"
```

## Add step(s) to plan

Add one or more steps to an existing plan

`POST /ai/missions/{mission_id}/runs/{run_id}/plan/steps` — Required: `steps`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "steps": [
    "string"
  ]
}' \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/plan/steps"
```

## Get step details

Get details of a specific plan step

`GET /ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}"
```

## Update step status

Update the status of a plan step

`PATCH /ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}`

Optional: `metadata` (object), `status` (enum)

```bash
curl \
  -X PATCH \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}"
```

## Resume run

Resume a paused run

`POST /ai/missions/{mission_id}/runs/{run_id}/resume`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/resume"
```

## List linked Telnyx agents

List all Telnyx agents linked to a run

`GET /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents"
```

## Link Telnyx agent to run

Link a Telnyx AI agent (voice/messaging) to a run

`POST /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents` — Required: `telnyx_agent_id`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "telnyx_agent_id": "string"
}' \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents"
```

## Unlink Telnyx agent

Unlink a Telnyx agent from a run

`DELETE /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents/{telnyx_agent_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents/{telnyx_agent_id}"
```

## List tools

List all tools for a mission

`GET /ai/missions/{mission_id}/tools`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/tools"
```

## Create tool

Create a new tool for a mission

`POST /ai/missions/{mission_id}/tools`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/tools"
```

## Get tool

Get a specific tool by ID

`GET /ai/missions/{mission_id}/tools/{tool_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/missions/{mission_id}/tools/{tool_id}"
```

## Update tool

Update a tool definition

`PUT /ai/missions/{mission_id}/tools/{tool_id}`

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/tools/{tool_id}"
```

## Delete tool

Delete a tool from a mission

`DELETE /ai/missions/{mission_id}/tools/{tool_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/missions/{mission_id}/tools/{tool_id}"
```
