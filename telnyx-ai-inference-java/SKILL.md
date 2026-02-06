---
name: telnyx-ai-inference-java
description: >-
  Access Telnyx LLM inference APIs, embeddings, and AI analytics for call
  insights and summaries. This skill provides Java SDK examples.
metadata:
  author: telnyx
  product: ai-inference
  language: java
---

# Telnyx Ai Inference - Java

## Installation

```bash
// Add to pom.xml or build.gradle - see https://github.com/team-telnyx/telnyx-java
```

## Setup

```java
import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;

TelnyxClient client = TelnyxOkHttpClient.fromEnv();
```

All examples below assume `client` is already initialized as shown above.

## List conversations

Retrieve a list of all AI conversations configured by the user.

`GET /ai/conversations`

```java
import com.telnyx.sdk.models.ai.conversations.ConversationListParams;
import com.telnyx.sdk.models.ai.conversations.ConversationListResponse;

ConversationListResponse conversations = client.ai().conversations().list();
```

## Create a conversation

Create a new AI Conversation.

`POST /ai/conversations`

```java
import com.telnyx.sdk.models.ai.conversations.Conversation;
import com.telnyx.sdk.models.ai.conversations.ConversationCreateParams;

Conversation conversation = client.ai().conversations().create();
```

## Get Insight Template Groups

Get all insight groups

`GET /ai/conversations/insight-groups`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightGroupRetrieveInsightGroupsPage;
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightGroupRetrieveInsightGroupsParams;

InsightGroupRetrieveInsightGroupsPage page = client.ai().conversations().insightGroups().retrieveInsightGroups();
```

## Create Insight Template Group

Create a new insight group

`POST /ai/conversations/insight-groups` — Required: `name`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightGroupInsightGroupsParams;
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightTemplateGroupDetail;

InsightGroupInsightGroupsParams params = InsightGroupInsightGroupsParams.builder()
    .name("name")
    .build();
InsightTemplateGroupDetail insightTemplateGroupDetail = client.ai().conversations().insightGroups().insightGroups(params);
```

## Get Insight Template Group

Get insight group by ID

`GET /ai/conversations/insight-groups/{group_id}`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightGroupRetrieveParams;
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightTemplateGroupDetail;

InsightTemplateGroupDetail insightTemplateGroupDetail = client.ai().conversations().insightGroups().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Update Insight Template Group

Update an insight template group

`PUT /ai/conversations/insight-groups/{group_id}`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightGroupUpdateParams;
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightTemplateGroupDetail;

InsightTemplateGroupDetail insightTemplateGroupDetail = client.ai().conversations().insightGroups().update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Delete Insight Template Group

Delete insight group by ID

`DELETE /ai/conversations/insight-groups/{group_id}`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.InsightGroupDeleteParams;

client.ai().conversations().insightGroups().delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Assign Insight Template To Group

Assign an insight to a group

`POST /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.insights.InsightAssignParams;

InsightAssignParams params = InsightAssignParams.builder()
    .groupId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .insightId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .build();
client.ai().conversations().insightGroups().insights().assign(params);
```

## Unassign Insight Template From Group

Remove an insight from a group

`DELETE /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign`

```java
import com.telnyx.sdk.models.ai.conversations.insightgroups.insights.InsightDeleteUnassignParams;

InsightDeleteUnassignParams params = InsightDeleteUnassignParams.builder()
    .groupId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .insightId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .build();
client.ai().conversations().insightGroups().insights().deleteUnassign(params);
```

## Get Insight Templates

Get all insights

`GET /ai/conversations/insights`

```java
import com.telnyx.sdk.models.ai.conversations.insights.InsightListPage;
import com.telnyx.sdk.models.ai.conversations.insights.InsightListParams;

InsightListPage page = client.ai().conversations().insights().list();
```

## Create Insight Template

Create a new insight

`POST /ai/conversations/insights` — Required: `instructions`, `name`

```java
import com.telnyx.sdk.models.ai.conversations.insights.InsightCreateParams;
import com.telnyx.sdk.models.ai.conversations.insights.InsightTemplateDetail;

InsightCreateParams params = InsightCreateParams.builder()
    .instructions("instructions")
    .name("name")
    .build();
InsightTemplateDetail insightTemplateDetail = client.ai().conversations().insights().create(params);
```

