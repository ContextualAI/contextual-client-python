# ContextualAI

Types:

```python
from contextual.types import LMUnitResponse
```

Methods:

- <code title="post /lmunit">client.<a href="./src/contextual/_client.py">lmunit</a>(\*\*<a href="src/contextual/types/client_lmunit_params.py">params</a>) -> <a href="./src/contextual/types/lmunit_response.py">LMUnitResponse</a></code>

# Datastores

Types:

```python
from contextual.types import (
    CreateDatastoreResponse,
    Datastore,
    DatastoresResponse,
    DatastoreDeleteResponse,
)
```

Methods:

- <code title="post /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">create</a>(\*\*<a href="src/contextual/types/datastore_create_params.py">params</a>) -> <a href="./src/contextual/types/create_datastore_response.py">CreateDatastoreResponse</a></code>
- <code title="get /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">list</a>(\*\*<a href="src/contextual/types/datastore_list_params.py">params</a>) -> <a href="./src/contextual/types/datastore.py">SyncDatastoresPage[Datastore]</a></code>
- <code title="delete /datastores/{datastore_id}">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">delete</a>(datastore_id) -> <a href="./src/contextual/types/datastore_delete_response.py">object</a></code>

## Metadata

Types:

```python
from contextual.types.datastores import GetDatastoreResponse
```

Methods:

- <code title="get /datastores/{datastore_id}/metadata">client.datastores.metadata.<a href="./src/contextual/resources/datastores/metadata.py">retrieve</a>(datastore_id) -> <a href="./src/contextual/types/datastores/get_datastore_response.py">GetDatastoreResponse</a></code>

## Documents

Types:

```python
from contextual.types.datastores import (
    DocumentDescription,
    GetDocumentsResponse,
    IngestionResponse,
    DocumentDeleteResponse,
)
```

Methods:

- <code title="post /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">create</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_create_params.py">params</a>) -> <a href="./src/contextual/types/datastores/ingestion_response.py">IngestionResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">retrieve</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_description.py">DocumentDescription</a></code>
- <code title="get /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">list</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_list_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_description.py">SyncDocumentsPage[DocumentDescription]</a></code>
- <code title="delete /datastores/{datastore_id}/documents/{document_id}">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">delete</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_delete_response.py">object</a></code>

# Agents

Types:

```python
from contextual.types import (
    Agent,
    AgentsResponse,
    CreateAgentOutput,
    AgentUpdateResponse,
    AgentDeleteResponse,
)
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">create</a>(\*\*<a href="src/contextual/types/agent_create_params.py">params</a>) -> <a href="./src/contextual/types/create_agent_output.py">CreateAgentOutput</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/contextual/types/agent_update_params.py">params</a>) -> <a href="./src/contextual/types/agent_update_response.py">object</a></code>
- <code title="get /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">list</a>(\*\*<a href="src/contextual/types/agent_list_params.py">params</a>) -> <a href="./src/contextual/types/agent.py">SyncPage[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/contextual/types/agent_delete_response.py">object</a></code>

## Metadata

Types:

```python
from contextual.types.agents import GetAgentResponse
```

Methods:

- <code title="get /agents/{agent_id}/metadata">client.agents.metadata.<a href="./src/contextual/resources/agents/metadata.py">retrieve</a>(agent_id) -> <a href="./src/contextual/types/agents/get_agent_response.py">GetAgentResponse</a></code>

## Query

Types:

```python
from contextual.types.agents import QueryResponse, QueryFeedbackResponse, QueryMetricsResponse
```

Methods:

- <code title="post /agents/{agent_id}/feedback">client.agents.query.<a href="./src/contextual/resources/agents/query.py">feedback</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_feedback_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_feedback_response.py">object</a></code>
- <code title="get /agents/{agent_id}/metrics">client.agents.query.<a href="./src/contextual/resources/agents/query.py">metrics</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_metrics_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_metrics_response.py">QueryMetricsResponse</a></code>
- <code title="post /agents/{agent_id}/query">client.agents.query.<a href="./src/contextual/resources/agents/query.py">start</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_start_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_response.py">QueryResponse</a></code>

## Evaluate

Types:

```python
from contextual.types.agents import LaunchEvaluationResponse
```

Methods:

- <code title="post /agents/{agent_id}/evaluate">client.agents.evaluate.<a href="./src/contextual/resources/agents/evaluate/evaluate.py">launch</a>(agent_id, \*\*<a href="src/contextual/types/agents/evaluate_launch_params.py">params</a>) -> <a href="./src/contextual/types/agents/launch_evaluation_response.py">LaunchEvaluationResponse</a></code>

### Jobs

Types:

```python
from contextual.types.agents.evaluate import (
    EvaluationRoundResponse,
    ListEvaluationResponse,
    JobCancelResponse,
)
```

Methods:

- <code title="get /agents/{agent_id}/evaluate/jobs">client.agents.evaluate.jobs.<a href="./src/contextual/resources/agents/evaluate/jobs/jobs.py">list</a>(agent_id) -> <a href="./src/contextual/types/agents/evaluate/list_evaluation_response.py">ListEvaluationResponse</a></code>
- <code title="post /agents/{agent_id}/evaluate/jobs/{job_id}/cancel">client.agents.evaluate.jobs.<a href="./src/contextual/resources/agents/evaluate/jobs/jobs.py">cancel</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/evaluate/job_cancel_response.py">object</a></code>

#### Metadata

Methods:

- <code title="get /agents/{agent_id}/evaluate/jobs/{job_id}/metadata">client.agents.evaluate.jobs.metadata.<a href="./src/contextual/resources/agents/evaluate/jobs/metadata.py">retrieve</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/evaluate/evaluation_round_response.py">EvaluationRoundResponse</a></code>

## Datasets

Types:

```python
from contextual.types.agents import (
    CreateDatasetResponse,
    DatasetsResponse,
    GetDatasetResponse,
    DatasetRetrieveResponse,
    DatasetDeleteResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}/datasets">client.agents.datasets.<a href="./src/contextual/resources/agents/datasets/datasets.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/dataset_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /agents/{agent_id}/datasets/{dataset_name}">client.agents.datasets.<a href="./src/contextual/resources/agents/datasets/datasets.py">retrieve</a>(dataset_name, \*, agent_id, \*\*<a href="src/contextual/types/agents/dataset_retrieve_params.py">params</a>) -> <a href="./src/contextual/types/agents/dataset_retrieve_response.py">object</a></code>
