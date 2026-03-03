---
name: telnyx-ai-inference-curl
description: >-
  Access Telnyx LLM inference APIs, embeddings, and AI analytics for call
  insights and summaries. This skill provides REST API (curl) examples.
metadata:
  author: telnyx
  product: ai-inference
  language: curl
  generated_by: telnyx-ext-skills-generator
---

<!-- Auto-generated from Telnyx OpenAPI specs. Do not edit. -->

# Telnyx Ai Inference - curl

## Installation

```text
# curl is pre-installed on macOS, Linux, and Windows 10+
```

## Setup

```bash
export TELNYX_API_KEY="YOUR_API_KEY_HERE"
```

All examples below use `$TELNYX_API_KEY` for authentication.

## Transcribe speech to text

Transcribe speech to text.

`POST /ai/audio/transcriptions`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "file=@/path/to/file" \
  -F "file_url=https://example.com/file.mp3" \
  -F "model=distil-whisper/distil-large-v2" \
  -F "response_format=json" \
  -F "timestamp_granularities[]=segment" \
  -F "language=en-US" \
  -F "model_config={'smart_format': True, 'punctuate': True}" \
  "https://api.telnyx.com/v2/ai/audio/transcriptions"
```

## Create a chat completion

Chat with a language model.

`POST /ai/chat/completions` — Required: `messages`

Optional: `api_key_ref` (string), `best_of` (integer), `early_stopping` (boolean), `frequency_penalty` (number), `guided_choice` (array[string]), `guided_json` (object), `guided_regex` (string), `length_penalty` (number), `logprobs` (boolean), `max_tokens` (integer), `min_p` (number), `model` (string), `n` (number), `presence_penalty` (number), `response_format` (object), `stream` (boolean), `temperature` (number), `tool_choice` (enum), `tools` (array[object]), `top_logprobs` (integer), `top_p` (number), `use_beam_search` (boolean)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a friendly chatbot."
    },
    {
      "role": "user",
      "content": "Hello, world!"
    }
  ]
}' \
  "https://api.telnyx.com/v2/ai/chat/completions"
```

## List conversations

Retrieve a list of all AI conversations configured by the user.

`GET /ai/conversations`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations"
```

## Create a conversation

Create a new AI Conversation.

`POST /ai/conversations`

Optional: `metadata` (object), `name` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/conversations"
```

## Get Insight Template Groups

Get all insight groups

`GET /ai/conversations/insight-groups`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/insight-groups"
```

## Create Insight Template Group

Create a new insight group

`POST /ai/conversations/insight-groups` — Required: `name`

Optional: `description` (string), `webhook` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}' \
  "https://api.telnyx.com/v2/ai/conversations/insight-groups"
```

## Get Insight Template Group

Get insight group by ID

`GET /ai/conversations/insight-groups/{group_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/insight-groups/{group_id}"
```

## Update Insight Template Group

Update an insight template group

`PUT /ai/conversations/insight-groups/{group_id}`

Optional: `description` (string), `name` (string), `webhook` (string)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/conversations/insight-groups/{group_id}"
```

## Delete Insight Template Group

Delete insight group by ID

`DELETE /ai/conversations/insight-groups/{group_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/conversations/insight-groups/{group_id}"
```

## Assign Insight Template To Group

Assign an insight to a group

`POST /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign"
```

## Unassign Insight Template From Group

Remove an insight from a group

`DELETE /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign"
```

## Get Insight Templates

Get all insights

`GET /ai/conversations/insights`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/insights"
```

## Create Insight Template

Create a new insight

`POST /ai/conversations/insights` — Required: `instructions`, `name`

Optional: `json_schema` (object), `webhook` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "instructions": "string",
  "name": "string"
}' \
  "https://api.telnyx.com/v2/ai/conversations/insights"