## Get Insight Template

Get insight by ID

`GET /ai/conversations/insights/{insight_id}`

```java
import com.telnyx.sdk.models.ai.conversations.insights.InsightRetrieveParams;
import com.telnyx.sdk.models.ai.conversations.insights.InsightTemplateDetail;

InsightTemplateDetail insightTemplateDetail = client.ai().conversations().insights().retrieve("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Update Insight Template

Update an insight template

`PUT /ai/conversations/insights/{insight_id}`

```java
import com.telnyx.sdk.models.ai.conversations.insights.InsightTemplateDetail;
import com.telnyx.sdk.models.ai.conversations.insights.InsightUpdateParams;

InsightTemplateDetail insightTemplateDetail = client.ai().conversations().insights().update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Delete Insight Template

Delete insight by ID

`DELETE /ai/conversations/insights/{insight_id}`

```java
import com.telnyx.sdk.models.ai.conversations.insights.InsightDeleteParams;

client.ai().conversations().insights().delete("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e");
```

## Get a conversation

Retrieve a specific AI conversation by its ID.

`GET /ai/conversations/{conversation_id}`

```java
import com.telnyx.sdk.models.ai.conversations.ConversationRetrieveParams;
import com.telnyx.sdk.models.ai.conversations.ConversationRetrieveResponse;

ConversationRetrieveResponse conversation = client.ai().conversations().retrieve("conversation_id");
```

## Update conversation metadata

Update metadata for a specific conversation.

`PUT /ai/conversations/{conversation_id}`

```java
import com.telnyx.sdk.models.ai.conversations.ConversationUpdateParams;
import com.telnyx.sdk.models.ai.conversations.ConversationUpdateResponse;

ConversationUpdateResponse conversation = client.ai().conversations().update("conversation_id");
```

## Delete a conversation

Delete a specific conversation by its ID.

`DELETE /ai/conversations/{conversation_id}`

```java
import com.telnyx.sdk.models.ai.conversations.ConversationDeleteParams;

client.ai().conversations().delete("conversation_id");
```

## Get insights for a conversation

Retrieve insights for a specific conversation

`GET /ai/conversations/{conversation_id}/conversations-insights`

```java
import com.telnyx.sdk.models.ai.conversations.ConversationRetrieveConversationsInsightsParams;
import com.telnyx.sdk.models.ai.conversations.ConversationRetrieveConversationsInsightsResponse;

ConversationRetrieveConversationsInsightsResponse response = client.ai().conversations().retrieveConversationsInsights("conversation_id");
```

## Create Message

Add a new message to the conversation.

`POST /ai/conversations/{conversation_id}/message` — Required: `role`

```java
import com.telnyx.sdk.models.ai.conversations.ConversationAddMessageParams;

ConversationAddMessageParams params = ConversationAddMessageParams.builder()
    .conversationId("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
    .role("role")
    .build();
client.ai().conversations().addMessage(params);
```

## Get conversation messages

Retrieve messages for a specific conversation, including tool calls made by the assistant.

`GET /ai/conversations/{conversation_id}/messages`

```java
import com.telnyx.sdk.models.ai.conversations.messages.MessageListParams;
import com.telnyx.sdk.models.ai.conversations.messages.MessageListResponse;

MessageListResponse messages = client.ai().conversations().messages().list("conversation_id");
```

## Get Tasks by Status

Retrieve tasks for the user that are either `queued`, `processing`, `failed`, `success` or `partial_success` based on the query string.

`GET /ai/embeddings`

```java
import com.telnyx.sdk.models.ai.embeddings.EmbeddingListParams;
import com.telnyx.sdk.models.ai.embeddings.EmbeddingListResponse;

EmbeddingListResponse embeddings = client.ai().embeddings().list();
```

## Embed documents

Perform embedding on a Telnyx Storage Bucket using the a embedding model.

`POST /ai/embeddings` — Required: `bucket_name`

```java
import com.telnyx.sdk.models.ai.embeddings.EmbeddingCreateParams;
import com.telnyx.sdk.models.ai.embeddings.EmbeddingResponse;

EmbeddingCreateParams params = EmbeddingCreateParams.builder()
    .bucketName("bucket_name")
    .build();
EmbeddingResponse embeddingResponse = client.ai().embeddings().create(params);
```