- <code title="put /agents/{agent_id}/datasets/{dataset_name}">client.agents.datasets.<a href="./src/contextual/resources/agents/datasets/datasets.py">update</a>(dataset_name, \*, agent_id, \*\*<a href="src/contextual/types/agents/dataset_update_params.py">params</a>) -> <a href="./src/contextual/types/agents/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /agents/{agent_id}/datasets">client.agents.datasets.<a href="./src/contextual/resources/agents/datasets/datasets.py">list</a>(agent_id, \*\*<a href="src/contextual/types/agents/dataset_list_params.py">params</a>) -> <a href="./src/contextual/types/agents/datasets_response.py">DatasetsResponse</a></code>
- <code title="delete /agents/{agent_id}/datasets/{dataset_name}">client.agents.datasets.<a href="./src/contextual/resources/agents/datasets/datasets.py">delete</a>(dataset_name, \*, agent_id) -> <a href="./src/contextual/types/agents/dataset_delete_response.py">object</a></code>

### Metadata

Methods:

- <code title="get /agents/{agent_id}/datasets/{dataset_name}/metadata">client.agents.datasets.metadata.<a href="./src/contextual/resources/agents/datasets/metadata.py">retrieve</a>(dataset_name, \*, agent_id, \*\*<a href="src/contextual/types/agents/datasets/metadata_retrieve_params.py">params</a>) -> <a href="./src/contextual/types/agents/get_dataset_response.py">GetDatasetResponse</a></code>

## Tune

Types:

```python
from contextual.types.agents import TuneResponse
```

Methods:

- <code title="post /agents/{agent_id}/tune">client.agents.tune.<a href="./src/contextual/resources/agents/tune/tune.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/tune_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/tune_response.py">TuneResponse</a></code>

### Jobs

Types:

```python
from contextual.types.agents.tune import (
    GetTuneJobResponse,
    ListGetTuneJobResponse,
    JobDeleteResponse,
)
```

Methods:

- <code title="get /agents/{agent_id}/tune/jobs">client.agents.tune.jobs.<a href="./src/contextual/resources/agents/tune/jobs/jobs.py">list</a>(agent_id) -> <a href="./src/contextual/types/agents/tune/list_get_tune_job_response.py">ListGetTuneJobResponse</a></code>
- <code title="delete /agents/{agent_id}/tune/jobs/{job_id}">client.agents.tune.jobs.<a href="./src/contextual/resources/agents/tune/jobs/jobs.py">delete</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/tune/job_delete_response.py">object</a></code>

#### Metadata

Methods:

- <code title="get /agents/{agent_id}/tune/jobs/{job_id}/metadata">client.agents.tune.jobs.metadata.<a href="./src/contextual/resources/agents/tune/jobs/metadata.py">retrieve</a>(job_id, \*, agent_id) -> <a href="./src/contextual/types/agents/tune/get_tune_job_response.py">GetTuneJobResponse</a></code>

### Models

Types:

```python
from contextual.types.agents.tune import ModelListResponse
```

Methods:

- <code title="get /agents/{agent_id}/tune/models">client.agents.tune.models.<a href="./src/contextual/resources/agents/tune/models.py">list</a>(agent_id) -> <a href="./src/contextual/types/agents/tune/model_list_response.py">ModelListResponse</a></code>
