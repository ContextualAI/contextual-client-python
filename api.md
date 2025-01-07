# Datastores

Types:

```python
from contextual.types import (
    CreateDatastoreResponse,
    DatastoresResponse,
    DatastoreListResponse,
    DatastoreDeleteResponse,
)
```

Methods:

- <code title="post /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">create</a>(\*\*<a href="src/contextual/types/datastore_create_params.py">params</a>) -> <a href="./src/contextual/types/create_datastore_response.py">CreateDatastoreResponse</a></code>
- <code title="get /datastores">client.datastores.<a href="./src/contextual/resources/datastores/datastores.py">list</a>(\*\*<a href="src/contextual/types/datastore_list_params.py">params</a>) -> <a href="./src/contextual/types/datastore_list_response.py">SyncDatastoresList[DatastoreListResponse]</a></code>
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
    GetDocumentsResponse,
    IngestionResponse,
    DocumentDeleteResponse,
)
```

Methods:

- <code title="post /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents/documents.py">create</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_create_params.py">params</a>) -> <a href="./src/contextual/types/datastores/ingestion_response.py">IngestionResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents/documents.py">list</a>(datastore_id, \*\*<a href="src/contextual/types/datastores/document_list_params.py">params</a>) -> <a href="./src/contextual/types/datastores/documents/document_description.py">SyncDatastoresDocumentsListPagination[DocumentDescription]</a></code>
- <code title="delete /datastores/{datastore_id}/documents/{document_id}">client.datastores.documents.<a href="./src/contextual/resources/datastores/documents/documents.py">delete</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/document_delete_response.py">object</a></code>

### Metadata

Types:

```python
from contextual.types.datastores.documents import DocumentDescription
```

Methods:

- <code title="get /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.metadata.<a href="./src/contextual/resources/datastores/documents/metadata.py">retrieve</a>(document_id, \*, datastore_id) -> <a href="./src/contextual/types/datastores/documents/document_description.py">DocumentDescription</a></code>

# Applications

Types:

```python
from contextual.types import (
    ApplicationsResponse,
    CreateApplicationOutput,
    ApplicationUpdateResponse,
    ApplicationListResponse,
    ApplicationDeleteResponse,
)
```

Methods:

- <code title="post /applications">client.applications.<a href="./src/contextual/resources/applications/applications.py">create</a>(\*\*<a href="src/contextual/types/application_create_params.py">params</a>) -> <a href="./src/contextual/types/create_application_output.py">CreateApplicationOutput</a></code>
- <code title="put /applications/{application_id}">client.applications.<a href="./src/contextual/resources/applications/applications.py">update</a>(application_id, \*\*<a href="src/contextual/types/application_update_params.py">params</a>) -> <a href="./src/contextual/types/application_update_response.py">object</a></code>
- <code title="get /applications">client.applications.<a href="./src/contextual/resources/applications/applications.py">list</a>(\*\*<a href="src/contextual/types/application_list_params.py">params</a>) -> <a href="./src/contextual/types/application_list_response.py">SyncApplicationsListPagination[ApplicationListResponse]</a></code>
- <code title="delete /applications/{application_id}">client.applications.<a href="./src/contextual/resources/applications/applications.py">delete</a>(application_id) -> <a href="./src/contextual/types/application_delete_response.py">object</a></code>

## Metadata

Types:

```python
from contextual.types.applications import GetApplicationResponse
```

Methods:

- <code title="get /applications/{application_id}/metadata">client.applications.metadata.<a href="./src/contextual/resources/applications/metadata.py">retrieve</a>(application_id) -> <a href="./src/contextual/types/applications/get_application_response.py">GetApplicationResponse</a></code>

## Query

Types:

```python
from contextual.types.applications import (
    QueryResponse,
    QueryFeedbackResponse,
    QueryFormFillingResponse,
)
```

Methods:

- <code title="post /applications/{application_id}/feedback">client.applications.query.<a href="./src/contextual/resources/applications/query/query.py">feedback</a>(application_id, \*\*<a href="src/contextual/types/applications/query_feedback_params.py">params</a>) -> <a href="./src/contextual/types/applications/query_feedback_response.py">object</a></code>
- <code title="post /applications/{application_id}/form_filling">client.applications.query.<a href="./src/contextual/resources/applications/query/query.py">form_filling</a>(application_id, \*\*<a href="src/contextual/types/applications/query_form_filling_params.py">params</a>) -> <a href="./src/contextual/types/applications/query_form_filling_response.py">QueryFormFillingResponse</a></code>
- <code title="post /applications/{application_id}/query">client.applications.query.<a href="./src/contextual/resources/applications/query/query.py">start</a>(application_id, \*\*<a href="src/contextual/types/applications/query_start_params.py">params</a>) -> <a href="./src/contextual/types/applications/query_response.py">QueryResponse</a></code>

### Metrics

Types:

```python
from contextual.types.applications.query import MetricRetrieveResponse
```

Methods:

- <code title="get /applications/{application_id}/metrics">client.applications.query.metrics.<a href="./src/contextual/resources/applications/query/metrics.py">retrieve</a>(application_id, \*\*<a href="src/contextual/types/applications/query/metric_retrieve_params.py">params</a>) -> <a href="./src/contextual/types/applications/query/metric_retrieve_response.py">MetricRetrieveResponse</a></code>

## Evaluate

Types:

```python
from contextual.types.applications import LaunchEvaluationResponse
```

Methods:

- <code title="post /applications/{application_id}/evaluate">client.applications.evaluate.<a href="./src/contextual/resources/applications/evaluate/evaluate.py">launch</a>(application_id, \*\*<a href="src/contextual/types/applications/evaluate_launch_params.py">params</a>) -> <a href="./src/contextual/types/applications/launch_evaluation_response.py">LaunchEvaluationResponse</a></code>

### Jobs

Types:

```python
from contextual.types.applications.evaluate import (
    EvaluationRoundResponse,
    ListEvaluationResponse,
    JobCancelResponse,
)
```

Methods:

- <code title="get /applications/{application_id}/evaluate/jobs">client.applications.evaluate.jobs.<a href="./src/contextual/resources/applications/evaluate/jobs/jobs.py">list</a>(application_id) -> <a href="./src/contextual/types/applications/evaluate/list_evaluation_response.py">ListEvaluationResponse</a></code>
- <code title="post /applications/{application_id}/evaluate/jobs/{job_id}/cancel">client.applications.evaluate.jobs.<a href="./src/contextual/resources/applications/evaluate/jobs/jobs.py">cancel</a>(job_id, \*, application_id) -> <a href="./src/contextual/types/applications/evaluate/job_cancel_response.py">object</a></code>

#### Metadata

Methods:

- <code title="get /applications/{application_id}/evaluate/jobs/{job_id}/metadata">client.applications.evaluate.jobs.metadata.<a href="./src/contextual/resources/applications/evaluate/jobs/metadata.py">retrieve</a>(job_id, \*, application_id) -> <a href="./src/contextual/types/applications/evaluate/evaluation_round_response.py">EvaluationRoundResponse</a></code>

## Datasets

Types:

```python
from contextual.types.applications import (
    CreateDatasetResponse,
    DatasetsResponse,
    GetDatasetResponse,
    DatasetRetrieveResponse,
    DatasetDeleteResponse,
)
```

Methods:

- <code title="post /applications/{application_id}/datasets">client.applications.datasets.<a href="./src/contextual/resources/applications/datasets/datasets.py">create</a>(application_id, \*\*<a href="src/contextual/types/applications/dataset_create_params.py">params</a>) -> <a href="./src/contextual/types/applications/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /applications/{application_id}/datasets/{dataset_name}">client.applications.datasets.<a href="./src/contextual/resources/applications/datasets/datasets.py">retrieve</a>(dataset_name, \*, application_id, \*\*<a href="src/contextual/types/applications/dataset_retrieve_params.py">params</a>) -> <a href="./src/contextual/types/applications/dataset_retrieve_response.py">object</a></code>
- <code title="put /applications/{application_id}/datasets/{dataset_name}">client.applications.datasets.<a href="./src/contextual/resources/applications/datasets/datasets.py">update</a>(dataset_name, \*, application_id, \*\*<a href="src/contextual/types/applications/dataset_update_params.py">params</a>) -> <a href="./src/contextual/types/applications/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /applications/{application_id}/datasets">client.applications.datasets.<a href="./src/contextual/resources/applications/datasets/datasets.py">list</a>(application_id, \*\*<a href="src/contextual/types/applications/dataset_list_params.py">params</a>) -> <a href="./src/contextual/types/applications/datasets_response.py">DatasetsResponse</a></code>
- <code title="delete /applications/{application_id}/datasets/{dataset_name}">client.applications.datasets.<a href="./src/contextual/resources/applications/datasets/datasets.py">delete</a>(dataset_name, \*, application_id) -> <a href="./src/contextual/types/applications/dataset_delete_response.py">object</a></code>

### Metadata

Methods:

- <code title="get /applications/{application_id}/datasets/{dataset_name}/metadata">client.applications.datasets.metadata.<a href="./src/contextual/resources/applications/datasets/metadata.py">retrieve</a>(dataset_name, \*, application_id, \*\*<a href="src/contextual/types/applications/datasets/metadata_retrieve_params.py">params</a>) -> <a href="./src/contextual/types/applications/get_dataset_response.py">GetDatasetResponse</a></code>

## Tune

Types:

```python
from contextual.types.applications import TuneResponse
```

Methods:

- <code title="post /applications/{application_id}/tune">client.applications.tune.<a href="./src/contextual/resources/applications/tune/tune.py">create</a>(application_id, \*\*<a href="src/contextual/types/applications/tune_create_params.py">params</a>) -> <a href="./src/contextual/types/applications/tune_response.py">TuneResponse</a></code>

### Jobs

Types:

```python
from contextual.types.applications.tune import (
    GetTuneJobResponse,
    ListGetTuneJobResponse,
    JobDeleteResponse,
)
```

Methods:

- <code title="get /applications/{application_id}/tune/jobs">client.applications.tune.jobs.<a href="./src/contextual/resources/applications/tune/jobs/jobs.py">list</a>(application_id) -> <a href="./src/contextual/types/applications/tune/list_get_tune_job_response.py">ListGetTuneJobResponse</a></code>
- <code title="delete /applications/{application_id}/tune/jobs/{job_id}">client.applications.tune.jobs.<a href="./src/contextual/resources/applications/tune/jobs/jobs.py">delete</a>(job_id, \*, application_id) -> <a href="./src/contextual/types/applications/tune/job_delete_response.py">object</a></code>

#### Metadata

Methods:

- <code title="get /applications/{application_id}/tune/jobs/{job_id}/metadata">client.applications.tune.jobs.metadata.<a href="./src/contextual/resources/applications/tune/jobs/metadata.py">retrieve</a>(job_id, \*, application_id) -> <a href="./src/contextual/types/applications/tune/get_tune_job_response.py">GetTuneJobResponse</a></code>

### Models

Types:

```python
from contextual.types.applications.tune import ModelListResponse
```

Methods:

- <code title="get /applications/{application_id}/tune/models">client.applications.tune.models.<a href="./src/contextual/resources/applications/tune/models.py">list</a>(application_id) -> <a href="./src/contextual/types/applications/tune/model_list_response.py">ModelListResponse</a></code>

# Standalone

Types:

```python
from contextual.types import StandaloneLmunitResponse
```

Methods:

- <code title="post /lmunit">client.standalone.<a href="./src/contextual/resources/standalone.py">lmunit</a>(\*\*<a href="src/contextual/types/standalone_lmunit_params.py">params</a>) -> <a href="./src/contextual/types/standalone_lmunit_response.py">StandaloneLmunitResponse</a></code>