## List embedded buckets

Get all embedding buckets for a user.

`GET /ai/embeddings/buckets`

```java
import com.telnyx.sdk.models.ai.embeddings.buckets.BucketListParams;
import com.telnyx.sdk.models.ai.embeddings.buckets.BucketListResponse;

BucketListResponse buckets = client.ai().embeddings().buckets().list();
```

## Get file-level embedding statuses for a bucket

Get all embedded files for a given user bucket, including their processing status.

`GET /ai/embeddings/buckets/{bucket_name}`

```java
import com.telnyx.sdk.models.ai.embeddings.buckets.BucketRetrieveParams;
import com.telnyx.sdk.models.ai.embeddings.buckets.BucketRetrieveResponse;

BucketRetrieveResponse bucket = client.ai().embeddings().buckets().retrieve("bucket_name");
```

## Disable AI for an Embedded Bucket

Deletes an entire bucket's embeddings and disables the bucket for AI-use, returning it to normal storage pricing.

`DELETE /ai/embeddings/buckets/{bucket_name}`

```java
import com.telnyx.sdk.models.ai.embeddings.buckets.BucketDeleteParams;

client.ai().embeddings().buckets().delete("bucket_name");
```

## Search for documents

Perform a similarity search on a Telnyx Storage Bucket, returning the most similar `num_docs` document chunks to the query.

`POST /ai/embeddings/similarity-search` — Required: `bucket_name`, `query`

```java
import com.telnyx.sdk.models.ai.embeddings.EmbeddingSimilaritySearchParams;
import com.telnyx.sdk.models.ai.embeddings.EmbeddingSimilaritySearchResponse;

EmbeddingSimilaritySearchParams params = EmbeddingSimilaritySearchParams.builder()
    .bucketName("bucket_name")
    .query("query")
    .build();
EmbeddingSimilaritySearchResponse response = client.ai().embeddings().similaritySearch(params);
```

## Embed URL content

Embed website content from a specified URL, including child pages up to 5 levels deep within the same domain.

`POST /ai/embeddings/url` — Required: `url`, `bucket_name`

```java
import com.telnyx.sdk.models.ai.embeddings.EmbeddingResponse;
import com.telnyx.sdk.models.ai.embeddings.EmbeddingUrlParams;

EmbeddingUrlParams params = EmbeddingUrlParams.builder()
    .bucketName("bucket_name")
    .url("url")
    .build();
EmbeddingResponse embeddingResponse = client.ai().embeddings().url(params);
```

## Get an embedding task's status

Check the status of a current embedding task.

`GET /ai/embeddings/{task_id}`

```java
import com.telnyx.sdk.models.ai.embeddings.EmbeddingRetrieveParams;
import com.telnyx.sdk.models.ai.embeddings.EmbeddingRetrieveResponse;

EmbeddingRetrieveResponse embedding = client.ai().embeddings().retrieve("task_id");
```

## List all clusters

`GET /ai/clusters`

```java
import com.telnyx.sdk.models.ai.clusters.ClusterListPage;
import com.telnyx.sdk.models.ai.clusters.ClusterListParams;

ClusterListPage page = client.ai().clusters().list();
```

## Compute new clusters