```

## Get Insight Template

Get insight by ID

`GET /ai/conversations/insights/{insight_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/insights/{insight_id}"
```

## Update Insight Template

Update an insight template

`PUT /ai/conversations/insights/{insight_id}`

Optional: `instructions` (string), `json_schema` (object), `name` (string), `webhook` (string)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/conversations/insights/{insight_id}"
```

## Delete Insight Template

Delete insight by ID

`DELETE /ai/conversations/insights/{insight_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/conversations/insights/{insight_id}"
```

## Get a conversation

Retrieve a specific AI conversation by its ID.

`GET /ai/conversations/{conversation_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/{conversation_id}"
```

## Update conversation metadata

Update metadata for a specific conversation.

`PUT /ai/conversations/{conversation_id}`

Optional: `metadata` (object)

```bash
curl \
  -X PUT \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/conversations/{conversation_id}"
```

## Delete a conversation

Delete a specific conversation by its ID.

`DELETE /ai/conversations/{conversation_id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/conversations/{conversation_id}"
```

## Get insights for a conversation

Retrieve insights for a specific conversation

`GET /ai/conversations/{conversation_id}/conversations-insights`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/{conversation_id}/conversations-insights"
```

## Create Message

Add a new message to the conversation.

`POST /ai/conversations/{conversation_id}/message` — Required: `role`

Optional: `content` (string), `metadata` (object), `name` (string), `sent_at` (date-time), `tool_call_id` (string), `tool_calls` (array[object]), `tool_choice` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "string"
}' \
  "https://api.telnyx.com/v2/ai/conversations/{conversation_id}/message"
```

## Get conversation messages

Retrieve messages for a specific conversation, including tool calls made by the assistant.

`GET /ai/conversations/{conversation_id}/messages`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/conversations/{conversation_id}/messages"
```

## Get Tasks by Status

Retrieve tasks for the user that are either `queued`, `processing`, `failed`, `success` or `partial_success` based on the query string.

`GET /ai/embeddings`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/embeddings"
```

## Embed documents

Perform embedding on a Telnyx Storage Bucket using an embedding model.

`POST /ai/embeddings` — Required: `bucket_name`

Optional: `document_chunk_overlap_size` (integer), `document_chunk_size` (integer), `embedding_model` (object), `loader` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "bucket_name": "string"
}' \
  "https://api.telnyx.com/v2/ai/embeddings"
```

## List embedded buckets

Get all embedding buckets for a user.

`GET /ai/embeddings/buckets`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/embeddings/buckets"
```

## Get file-level embedding statuses for a bucket

Get all embedded files for a given user bucket, including their processing status.

`GET /ai/embeddings/buckets/{bucket_name}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/embeddings/buckets/{bucket_name}"
```

## Disable AI for an Embedded Bucket

Deletes an entire bucket's embeddings and disables the bucket for AI-use, returning it to normal storage pricing.

`DELETE /ai/embeddings/buckets/{bucket_name}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/embeddings/buckets/{bucket_name}"
```

## Search for documents

Perform a similarity search on a Telnyx Storage Bucket, returning the most similar `num_docs` document chunks to the query.

`POST /ai/embeddings/similarity-search` — Required: `bucket_name`, `query`

Optional: `num_of_docs` (integer)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "bucket_name": "string",
  "query": "string"
}' \
  "https://api.telnyx.com/v2/ai/embeddings/similarity-search"
```

## Embed URL content

Embed website content from a specified URL, including child pages up to 5 levels deep within the same domain.

`POST /ai/embeddings/url` — Required: `url`, `bucket_name`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "url": "string",
  "bucket_name": "string"
}' \
  "https://api.telnyx.com/v2/ai/embeddings/url"
```

## Get an embedding task's status

Check the status of a current embedding task.

`GET /ai/embeddings/{task_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/embeddings/{task_id}"
```

## List fine tuning jobs

Retrieve a list of all fine tuning jobs created by the user.

`GET /ai/fine_tuning/jobs`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/fine_tuning/jobs"
```

## Create a fine tuning job

Create a new fine tuning job.

`POST /ai/fine_tuning/jobs` — Required: `model`, `training_file`

Optional: `hyperparameters` (object), `suffix` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "string",
  "training_file": "string"
}' \
  "https://api.telnyx.com/v2/ai/fine_tuning/jobs"
```

## Get a fine tuning job

Retrieve a fine tuning job by `job_id`.

`GET /ai/fine_tuning/jobs/{job_id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/fine_tuning/jobs/{job_id}"
```

## Cancel a fine tuning job

Cancel a fine tuning job.

`POST /ai/fine_tuning/jobs/{job_id}/cancel`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/ai/fine_tuning/jobs/{job_id}/cancel"
```

## Get available models

This endpoint returns a list of Open Source and OpenAI models that are available for use.

`GET /ai/models`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/models"
```

## Create embeddings

Creates an embedding vector representing the input text.

