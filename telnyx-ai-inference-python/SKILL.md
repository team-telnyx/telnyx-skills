---
name: telnyx-ai-inference-python
description: >-
  Access Telnyx LLM inference APIs, embeddings, and AI analytics for call
  insights and summaries. This skill provides Python SDK examples.
metadata:
  author: telnyx
  product: ai-inference
  language: python
---

# Telnyx Ai Inference - Python

## Installation

```bash
pip install telnyx
```

## Setup

```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),  # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## List conversations

Retrieve a list of all AI conversations configured by the user.

`GET /ai/conversations`

```python
conversations = client.ai.conversations.list()
print(conversations.data)
```

## Create a conversation

Create a new AI Conversation.

`POST /ai/conversations`

```python
conversation = client.ai.conversations.create()
print(conversation.id)
```

## Get Insight Template Groups

Get all insight groups

`GET /ai/conversations/insight-groups`

```python
page = client.ai.conversations.insight_groups.retrieve_insight_groups()
page = page.data[0]
print(page.id)
```

## Create Insight Template Group

Create a new insight group

`POST /ai/conversations/insight-groups` — Required: `name`

```python
insight_template_group_detail = client.ai.conversations.insight_groups.insight_groups(
    name="name",
)
print(insight_template_group_detail.data)
```

## Get Insight Template Group

Get insight group by ID

`GET /ai/conversations/insight-groups/{group_id}`

```python
insight_template_group_detail = client.ai.conversations.insight_groups.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(insight_template_group_detail.data)
```

## Update Insight Template Group

Update an insight template group

`PUT /ai/conversations/insight-groups/{group_id}`

```python
insight_template_group_detail = client.ai.conversations.insight_groups.update(
    group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(insight_template_group_detail.data)
```

## Delete Insight Template Group

Delete insight group by ID

`DELETE /ai/conversations/insight-groups/{group_id}`

```python
client.ai.conversations.insight_groups.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Assign Insight Template To Group

Assign an insight to a group

`POST /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign`

```python
client.ai.conversations.insight_groups.insights.assign(
    insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Unassign Insight Template From Group

Remove an insight from a group

`DELETE /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign`

```python
client.ai.conversations.insight_groups.insights.delete_unassign(
    insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Get Insight Templates

Get all insights

`GET /ai/conversations/insights`

```python
page = client.ai.conversations.insights.list()
page = page.data[0]
print(page.id)
```

## Create Insight Template

Create a new insight

`POST /ai/conversations/insights` — Required: `instructions`, `name`

```python
insight_template_detail = client.ai.conversations.insights.create(
    instructions="instructions",
    name="name",
)
print(insight_template_detail.data)
```

## Get Insight Template

Get insight by ID

`GET /ai/conversations/insights/{insight_id}`

```python
insight_template_detail = client.ai.conversations.insights.retrieve(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(insight_template_detail.data)
```

## Update Insight Template

Update an insight template

`PUT /ai/conversations/insights/{insight_id}`

```python
insight_template_detail = client.ai.conversations.insights.update(
    insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(insight_template_detail.data)
```

## Delete Insight Template

Delete insight by ID

`DELETE /ai/conversations/insights/{insight_id}`

```python
client.ai.conversations.insights.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Get a conversation

Retrieve a specific AI conversation by its ID.

`GET /ai/conversations/{conversation_id}`

```python
conversation = client.ai.conversations.retrieve(
    "conversation_id",
)
print(conversation.data)
```

## Update conversation metadata

Update metadata for a specific conversation.

`PUT /ai/conversations/{conversation_id}`

```python
conversation = client.ai.conversations.update(
    conversation_id="conversation_id",
)
print(conversation.data)
```

## Delete a conversation

Delete a specific conversation by its ID.

`DELETE /ai/conversations/{conversation_id}`

```python
client.ai.conversations.delete(
    "conversation_id",
)
```

## Get insights for a conversation

Retrieve insights for a specific conversation

`GET /ai/conversations/{conversation_id}/conversations-insights`

```python
response = client.ai.conversations.retrieve_conversations_insights(
    "conversation_id",
)
print(response.data)
```

## Create Message

Add a new message to the conversation.

`POST /ai/conversations/{conversation_id}/message` — Required: `role`

```python
client.ai.conversations.add_message(
    conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    role="role",
)
```

## Get conversation messages

Retrieve messages for a specific conversation, including tool calls made by the assistant.

`GET /ai/conversations/{conversation_id}/messages`

```python
messages = client.ai.conversations.messages.list(
    "conversation_id",
)
print(messages.data)
```

## Get Tasks by Status

Retrieve tasks for the user that are either `queued`, `processing`, `failed`, `success` or `partial_success` based on the query string.

`GET /ai/embeddings`

```python
embeddings = client.ai.embeddings.list()
print(embeddings.data)
```

## Embed documents

Perform embedding on a Telnyx Storage Bucket using the a embedding model.

`POST /ai/embeddings` — Required: `bucket_name`

```python
embedding_response = client.ai.embeddings.create(
    bucket_name="bucket_name",
)
print(embedding_response.data)
```

## List embedded buckets

Get all embedding buckets for a user.

`GET /ai/embeddings/buckets`

```python
buckets = client.ai.embeddings.buckets.list()
print(buckets.data)
```

## Get file-level embedding statuses for a bucket

Get all embedded files for a given user bucket, including their processing status.

`GET /ai/embeddings/buckets/{bucket_name}`

```python
bucket = client.ai.embeddings.buckets.retrieve(
    "bucket_name",
)
print(bucket.data)
```

## Disable AI for an Embedded Bucket

Deletes an entire bucket's embeddings and disables the bucket for AI-use, returning it to normal storage pricing.

`DELETE /ai/embeddings/buckets/{bucket_name}`

```python
client.ai.embeddings.buckets.delete(
    "bucket_name",
)
```

## Search for documents

Perform a similarity search on a Telnyx Storage Bucket, returning the most similar `num_docs` document chunks to the query.

`POST /ai/embeddings/similarity-search` — Required: `bucket_name`, `query`

```python
response = client.ai.embeddings.similarity_search(
    bucket_name="bucket_name",
    query="query",
)
print(response.data)
```

## Embed URL content

Embed website content from a specified URL, including child pages up to 5 levels deep within the same domain.

`POST /ai/embeddings/url` — Required: `url`, `bucket_name`

```python
embedding_response = client.ai.embeddings.url(
    bucket_name="bucket_name",
    url="url",
)
print(embedding_response.data)
```

## Get an embedding task's status

Check the status of a current embedding task.

`GET /ai/embeddings/{task_id}`

```python
embedding = client.ai.embeddings.retrieve(
    "task_id",
)
print(embedding.data)
```

## List all clusters

`GET /ai/clusters`

```python
page = client.ai.clusters.list()
page = page.data[0]
print(page.task_id)
```

## Compute new clusters

Starts a background task to compute how the data in an [embedded storage bucket](https://developers.telnyx.com/api-reference/embeddings/embed-documents) is clustered.

`POST /ai/clusters` — Required: `bucket`

```python
response = client.ai.clusters.compute(
    bucket="bucket",
)
print(response.data)
```

## Fetch a cluster

`GET /ai/clusters/{task_id}`

```python
cluster = client.ai.clusters.retrieve(
    task_id="task_id",
)
print(cluster.data)
```

## Delete a cluster

`DELETE /ai/clusters/{task_id}`

```python
client.ai.clusters.delete(
    "task_id",
)
```

## Fetch a cluster visualization

`GET /ai/clusters/{task_id}/graph`

```python
response = client.ai.clusters.fetch_graph(
    task_id="task_id",
)
print(response)
content = response.read()
print(content)
```

## Transcribe speech to text

Transcribe speech to text.

`POST /ai/audio/transcriptions`

```python
response = client.ai.audio.transcribe(
    model="distil-whisper/distil-large-v2",
)
print(response.text)
```

## Create a chat completion

Chat with a language model.

`POST /ai/chat/completions` — Required: `messages`

```python
response = client.ai.chat.create_completion(
    messages=[{
        "role": "system",
        "content": "You are a friendly chatbot.",
    }, {
        "role": "user",
        "content": "Hello, world!",
    }],
)
print(response)
```

## List fine tuning jobs

Retrieve a list of all fine tuning jobs created by the user.

`GET /ai/fine_tuning/jobs`

```python
jobs = client.ai.fine_tuning.jobs.list()
print(jobs.data)
```

## Create a fine tuning job

Create a new fine tuning job.

`POST /ai/fine_tuning/jobs` — Required: `model`, `training_file`

```python
fine_tuning_job = client.ai.fine_tuning.jobs.create(
    model="model",
    training_file="training_file",
)
print(fine_tuning_job.id)
```

## Get a fine tuning job

Retrieve a fine tuning job by `job_id`.

`GET /ai/fine_tuning/jobs/{job_id}`

```python
fine_tuning_job = client.ai.fine_tuning.jobs.retrieve(
    "job_id",
)
print(fine_tuning_job.id)
```

## Cancel a fine tuning job

Cancel a fine tuning job.

`POST /ai/fine_tuning/jobs/{job_id}/cancel`

```python
fine_tuning_job = client.ai.fine_tuning.jobs.cancel(
    "job_id",
)
print(fine_tuning_job.id)
```

## Get available models

This endpoint returns a list of Open Source and OpenAI models that are available for use.

`GET /ai/models`

```python
response = client.ai.retrieve_models()
print(response.data)
```

## Summarize file content

Generate a summary of a file's contents.

`POST /ai/summarize` — Required: `bucket`, `filename`

```python
response = client.ai.summarize(
    bucket="bucket",
    filename="filename",
)
print(response.data)
```
