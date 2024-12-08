# Datastores

Types:

```python
from sunrise.types import CreateDatastoreOutput, Datastore, DatastoreDeleteResponse
```

Methods:

- <code title="post /datastores">client.datastores.<a href="./src/sunrise/resources/datastores/datastores.py">create</a>(\*\*<a href="src/sunrise/types/datastore_create_params.py">params</a>) -> <a href="./src/sunrise/types/create_datastore_output.py">CreateDatastoreOutput</a></code>
- <code title="get /datastores">client.datastores.<a href="./src/sunrise/resources/datastores/datastores.py">list</a>(\*\*<a href="src/sunrise/types/datastore_list_params.py">params</a>) -> <a href="./src/sunrise/types/datastore.py">Datastore</a></code>
- <code title="delete /datastores/{datastore_id}">client.datastores.<a href="./src/sunrise/resources/datastores/datastores.py">delete</a>(datastore_id) -> <a href="./src/sunrise/types/datastore_delete_response.py">object</a></code>

## Metadata

Types:

```python
from sunrise.types.datastores import GetDatastoreResponse
```

Methods:

- <code title="get /datastores/{datastore_id}/metadata">client.datastores.metadata.<a href="./src/sunrise/resources/datastores/metadata.py">retrieve</a>(datastore_id) -> <a href="./src/sunrise/types/datastores/get_datastore_response.py">GetDatastoreResponse</a></code>

## Documents

Types:

```python
from sunrise.types.datastores import GetDocumentsResponse, IngestionResponse, DocumentDeleteResponse
```

Methods:

- <code title="post /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/sunrise/resources/datastores/documents/documents.py">create</a>(datastore_id, \*\*<a href="src/sunrise/types/datastores/document_create_params.py">params</a>) -> <a href="./src/sunrise/types/datastores/ingestion_response.py">IngestionResponse</a></code>
- <code title="get /datastores/{datastore_id}/documents">client.datastores.documents.<a href="./src/sunrise/resources/datastores/documents/documents.py">list</a>(datastore_id, \*\*<a href="src/sunrise/types/datastores/document_list_params.py">params</a>) -> <a href="./src/sunrise/types/datastores/get_documents_response.py">GetDocumentsResponse</a></code>
- <code title="delete /datastores/{datastore_id}/documents/{document_id}">client.datastores.documents.<a href="./src/sunrise/resources/datastores/documents/documents.py">delete</a>(document_id, \*, datastore_id) -> <a href="./src/sunrise/types/datastores/document_delete_response.py">object</a></code>

### Metadata

Types:

```python
from sunrise.types.datastores.documents import DocumentDescription
```

Methods:

- <code title="get /datastores/{datastore_id}/documents/{document_id}/metadata">client.datastores.documents.metadata.<a href="./src/sunrise/resources/datastores/documents/metadata.py">retrieve</a>(document_id, \*, datastore_id) -> <a href="./src/sunrise/types/datastores/documents/document_description.py">DocumentDescription</a></code>

# Applications

Types:

```python
from sunrise.types import (
    ApplicationList,
    CreateApplicationOutput,
    ApplicationUpdateResponse,
    ApplicationDeleteResponse,
)
```

Methods:

- <code title="post /applications">client.applications.<a href="./src/sunrise/resources/applications/applications.py">create</a>(\*\*<a href="src/sunrise/types/application_create_params.py">params</a>) -> <a href="./src/sunrise/types/create_application_output.py">CreateApplicationOutput</a></code>
- <code title="put /applications/{application_id}">client.applications.<a href="./src/sunrise/resources/applications/applications.py">update</a>(application_id, \*\*<a href="src/sunrise/types/application_update_params.py">params</a>) -> <a href="./src/sunrise/types/application_update_response.py">object</a></code>
- <code title="get /applications">client.applications.<a href="./src/sunrise/resources/applications/applications.py">list</a>(\*\*<a href="src/sunrise/types/application_list_params.py">params</a>) -> <a href="./src/sunrise/types/application_list.py">ApplicationList</a></code>
- <code title="delete /applications/{application_id}">client.applications.<a href="./src/sunrise/resources/applications/applications.py">delete</a>(application_id) -> <a href="./src/sunrise/types/application_delete_response.py">object</a></code>

