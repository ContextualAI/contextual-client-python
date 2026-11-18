# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, cast

import httpx

from ..types import (
    extract_list_jobs_params,
    extract_create_job_params,
    extract_list_schemas_params,
    extract_create_schema_params,
    extract_update_schema_params,
    extract_list_documents_params,
    extract_upload_document_params,
    extract_update_job_results_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.extract_list_jobs_response import ExtractListJobsResponse
from ..types.extract_create_job_response import ExtractCreateJobResponse
from ..types.extract_list_schemas_response import ExtractListSchemasResponse
from ..types.extract_retrieve_job_response import ExtractRetrieveJobResponse
from ..types.extract_create_schema_response import ExtractCreateSchemaResponse
from ..types.extract_delete_schema_response import ExtractDeleteSchemaResponse
from ..types.extract_update_schema_response import ExtractUpdateSchemaResponse
from ..types.extract_list_documents_response import ExtractListDocumentsResponse
from ..types.extract_delete_document_response import ExtractDeleteDocumentResponse
from ..types.extract_retrieve_schema_response import ExtractRetrieveSchemaResponse
from ..types.extract_upload_document_response import ExtractUploadDocumentResponse
from ..types.extract_retrieve_document_response import ExtractRetrieveDocumentResponse
from ..types.extract_retrieve_job_results_response import ExtractRetrieveJobResultsResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def delete_document(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractDeleteDocumentResponse:
        """
        Delete a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._delete(
            f"/extract/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractDeleteDocumentResponse,
        )

    def delete_schema(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractDeleteSchemaResponse:
        """
        Delete a schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._delete(
            f"/extract/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractDeleteSchemaResponse,
        )

    def list_documents(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        search: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractListDocumentsResponse:
        """
        List documents for structured extraction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/extract/documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "search": search,
                    },
                    extract_list_documents_params.ExtractListDocumentsParams,
                ),
            ),
            cast_to=ExtractListDocumentsResponse,
        )

    def retrieve_document(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveDocumentResponse:
        """
        Get document information by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            f"/extract/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveDocumentResponse,
        )

    def list_jobs(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        job_status: object | Omit = omit,
        search: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractListJobsResponse:
        """
        List extraction jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/extract/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "job_status": job_status,
                        "search": search,
                    },
                    extract_list_jobs_params.ExtractListJobsParams,
                ),
            ),
            cast_to=ExtractListJobsResponse,
        )

    def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveJobResponse:
        """
        Get the status of an extraction job.

        For running jobs with a Temporal workflow, returns accumulated results and failed subtrees from workflow queries. For completed/failed jobs or jobs without workflow, these fields are empty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/extract/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveJobResponse,
        )

    def retrieve_job_results(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveJobResultsResponse:
        """
        Get the results of a completed extraction job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/extract/jobs/{job_id}/results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveJobResultsResponse,
        )

    def list_schemas(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        search: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractListSchemasResponse:
        """
        List schemas with optional search.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/extract/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "search": search,
                    },
                    extract_list_schemas_params.ExtractListSchemasParams,
                ),
            ),
            cast_to=ExtractListSchemasResponse,
        )

    def retrieve_schema(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveSchemaResponse:
        """
        Get schema information by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._get(
            f"/extract/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveSchemaResponse,
        )

    def upload_document(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractUploadDocumentResponse:
        """
        Upload a document for structured extraction.

        Uploads a PDF document that can be used for structured data extraction. Only PDF files are supported.

        Supported File Types:

        1. PDF files only (`.pdf` extension)
        2. Maximum file size: 50MB (recommended)
        3. Documents are processed and validated upon upload

        Document Processing:

        1. File size and page count are automatically calculated
        2. Document is validated for PDF format and readability
        3. Metadata is extracted and stored for future reference
        4. Document is stored securely and can be referenced by ID

        Usage:

        After uploading, you'll receive a `document_id` that can be used with:

        1. `POST /jobs` endpoint to start extraction jobs
        2. `GET /documents/{document_id}` to retrieve document information
        3. `DELETE /documents/{document_id}` to remove the document

        Example Response:
        ```json
        {
          "document_id": "123e4567-e89b-12d3-a456-426614174000",
          "file_name": "financial_report.pdf",
          "file_size": 2048576,
          "page_count": 45,
          "uploaded_at": "2025-01-11T18:35:00Z",
          "status": "uploaded"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/extract/documents/upload",
            body=maybe_transform(body, extract_upload_document_params.ExtractUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractUploadDocumentResponse,
        )

    def create_job(
        self,
        *,
        document_id: str,
        schema_id: str,
        config: object | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateJobResponse:
        """
        Start a new structured extraction job.

        Extracts structured data from a PDF document using AI models based on a JSON Schema. The `document_id` and `schema_id` must be valid UUIDs of previously uploaded documents and created schemas.

        How It Works:

        1. Document Processing: The system analyzes the PDF document and splits it into manageable sections
        2. Schema Analysis: Your JSON schema is parsed and validated for supported features
        3. Extraction: The pipeline processes each section and extracts data according to your schema
        4. Validation: Extracted data is validated against your schema to ensure constraints and requirements are met
        5. Results: Structured data is returned in the format defined by your schema

        Supported Models:

        1. `gemini-2.5-flash`: Fast, cost-effective model for most use cases (default)
        2. `gemini-2.5-pro`: More powerful model for complex extractions

        Configuration Options:

        Basic Settings:

        1. `model`: AI model to use for extraction
        2. `max_num_concurrent_requests`: Number of parallel processing requests (1-20)
        3. `validate_response_schema`: Whether to validate extracted data against schema

        Advanced Settings:

        1. `per_key_attribution`: Enable detailed reasoning and confidence scores for each field
        2. `temperature`: Control randomness in AI responses (0.0-2.0)
        3. `seed`: Set random seed for reproducible results
        4. `enable_thinking`: Show AI reasoning process
        5. `n_max_retries`: Maximum retry attempts for failed requests

        Streaming Mode (`stream=true`):

        When `stream=true`, the endpoint returns an SSE stream instead of a job ID. Results are streamed as subtrees complete, enabling real-time progress visibility in the frontend.

        - Response: SSE stream (`text/event-stream`) with events: `start`, `subtree_result`, `subtree_error`, `agentic_array_progress`
        - Job records are still created and results persisted (retrievable via `GET /jobs/{job_id}`)
        - Always durable: Uses Temporal workflow—job continues running even if client disconnects
        - Automatic retries: Temporal handles activity failures and retries automatically
        - Use case: Interactive frontend UI where users want real-time extraction progress

        SSE Event Types:

        1. `start`: Emitted once with `job_id`, `total_subtrees`, and `start_time`
        2. `subtree_result`: Emitted per successful subtree with `extracted_result`, `attributions`, `usage_metadata`
        3. `subtree_error`: Emitted per failed subtree with `error_message` and `error_type`

        See `STREAMING-DESIGN.md` for full protocol specification.

        Job Lifecycle:

        1. `pending`: Job is queued and waiting to start
        2. `processing`: AI is actively extracting data from the document
        3. `completed`: Extraction finished successfully with results
        4. `failed`: Extraction failed due to an error
        5. `cancelled`: Job was cancelled before completion

        Monitoring Progress:

        Use the `GET /jobs/{job_id}` endpoint to check job status and progress:

        1. `completion_percentage`: Overall progress (0-100)
        2. `current_step`: Current processing stage
        3. `fields_processed`: Number of schema fields completed
        4. `total_fields`: Total number of schema fields to process

        Getting Results:

        Once a job is completed, use `GET /jobs/{job_id}/results` to retrieve:

        1. `results`: Extracted data conforming to your schema
        2. `metadata`: Processing information, costs, and performance metrics
        3. `attributions`: (if enabled) Reasoning and confidence scores for each field

        Example Request:
        ```json
        {
          "document_id": "123e4567-e89b-12d3-a456-426614174000",
          "schema_id": "987fcdeb-51a2-43d1-b456-426614174000",
          "config": {
            "model": "gemini-2.5-flash",
            "per_key_attribution": true,
            "temperature": 0.1,
            "enable_thinking": true
            "additional_instructions": "Extract information only about company X. Do not include information about company Y."
          }
        }
        ```

        Example Response:
        ```json
        {
          "job_id": "456e7890-e89b-12d3-a456-426614174000",
          "status": "pending",
          "created_at": "2025-01-11T18:35:00Z",
          "estimated_completion": "2025-01-11T18:40:00Z"
        }
        ```

        Error Handling:

        Document and schema validation occurs before job creation for both streaming and non-streaming paths:

        - `400`: Bad Request (invalid `document_id` or `schema_id` format)
        - `404`: Not Found (document or schema not found)
        - `422`: Unprocessable Entity (invalid schema definition)
        - `429`: Too Many Requests (user has exceeded concurrency limit of 5 active jobs)
        - `500`: Internal Server Error (processing error)

        Args:
          document_id: ID of the document to extract from

          schema_id: ID of the schema to use for extraction

          config: Configuration options for the extraction process

          stream: Whether to stream the results as they become available. If true, the response will be a stream of JSON objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract/jobs",
            body=maybe_transform(
                {
                    "document_id": document_id,
                    "schema_id": schema_id,
                    "config": config,
                    "stream": stream,
                },
                extract_create_job_params.ExtractCreateJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateJobResponse,
        )

    def create_schema(
        self,
        *,
        name: str,
        schema_definition: Dict[str, object],
        description: object | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateSchemaResponse:
        """
        Create a new extraction schema.

        Creates a JSON Schema that defines the structure of data to extract from documents. The schema must conform to our supported subset of JSON Schema 2020-12 features.

        Supported Schema Features:

        Basic Types:

        1. `string`: Text data with optional constraints (`minLength`, `maxLength`, `pattern`, `enum`)
        2. `integer`: Whole numbers with optional constraints (`minimum`, `maximum`, `enum`)
        3. `number`: Decimal numbers with optional constraints (`minimum`, `maximum`, `enum`)
        4. `boolean`: True/false values
        5. `null`: Null values (often used with `anyOf` for optional fields)

        Complex Types:

        1. `object`: Key-value pairs with defined properties
        2. `array`: Lists of items with defined item schemas
        3. `anyOf`: Union types (e.g., string or null for optional fields)

        String Formats:

        Supported formats: `date-time`, `time`, `date`, `duration`, `email`, `hostname`, `ipv4`, `ipv6`, `uuid`, `uri`

        Schema Structure:

        1. Root schema must be an `object` type
        2. Use `$defs` for reusable schema components
        3. Use `$ref` to reference definitions
        4. Arrays must have `items` schema defined

        Constraints:

        1. Maximum 10 leaf nodes per array (prevents overly complex schemas)
        2. No circular references in `$ref` definitions
        3. String formats must be from the supported list

        Example Schemas:

        Simple Company Schema:
        ```json
        {
          "type": "object",
          "properties": {
            "company_name": {
              "type": "string",
              "description": "The name of the company exactly as it appears in the document"
            },
            "form_type": {
              "type": "string",
              "enum": ["10-K", "10-Q", "8-K", "S-1"],
              "description": "The type of SEC form"
            },
            "trading_symbol": {
              "type": "string",
              "description": "The trading symbol of the company"
            },
            "zip_code": {
              "type": "integer",
              "description": "The zip code of the company headquarters"
            }
          },
          "required": ["company_name", "form_type", "trading_symbol", "zip_code"]
        }
        ```

        Complex Resume Schema:
        ```json
        {
          "type": "object",
          "properties": {
            "personalInfo": {
              "type": "object",
              "properties": {
                "fullName": {"type": "string"},
                "contact": {
                  "type": "object",
                  "properties": {
                    "emails": {
                      "type": "array",
                      "items": {"type": "string", "format": "email"}
                    },
                    "phones": {
                      "type": "array",
                      "items": {"type": "string"}
                    }
                  }
                }
              },
              "required": ["fullName"]
            },
            "workExperience": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "jobTitle": {"type": "string"},
                  "company": {"type": "string"},
                  "startDate": {"type": "string"},
                  "endDate": {"type": ["string", "null"]},
                  "isCurrent": {"type": "boolean"}
                },
                "required": ["jobTitle", "company", "startDate"]
              }
            }
          },
          "required": ["personalInfo", "workExperience"]
        }
        ```

        Schema with References:
        ```json
        {
          "type": "object",
          "properties": {
            "algorithms": {
              "type": "array",
              "items": {"$ref": "#/$defs/algorithm"}
            }
          },
          "$defs": {
            "algorithm": {
              "type": "object",
              "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"}
              },
              "required": ["name"]
            }
          }
        }
        ```

        Best Practices:

        1. Use descriptive field names that clearly indicate what data should be extracted
        2. Add detailed descriptions to help the AI understand what to extract
        3. Use `enum` for known values (e.g., form types, status values)
        4. Make fields optional by using `anyOf` with `null` or omitting from `required`
        5. Use arrays for lists of similar items (e.g., work experience, education)
        6. Keep schemas focused - avoid overly complex nested structures
        7. Test with sample documents to ensure the schema captures the expected data

        Args:
          name: Name of the schema

          description: Description of the schema

          schema_definition: JSON Schema definition. Must be a valid JSON Schema that defines the structure of data to extract from documents. See the comprehensive schema guide in the API documentation for detailed examples and supported features.

          metadata: Additional metadata for the schema

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract/schemas",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "schema_definition": schema_definition,
                    "metadata": metadata,
                },
                extract_create_schema_params.ExtractCreateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateSchemaResponse,
        )

    def update_job_results(
        self,
        job_id: str,
        *,
        results: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update the results of a completed extraction job.

        Args:
          results: Extracted results conforming to the provided JSON Schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._put(
            f"/extract/jobs/{job_id}/results",
            body=maybe_transform(
                {
                    "results": results,
                },
                extract_update_job_results_params.ExtractUpdateJobResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_schema(
        self,
        schema_id: str,
        *,
        name: object | Omit = omit,
        description: object | Omit = omit,
        schema_definition: object | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractUpdateSchemaResponse:
        """
        Update an existing schema.

        Args:
          name: Name of the schema

          description: Description of the schema

          schema_definition: JSON schema definition

          metadata: Additional metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._put(
            f"/extract/schemas/{schema_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "schema_definition": schema_definition,
                    "metadata": metadata,
                },
                extract_update_schema_params.ExtractUpdateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractUpdateSchemaResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def delete_document(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractDeleteDocumentResponse:
        """
        Delete a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._delete(
            f"/extract/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractDeleteDocumentResponse,
        )

    async def delete_schema(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractDeleteSchemaResponse:
        """
        Delete a schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._delete(
            f"/extract/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractDeleteSchemaResponse,
        )

    async def list_documents(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        search: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractListDocumentsResponse:
        """
        List documents for structured extraction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/extract/documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "search": search,
                    },
                    extract_list_documents_params.ExtractListDocumentsParams,
                ),
            ),
            cast_to=ExtractListDocumentsResponse,
        )

    async def retrieve_document(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveDocumentResponse:
        """
        Get document information by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            f"/extract/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveDocumentResponse,
        )

    async def list_jobs(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        job_status: object | Omit = omit,
        search: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractListJobsResponse:
        """
        List extraction jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/extract/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "job_status": job_status,
                        "search": search,
                    },
                    extract_list_jobs_params.ExtractListJobsParams,
                ),
            ),
            cast_to=ExtractListJobsResponse,
        )

    async def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveJobResponse:
        """
        Get the status of an extraction job.

        For running jobs with a Temporal workflow, returns accumulated results and failed subtrees from workflow queries. For completed/failed jobs or jobs without workflow, these fields are empty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/extract/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveJobResponse,
        )

    async def retrieve_job_results(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveJobResultsResponse:
        """
        Get the results of a completed extraction job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/extract/jobs/{job_id}/results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveJobResultsResponse,
        )

    async def list_schemas(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        search: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractListSchemasResponse:
        """
        List schemas with optional search.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/extract/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "search": search,
                    },
                    extract_list_schemas_params.ExtractListSchemasParams,
                ),
            ),
            cast_to=ExtractListSchemasResponse,
        )

    async def retrieve_schema(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRetrieveSchemaResponse:
        """
        Get schema information by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._get(
            f"/extract/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRetrieveSchemaResponse,
        )

    async def upload_document(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractUploadDocumentResponse:
        """
        Upload a document for structured extraction.

        Uploads a PDF document that can be used for structured data extraction. Only PDF files are supported.

        Supported File Types:

        1. PDF files only (`.pdf` extension)
        2. Maximum file size: 50MB (recommended)
        3. Documents are processed and validated upon upload

        Document Processing:

        1. File size and page count are automatically calculated
        2. Document is validated for PDF format and readability
        3. Metadata is extracted and stored for future reference
        4. Document is stored securely and can be referenced by ID

        Usage:

        After uploading, you'll receive a `document_id` that can be used with:

        1. `POST /jobs` endpoint to start extraction jobs
        2. `GET /documents/{document_id}` to retrieve document information
        3. `DELETE /documents/{document_id}` to remove the document

        Example Response:
        ```json
        {
          "document_id": "123e4567-e89b-12d3-a456-426614174000",
          "file_name": "financial_report.pdf",
          "file_size": 2048576,
          "page_count": 45,
          "uploaded_at": "2025-01-11T18:35:00Z",
          "status": "uploaded"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/extract/documents/upload",
            body=await async_maybe_transform(body, extract_upload_document_params.ExtractUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractUploadDocumentResponse,
        )

    async def create_job(
        self,
        *,
        document_id: str,
        schema_id: str,
        config: object | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateJobResponse:
        """
        Start a new structured extraction job.

        Extracts structured data from a PDF document using AI models based on a JSON Schema. The `document_id` and `schema_id` must be valid UUIDs of previously uploaded documents and created schemas.

        How It Works:

        1. Document Processing: The system analyzes the PDF document and splits it into manageable sections
        2. Schema Analysis: Your JSON schema is parsed and validated for supported features
        3. Extraction: The pipeline processes each section and extracts data according to your schema
        4. Validation: Extracted data is validated against your schema to ensure constraints and requirements are met
        5. Results: Structured data is returned in the format defined by your schema

        Supported Models:

        1. `gemini-2.5-flash`: Fast, cost-effective model for most use cases (default)
        2. `gemini-2.5-pro`: More powerful model for complex extractions

        Configuration Options:

        Basic Settings:

        1. `model`: AI model to use for extraction
        2. `max_num_concurrent_requests`: Number of parallel processing requests (1-20)
        3. `validate_response_schema`: Whether to validate extracted data against schema

        Advanced Settings:

        1. `per_key_attribution`: Enable detailed reasoning and confidence scores for each field
        2. `temperature`: Control randomness in AI responses (0.0-2.0)
        3. `seed`: Set random seed for reproducible results
        4. `enable_thinking`: Show AI reasoning process
        5. `n_max_retries`: Maximum retry attempts for failed requests

        Streaming Mode (`stream=true`):

        When `stream=true`, the endpoint returns an SSE stream instead of a job ID. Results are streamed as subtrees complete, enabling real-time progress visibility in the frontend.

        - Response: SSE stream (`text/event-stream`) with events: `start`, `subtree_result`, `subtree_error`, `agentic_array_progress`
        - Job records are still created and results persisted (retrievable via `GET /jobs/{job_id}`)
        - Always durable: Uses Temporal workflow—job continues running even if client disconnects
        - Automatic retries: Temporal handles activity failures and retries automatically
        - Use case: Interactive frontend UI where users want real-time extraction progress

        SSE Event Types:

        1. `start`: Emitted once with `job_id`, `total_subtrees`, and `start_time`
        2. `subtree_result`: Emitted per successful subtree with `extracted_result`, `attributions`, `usage_metadata`
        3. `subtree_error`: Emitted per failed subtree with `error_message` and `error_type`

        See `STREAMING-DESIGN.md` for full protocol specification.

        Job Lifecycle:

        1. `pending`: Job is queued and waiting to start
        2. `processing`: AI is actively extracting data from the document
        3. `completed`: Extraction finished successfully with results
        4. `failed`: Extraction failed due to an error
        5. `cancelled`: Job was cancelled before completion

        Monitoring Progress:

        Use the `GET /jobs/{job_id}` endpoint to check job status and progress:

        1. `completion_percentage`: Overall progress (0-100)
        2. `current_step`: Current processing stage
        3. `fields_processed`: Number of schema fields completed
        4. `total_fields`: Total number of schema fields to process

        Getting Results:

        Once a job is completed, use `GET /jobs/{job_id}/results` to retrieve:

        1. `results`: Extracted data conforming to your schema
        2. `metadata`: Processing information, costs, and performance metrics
        3. `attributions`: (if enabled) Reasoning and confidence scores for each field

        Example Request:
        ```json
        {
          "document_id": "123e4567-e89b-12d3-a456-426614174000",
          "schema_id": "987fcdeb-51a2-43d1-b456-426614174000",
          "config": {
            "model": "gemini-2.5-flash",
            "per_key_attribution": true,
            "temperature": 0.1,
            "enable_thinking": true
            "additional_instructions": "Extract information only about company X. Do not include information about company Y."
          }
        }
        ```

        Example Response:
        ```json
        {
          "job_id": "456e7890-e89b-12d3-a456-426614174000",
          "status": "pending",
          "created_at": "2025-01-11T18:35:00Z",
          "estimated_completion": "2025-01-11T18:40:00Z"
        }
        ```

        Error Handling:

        Document and schema validation occurs before job creation for both streaming and non-streaming paths:

        - `400`: Bad Request (invalid `document_id` or `schema_id` format)
        - `404`: Not Found (document or schema not found)
        - `422`: Unprocessable Entity (invalid schema definition)
        - `429`: Too Many Requests (user has exceeded concurrency limit of 5 active jobs)
        - `500`: Internal Server Error (processing error)

        Args:
          document_id: ID of the document to extract from

          schema_id: ID of the schema to use for extraction

          config: Configuration options for the extraction process

          stream: Whether to stream the results as they become available. If true, the response will be a stream of JSON objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract/jobs",
            body=await async_maybe_transform(
                {
                    "document_id": document_id,
                    "schema_id": schema_id,
                    "config": config,
                    "stream": stream,
                },
                extract_create_job_params.ExtractCreateJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateJobResponse,
        )

    async def create_schema(
        self,
        *,
        name: str,
        schema_definition: Dict[str, object],
        description: object | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateSchemaResponse:
        """
        Create a new extraction schema.

        Creates a JSON Schema that defines the structure of data to extract from documents. The schema must conform to our supported subset of JSON Schema 2020-12 features.

        Supported Schema Features:

        Basic Types:

        1. `string`: Text data with optional constraints (`minLength`, `maxLength`, `pattern`, `enum`)
        2. `integer`: Whole numbers with optional constraints (`minimum`, `maximum`, `enum`)
        3. `number`: Decimal numbers with optional constraints (`minimum`, `maximum`, `enum`)
        4. `boolean`: True/false values
        5. `null`: Null values (often used with `anyOf` for optional fields)

        Complex Types:

        1. `object`: Key-value pairs with defined properties
        2. `array`: Lists of items with defined item schemas
        3. `anyOf`: Union types (e.g., string or null for optional fields)

        String Formats:

        Supported formats: `date-time`, `time`, `date`, `duration`, `email`, `hostname`, `ipv4`, `ipv6`, `uuid`, `uri`

        Schema Structure:

        1. Root schema must be an `object` type
        2. Use `$defs` for reusable schema components
        3. Use `$ref` to reference definitions
        4. Arrays must have `items` schema defined

        Constraints:

        1. Maximum 10 leaf nodes per array (prevents overly complex schemas)
        2. No circular references in `$ref` definitions
        3. String formats must be from the supported list

        Example Schemas:

        Simple Company Schema:
        ```json
        {
          "type": "object",
          "properties": {
            "company_name": {
              "type": "string",
              "description": "The name of the company exactly as it appears in the document"
            },
            "form_type": {
              "type": "string",
              "enum": ["10-K", "10-Q", "8-K", "S-1"],
              "description": "The type of SEC form"
            },
            "trading_symbol": {
              "type": "string",
              "description": "The trading symbol of the company"
            },
            "zip_code": {
              "type": "integer",
              "description": "The zip code of the company headquarters"
            }
          },
          "required": ["company_name", "form_type", "trading_symbol", "zip_code"]
        }
        ```

        Complex Resume Schema:
        ```json
        {
          "type": "object",
          "properties": {
            "personalInfo": {
              "type": "object",
              "properties": {
                "fullName": {"type": "string"},
                "contact": {
                  "type": "object",
                  "properties": {
                    "emails": {
                      "type": "array",
                      "items": {"type": "string", "format": "email"}
                    },
                    "phones": {
                      "type": "array",
                      "items": {"type": "string"}
                    }
                  }
                }
              },
              "required": ["fullName"]
            },
            "workExperience": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "jobTitle": {"type": "string"},
                  "company": {"type": "string"},
                  "startDate": {"type": "string"},
                  "endDate": {"type": ["string", "null"]},
                  "isCurrent": {"type": "boolean"}
                },
                "required": ["jobTitle", "company", "startDate"]
              }
            }
          },
          "required": ["personalInfo", "workExperience"]
        }
        ```

        Schema with References:
        ```json
        {
          "type": "object",
          "properties": {
            "algorithms": {
              "type": "array",
              "items": {"$ref": "#/$defs/algorithm"}
            }
          },
          "$defs": {
            "algorithm": {
              "type": "object",
              "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"}
              },
              "required": ["name"]
            }
          }
        }
        ```

        Best Practices:

        1. Use descriptive field names that clearly indicate what data should be extracted
        2. Add detailed descriptions to help the AI understand what to extract
        3. Use `enum` for known values (e.g., form types, status values)
        4. Make fields optional by using `anyOf` with `null` or omitting from `required`
        5. Use arrays for lists of similar items (e.g., work experience, education)
        6. Keep schemas focused - avoid overly complex nested structures
        7. Test with sample documents to ensure the schema captures the expected data

        Args:
          name: Name of the schema

          description: Description of the schema

          schema_definition: JSON Schema definition. Must be a valid JSON Schema that defines the structure of data to extract from documents. See the comprehensive schema guide in the API documentation for detailed examples and supported features.

          metadata: Additional metadata for the schema

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract/schemas",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "schema_definition": schema_definition,
                    "metadata": metadata,
                },
                extract_create_schema_params.ExtractCreateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateSchemaResponse,
        )

    async def update_job_results(
        self,
        job_id: str,
        *,
        results: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update the results of a completed extraction job.

        Args:
          results: Extracted results conforming to the provided JSON Schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._put(
            f"/extract/jobs/{job_id}/results",
            body=await async_maybe_transform(
                {
                    "results": results,
                },
                extract_update_job_results_params.ExtractUpdateJobResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_schema(
        self,
        schema_id: str,
        *,
        name: object | Omit = omit,
        description: object | Omit = omit,
        schema_definition: object | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractUpdateSchemaResponse:
        """
        Update an existing schema.

        Args:
          name: Name of the schema

          description: Description of the schema

          schema_definition: JSON schema definition

          metadata: Additional metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._put(
            f"/extract/schemas/{schema_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "schema_definition": schema_definition,
                    "metadata": metadata,
                },
                extract_update_schema_params.ExtractUpdateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractUpdateSchemaResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.delete_document = to_raw_response_wrapper(
            extract.delete_document,
        )
        self.delete_schema = to_raw_response_wrapper(
            extract.delete_schema,
        )
        self.list_documents = to_raw_response_wrapper(
            extract.list_documents,
        )
        self.retrieve_document = to_raw_response_wrapper(
            extract.retrieve_document,
        )
        self.list_jobs = to_raw_response_wrapper(
            extract.list_jobs,
        )
        self.retrieve_job = to_raw_response_wrapper(
            extract.retrieve_job,
        )
        self.retrieve_job_results = to_raw_response_wrapper(
            extract.retrieve_job_results,
        )
        self.list_schemas = to_raw_response_wrapper(
            extract.list_schemas,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            extract.retrieve_schema,
        )
        self.upload_document = to_raw_response_wrapper(
            extract.upload_document,
        )
        self.create_job = to_raw_response_wrapper(
            extract.create_job,
        )
        self.create_schema = to_raw_response_wrapper(
            extract.create_schema,
        )
        self.update_job_results = to_raw_response_wrapper(
            extract.update_job_results,
        )
        self.update_schema = to_raw_response_wrapper(
            extract.update_schema,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.delete_document = async_to_raw_response_wrapper(
            extract.delete_document,
        )
        self.delete_schema = async_to_raw_response_wrapper(
            extract.delete_schema,
        )
        self.list_documents = async_to_raw_response_wrapper(
            extract.list_documents,
        )
        self.retrieve_document = async_to_raw_response_wrapper(
            extract.retrieve_document,
        )
        self.list_jobs = async_to_raw_response_wrapper(
            extract.list_jobs,
        )
        self.retrieve_job = async_to_raw_response_wrapper(
            extract.retrieve_job,
        )
        self.retrieve_job_results = async_to_raw_response_wrapper(
            extract.retrieve_job_results,
        )
        self.list_schemas = async_to_raw_response_wrapper(
            extract.list_schemas,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            extract.retrieve_schema,
        )
        self.upload_document = async_to_raw_response_wrapper(
            extract.upload_document,
        )
        self.create_job = async_to_raw_response_wrapper(
            extract.create_job,
        )
        self.create_schema = async_to_raw_response_wrapper(
            extract.create_schema,
        )
        self.update_job_results = async_to_raw_response_wrapper(
            extract.update_job_results,
        )
        self.update_schema = async_to_raw_response_wrapper(
            extract.update_schema,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.delete_document = to_streamed_response_wrapper(
            extract.delete_document,
        )
        self.delete_schema = to_streamed_response_wrapper(
            extract.delete_schema,
        )
        self.list_documents = to_streamed_response_wrapper(
            extract.list_documents,
        )
        self.retrieve_document = to_streamed_response_wrapper(
            extract.retrieve_document,
        )
        self.list_jobs = to_streamed_response_wrapper(
            extract.list_jobs,
        )
        self.retrieve_job = to_streamed_response_wrapper(
            extract.retrieve_job,
        )
        self.retrieve_job_results = to_streamed_response_wrapper(
            extract.retrieve_job_results,
        )
        self.list_schemas = to_streamed_response_wrapper(
            extract.list_schemas,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            extract.retrieve_schema,
        )
        self.upload_document = to_streamed_response_wrapper(
            extract.upload_document,
        )
        self.create_job = to_streamed_response_wrapper(
            extract.create_job,
        )
        self.create_schema = to_streamed_response_wrapper(
            extract.create_schema,
        )
        self.update_job_results = to_streamed_response_wrapper(
            extract.update_job_results,
        )
        self.update_schema = to_streamed_response_wrapper(
            extract.update_schema,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.delete_document = async_to_streamed_response_wrapper(
            extract.delete_document,
        )
        self.delete_schema = async_to_streamed_response_wrapper(
            extract.delete_schema,
        )
        self.list_documents = async_to_streamed_response_wrapper(
            extract.list_documents,
        )
        self.retrieve_document = async_to_streamed_response_wrapper(
            extract.retrieve_document,
        )
        self.list_jobs = async_to_streamed_response_wrapper(
            extract.list_jobs,
        )
        self.retrieve_job = async_to_streamed_response_wrapper(
            extract.retrieve_job,
        )
        self.retrieve_job_results = async_to_streamed_response_wrapper(
            extract.retrieve_job_results,
        )
        self.list_schemas = async_to_streamed_response_wrapper(
            extract.list_schemas,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            extract.retrieve_schema,
        )
        self.upload_document = async_to_streamed_response_wrapper(
            extract.upload_document,
        )
        self.create_job = async_to_streamed_response_wrapper(
            extract.create_job,
        )
        self.create_schema = async_to_streamed_response_wrapper(
            extract.create_schema,
        )
        self.update_job_results = async_to_streamed_response_wrapper(
            extract.update_job_results,
        )
        self.update_schema = async_to_streamed_response_wrapper(
            extract.update_schema,
        )
