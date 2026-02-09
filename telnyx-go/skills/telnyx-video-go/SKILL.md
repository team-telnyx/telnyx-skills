---
name: telnyx-video-go
description: >-
  Create and manage video rooms for real-time video communication and
  conferencing. This skill provides Go SDK examples.
metadata:
  author: telnyx
  product: video
  language: go
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Video - Go

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

## View a list of room compositions.

`GET /room_compositions`

```go
	page, err := client.RoomCompositions.List(context.TODO(), telnyx.RoomCompositionListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create a room composition.

Asynchronously create a room composition.

`POST /room_compositions`

```go
	roomComposition, err := client.RoomCompositions.New(context.TODO(), telnyx.RoomCompositionNewParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", roomComposition.Data)
```

## View a room composition.

`GET /room_compositions/{room_composition_id}`

```go
	roomComposition, err := client.RoomCompositions.Get(context.TODO(), "5219b3af-87c6-4c08-9b58-5a533d893e21")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", roomComposition.Data)
```

## Delete a room composition.

Synchronously delete a room composition.

`DELETE /room_compositions/{room_composition_id}`

```go
	err := client.RoomCompositions.Delete(context.TODO(), "5219b3af-87c6-4c08-9b58-5a533d893e21")
	if err != nil {
		panic(err.Error())
	}
```

## View a list of room participants.

`GET /room_participants`

```go
	page, err := client.RoomParticipants.List(context.TODO(), telnyx.RoomParticipantListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## View a room participant.

`GET /room_participants/{room_participant_id}`

```go
	roomParticipant, err := client.RoomParticipants.Get(context.TODO(), "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", roomParticipant.Data)
```

## View a list of room recordings.

`GET /room_recordings`

```go
	page, err := client.RoomRecordings.List(context.TODO(), telnyx.RoomRecordingListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Delete several room recordings in a bulk.

`DELETE /room_recordings`

```go
	response, err := client.RoomRecordings.DeleteBulk(context.TODO(), telnyx.RoomRecordingDeleteBulkParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## View a room recording.

`GET /room_recordings/{room_recording_id}`

```go
	roomRecording, err := client.RoomRecordings.Get(context.TODO(), "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", roomRecording.Data)
```

## Delete a room recording.

Synchronously delete a Room Recording.

`DELETE /room_recordings/{room_recording_id}`

```go
	err := client.RoomRecordings.Delete(context.TODO(), "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")
	if err != nil {
		panic(err.Error())
	}
```

## View a list of room sessions.

`GET /room_sessions`

```go
	page, err := client.Rooms.Sessions.List0(context.TODO(), telnyx.RoomSessionList0Params{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## View a room session.

`GET /room_sessions/{room_session_id}`

```go
	session, err := client.Rooms.Sessions.Get(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomSessionGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", session.Data)
```

## End a room session.

Note: this will also kick all participants currently present in the room

`POST /room_sessions/{room_session_id}/actions/end`

```go
	response, err := client.Rooms.Sessions.Actions.End(context.TODO(), "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Kick participants from a room session.

`POST /room_sessions/{room_session_id}/actions/kick`

```go
	response, err := client.Rooms.Sessions.Actions.Kick(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomSessionActionKickParams{
			ActionsParticipantsRequest: telnyx.ActionsParticipantsRequestParam{},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Mute participants in room session.

`POST /room_sessions/{room_session_id}/actions/mute`

```go
	response, err := client.Rooms.Sessions.Actions.Mute(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomSessionActionMuteParams{
			ActionsParticipantsRequest: telnyx.ActionsParticipantsRequestParam{},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Unmute participants in room session.

`POST /room_sessions/{room_session_id}/actions/unmute`

```go
	response, err := client.Rooms.Sessions.Actions.Unmute(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomSessionActionUnmuteParams{
			ActionsParticipantsRequest: telnyx.ActionsParticipantsRequestParam{},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## View a list of room participants.

`GET /room_sessions/{room_session_id}/participants`

```go
	page, err := client.Rooms.Sessions.GetParticipants(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomSessionGetParticipantsParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## View a list of rooms.

`GET /rooms`

```go
	page, err := client.Rooms.List(context.TODO(), telnyx.RoomListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```

## Create a room.

Synchronously create a Room.

`POST /rooms`

```go
	room, err := client.Rooms.New(context.TODO(), telnyx.RoomNewParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", room.Data)
```

## View a room.

`GET /rooms/{room_id}`

```go
	room, err := client.Rooms.Get(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", room.Data)
```

## Update a room.

Synchronously update a Room.

`PATCH /rooms/{room_id}`

```go
	room, err := client.Rooms.Update(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", room.Data)
```

## Delete a room.

Synchronously delete a Room.

`DELETE /rooms/{room_id}`

```go
	err := client.Rooms.Delete(context.TODO(), "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")
	if err != nil {
		panic(err.Error())
	}
```

## Create Client Token to join a room.

Synchronously create an Client Token to join a Room.

`POST /rooms/{room_id}/actions/generate_join_client_token`

```go
	response, err := client.Rooms.Actions.GenerateJoinClientToken(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomActionGenerateJoinClientTokenParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## Refresh Client Token to join a room.

Synchronously refresh an Client Token to join a Room.

`POST /rooms/{room_id}/actions/refresh_client_token` — Required: `refresh_token`

```go
	response, err := client.Rooms.Actions.RefreshClientToken(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomActionRefreshClientTokenParams{
			RefreshToken: "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0ZWxueXhfdGVsZXBob255IiwiZXhwIjoxNTkwMDEwMTQzLCJpYXQiOjE1ODc1OTA5NDMsImlzcyI6InRlbG55eF90ZWxlcGhvbnkiLCJqdGkiOiJiOGM3NDgzNy1kODllLTRhNjUtOWNmMi0zNGM3YTZmYTYwYzgiLCJuYmYiOjE1ODc1OTA5NDIsInN1YiI6IjVjN2FjN2QwLWRiNjUtNGYxMS05OGUxLWVlYzBkMWQ1YzZhZSIsInRlbF90b2tlbiI6InJqX1pra1pVT1pNeFpPZk9tTHBFVUIzc2lVN3U2UmpaRmVNOXMtZ2JfeENSNTZXRktGQUppTXlGMlQ2Q0JSbWxoX1N5MGlfbGZ5VDlBSThzRWlmOE1USUlzenl6U2xfYURuRzQ4YU81MHlhSEd1UlNZYlViU1ltOVdJaVEwZz09IiwidHlwIjoiYWNjZXNzIn0.gNEwzTow5MLLPLQENytca7pUN79PmPj6FyqZWW06ZeEmesxYpwKh0xRtA0TzLh6CDYIRHrI8seofOO0YFGDhpQ",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.Data)
```

## View a list of room sessions.

`GET /rooms/{room_id}/sessions`

```go
	page, err := client.Rooms.Sessions.List1(
		context.TODO(),
		"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
		telnyx.RoomSessionList1Params{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
```