## Metadata

Types:

```python
from sunrise.types.applications import GetApplicationResponse
```

Methods:

- <code title="get /applications/{application_id}/metadata">client.applications.metadata.<a href="./src/sunrise/resources/applications/metadata.py">retrieve</a>(application_id) -> <a href="./src/sunrise/types/applications/get_application_response.py">GetApplicationResponse</a></code>

## Query

Types:

```python
from sunrise.types.applications import QueryResponse, QueryFeedbackResponse
```

Methods:

- <code title="post /applications/{application_id}/feedback">client.applications.query.<a href="./src/sunrise/resources/applications/query.py">feedback</a>(application_id, \*\*<a href="src/sunrise/types/applications/query_feedback_params.py">params</a>) -> <a href="./src/sunrise/types/applications/query_feedback_response.py">object</a></code>
- <code title="post /applications/{application_id}/query">client.applications.query.<a href="./src/sunrise/resources/applications/query.py">start</a>(application_id, \*\*<a href="src/sunrise/types/applications/query_start_params.py">params</a>) -> <a href="./src/sunrise/types/applications/query_response.py">QueryResponse</a></code>

## Evaluate

Types:

```python
from sunrise.types.applications import LaunchEvaluationResponse
```

Methods:

- <code title="post /applications/{application_id}/evaluate">client.applications.evaluate.<a href="./src/sunrise/resources/applications/evaluate/evaluate.py">launch</a>(application_id, \*\*<a href="src/sunrise/types/applications/evaluate_launch_params.py">params</a>) -> <a href="./src/sunrise/types/applications/launch_evaluation_response.py">LaunchEvaluationResponse</a></code>

### Jobs

Types:

```python
from sunrise.types.applications.evaluate import (
    EvaluationRoundResponse,
    ListEvaluationResponse,
    JobCancelResponse,
)
```

Methods:

- <code title="get /applications/{application_id}/evaluate/jobs">client.applications.evaluate.jobs.<a href="./src/sunrise/resources/applications/evaluate/jobs/jobs.py">list</a>(application_id) -> <a href="./src/sunrise/types/applications/evaluate/list_evaluation_response.py">ListEvaluationResponse</a></code>
- <code title="post /applications/{application_id}/evaluate/jobs/{job_id}/cancel">client.applications.evaluate.jobs.<a href="./src/sunrise/resources/applications/evaluate/jobs/jobs.py">cancel</a>(job_id, \*, application_id) -> <a href="./src/sunrise/types/applications/evaluate/job_cancel_response.py">object</a></code>

#### Metadata

Methods:

- <code title="get /applications/{application_id}/evaluate/jobs/{job_id}/metadata">client.applications.evaluate.jobs.metadata.<a href="./src/sunrise/resources/applications/evaluate/jobs/metadata.py">retrieve</a>(job_id, \*, application_id) -> <a href="./src/sunrise/types/applications/evaluate/evaluation_round_response.py">EvaluationRoundResponse</a></code>

## Datasets

Types:

```python
from sunrise.types.applications import (
    CreateDatasetResponse,
    GetDatasetResponse,
    ListDatasetResponse,
    DatasetRetrieveResponse,
    DatasetDeleteResponse,
)
```

Methods:

- <code title="post /applications/{application_id}/datasets">client.applications.datasets.<a href="./src/sunrise/resources/applications/datasets/datasets.py">create</a>(application_id, \*\*<a href="src/sunrise/types/applications/dataset_create_params.py">params</a>) -> <a href="./src/sunrise/types/applications/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /applications/{application_id}/datasets/{dataset_name}">client.applications.datasets.<a href="./src/sunrise/resources/applications/datasets/datasets.py">retrieve</a>(dataset_name, \*, application_id, \*\*<a href="src/sunrise/types/applications/dataset_retrieve_params.py">params</a>) -> <a href="./src/sunrise/types/applications/dataset_retrieve_response.py">object</a></code>
- <code title="put /applications/{application_id}/datasets/{dataset_name}">client.applications.datasets.<a href="./src/sunrise/resources/applications/datasets/datasets.py">update</a>(dataset_name, \*, application_id, \*\*<a href="src/sunrise/types/applications/dataset_update_params.py">params</a>) -> <a href="./src/sunrise/types/applications/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /applications/{application_id}/datasets">client.applications.datasets.<a href="./src/sunrise/resources/applications/datasets/datasets.py">list</a>(application_id, \*\*<a href="src/sunrise/types/applications/dataset_list_params.py">params</a>) -> <a href="./src/sunrise/types/applications/list_dataset_response.py">ListDatasetResponse</a></code>
- <code title="delete /applications/{application_id}/datasets/{dataset_name}">client.applications.datasets.<a href="./src/sunrise/resources/applications/datasets/datasets.py">delete</a>(dataset_name, \*, application_id) -> <a href="./src/sunrise/types/applications/dataset_delete_response.py">object</a></code>

### Metadata

Methods:

- <code title="get /applications/{application_id}/datasets/{dataset_name}/metadata">client.applications.datasets.metadata.<a href="./src/sunrise/resources/applications/datasets/metadata.py">retrieve</a>(dataset_name, \*, application_id, \*\*<a href="src/sunrise/types/applications/datasets/metadata_retrieve_params.py">params</a>) -> <a href="./src/sunrise/types/applications/get_dataset_response.py">GetDatasetResponse</a></code>

## Tune

Types:

```python
from sunrise.types.applications import TuneResponse
```

Methods:

- <code title="post /applications/{application_id}/tune">client.applications.tune.<a href="./src/sunrise/resources/applications/tune/tune.py">create</a>(application_id, \*\*<a href="src/sunrise/types/applications/tune_create_params.py">params</a>) -> <a href="./src/sunrise/types/applications/tune_response.py">TuneResponse</a></code>

### Jobs

Types:

```python
from sunrise.types.applications.tune import (
    GetTuneJobResponse,
    ListGetTuneJobResponse,
    JobDeleteResponse,
)
```

Methods:

- <code title="get /applications/{application_id}/tune/jobs">client.applications.tune.jobs.<a href="./src/sunrise/resources/applications/tune/jobs/jobs.py">list</a>(application_id) -> <a href="./src/sunrise/types/applications/tune/list_get_tune_job_response.py">ListGetTuneJobResponse</a></code>
- <code title="delete /applications/{application_id}/tune/jobs/{job_id}">client.applications.tune.jobs.<a href="./src/sunrise/resources/applications/tune/jobs/jobs.py">delete</a>(job_id, \*, application_id) -> <a href="./src/sunrise/types/applications/tune/job_delete_response.py">object</a></code>

#### Metadata

Methods:

- <code title="get /applications/{application_id}/tune/jobs/{job_id}/metadata">client.applications.tune.jobs.metadata.<a href="./src/sunrise/resources/applications/tune/jobs/metadata.py">retrieve</a>(job_id, \*, application_id) -> <a href="./src/sunrise/types/applications/tune/get_tune_job_response.py">GetTuneJobResponse</a></code>

### Models

Types:

```python
from sunrise.types.applications.tune import ModelListResponse
```

Methods:

- <code title="get /applications/{application_id}/tune/models">client.applications.tune.models.<a href="./src/sunrise/resources/applications/tune/models.py">list</a>(application_id) -> <a href="./src/sunrise/types/applications/tune/model_list_response.py">ModelListResponse</a></code>
