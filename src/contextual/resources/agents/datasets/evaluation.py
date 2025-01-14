# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.datasets import (
    evaluation_list_params,
    evaluation_create_params,
    evaluation_update_params,
    evaluation_metadata_params,
    evaluation_retrieve_params,
)
from ....types.agents.dataset_response import DatasetResponse
from ....types.agents.list_datasets_response import ListDatasetsResponse
from ....types.agents.create_dataset_response import CreateDatasetResponse

__all__ = ["EvaluationResource", "AsyncEvaluationResource"]


class EvaluationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return EvaluationResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        dataset_name: str,
        dataset_type: Literal["evaluation_set"],
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatasetResponse:
        """
        Create a new evaluation `Dataset` for the specified `Agent` using the provided
        JSONL file. A `Dataset` is a versioned collection of samples conforming to a
        particular schema, and can be used to store `Evaluation` test-sets and retrieve
        `Evaluation` results.

        Each `Dataset` is versioned and validated against its schema during creation and
        subsequent updates. The provided `Dataset` file must conform to the schema
        defined for the `dataset_type`.

        File schema for `dataset_type` `evaluation_set` is a JSONL or CSV file where
        each line is one JSON object with the following keys:

        - `prompt` (required, `string`): Prompt or question

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional retrieved context for evaluation,
          as a list of string text chunks

        Args:
          agent_id: Agent ID to associate with the evaluation dataset

          dataset_name: Name of the evaluation dataset

          dataset_type: Type of evaluation dataset which determines its schema and validation rules.

          file: JSONL file containing the evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        body = deepcopy_minimal(
            {
                "dataset_name": dataset_name,
                "dataset_type": dataset_type,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/agents/{agent_id}/datasets/evaluation",
            body=maybe_transform(body, evaluation_create_params.EvaluationCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
        )

    def retrieve(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        batch_size: int | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Stream the raw content of an evaluation `Dataset` version.

        If no version is
        specified, the latest version is used.

        The `Dataset` content is downloaded in batches. Batch size can be configured to
        meet specific processing requirements.

        Returns a `StreamingResponse`, an asynchronous stream of `Dataset` content
        with: - Content-Type: application/octet-stream - Content-Disposition:
        attachment - Chunked transfer encoding

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to retrieve

          batch_size: Batch size for processing

          version: Version number of the evaluation dataset to retrieve. Defaults to the latest
              version if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batch_size": batch_size,
                        "version": version,
                    },
                    evaluation_retrieve_params.EvaluationRetrieveParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        dataset_type: Literal["evaluation_set"],
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatasetResponse:
        """
        Append to an existing evaluation `Dataset`.

        Create a new version of the dataset by appending content to the `Dataset` and
        validating against its schema.

        File schema for `dataset_type` `evaluation_set` is a JSONL file where each line
        is one JSON object with the following keys:

        - `prompt` (required, `string`): Prompt or question

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional retrieved context for evaluation,
          as a list of string text chunks

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to append to

          dataset_type: Type of evaluation dataset which determines its schema and validation rules.
              Must match the `dataset_type` used at dataset creation time.

          file: JSONL file containing the entries to append to the evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        body = deepcopy_minimal(
            {
                "dataset_type": dataset_type,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}",
            body=maybe_transform(body, evaluation_update_params.EvaluationUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        dataset_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDatasetsResponse:
        """
        List all evaluation `Datasets` and their versions belonging to a particular
        `Agent`.

        If a `dataset_name` filter is provided, all versions of that `Dataset` will be
        listed.

        Includes metadata and schema for each `Dataset` version.

        Args:
          agent_id: Agent ID for which to list associated evaluation datasets

          dataset_name: Optional dataset name to filter the results by. If provided, only versions from
              that dataset are listed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}/datasets/evaluation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_name": dataset_name}, evaluation_list_params.EvaluationListParams),
            ),
            cast_to=ListDatasetsResponse,
        )

    def delete(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete an evaluation `Dataset` and all its versions.

        Permanently removes the `Dataset`, including all associated metadata.

        This operation is irreversible.

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return self._delete(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def metadata(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetResponse:
        """
        Retrieve details of a specific evaluation `Dataset` version, or the latest
        version if no `version` is specified.

        Provides comprehensive information about the `Dataset`, including its metadata
        and schema.

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to retrieve details for

          version: Version number of the dataset. Defaults to the latest version if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return self._get(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, evaluation_metadata_params.EvaluationMetadataParams),
            ),
            cast_to=DatasetResponse,
        )


class AsyncEvaluationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncEvaluationResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        dataset_name: str,
        dataset_type: Literal["evaluation_set"],
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatasetResponse:
        """
        Create a new evaluation `Dataset` for the specified `Agent` using the provided
        JSONL file. A `Dataset` is a versioned collection of samples conforming to a
        particular schema, and can be used to store `Evaluation` test-sets and retrieve
        `Evaluation` results.

        Each `Dataset` is versioned and validated against its schema during creation and
        subsequent updates. The provided `Dataset` file must conform to the schema
        defined for the `dataset_type`.

        File schema for `dataset_type` `evaluation_set` is a JSONL or CSV file where
        each line is one JSON object with the following keys:

        - `prompt` (required, `string`): Prompt or question

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional retrieved context for evaluation,
          as a list of string text chunks

        Args:
          agent_id: Agent ID to associate with the evaluation dataset

          dataset_name: Name of the evaluation dataset

          dataset_type: Type of evaluation dataset which determines its schema and validation rules.

          file: JSONL file containing the evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        body = deepcopy_minimal(
            {
                "dataset_name": dataset_name,
                "dataset_type": dataset_type,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/agents/{agent_id}/datasets/evaluation",
            body=await async_maybe_transform(body, evaluation_create_params.EvaluationCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
        )

    async def retrieve(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        batch_size: int | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Stream the raw content of an evaluation `Dataset` version.

        If no version is
        specified, the latest version is used.

        The `Dataset` content is downloaded in batches. Batch size can be configured to
        meet specific processing requirements.

        Returns a `StreamingResponse`, an asynchronous stream of `Dataset` content
        with: - Content-Type: application/octet-stream - Content-Disposition:
        attachment - Chunked transfer encoding

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to retrieve

          batch_size: Batch size for processing

          version: Version number of the evaluation dataset to retrieve. Defaults to the latest
              version if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batch_size": batch_size,
                        "version": version,
                    },
                    evaluation_retrieve_params.EvaluationRetrieveParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        dataset_type: Literal["evaluation_set"],
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatasetResponse:
        """
        Append to an existing evaluation `Dataset`.

        Create a new version of the dataset by appending content to the `Dataset` and
        validating against its schema.

        File schema for `dataset_type` `evaluation_set` is a JSONL file where each line
        is one JSON object with the following keys:

        - `prompt` (required, `string`): Prompt or question

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional retrieved context for evaluation,
          as a list of string text chunks

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to append to

          dataset_type: Type of evaluation dataset which determines its schema and validation rules.
              Must match the `dataset_type` used at dataset creation time.

          file: JSONL file containing the entries to append to the evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        body = deepcopy_minimal(
            {
                "dataset_type": dataset_type,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}",
            body=await async_maybe_transform(body, evaluation_update_params.EvaluationUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        dataset_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDatasetsResponse:
        """
        List all evaluation `Datasets` and their versions belonging to a particular
        `Agent`.

        If a `dataset_name` filter is provided, all versions of that `Dataset` will be
        listed.

        Includes metadata and schema for each `Dataset` version.

        Args:
          agent_id: Agent ID for which to list associated evaluation datasets

          dataset_name: Optional dataset name to filter the results by. If provided, only versions from
              that dataset are listed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}/datasets/evaluation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name}, evaluation_list_params.EvaluationListParams
                ),
            ),
            cast_to=ListDatasetsResponse,
        )

    async def delete(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete an evaluation `Dataset` and all its versions.

        Permanently removes the `Dataset`, including all associated metadata.

        This operation is irreversible.

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return await self._delete(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def metadata(
        self,
        dataset_name: str,
        *,
        agent_id: str,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetResponse:
        """
        Retrieve details of a specific evaluation `Dataset` version, or the latest
        version if no `version` is specified.

        Provides comprehensive information about the `Dataset`, including its metadata
        and schema.

        Args:
          agent_id: Agent ID associated with the evaluation dataset

          dataset_name: Name of the evaluation dataset to retrieve details for

          version: Version number of the dataset. Defaults to the latest version if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return await self._get(
            f"/agents/{agent_id}/datasets/evaluation/{dataset_name}/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, evaluation_metadata_params.EvaluationMetadataParams
                ),
            ),
            cast_to=DatasetResponse,
        )


class EvaluationResourceWithRawResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = to_raw_response_wrapper(
            evaluation.create,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            evaluation.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_raw_response_wrapper(
            evaluation.update,
        )
        self.list = to_raw_response_wrapper(
            evaluation.list,
        )
        self.delete = to_raw_response_wrapper(
            evaluation.delete,
        )
        self.metadata = to_raw_response_wrapper(
            evaluation.metadata,
        )


class AsyncEvaluationResourceWithRawResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = async_to_raw_response_wrapper(
            evaluation.create,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            evaluation.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_raw_response_wrapper(
            evaluation.update,
        )
        self.list = async_to_raw_response_wrapper(
            evaluation.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evaluation.delete,
        )
        self.metadata = async_to_raw_response_wrapper(
            evaluation.metadata,
        )


class EvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = to_streamed_response_wrapper(
            evaluation.create,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            evaluation.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_streamed_response_wrapper(
            evaluation.update,
        )
        self.list = to_streamed_response_wrapper(
            evaluation.list,
        )
        self.delete = to_streamed_response_wrapper(
            evaluation.delete,
        )
        self.metadata = to_streamed_response_wrapper(
            evaluation.metadata,
        )


class AsyncEvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.create = async_to_streamed_response_wrapper(
            evaluation.create,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            evaluation.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_streamed_response_wrapper(
            evaluation.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluation.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evaluation.delete,
        )
        self.metadata = async_to_streamed_response_wrapper(
            evaluation.metadata,
        )
