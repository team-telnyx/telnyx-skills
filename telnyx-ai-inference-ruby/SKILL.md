---
name: telnyx-ai-inference-ruby
description: >-
  Access Telnyx LLM inference APIs, embeddings, and AI analytics for call
  insights and summaries. This skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: ai-inference
  language: ruby
---

# Telnyx Ai Inference - Ruby

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

## List conversations

Retrieve a list of all AI conversations configured by the user.

`GET /ai/conversations`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

conversations = telnyx.ai.conversations.list

puts(conversations)
```

## Create a conversation

Create a new AI Conversation.

`POST /ai/conversations`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

conversation = telnyx.ai.conversations.create

puts(conversation)
```

## Get Insight Template Groups

Get all insight groups

`GET /ai/conversations/insight-groups`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.conversations.insight_groups.retrieve_insight_groups

puts(page)
```

## Create Insight Template Group

Create a new insight group

`POST /ai/conversations/insight-groups` — Required: `name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

insight_template_group_detail = telnyx.ai.conversations.insight_groups.insight_groups(name: "name")

puts(insight_template_group_detail)
```

## Get Insight Template Group

Get insight group by ID

`GET /ai/conversations/insight-groups/{group_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

insight_template_group_detail = telnyx.ai.conversations.insight_groups.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(insight_template_group_detail)
```

## Update Insight Template Group

Update an insight template group

`PUT /ai/conversations/insight-groups/{group_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

insight_template_group_detail = telnyx.ai.conversations.insight_groups.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(insight_template_group_detail)
```

## Delete Insight Template Group

Delete insight group by ID

`DELETE /ai/conversations/insight-groups/{group_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.conversations.insight_groups.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(result)
```

## Assign Insight Template To Group

Assign an insight to a group

`POST /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.conversations.insight_groups.insights.assign(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  group_id: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
)

puts(result)
```

## Unassign Insight Template From Group

Remove an insight from a group

`DELETE /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.conversations.insight_groups.insights.delete_unassign(
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  group_id: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
)

puts(result)
```

## Get Insight Templates

Get all insights

`GET /ai/conversations/insights`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.conversations.insights.list

puts(page)
```

## Create Insight Template

Create a new insight

`POST /ai/conversations/insights` — Required: `instructions`, `name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

insight_template_detail = telnyx.ai.conversations.insights.create(instructions: "instructions", name: "name")

puts(insight_template_detail)
```

## Get Insight Template

Get insight by ID

`GET /ai/conversations/insights/{insight_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

insight_template_detail = telnyx.ai.conversations.insights.retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(insight_template_detail)
```

## Update Insight Template

Update an insight template

`PUT /ai/conversations/insights/{insight_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

insight_template_detail = telnyx.ai.conversations.insights.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(insight_template_detail)
```

## Delete Insight Template

Delete insight by ID

`DELETE /ai/conversations/insights/{insight_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.conversations.insights.delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")

puts(result)
```

## Get a conversation

Retrieve a specific AI conversation by its ID.

`GET /ai/conversations/{conversation_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

conversation = telnyx.ai.conversations.retrieve("conversation_id")

puts(conversation)
```

## Update conversation metadata

Update metadata for a specific conversation.

`PUT /ai/conversations/{conversation_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

conversation = telnyx.ai.conversations.update("conversation_id")

puts(conversation)
```

## Delete a conversation

Delete a specific conversation by its ID.

`DELETE /ai/conversations/{conversation_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.conversations.delete("conversation_id")

puts(result)
```

## Get insights for a conversation

Retrieve insights for a specific conversation

`GET /ai/conversations/{conversation_id}/conversations-insights`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.conversations.retrieve_conversations_insights("conversation_id")

puts(response)
```

## Create Message

Add a new message to the conversation.

`POST /ai/conversations/{conversation_id}/message` — Required: `role`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.conversations.add_message("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", role: "role")

puts(result)
```

## Get conversation messages

Retrieve messages for a specific conversation, including tool calls made by the assistant.

`GET /ai/conversations/{conversation_id}/messages`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

messages = telnyx.ai.conversations.messages.list("conversation_id")

puts(messages)
```

## Get Tasks by Status

Retrieve tasks for the user that are either `queued`, `processing`, `failed`, `success` or `partial_success` based on the query string.

`GET /ai/embeddings`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

embeddings = telnyx.ai.embeddings.list

puts(embeddings)
```

## Embed documents

Perform embedding on a Telnyx Storage Bucket using the a embedding model.

`POST /ai/embeddings` — Required: `bucket_name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

embedding_response = telnyx.ai.embeddings.create(bucket_name: "bucket_name")

puts(embedding_response)
```

## List embedded buckets

Get all embedding buckets for a user.

`GET /ai/embeddings/buckets`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

buckets = telnyx.ai.embeddings.buckets.list

puts(buckets)
```

## Get file-level embedding statuses for a bucket

Get all embedded files for a given user bucket, including their processing status.

`GET /ai/embeddings/buckets/{bucket_name}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

bucket = telnyx.ai.embeddings.buckets.retrieve("bucket_name")

puts(bucket)
```

## Disable AI for an Embedded Bucket

Deletes an entire bucket's embeddings and disables the bucket for AI-use, returning it to normal storage pricing.

`DELETE /ai/embeddings/buckets/{bucket_name}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.embeddings.buckets.delete("bucket_name")

puts(result)
```

## Search for documents

Perform a similarity search on a Telnyx Storage Bucket, returning the most similar `num_docs` document chunks to the query.

`POST /ai/embeddings/similarity-search` — Required: `bucket_name`, `query`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.embeddings.similarity_search(bucket_name: "bucket_name", query: "query")

puts(response)
```

## Embed URL content

Embed website content from a specified URL, including child pages up to 5 levels deep within the same domain.

`POST /ai/embeddings/url` — Required: `url`, `bucket_name`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

embedding_response = telnyx.ai.embeddings.url(bucket_name: "bucket_name", url: "url")

puts(embedding_response)
```

## Get an embedding task's status

Check the status of a current embedding task.

`GET /ai/embeddings/{task_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

embedding = telnyx.ai.embeddings.retrieve("task_id")

puts(embedding)
```

## List all clusters

`GET /ai/clusters`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

page = telnyx.ai.clusters.list

puts(page)
```

## Compute new clusters

Starts a background task to compute how the data in an [embedded storage bucket](https://developers.telnyx.com/api-reference/embeddings/embed-documents) is clustered.

`POST /ai/clusters` — Required: `bucket`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.clusters.compute(bucket: "bucket")

puts(response)
```

## Fetch a cluster

`GET /ai/clusters/{task_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

cluster = telnyx.ai.clusters.retrieve("task_id")

puts(cluster)
```

## Delete a cluster

`DELETE /ai/clusters/{task_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

result = telnyx.ai.clusters.delete("task_id")

puts(result)
```

## Fetch a cluster visualization

`GET /ai/clusters/{task_id}/graph`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.clusters.fetch_graph("task_id")

puts(response)
```

## Transcribe speech to text

Transcribe speech to text.

`POST /ai/audio/transcriptions`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.audio.transcribe(model: :"distil-whisper/distil-large-v2")

puts(response)
```

## Create a chat completion

Chat with a language model.

`POST /ai/chat/completions` — Required: `messages`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.chat.create_completion(
  messages: [{content: "You are a friendly chatbot.", role: :system}, {content: "Hello, world!", role: :user}]
)

puts(response)
```

## List fine tuning jobs

Retrieve a list of all fine tuning jobs created by the user.

`GET /ai/fine_tuning/jobs`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

jobs = telnyx.ai.fine_tuning.jobs.list

puts(jobs)
```

## Create a fine tuning job

Create a new fine tuning job.

`POST /ai/fine_tuning/jobs` — Required: `model`, `training_file`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

fine_tuning_job = telnyx.ai.fine_tuning.jobs.create(model: "model", training_file: "training_file")

puts(fine_tuning_job)
```

## Get a fine tuning job

Retrieve a fine tuning job by `job_id`.

`GET /ai/fine_tuning/jobs/{job_id}`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

fine_tuning_job = telnyx.ai.fine_tuning.jobs.retrieve("job_id")

puts(fine_tuning_job)
```

## Cancel a fine tuning job

Cancel a fine tuning job.

`POST /ai/fine_tuning/jobs/{job_id}/cancel`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

fine_tuning_job = telnyx.ai.fine_tuning.jobs.cancel("job_id")

puts(fine_tuning_job)
```

## Get available models

This endpoint returns a list of Open Source and OpenAI models that are available for use.

`GET /ai/models`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.retrieve_models

puts(response)
```

## Summarize file content

Generate a summary of a file's contents.

`POST /ai/summarize` — Required: `bucket`, `filename`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.ai.summarize(bucket: "bucket", filename: "filename")

puts(response)
```
