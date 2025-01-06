# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
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
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.applications import (
    dataset_list_params,
    dataset_create_params,
    dataset_update_params,
    dataset_retrieve_params,
)
from ....types.applications.list_dataset_response import ListDatasetResponse
from ....types.applications.create_dataset_response import CreateDatasetResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        application_id: str,
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
        Create a new `Dataset` in the specified `Application` using the provided JSONL
        file. A `Dataset` is a versioned collection of samples conforming to a
        particular schema, and can be used to store `Evaluation` test-sets and retrieve
        `Evaluation` results.

        Each `Dataset` is versioned and validated against its schema during creation and
        subsequent updates. The provided `Dataset` file must conform to the schema
        defined for the `dataset_type`.

        File schema for `dataset_type` `evaluation_set` is a JSONL or CSV file where
        each line is one JSON object with the following keys:

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional context for evaluation

        Args:
          application_id: Application ID to associate with the dataset

          dataset_name: Name of the dataset

          dataset_type: Type of dataset which determines its schema and validation rules.

          file: JSONL file containing the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
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
            f"/applications/{application_id}/datasets",
            body=maybe_transform(body, dataset_create_params.DatasetCreateParams),
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
        application_id: str,
        batch_size: int | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Stream the raw content of a `Dataset` version.

        If no version is specified, the
        latest version is used.

        The `Dataset` content is downloaded in batches. Batch size can be configured to
        meet specific processing requirements.

        Returns a `StreamingResponse`, an asynchronous stream of `Dataset` content
        with: - Content-Type: application/octet-stream - Content-Disposition:
        attachment - Chunked transfer encoding

        Args:
          application_id: Application ID associated with the dataset

          dataset_name: Name of the dataset to retrieve

          batch_size: Batch size for processing

          version: Version number of the dataset to retrieve. Defaults to the latest version if not
              specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return self._get(
            f"/applications/{application_id}/datasets/{dataset_name}",
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
                    dataset_retrieve_params.DatasetRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    def update(
        self,
        dataset_name: str,
        *,
        application_id: str,
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
        Append to an existing `Dataset`.

        Create a new version by appending content to the `Dataset` and validating
        against its schema.

        File schema for `dataset_type` `evaluation_set` is a JSONL file where each line
        is one JSON object with the following keys:

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional context for evaluation

        Args:
          application_id: Application ID associated with the dataset

          dataset_name: Name of the dataset to append to

          dataset_type: Type of dataset which determines its schema and validation rules. Must match the
              `dataset_type` used at dataset creation time.

          file: JSONL file containing the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
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
            f"/applications/{application_id}/datasets/{dataset_name}",
            body=maybe_transform(body, dataset_update_params.DatasetUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
        )

    def list(
        self,
        application_id: str,
        *,
        dataset_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDatasetResponse:
        """
        List all `Datasets` and their versions belonging to a particular `Application`.

        If a `dataset_name` filter is provided, all versions of that `Dataset` will be
        listed.

        Includes metadata and schema for each `Dataset` version.

        Args:
          application_id: Application ID for which to list associated datasets

          dataset_name: Optional dataset name to filter the results by. If provided, only versions from
              that dataset are listed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get(
            f"/applications/{application_id}/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_name": dataset_name}, dataset_list_params.DatasetListParams),
            ),
            cast_to=ListDatasetResponse,
        )

    def delete(
        self,
        dataset_name: str,
        *,
        application_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a `Dataset` and all its versions.

        Permanently removes the `Dataset`, including all associated metadata.

        This operation is irreversible.

        Args:
          application_id: Application ID associated with the dataset

          dataset_name: Name of the dataset to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return self._delete(
            f"/applications/{application_id}/datasets/{dataset_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        application_id: str,
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
        Create a new `Dataset` in the specified `Application` using the provided JSONL
        file. A `Dataset` is a versioned collection of samples conforming to a
        particular schema, and can be used to store `Evaluation` test-sets and retrieve
        `Evaluation` results.

        Each `Dataset` is versioned and validated against its schema during creation and
        subsequent updates. The provided `Dataset` file must conform to the schema
        defined for the `dataset_type`.

        File schema for `dataset_type` `evaluation_set` is a JSONL or CSV file where
        each line is one JSON object with the following keys:

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional context for evaluation

        Args:
          application_id: Application ID to associate with the dataset

          dataset_name: Name of the dataset

          dataset_type: Type of dataset which determines its schema and validation rules.

          file: JSONL file containing the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
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
            f"/applications/{application_id}/datasets",
            body=await async_maybe_transform(body, dataset_create_params.DatasetCreateParams),
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
        application_id: str,
        batch_size: int | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Stream the raw content of a `Dataset` version.

        If no version is specified, the
        latest version is used.

        The `Dataset` content is downloaded in batches. Batch size can be configured to
        meet specific processing requirements.

        Returns a `StreamingResponse`, an asynchronous stream of `Dataset` content
        with: - Content-Type: application/octet-stream - Content-Disposition:
        attachment - Chunked transfer encoding

        Args:
          application_id: Application ID associated with the dataset

          dataset_name: Name of the dataset to retrieve

          batch_size: Batch size for processing

          version: Version number of the dataset to retrieve. Defaults to the latest version if not
              specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return await self._get(
            f"/applications/{application_id}/datasets/{dataset_name}",
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
                    dataset_retrieve_params.DatasetRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    async def update(
        self,
        dataset_name: str,
        *,
        application_id: str,
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
        Append to an existing `Dataset`.

        Create a new version by appending content to the `Dataset` and validating
        against its schema.

        File schema for `dataset_type` `evaluation_set` is a JSONL file where each line
        is one JSON object with the following keys:

        - `response` (optional, `string`): Optional response to evaluate

        - `reference` (required, `string`): Required reference or ground truth response

        - `guideline` (optional, `string`): Optional evaluation guidelines

        - `knowledge` (optional, `string`): Optional context for evaluation

        Args:
          application_id: Application ID associated with the dataset

          dataset_name: Name of the dataset to append to

          dataset_type: Type of dataset which determines its schema and validation rules. Must match the
              `dataset_type` used at dataset creation time.

          file: JSONL file containing the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
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
            f"/applications/{application_id}/datasets/{dataset_name}",
            body=await async_maybe_transform(body, dataset_update_params.DatasetUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
        )

    async def list(
        self,
        application_id: str,
        *,
        dataset_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDatasetResponse:
        """
        List all `Datasets` and their versions belonging to a particular `Application`.

        If a `dataset_name` filter is provided, all versions of that `Dataset` will be
        listed.

        Includes metadata and schema for each `Dataset` version.

        Args:
          application_id: Application ID for which to list associated datasets

          dataset_name: Optional dataset name to filter the results by. If provided, only versions from
              that dataset are listed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._get(
            f"/applications/{application_id}/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name}, dataset_list_params.DatasetListParams
                ),
            ),
            cast_to=ListDatasetResponse,
        )

    async def delete(
        self,
        dataset_name: str,
        *,
        application_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a `Dataset` and all its versions.

        Permanently removes the `Dataset`, including all associated metadata.

        This operation is irreversible.

        Args:
          application_id: Application ID associated with the dataset

          dataset_name: Name of the dataset to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not dataset_name:
            raise ValueError(f"Expected a non-empty value for `dataset_name` but received {dataset_name!r}")
        return await self._delete(
            f"/applications/{application_id}/datasets/{dataset_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            datasets.update,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._datasets.metadata)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            datasets.update,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._datasets.metadata)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._datasets.metadata)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._datasets.metadata)
