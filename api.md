# Datastores

Types:

```python
from contextual.types import (
    CreateDatastoreResponse,
    Datastore,
    DatastoreMetadata,
    ListDatastoresResponse,
    DatastoreDeleteResponse,
)
```

Methods:

- <code title="post /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">create</a>(\*\*<a href="src/contextual/types/datastore_create_params.py">params</a>) -> <a href="./src/contextual/types/create_datastore_response.py">CreateDatastoreResponse</a></code>
- <code title="get /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">list</a>(\*\*<a href="src/contextual/types/datastore_list_params.py">params</a>) -> <a href="./src/contextual/types/datastore.py">SyncDatastoresPage[Datastore]</a></code>
- <code title="delete /datastores/{datastore_id}">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">delete</a>(datastore_id) -> <a href="./src/contextual/types/datastore_delete_response.py">object</a></code>
- <code title="get /datastores/{datastore_id}/metadata">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">metadata</a>(datastore_id) -> <a href="./src/contextual/types/datastore_metadata.py">DatastoreMetadata</a></code>

## Documents

Types:

```python
from contextual.types.datastores import (
    DocumentMetadata,
    IngestionResponse,
    ListDocumentsResponse,
    DocumentDeleteResponse,
)
```

Methods:

- <code title="get /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">list</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_list_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_metadata.py">SyncDocumentsPage[DocumentMetadata]</a></code>
- <code title="delete /datastores/{datastore_id}/documents/{document_id}">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">delete</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_delete_response.py">object</a></code>
- <code title="post /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">ingest</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_ingest_params.py">params</a>) -> <a href="./src/contextual/types/datastores/ingestion_response.py">IngestionResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">metadata</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_metadata.py">DocumentMetadata</a></code>

# Agents

Types:

```python
from contextual.types import (
    Agent,
    AgentMetadata,
    CreateAgentOutput,
    ListAgentsResponse,
    AgentUpdateResponse,
    AgentDeleteResponse,
)
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">create</a>(\*\*<a href="src/contextual/types/agent_create_params.py">params</a>) -> <a href="./src/contextual/types/create_agent_output.py">CreateAgentOutput</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/contextual/types/agent_update_params.py">params</a>) -> <a href="./src/contextual/types/agent_update_response.py">object</a></code>
- <code title="get /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">list</a>(\*\*<a href="src/contextual/types/agent_list_params.py">params</a>) -> <a href="./src/contextual/types/agent.py">SyncPage[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/contextual/types/agent_delete_response.py">object</a></code>
- <code title="get /agents/{agent_id}/metadata">client.agents.<a href="./src/contextual/resources/agents/agents.py">metadata</a>(agent_id) -> <a href="./src/contextual/types/agent_metadata.py">AgentMetadata</a></code>

## Query

Types:

```python
from contextual.types.agents import (
    QueryResponse,
    RetrievalInfoResponse,
    QueryFeedbackResponse,
    QueryMetricsResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}/query">client.agents.query.<a href="./src/contextual/resources/agents/query.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_response.py">QueryResponse</a></code>
- <code title="post /agents/{agent_id}/feedback">client.agents.query.<a href="./src/contextual/resources/agents/query.py">feedback</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_feedback_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_feedback_response.py">object</a></code>
- <code title="get /agents/{agent_id}/metrics">client.agents.query.<a href="./src/contextual/resources/agents/query.py">metrics</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_metrics_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_metrics_response.py">QueryMetricsResponse</a></code>
- <code title="get /agents/{agent_id}/query/{message_id}/retrieval/info">client.agents.query.<a href="./src/contextual/resources/agents/query.py">retrieval_info</a>(message_id, \*, agent_id, \*\*<a href="src/contextual/types/agents/query_retrieval_info_params.py">params</a>) -> <a href="./src/contextual/types/agents/retrieval_info_response.py">RetrievalInfoResponse</a></code>

## Evaluate

Types:

```python
from contextual.types.agents import CreateEvaluationResponse
```

Methods:

- <code title="post /agents/{agent_id}/evaluate">client.agents.evaluate.<a href="./src/contextual/resources/agents/evaluate/evaluate.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/evaluate_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/create_evaluation_response.py">CreateEvaluationResponse</a></code>

### Jobs

Types:

```python
from contextual.types.agents.evaluate import (
    EvaluationJobMetadata,
    ListEvaluationJobsResponse,
    JobCancelResponse,
)
```

Methods:

- <code title="get /agents/{agent_id}/evaluate/jobs">client.agents.evaluate.jobs.<a href="./src/contextual/resources/agents/evaluate/jobs.py">list</a>(agent_id) -> <a href="./src/contextual/types/agents/evaluate/list_evaluation_jobs_response.py">ListEvaluationJobsResponse</a></code>
- <code title="post /agents/{agent_id}/evaluate/jobs/{job_id}/cancel">client.agents.evaluate.jobs.<a href="./src/contextual/resources/agents/evaluate/jobs.py">cancel</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/evaluate/job_cancel_response.py">object</a></code>
- <code title="get /agents/{agent_id}/evaluate/jobs/{job_id}/metadata">client.agents.evaluate.jobs.<a href="./src/contextual/resources/agents/evaluate/jobs.py">metadata</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/evaluate/evaluation_job_metadata.py">EvaluationJobMetadata</a></code>

## Datasets

Types:

```python
from contextual.types.agents import CreateDatasetResponse, DatasetMetadata, ListDatasetsResponse
```

### Evaluate

Types:

```python
from contextual.types.agents.datasets import EvaluateDeleteResponse
```

Methods:

- <code title="post /agents/{agent_id}/datasets/evaluate">client.agents.datasets.evaluate.<a href="./src/contextual/resources/agents/datasets/evaluate.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/datasets/evaluate_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /agents/{agent_id}/datasets/evaluate/{dataset_name}">client.agents.datasets.evaluate.<a href="./src/contextual/resources/agents/datasets/evaluate.py">retrieve</a>(dataset_name, \*, agent_id, \*\*<a href="src/contextual/types/agents/datasets/evaluate_retrieve_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /agents/{agent_id}/datasets/evaluate/{dataset_name}">client.agents.datasets.evaluate.<a href="./src/contextual/resources/agents/datasets/evaluate.py">update</a>(dataset_name, \*, agent_id, \*\*<a href="src/contextual/types/agents/datasets/evaluate_update_params.py">params</a>) -> <a href="./src/contextual/types/agents/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /agents/{agent_id}/datasets/evaluate">client.agents.datasets.evaluate.<a href="./src/contextual/resources/agents/datasets/evaluate.py">list</a>(agent_id, \*\*<a href="src/contextual/types/agents/datasets/evaluate_list_params.py">params</a>) -> <a href="./src/contextual/types/agents/list_datasets_response.py">ListDatasetsResponse</a></code>
- <code title="delete /agents/{agent_id}/datasets/evaluate/{dataset_name}">client.agents.datasets.evaluate.<a href="./src/contextual/resources/agents/datasets/evaluate.py">delete</a>(dataset_name, \*, agent_id) -> <a href="./src/contextual/types/agents/datasets/evaluate_delete_response.py">object</a></code>
- <code title="get /agents/{agent_id}/datasets/evaluate/{dataset_name}/metadata">client.agents.datasets.evaluate.<a href="./src/contextual/resources/agents/datasets/evaluate.py">metadata</a>(dataset_name, \*, agent_id, \*\*<a href="src/contextual/types/agents/datasets/evaluate_metadata_params.py">params</a>) -> <a href="./src/contextual/types/agents/dataset_metadata.py">DatasetMetadata</a></code>

## Tune

Types:

```python
from contextual.types.agents import CreateTuneResponse
```

Methods:

- <code title="post /agents/{agent_id}/tune">client.agents.tune.<a href="./src/contextual/resources/agents/tune/tune.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/tune_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/create_tune_response.py">CreateTuneResponse</a></code>

### Jobs

Types:

```python
from contextual.types.agents.tune import ListTuneJobsResponse, TuneJobMetadata, JobDeleteResponse
```

Methods:

- <code title="get /agents/{agent_id}/tune/jobs">client.agents.tune.jobs.<a href="./src/contextual/resources/agents/tune/jobs.py">list</a>(agent_id) -> <a href="./src/contextual/types/agents/tune/list_tune_jobs_response.py">ListTuneJobsResponse</a></code>
- <code title="delete /agents/{agent_id}/tune/jobs/{job_id}">client.agents.tune.jobs.<a href="./src/contextual/resources/agents/tune/jobs.py">delete</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/tune/job_delete_response.py">object</a></code>
- <code title="get /agents/{agent_id}/tune/jobs/{job_id}/metadata">client.agents.tune.jobs.<a href="./src/contextual/resources/agents/tune/jobs.py">metadata</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/tune/tune_job_metadata.py">TuneJobMetadata</a></code>

### Models

Types:

```python
from contextual.types.agents.tune import ListTuneModelsResponse
```

Methods:

- <code title="get /agents/{agent_id}/tune/models">client.agents.tune.models.<a href="./src/contextual/resources/agents/tune/models.py">list</a>(agent_id) -> <a href="./src/contextual/types/agents/tune/list_tune_models_response.py">ListTuneModelsResponse</a></code>

# LMUnit

Types:

```python
from contextual.types import LMUnitCreateResponse
```

Methods:

- <code title="post /lmunit">client.lmunit.<a href="./src/contextual/resources/lmunit.py">create</a>(\*\*<a href="src/contextual/types/lmunit_create_params.py">params</a>) -> <a href="./src/contextual/types/lmunit_create_response.py">LMUnitCreateResponse</a></code>