Starts a background task to compute how the data in an [embedded storage bucket](https://developers.telnyx.com/api-reference/embeddings/embed-documents) is clustered.

`POST /ai/clusters` — Required: `bucket`

```java
import com.telnyx.sdk.models.ai.clusters.ClusterComputeParams;
import com.telnyx.sdk.models.ai.clusters.ClusterComputeResponse;

ClusterComputeParams params = ClusterComputeParams.builder()
    .bucket("bucket")
    .build();
ClusterComputeResponse response = client.ai().clusters().compute(params);
```

## Fetch a cluster

`GET /ai/clusters/{task_id}`

```java
import com.telnyx.sdk.models.ai.clusters.ClusterRetrieveParams;
import com.telnyx.sdk.models.ai.clusters.ClusterRetrieveResponse;

ClusterRetrieveResponse cluster = client.ai().clusters().retrieve("task_id");
```

## Delete a cluster

`DELETE /ai/clusters/{task_id}`

```java
import com.telnyx.sdk.models.ai.clusters.ClusterDeleteParams;

client.ai().clusters().delete("task_id");
```

## Fetch a cluster visualization

`GET /ai/clusters/{task_id}/graph`

```java
import com.telnyx.sdk.core.http.HttpResponse;
import com.telnyx.sdk.models.ai.clusters.ClusterFetchGraphParams;

HttpResponse response = client.ai().clusters().fetchGraph("task_id");
```

## Transcribe speech to text

Transcribe speech to text.

`POST /ai/audio/transcriptions`

```java
import com.telnyx.sdk.models.ai.audio.AudioTranscribeParams;
import com.telnyx.sdk.models.ai.audio.AudioTranscribeResponse;

AudioTranscribeParams params = AudioTranscribeParams.builder()
    .model(AudioTranscribeParams.Model.DISTIL_WHISPER_DISTIL_LARGE_V2)
    .build();
AudioTranscribeResponse response = client.ai().audio().transcribe(params);
```

## Create a chat completion

Chat with a language model.

`POST /ai/chat/completions` — Required: `messages`

```java
import com.telnyx.sdk.models.ai.chat.ChatCreateCompletionParams;
import com.telnyx.sdk.models.ai.chat.ChatCreateCompletionResponse;

ChatCreateCompletionParams params = ChatCreateCompletionParams.builder()
    .addMessage(ChatCreateCompletionParams.Message.builder()
        .content("You are a friendly chatbot.")
        .role(ChatCreateCompletionParams.Message.Role.SYSTEM)
        .build())
    .addMessage(ChatCreateCompletionParams.Message.builder()
        .content("Hello, world!")
        .role(ChatCreateCompletionParams.Message.Role.USER)
        .build())
    .build();
ChatCreateCompletionResponse response = client.ai().chat().createCompletion(params);
```

## List fine tuning jobs

Retrieve a list of all fine tuning jobs created by the user.

`GET /ai/fine_tuning/jobs`

```java
import com.telnyx.sdk.models.ai.finetuning.jobs.JobListParams;
import com.telnyx.sdk.models.ai.finetuning.jobs.JobListResponse;

JobListResponse jobs = client.ai().fineTuning().jobs().list();
```

## Create a fine tuning job

Create a new fine tuning job.

`POST /ai/fine_tuning/jobs` — Required: `model`, `training_file`

```java
import com.telnyx.sdk.models.ai.finetuning.jobs.FineTuningJob;
import com.telnyx.sdk.models.ai.finetuning.jobs.JobCreateParams;

JobCreateParams params = JobCreateParams.builder()
    .model("model")
    .trainingFile("training_file")
    .build();
FineTuningJob fineTuningJob = client.ai().fineTuning().jobs().create(params);
```

## Get a fine tuning job

Retrieve a fine tuning job by `job_id`.

`GET /ai/fine_tuning/jobs/{job_id}`

```java
import com.telnyx.sdk.models.ai.finetuning.jobs.FineTuningJob;
import com.telnyx.sdk.models.ai.finetuning.jobs.JobRetrieveParams;

FineTuningJob fineTuningJob = client.ai().fineTuning().jobs().retrieve("job_id");
```

## Cancel a fine tuning job

Cancel a fine tuning job.

`POST /ai/fine_tuning/jobs/{job_id}/cancel`

```java
import com.telnyx.sdk.models.ai.finetuning.jobs.FineTuningJob;
import com.telnyx.sdk.models.ai.finetuning.jobs.JobCancelParams;

FineTuningJob fineTuningJob = client.ai().fineTuning().jobs().cancel("job_id");
```

## Get available models

This endpoint returns a list of Open Source and OpenAI models that are available for use.

`GET /ai/models`

```java
import com.telnyx.sdk.models.ai.AiRetrieveModelsParams;
import com.telnyx.sdk.models.ai.AiRetrieveModelsResponse;

AiRetrieveModelsResponse response = client.ai().retrieveModels();
```

## Summarize file content

Generate a summary of a file's contents.

`POST /ai/summarize` — Required: `bucket`, `filename`

```java
import com.telnyx.sdk.models.ai.AiSummarizeParams;
import com.telnyx.sdk.models.ai.AiSummarizeResponse;

AiSummarizeParams params = AiSummarizeParams.builder()
    .bucket("bucket")
    .filename("filename")
    .build();
AiSummarizeResponse response = client.ai().summarize(params);
```
