# Datastores

Types:

```python
from contextual.types import (
    CreateDatastoreResponse,
    Datastore,
    DatastoreMetadata,
    ListDatastoresResponse,
)
```

Methods:

- <code title="post /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">create</a>(\*\*<a href="src/contextual/types/datastore_create_params.py">params</a>) -> <a href="./src/contextual/types/create_datastore_response.py">CreateDatastoreResponse</a></code>
- <code title="get /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">list</a>(\*\*<a href="src/contextual/types/datastore_list_params.py">params</a>) -> <a href="./src/contextual/types/datastore.py">SyncDatastoresPage[Datastore]</a></code>
- <code title="delete /datastores/{datastore_id}">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">delete</a>(datastore_id) -> object</code>
- <code title="get /datastores/{datastore_id}/metadata">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">metadata</a>(datastore_id) -> <a href="./src/contextual/types/datastore_metadata.py">DatastoreMetadata</a></code>
- <code title="put /datastores/{datastore_id}/reset">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">reset</a>(datastore_id) -> object</code>

## Documents

Types:

```python
from contextual.types.datastores import DocumentMetadata, IngestionResponse, ListDocumentsResponse
```

Methods:

- <code title="get /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">list</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_list_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_metadata.py">SyncDocumentsPage[DocumentMetadata]</a></code>
- <code title="delete /datastores/{datastore_id}/documents/{document_id}">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">delete</a>(document_id, \*, datastore_id) -> object</code>
- <code title="post /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">ingest</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_ingest_params.py">params</a>) -> <a href="./src/contextual/types/datastores/ingestion_response.py">IngestionResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">metadata</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_metadata.py">DocumentMetadata</a></code>
- <code title="post /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">set_metadata</a>(document_id, \*, datastore_id, \*\*<a href="src/contextual/types/datastores/document_set_metadata_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_metadata.py">DocumentMetadata</a></code>

# Agents

Types:

```python
from contextual.types import (
    Agent,
    AgentMetadata,
    CreateAgentOutput,
    GenerateResponseConfig,
    GlobalConfig,
    ListAgentsResponse,
    RetrievalConfig,
    AgentMetadataResponse,
)
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">create</a>(\*\*<a href="src/contextual/types/agent_create_params.py">params</a>) -> <a href="./src/contextual/types/create_agent_output.py">CreateAgentOutput</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/contextual/types/agent_update_params.py">params</a>) -> object</code>
- <code title="get /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">list</a>(\*\*<a href="src/contextual/types/agent_list_params.py">params</a>) -> <a href="./src/contextual/types/agent.py">SyncPage[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">delete</a>(agent_id) -> object</code>
- <code title="get /agents/{agent_id}/metadata">client.agents.<a href="./src/contextual/resources/agents/agents.py">metadata</a>(agent_id) -> <a href="./src/contextual/types/agent_metadata_response.py">AgentMetadataResponse</a></code>
- <code title="put /agents/{agent_id}/reset">client.agents.<a href="./src/contextual/resources/agents/agents.py">reset</a>(agent_id) -> object</code>

## Query

Types:

```python
from contextual.types.agents import QueryResponse, RetrievalInfoResponse, QueryMetricsResponse
```

Methods:

- <code title="post /agents/{agent_id}/query">client.agents.query.<a href="./src/contextual/resources/agents/query.py">create</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_create_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_response.py">QueryResponse</a></code>
- <code title="post /agents/{agent_id}/feedback">client.agents.query.<a href="./src/contextual/resources/agents/query.py">feedback</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_feedback_params.py">params</a>) -> object</code>
- <code title="get /agents/{agent_id}/metrics">client.agents.query.<a href="./src/contextual/resources/agents/query.py">metrics</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_metrics_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_metrics_response.py">QueryMetricsResponse</a></code>
- <code title="get /agents/{agent_id}/query/{message_id}/retrieval/info">client.agents.query.<a href="./src/contextual/resources/agents/query.py">retrieval_info</a>(message_id, \*, agent_id, \*\*<a href="src/contextual/types/agents/query_retrieval_info_params.py">params</a>) -> <a href="./src/contextual/types/agents/retrieval_info_response.py">RetrievalInfoResponse</a></code>

# Users

Types:

```python
from contextual.types import InviteUsersResponse, ListUsersResponse, NewUser
```

Methods:

- <code title="put /users">client.users.<a href="./src/contextual/resources/users.py">update</a>(\*\*<a href="src/contextual/types/user_update_params.py">params</a>) -> object</code>
- <code title="get /users">client.users.<a href="./src/contextual/resources/users.py">list</a>(\*\*<a href="src/contextual/types/user_list_params.py">params</a>) -> SyncUsersPage[User]</code>
- <code title="delete /users">client.users.<a href="./src/contextual/resources/users.py">deactivate</a>(\*\*<a href="src/contextual/types/user_deactivate_params.py">params</a>) -> object</code>
- <code title="post /users">client.users.<a href="./src/contextual/resources/users.py">invite</a>(\*\*<a href="src/contextual/types/user_invite_params.py">params</a>) -> <a href="./src/contextual/types/invite_users_response.py">InviteUsersResponse</a></code>

# LMUnit

Types:

```python
from contextual.types import LMUnitCreateResponse
```

Methods:

- <code title="post /lmunit">client.lmunit.<a href="./src/contextual/resources/lmunit.py">create</a>(\*\*<a href="src/contextual/types/lmunit_create_params.py">params</a>) -> <a href="./src/contextual/types/lmunit_create_response.py">LMUnitCreateResponse</a></code>

# Rerank

Types:

```python
from contextual.types import RerankCreateResponse
```

Methods:

- <code title="post /rerank">client.rerank.<a href="./src/contextual/resources/rerank.py">create</a>(\*\*<a href="src/contextual/types/rerank_create_params.py">params</a>) -> <a href="./src/contextual/types/rerank_create_response.py">RerankCreateResponse</a></code>

# Generate

Types:

```python
from contextual.types import GenerateCreateResponse
```

Methods:

- <code title="post /generate">client.generate.<a href="./src/contextual/resources/generate.py">create</a>(\*\*<a href="src/contextual/types/generate_create_params.py">params</a>) -> <a href="./src/contextual/types/generate_create_response.py">GenerateCreateResponse</a></code>

# Parse

Types:

```python
from contextual.types import (
    ParseCreateResponse,
    ParseJobResultsResponse,
    ParseJobStatusResponse,
    ParseJobsResponse,
)
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/contextual/resources/parse.py">create</a>(\*\*<a href="src/contextual/types/parse_create_params.py">params</a>) -> <a href="./src/contextual/types/parse_create_response.py">ParseCreateResponse</a></code>
- <code title="get /parse/jobs/{job_id}/results">client.parse.<a href="./src/contextual/resources/parse.py">job_results</a>(job_id, \*\*<a href="src/contextual/types/parse_job_results_params.py">params</a>) -> <a href="./src/contextual/types/parse_job_results_response.py">ParseJobResultsResponse</a></code>
- <code title="get /parse/jobs/{job_id}/status">client.parse.<a href="./src/contextual/resources/parse.py">job_status</a>(job_id) -> <a href="./src/contextual/types/parse_job_status_response.py">ParseJobStatusResponse</a></code>
- <code title="get /parse/jobs">client.parse.<a href="./src/contextual/resources/parse.py">jobs</a>(\*\*<a href="src/contextual/types/parse_jobs_params.py">params</a>) -> <a href="./src/contextual/types/parse_jobs_response.py">ParseJobsResponse</a></code>
