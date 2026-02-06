---
name: telnyx-video-ruby
description: >-
  Create and manage video rooms for real-time video communication and
  conferencing. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: video
  language: ruby
---

# Telnyx Video - Ruby

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

## View a list of room compositions.

`GET /room_compositions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.room_compositions.list

puts(page)
```

## Create a room composition.

Asynchronously create a room composition.

`POST /room_compositions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room_composition = telnyx.room_compositions.create

puts(room_composition)
```

## View a room composition.

`GET /room_compositions/{room_composition_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room_composition = telnyx.room_compositions.retrieve("5219b3af-87c6-4c08-9b58-5a533d893e21")

puts(room_composition)
```

## Delete a room composition.

Synchronously delete a room composition.

`DELETE /room_compositions/{room_composition_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.room_compositions.delete("5219b3af-87c6-4c08-9b58-5a533d893e21")

puts(result)
```

## View a list of room participants.

`GET /room_participants`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.room_participants.list

puts(page)
```

## View a room participant.

`GET /room_participants/{room_participant_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room_participant = telnyx.room_participants.retrieve("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(room_participant)
```

## View a list of room recordings.

`GET /room_recordings`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.room_recordings.list

puts(page)
```

## Delete several room recordings in a bulk.

`DELETE /room_recordings`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.room_recordings.delete_bulk

puts(response)
```

## View a room recording.

`GET /room_recordings/{room_recording_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room_recording = telnyx.room_recordings.retrieve("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(room_recording)
```

## Delete a room recording.

Synchronously delete a Room Recording.

`DELETE /room_recordings/{room_recording_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.room_recordings.delete("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(result)
```

## View a list of room sessions.

`GET /room_sessions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.rooms.sessions.list_0

puts(page)
```

## View a room session.

`GET /room_sessions/{room_session_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

session = telnyx.rooms.sessions.retrieve("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(session)
```

## End a room session.

Note: this will also kick all participants currently present in the room

`POST /room_sessions/{room_session_id}/actions/end`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.rooms.sessions.actions.end_("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(response)
```

## Kick participants from a room session.

`POST /room_sessions/{room_session_id}/actions/kick`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.rooms.sessions.actions.kick("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(response)
```

## Mute participants in room session.

`POST /room_sessions/{room_session_id}/actions/mute`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.rooms.sessions.actions.mute("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(response)
```

## Unmute participants in room session.

`POST /room_sessions/{room_session_id}/actions/unmute`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.rooms.sessions.actions.unmute("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(response)
```

## View a list of room participants.

`GET /room_sessions/{room_session_id}/participants`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.rooms.sessions.retrieve_participants("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(page)
```

## View a list of rooms.

`GET /rooms`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.rooms.list

puts(page)
```

## Create a room.

Synchronously create a Room.

`POST /rooms`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room = telnyx.rooms.create

puts(room)
```

## View a room.

`GET /rooms/{room_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room = telnyx.rooms.retrieve("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(room)
```

## Update a room.

Synchronously update a Room.

`PATCH /rooms/{room_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

room = telnyx.rooms.update("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(room)
```

## Delete a room.

Synchronously delete a Room.

`DELETE /rooms/{room_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.rooms.delete("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(result)
```

## Create Client Token to join a room.

Synchronously create an Client Token to join a Room.

`POST /rooms/{room_id}/actions/generate_join_client_token`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.rooms.actions.generate_join_client_token("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(response)
```

## Refresh Client Token to join a room.

Synchronously refresh an Client Token to join a Room.

`POST /rooms/{room_id}/actions/refresh_client_token` — Required: `refresh_token`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.rooms.actions.refresh_client_token(
  "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
  refresh_token: "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0ZWxueXhfdGVsZXBob255IiwiZXhwIjoxNTkwMDEwMTQzLCJpYXQiOjE1ODc1OTA5NDMsImlzcyI6InRlbG55eF90ZWxlcGhvbnkiLCJqdGkiOiJiOGM3NDgzNy1kODllLTRhNjUtOWNmMi0zNGM3YTZmYTYwYzgiLCJuYmYiOjE1ODc1OTA5NDIsInN1YiI6IjVjN2FjN2QwLWRiNjUtNGYxMS05OGUxLWVlYzBkMWQ1YzZhZSIsInRlbF90b2tlbiI6InJqX1pra1pVT1pNeFpPZk9tTHBFVUIzc2lVN3U2UmpaRmVNOXMtZ2JfeENSNTZXRktGQUppTXlGMlQ2Q0JSbWxoX1N5MGlfbGZ5VDlBSThzRWlmOE1USUlzenl6U2xfYURuRzQ4YU81MHlhSEd1UlNZYlViU1ltOVdJaVEwZz09IiwidHlwIjoiYWNjZXNzIn0.gNEwzTow5MLLPLQENytca7pUN79PmPj6FyqZWW06ZeEmesxYpwKh0xRtA0TzLh6CDYIRHrI8seofOO0YFGDhpQ"
)

puts(response)
```

## View a list of room sessions.

`GET /rooms/{room_id}/sessions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.rooms.sessions.list_1("0ccc7b54-4df3-4bca-a65a-3da1ecc777f0")

puts(page)
```
