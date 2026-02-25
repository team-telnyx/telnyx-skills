---
name: telnyx-missions-go
description: >-
  Telnyx Missions SDK operations. This skill provides Go SDK examples.
metadata:
  author: telnyx
  product: missions
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Missions - Go

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
import (
  "context"
  "fmt"
  "os"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

client := telnyx.NewClient(
  option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
)
```

All examples below assume `client` is already initialized as shown above.

## List missions

List all missions for the organization

`GET /ai/missions`

```go
	page, err := client.AI.Missions.List(context.TODO(), telnyx.AIMissionListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create mission

Create a new mission definition

`POST /ai/missions` — Required: `name`

Optional: `description` (string), `execution_mode` (enum), `instructions` (string), `metadata` (object), `model` (string)

```go
	mission, err := client.AI.Missions.New(context.TODO(), telnyx.AIMissionNewParams{
		Name: "name",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mission.Data)
```

## List recent events

List recent events across all missions

`GET /ai/missions/events`

```go
	page, err := client.AI.Missions.ListEvents(context.TODO(), telnyx.AIMissionListEventsParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## List recent runs

List recent runs across all missions

`GET /ai/missions/runs`

```go
	page, err := client.AI.Missions.Runs.ListRuns(context.TODO(), telnyx.AIMissionRunListRunsParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Get mission

Get a mission by ID (includes tools, knowledge_bases, mcp_servers)

`GET /ai/missions/{mission_id}`

```go
	mission, err := client.AI.Missions.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", mission.Data)
```

## Update mission

Update a mission definition

`PUT /ai/missions/{mission_id}`

Optional: `description` (string), `execution_mode` (enum), `instructions` (string), `metadata` (object), `model` (string), `name` (string)

```go
	response, err := client.AI.Missions.UpdateMission(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionUpdateMissionParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Delete mission

Delete a mission

`DELETE /ai/missions/{mission_id}`

```go
	err := client.AI.Missions.DeleteMission(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
	if err != nil {
		panic(err.Error())
	}
```

## Clone mission

Clone an existing mission

`POST /ai/missions/{mission_id}/clone`

```go
	response, err := client.AI.Missions.CloneMission(context.TODO(), "mission_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response)
```

## List runs for mission

List all runs for a specific mission

`GET /ai/missions/{mission_id}/runs`

```go
	page, err := client.AI.Missions.Runs.List(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Start a run

Start a new run for a mission

`POST /ai/missions/{mission_id}/runs`

Optional: `input` (object), `metadata` (object)

```go
	run, err := client.AI.Missions.Runs.New(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunNewParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", run.Data)
```

## Get run details

Get details of a specific run

`GET /ai/missions/{mission_id}/runs/{run_id}`

```go
	run, err := client.AI.Missions.Runs.Get(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunGetParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", run.Data)
```

## Update run

Update run status and/or result

`PATCH /ai/missions/{mission_id}/runs/{run_id}`

Optional: `error` (string), `metadata` (object), `result_payload` (object), `result_summary` (string), `status` (enum)

```go
	run, err := client.AI.Missions.Runs.Update(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunUpdateParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", run.Data)
```

## Cancel run

Cancel a running or paused run

`POST /ai/missions/{mission_id}/runs/{run_id}/cancel`

```go
	response, err := client.AI.Missions.Runs.CancelRun(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunCancelRunParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List events

List events for a run (paginated)

`GET /ai/missions/{mission_id}/runs/{run_id}/events`

```go
	page, err := client.AI.Missions.Runs.Events.List(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunEventListParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Log event

Log an event for a run

`POST /ai/missions/{mission_id}/runs/{run_id}/events` — Required: `type`, `summary`

Optional: `agent_id` (string), `idempotency_key` (string), `payload` (object), `step_id` (string)

```go
	response, err := client.AI.Missions.Runs.Events.Log(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunEventLogParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			Summary:   "summary",
			Type:      telnyx.AIMissionRunEventLogParamsTypeStatusChange,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Get event details

Get details of a specific event

`GET /ai/missions/{mission_id}/runs/{run_id}/events/{event_id}`

```go
	response, err := client.AI.Missions.Runs.Events.GetEventDetails(
		context.TODO(),
		"event_id",
		telnyx.AIMissionRunEventGetEventDetailsParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			RunID:     "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Pause run

Pause a running run

`POST /ai/missions/{mission_id}/runs/{run_id}/pause`

```go
	response, err := client.AI.Missions.Runs.PauseRun(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunPauseRunParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Get plan

Get the plan (all steps) for a run

`GET /ai/missions/{mission_id}/runs/{run_id}/plan`

```go
	plan, err := client.AI.Missions.Runs.Plan.Get(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunPlanGetParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", plan.Data)
```

## Create initial plan

Create the initial plan for a run

`POST /ai/missions/{mission_id}/runs/{run_id}/plan` — Required: `steps`

```go
	plan, err := client.AI.Missions.Runs.Plan.New(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunPlanNewParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			Steps: []telnyx.AIMissionRunPlanNewParamsStep{{
				Description: "description",
				Sequence:    0,
				StepID:      "step_id",
			}},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", plan.Data)
```

## Add step(s) to plan

Add one or more steps to an existing plan

`POST /ai/missions/{mission_id}/runs/{run_id}/plan/steps` — Required: `steps`

```go
	response, err := client.AI.Missions.Runs.Plan.AddStepsToPlan(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunPlanAddStepsToPlanParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			Steps: []telnyx.AIMissionRunPlanAddStepsToPlanParamsStep{{
				Description: "description",
				Sequence:    0,
				StepID:      "step_id",
			}},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Get step details

Get details of a specific plan step

`GET /ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}`

```go
	response, err := client.AI.Missions.Runs.Plan.GetStepDetails(
		context.TODO(),
		"step_id",
		telnyx.AIMissionRunPlanGetStepDetailsParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			RunID:     "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Update step status

Update the status of a plan step

`PATCH /ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}`

Optional: `metadata` (object), `status` (enum)

```go
	response, err := client.AI.Missions.Runs.Plan.UpdateStep(
		context.TODO(),
		"step_id",
		telnyx.AIMissionRunPlanUpdateStepParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			RunID:     "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Resume run

Resume a paused run

`POST /ai/missions/{mission_id}/runs/{run_id}/resume`

```go
	response, err := client.AI.Missions.Runs.ResumeRun(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunResumeRunParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## List linked Telnyx agents

List all Telnyx agents linked to a run

`GET /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents`

```go
	telnyxAgents, err := client.AI.Missions.Runs.TelnyxAgents.List(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunTelnyxAgentListParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", telnyxAgents.Data)
```

## Link Telnyx agent to run

Link a Telnyx AI agent (voice/messaging) to a run

`POST /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents` — Required: `telnyx_agent_id`

```go
	response, err := client.AI.Missions.Runs.TelnyxAgents.Link(
		context.TODO(),
		"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		telnyx.AIMissionRunTelnyxAgentLinkParams{
			MissionID:     "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			TelnyxAgentID: "telnyx_agent_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Unlink Telnyx agent

Unlink a Telnyx agent from a run

`DELETE /ai/missions/{mission_id}/runs/{run_id}/telnyx-agents/{telnyx_agent_id}`

```go
	err := client.AI.Missions.Runs.TelnyxAgents.Unlink(
		context.TODO(),
		"telnyx_agent_id",
		telnyx.AIMissionRunTelnyxAgentUnlinkParams{
			MissionID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
			RunID:     "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
		},
	)
	if err != nil {
		panic(err.Error())
	}
```
