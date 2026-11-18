# Shared Types

```python
from contextual.types import ParsedBlock
```

# Datastores

Types:

```python
from contextual.types import (
    ChunkingConfiguration,
    CreateDatastoreResponse,
    Datastore,
    DatastoreMetadata,
    DatastoreParseConfiguration,
    HTMLConfiguration,
    ListDatastoresResponse,
    UnstructuredDatastoreConfigModel,
    DatastoreUpdateResponse,
    DatastoreDeleteResponse,
    DatastoreResetResponse,
)
```

Methods:

- <code title="post /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">create</a>(\*\*<a href="src/contextual/types/datastore_create_params.py">params</a>) -> <a href="./src/contextual/types/create_datastore_response.py">CreateDatastoreResponse</a></code>
- <code title="put /datastores/{datastore_id}">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">update</a>(datastore_id, \*\*<a href="src/contextual/types/datastore_update_params.py">params</a>) -> <a href="./src/contextual/types/datastore_update_response.py">DatastoreUpdateResponse</a></code>
- <code title="get /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">list</a>(\*\*<a href="src/contextual/types/datastore_list_params.py">params</a>) -> <a href="./src/contextual/types/datastore.py">SyncDatastoresPage[Datastore]</a></code>
- <code title="delete /datastores/{datastore_id}">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">delete</a>(datastore_id) -> <a href="./src/contextual/types/datastore_delete_response.py">DatastoreDeleteResponse</a></code>
- <code title="get /datastores/{datastore_id}/metadata">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">metadata</a>(datastore_id) -> <a href="./src/contextual/types/datastore_metadata.py">DatastoreMetadata</a></code>
- <code title="put /datastores/{datastore_id}/reset">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">reset</a>(datastore_id) -> <a href="./src/contextual/types/datastore_reset_response.py">DatastoreResetResponse</a></code>

## Documents

Types:

```python
from contextual.types.datastores import (
    BaseMetadataFilter,
    CompositeMetadataFilter,
    DocumentMetadata,
    IngestionResponse,
    ListDocumentsResponse,
    DocumentDeleteResponse,
    DocumentGetParseResultResponse,
)
```

Methods:

- <code title="get /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">list</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_list_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_metadata.py">SyncDocumentsPage[DocumentMetadata]</a></code>
- <code title="delete /datastores/{datastore_id}/documents/{document_id}">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">delete</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_delete_response.py">DocumentDeleteResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents/{document_id}/parse">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">get_parse_result</a>(document_id, \*, datastore_id, \*\*<a href="src/contextual/types/datastores/document_get_parse_result_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_get_parse_result_response.py">DocumentGetParseResultResponse</a></code>
- <code title="post /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">ingest</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_ingest_params.py">params</a>) -> <a href="./src/contextual/types/datastores/ingestion_response.py">IngestionResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">metadata</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_metadata.py">DocumentMetadata</a></code>
- <code title="put /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents.py">set_metadata</a>(document_id, \*, datastore_id, \*\*<a href="src/contextual/types/datastores/document_set_metadata_params.py">params</a>) -> <a href="./src/contextual/types/datastores/document_metadata.py">DocumentMetadata</a></code>

## Contents

Types:

```python
from contextual.types.datastores import ContentListResponse, ContentMetadataResponse
```

Methods:

- <code title="get /datastores/{datastore_id}/contents">client.datastores.contents.<a href="./src/contextual/resources/datastores/contents.py">list</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/content_list_params.py">params</a>) -> <a href="./src/contextual/types/datastores/content_list_response.py">SyncContentsPage[ContentListResponse]</a></code>
- <code title="get /datastores/{datastore_id}/contents/{content_id}/metadata">client.datastores.contents.<a href="./src/contextual/resources/datastores/contents.py">metadata</a>(content_id, \*, datastore_id, \*\*<a href="src/contextual/types/datastores/content_metadata_params.py">params</a>) -> <a href="./src/contextual/types/datastores/content_metadata_response.py">ContentMetadataResponse</a></code>

## Chunks

Types:

```python
from contextual.types.datastores import ChunkUpdateContentResponse
```

Methods:

- <code title="put /datastores/{datastore_id}/chunks/{content_id}/content">client.datastores.chunks.<a href="./src/contextual/resources/datastores/chunks.py">update_content</a>(content_id, \*, datastore_id, \*\*<a href="src/contextual/types/datastores/chunk_update_content_params.py">params</a>) -> <a href="./src/contextual/types/datastores/chunk_update_content_response.py">ChunkUpdateContentResponse</a></code>

# Agents

Types:

```python
from contextual.types import (
    ACLConfig,
    Agent,
    AgentConfigs,
    AgentMetadata,
    CreateAgentOutput,
    FilterAndRerankConfig,
    GenerateResponseConfig,
    GlobalConfig,
    ListAgentsResponse,
    ReformulationConfig,
    RetrievalConfig,
    TranslationConfig,
    AgentUpdateResponse,
    AgentDeleteResponse,
    AgentMetadataResponse,
)
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">create</a>(\*\*<a href="src/contextual/types/agent_create_params.py">params</a>) -> <a href="./src/contextual/types/create_agent_output.py">CreateAgentOutput</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/contextual/types/agent_update_params.py">params</a>) -> <a href="./src/contextual/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /agents">client.agents.<a href="./src/contextual/resources/agents/agents.py">list</a>(\*\*<a href="src/contextual/types/agent_list_params.py">params</a>) -> <a href="./src/contextual/types/agent.py">SyncPage[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/contextual/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/contextual/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="post /agents/{agent_id}/copy">client.agents.<a href="./src/contextual/resources/agents/agents.py">copy</a>(agent_id) -> <a href="./src/contextual/types/create_agent_output.py">CreateAgentOutput</a></code>
- <code title="get /agents/{agent_id}/metadata">client.agents.<a href="./src/contextual/resources/agents/agents.py">metadata</a>(agent_id) -> <a href="./src/contextual/types/agent_metadata_response.py">AgentMetadataResponse</a></code>
- <code title="put /agents/{agent_id}/reset">client.agents.<a href="./src/contextual/resources/agents/agents.py">reset</a>(agent_id) -> object</code>
- <code title="post /agents/{agent_id}/template">client.agents.<a href="./src/contextual/resources/agents/agents.py">save_template</a>(agent_id, \*\*<a href="src/contextual/types/agent_save_template_params.py">params</a>) -> object</code>

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
- <code title="post /agents/{agent_id}/feedback">client.agents.query.<a href="./src/contextual/resources/agents/query.py">feedback</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_feedback_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_feedback_response.py">QueryFeedbackResponse</a></code>
- <code title="get /agents/{agent_id}/metrics">client.agents.query.<a href="./src/contextual/resources/agents/query.py">metrics</a>(agent_id, \*\*<a href="src/contextual/types/agents/query_metrics_params.py">params</a>) -> <a href="./src/contextual/types/agents/query_metrics_response.py">QueryMetricsResponse</a></code>
- <code title="get /agents/{agent_id}/query/{message_id}/retrieval/info">client.agents.query.<a href="./src/contextual/resources/agents/query.py">retrieval_info</a>(message_id, \*, agent_id, \*\*<a href="src/contextual/types/agents/query_retrieval_info_params.py">params</a>) -> <a href="./src/contextual/types/agents/retrieval_info_response.py">RetrievalInfoResponse</a></code>

## Templates

Types:

```python
from contextual.types.agents import TemplateListResponse
```

Methods:

- <code title="get /agents/templates/{template}">client.agents.templates.<a href="./src/contextual/resources/agents/templates.py">retrieve</a>(template) -> <a href="./src/contextual/types/agent_metadata.py">AgentMetadata</a></code>
- <code title="get /agents/templates">client.agents.templates.<a href="./src/contextual/resources/agents/templates.py">list</a>() -> <a href="./src/contextual/types/agents/template_list_response.py">TemplateListResponse</a></code>

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

# Extract

Types:

```python
from contextual.types import ExtractDeleteDocumentResponse, ExtractDeleteSchemaResponse, ExtractListDocumentsResponse, ExtractRetrieveDocumentResponse, ExtractListJobsResponse, ExtractRetrieveJobResponse, ExtractRetrieveJobResultsResponse, ExtractListSchemasResponse, ExtractRetrieveSchemaResponse, ExtractUploadDocumentResponse, ExtractCreateJobResponse, ExtractCreateSchemaResponse, ExtractUpdateSchemaResponse
```

Methods:

- <code title="delete /extract/documents/{document_id}">client.extract.<a href="./src/contextual/resources/extract.py">delete_document</a>(document_id) -> <a href="./src/contextual/types/extract_delete_document_response.py">ExtractDeleteDocumentResponse</a></code>
- <code title="delete /extract/schemas/{schema_id}">client.extract.<a href="./src/contextual/resources/extract.py">delete_schema</a>(schema_id) -> <a href="./src/contextual/types/extract_delete_schema_response.py">ExtractDeleteSchemaResponse</a></code>
- <code title="get /extract/documents">client.extract.<a href="./src/contextual/resources/extract.py">list_documents</a>(\*\*<a href="src/contextual/types/extract_list_documents_params.py">params</a>) -> <a href="./src/contextual/types/extract_list_documents_response.py">ExtractListDocumentsResponse</a></code>
- <code title="get /extract/documents/{document_id}">client.extract.<a href="./src/contextual/resources/extract.py">retrieve_document</a>(document_id) -> <a href="./src/contextual/types/extract_retrieve_document_response.py">ExtractRetrieveDocumentResponse</a></code>
- <code title="get /extract/jobs">client.extract.<a href="./src/contextual/resources/extract.py">list_jobs</a>(\*\*<a href="src/contextual/types/extract_list_jobs_params.py">params</a>) -> <a href="./src/contextual/types/extract_list_jobs_response.py">ExtractListJobsResponse</a></code>
- <code title="get /extract/jobs/{job_id}">client.extract.<a href="./src/contextual/resources/extract.py">retrieve_job</a>(job_id) -> <a href="./src/contextual/types/extract_retrieve_job_response.py">ExtractRetrieveJobResponse</a></code>
- <code title="get /extract/jobs/{job_id}/results">client.extract.<a href="./src/contextual/resources/extract.py">retrieve_job_results</a>(job_id) -> <a href="./src/contextual/types/extract_retrieve_job_results_response.py">ExtractRetrieveJobResultsResponse</a></code>
- <code title="get /extract/schemas">client.extract.<a href="./src/contextual/resources/extract.py">list_schemas</a>(\*\*<a href="src/contextual/types/extract_list_schemas_params.py">params</a>) -> <a href="./src/contextual/types/extract_list_schemas_response.py">ExtractListSchemasResponse</a></code>
- <code title="get /extract/schemas/{schema_id}">client.extract.<a href="./src/contextual/resources/extract.py">retrieve_schema</a>(schema_id) -> <a href="./src/contextual/types/extract_retrieve_schema_response.py">ExtractRetrieveSchemaResponse</a></code>
- <code title="post /extract/documents/upload">client.extract.<a href="./src/contextual/resources/extract.py">upload_document</a>(\*\*<a href="src/contextual/types/extract_upload_document_params.py">params</a>) -> <a href="./src/contextual/types/extract_upload_document_response.py">ExtractUploadDocumentResponse</a></code>
- <code title="post /extract/jobs">client.extract.<a href="./src/contextual/resources/extract.py">create_job</a>(\*\*<a href="src/contextual/types/extract_create_job_params.py">params</a>) -> <a href="./src/contextual/types/extract_create_job_response.py">ExtractCreateJobResponse</a></code>
- <code title="post /extract/schemas">client.extract.<a href="./src/contextual/resources/extract.py">create_schema</a>(\*\*<a href="src/contextual/types/extract_create_schema_params.py">params</a>) -> <a href="./src/contextual/types/extract_create_schema_response.py">ExtractCreateSchemaResponse</a></code>
- <code title="put /extract/jobs/{job_id}/results">client.extract.<a href="./src/contextual/resources/extract.py">update_job_results</a>(job_id, \*\*<a href="src/contextual/types/extract_update_job_results_params.py">params</a>) -> object</code>
- <code title="put /extract/schemas/{schema_id}">client.extract.<a href="./src/contextual/resources/extract.py">update_schema</a>(schema_id, \*\*<a href="src/contextual/types/extract_update_schema_params.py">params</a>) -> <a href="./src/contextual/types/extract_update_schema_response.py">ExtractUpdateSchemaResponse</a></code>

# Billing

Types:

```python
from contextual.types import BillingRetrieveBalanceResponse, BillingListTopUpsResponse, BillingRetrieveBillingModeHistoryResponse, BillingRetrieveMetadataResponse, BillingRetrieveAclUsageResponse, BillingRetrieveEarliestUsageDateResponse, BillingRetrieveMonthlyUsageResponse
```

Methods:

- <code title="get /billing/balance">client.billing.<a href="./src/contextual/resources/billing.py">retrieve_balance</a>() -> <a href="./src/contextual/types/billing_retrieve_balance_response.py">BillingRetrieveBalanceResponse</a></code>
- <code title="get /billing/balance/top-ups">client.billing.<a href="./src/contextual/resources/billing.py">list_top_ups</a>(\*\*<a href="src/contextual/types/billing_list_top_ups_params.py">params</a>) -> <a href="./src/contextual/types/billing_list_top_ups_response.py">BillingListTopUpsResponse</a></code>
- <code title="get /billing/billing_mode/history">client.billing.<a href="./src/contextual/resources/billing.py">retrieve_billing_mode_history</a>(\*\*<a href="src/contextual/types/billing_retrieve_billing_mode_history_params.py">params</a>) -> <a href="./src/contextual/types/billing_retrieve_billing_mode_history_response.py">BillingRetrieveBillingModeHistoryResponse</a></code>
- <code title="get /billing/metadata">client.billing.<a href="./src/contextual/resources/billing.py">retrieve_metadata</a>() -> <a href="./src/contextual/types/billing_retrieve_metadata_response.py">BillingRetrieveMetadataResponse</a></code>
- <code title="get /billing/usages/acl">client.billing.<a href="./src/contextual/resources/billing.py">retrieve_acl_usage</a>(\*\*<a href="src/contextual/types/billing_retrieve_acl_usage_params.py">params</a>) -> <a href="./src/contextual/types/billing_retrieve_acl_usage_response.py">BillingRetrieveAclUsageResponse</a></code>
- <code title="get /billing/usages/earliest_date">client.billing.<a href="./src/contextual/resources/billing.py">retrieve_earliest_usage_date</a>() -> <a href="./src/contextual/types/billing_retrieve_earliest_usage_date_response.py">BillingRetrieveEarliestUsageDateResponse</a></code>
- <code title="get /billing/usages/monthly">client.billing.<a href="./src/contextual/resources/billing.py">retrieve_monthly_usage</a>(\*\*<a href="src/contextual/types/billing_retrieve_monthly_usage_params.py">params</a>) -> <a href="./src/contextual/types/billing_retrieve_monthly_usage_response.py">BillingRetrieveMonthlyUsageResponse</a></code>

# Workspaces

Types:

```python
from contextual.types import WorkspaceRetrieveConsentResponse, WorkspaceUpdateConsentResponse
```

Methods:

- <code title="get /workspaces/consent">client.workspaces.<a href="./src/contextual/resources/workspaces.py">retrieve_consent</a>() -> <a href="./src/contextual/types/workspace_retrieve_consent_response.py">WorkspaceRetrieveConsentResponse</a></code>
- <code title="put /workspaces/consent">client.workspaces.<a href="./src/contextual/resources/workspaces.py">update_consent</a>(\*\*<a href="src/contextual/types/workspace_update_consent_params.py">params</a>) -> <a href="./src/contextual/types/workspace_update_consent_response.py">WorkspaceUpdateConsentResponse</a></code>
