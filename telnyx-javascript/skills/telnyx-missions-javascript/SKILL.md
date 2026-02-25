---
name: telnyx-missions-javascript
description: >-
  Telnyx Missions SDK operations. This skill provides JavaScript SDK examples.
metadata:
  author: telnyx
  product: missions
  language: javascript
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Missions - JavaScript

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

## List missions

List all missions for the organization

`GET /ai/missions`

```javascript
// Automatically fetches more pages as needed.
for await (const missionListResponse of client.ai.missions.list()) {
  console.log(missionListResponse.mission_id);
}
```

## Create mission

Create a new mission definition

`POST /ai/missions` — Required: `name`

Optional: `description` (string), `execution_mode` (enum), `instructions` (string), `metadata` (object), `model` (string)

```javascript
const mission = await client.ai.missions.create({ name: 'name' });

console.log(mission.data);
```

## List recent events

List recent events across all missions

`GET /ai/missions/events`

```javascript
// Automatically fetches more pages as needed.
for await (const missionListEventsResponse of client.ai.missions.listEvents()) {
  console.log(missionListEventsResponse.event_id);
}
```

## List recent runs

List recent runs across all missions

`GET /ai/missions/runs`

```javascript
// Automatically fetches more pages as needed.
for await (const runListRunsResponse of client.ai.missions.runs.listRuns()) {
  console.log(runListRunsResponse.mission_id);
}
```

## Get mission

Get a mission by ID (includes tools, knowledge_bases, mcp_servers)

`GET /ai/missions/{mission_id}`

```javascript
const mission = await client.ai.missions.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(mission.data);
```

## Update mission

Update a mission definition

`PUT /ai/missions/{mission_id}`

Optional: `description` (string), `execution_mode` (enum), `instructions` (string), `metadata` (object), `model` (string), `name` (string)

```javascript
const response = await client.ai.missions.updateMission('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(response.data);
```

## Delete mission

Delete a mission

`DELETE /ai/missions/{mission_id}`

```javascript
await client.ai.missions.deleteMission('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```

## Clone mission

Clone an existing mission

`POST /ai/missions/{mission_id}/clone`

```javascript
const response = await client.ai.missions.cloneMission('mission_id');

console.log(response);
```

## List runs for mission

List all runs for a specific mission

`GET /ai/missions/{mission_id}/runs`

```javascript
// Automatically fetches more pages as needed.
for await (const runListResponse of client.ai.missions.runs.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(runListResponse.mission_id);
}
```

## Start a run

Start a new run for a mission

`POST /ai/missions/{mission_id}/runs`

Optional: `input` (object), `metadata` (object)

```javascript
const run = await client.ai.missions.runs.create('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(run.data);
```

## Get run details

Get details of a specific run

`GET /ai/missions/{mission_id}/runs/{run_id}`

```javascript
const run = await client.ai.missions.runs.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(run.data);
```

## Update run

Update run status and/or result

`PATCH /ai/missions/{mission_id}/runs/{run_id}`

Optional: `error` (string), `metadata` (object), `result_payload` (object), `result_summary` (string), `status` (enum)

```javascript
const run = await client.ai.missions.runs.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(run.data);
```

## Cancel run

Cancel a running or paused run

`POST /ai/missions/{mission_id}/runs/{run_id}/cancel`

```javascript
const response = await client.ai.missions.runs.cancelRun('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response.data);
```

## List events

List events for a run (paginated)

`GET /ai/missions/{mission_id}/runs/{run_id}/events`

```javascript
// Automatically fetches more pages as needed.
for await (const eventListResponse of client.ai.missions.runs.events.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
)) {
  console.log(eventListResponse.event_id);
}
```

## Log event

Log an event for a run

`POST /ai/missions/{mission_id}/runs/{run_id}/events` — Required: `type`, `summary`

Optional: `agent_id` (string), `idempotency_key` (string), `payload` (object), `step_id` (string)

```javascript
const response = await client.ai.missions.runs.events.log('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  summary: 'summary',
  type: 'status_change',
});

console.log(response.data);
```

## Get event details

Get details of a specific event

`GET /ai/missions/{mission_id}/runs/{run_id}/events/{event_id}`

```javascript
const response = await client.ai.missions.runs.events.getEventDetails('event_id', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  run_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response.data);
```

## Pause run

Pause a running run

`POST /ai/missions/{mission_id}/runs/{run_id}/pause`

```javascript
const response = await client.ai.missions.runs.pauseRun('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response.data);
```

## Get plan

Get the plan (all steps) for a run

`GET /ai/missions/{mission_id}/runs/{run_id}/plan`

```javascript
const plan = await client.ai.missions.runs.plan.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(plan.data);
```

## Create initial plan

Create the initial plan for a run

`POST /ai/missions/{mission_id}/runs/{run_id}/plan` — Required: `steps`

```javascript
const plan = await client.ai.missions.runs.plan.create('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  steps: [
    {
      description: 'description',
      sequence: 0,
      step_id: 'step_id',
    },
  ],
});

console.log(plan.data);
```

## Add step(s) to plan

Add one or more steps to an existing plan

`POST /ai/missions/{mission_id}/runs/{run_id}/plan/steps` — Required: `steps`

```javascript
const response = await client.ai.missions.runs.plan.addStepsToPlan(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
    steps: [
      {
        description: 'description',
        sequence: 0,
        step_id: 'step_id',
      },
    ],
  },
);

console.log(response.data);
```

## Get step details

Get details of a specific plan step

`GET /ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}`

```javascript
const response = await client.ai.missions.runs.plan.getStepDetails('step_id', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  run_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response.data);
```

## Update step status

Update the status of a plan step

`PATCH /ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}`

Optional: `metadata` (object), `status` (enum)

```javascript
const response = await client.ai.missions.runs.plan.updateStep('step_id', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  run_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response.data);
```

## Resume run

Resume a paused run

`POST /ai/missions/{mission_id}/runs/{run_id}/resume`

```javascript
const response = await client.ai.missions.runs.resumeRun('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response.data);
```

## List linked Telnyx agents

List all Telnyx agents linked to a run

`GET /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents`

```javascript
const telnyxAgents = await client.ai.missions.runs.telnyxAgents.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(telnyxAgents.data);
```

## Link Telnyx agent to run

Link a Telnyx AI agent (voice/messaging) to a run

`POST /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents` — Required: `telnyx_agent_id`

```javascript
const response = await client.ai.missions.runs.telnyxAgents.link(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', telnyx_agent_id: 'telnyx_agent_id' },
);

console.log(response.data);
```

## Unlink Telnyx agent

Unlink a Telnyx agent from a run

`DELETE /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents/{telnyx_agent_id}`

```javascript
await client.ai.missions.runs.telnyxAgents.unlink('telnyx_agent_id', {
  mission_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  run_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});
```