`POST /ai/openai/embeddings` — Required: `input`, `model`

Optional: `dimensions` (integer), `encoding_format` (enum), `user` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "input": "The quick brown fox jumps over the lazy dog",
  "model": "thenlper/gte-large"
}' \
  "https://api.telnyx.com/v2/ai/openai/embeddings"
```

## List embedding models

Returns a list of available embedding models.

`GET /ai/openai/embeddings/models`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/ai/openai/embeddings/models"
```

## Summarize file content

Generate a summary of a file's contents.

`POST /ai/summarize` — Required: `bucket`, `filename`

Optional: `system_prompt` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "bucket": "string",
  "filename": "string"
}' \
  "https://api.telnyx.com/v2/ai/summarize"
```

## Get all Speech to Text batch report requests

Retrieves all Speech to Text batch report requests for the authenticated user

`GET /legacy/reporting/batch_detail_records/speech_to_text`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/speech_to_text"
```

## Create a new Speech to Text batch report request

Creates a new Speech to Text batch report request with the specified filters

`POST /legacy/reporting/batch_detail_records/speech_to_text` — Required: `start_date`, `end_date`

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "start_date": "2020-07-01T00:00:00-06:00",
  "end_date": "2020-07-01T00:00:00-06:00"
}' \
  "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/speech_to_text"
```

## Get a specific Speech to Text batch report request

Retrieves a specific Speech to Text batch report request by ID

`GET /legacy/reporting/batch_detail_records/speech_to_text/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/speech_to_text/{id}"
```

## Delete a Speech to Text batch report request

Deletes a specific Speech to Text batch report request by ID

`DELETE /legacy/reporting/batch_detail_records/speech_to_text/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/legacy/reporting/batch_detail_records/speech_to_text/{id}"
```

## Get speech to text usage report

Generate and fetch speech to text usage report synchronously.

`GET /legacy/reporting/usage_reports/speech_to_text`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/legacy/reporting/usage_reports/speech_to_text?start_date=2020-07-01T00:00:00-06:00&end_date=2020-07-01T00:00:00-06:00"
```

## Speech to text over websocket

Transcribe audio streams to text over WebSocket.

`GET /speech-to-text/transcription`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Telnyx&input_format=mp3&language=en-US&interim_results=True"
```

## Stream text to speech over WebSocket

Open a WebSocket connection to stream text and receive synthesized audio in real time.

`GET /text-to-speech/speech`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/text-to-speech/speech"
```

## Generate speech from text

Generate synthesized speech audio from text input.

`POST /text-to-speech/speech`

Optional: `aws` (object), `azure` (object), `disable_cache` (boolean), `elevenlabs` (object), `language` (string), `minimax` (object), `output_type` (enum), `provider` (enum), `resemble` (object), `rime` (object), `telnyx` (object), `text` (string), `text_type` (enum), `voice` (string), `voice_settings` (object)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.telnyx.com/v2/text-to-speech/speech"
```

## List available voices

Retrieve a list of available voices from one or all TTS providers.

`GET /text-to-speech/voices`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/text-to-speech/voices"
```

## Get all Wireless Detail Records (WDRs) Reports

Returns the WDR Reports that match the given parameters.

`GET /wireless/detail_records_reports`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireless/detail_records_reports"
```

## Create a Wireless Detail Records (WDRs) Report

Asynchronously create a report containing Wireless Detail Records (WDRs) for the SIM cards that consumed wireless data in the given time period.

`POST /wireless/detail_records_reports`

Optional: `end_time` (string), `start_time` (string)

```bash
curl \
  -X POST \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "start_time": "2018-02-02T22:25:27.521Z",
  "end_time": "2018-02-02T22:25:27.521Z"
}' \
  "https://api.telnyx.com/v2/wireless/detail_records_reports"
```

## Get a Wireless Detail Record (WDR) Report

Returns one specific WDR report

`GET /wireless/detail_records_reports/{id}`

```bash
curl -H "Authorization: Bearer $TELNYX_API_KEY" "https://api.telnyx.com/v2/wireless/detail_records_reports/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```

## Delete a Wireless Detail Record (WDR) Report

Deletes one specific WDR report.

`DELETE /wireless/detail_records_reports/{id}`

```bash
curl \
  -X DELETE \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/wireless/detail_records_reports/6a09cdc3-8948-47f0-aa62-74ac943d6c58"
```
