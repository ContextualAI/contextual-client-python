# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import datastore_list_params, datastore_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDatastoresListPagination, AsyncDatastoresListPagination
from ..._base_client import AsyncPaginator, make_request_options
from .documents.documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ...types.create_datastore_output import CreateDatastoreOutput
from ...types.datastore_list_response import DatastoreListResponse

__all__ = ["DatastoresResource", "AsyncDatastoresResource"]


class DatastoresResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatastoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return DatastoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatastoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return DatastoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatastoreOutput:
        """Create a new `Datastore`.

        A `Datastore` is a collection of documents.

        Documents can be ingested into and
        deleted from a `Datastore`.

        A `Datastore` can be linked to one or more `Applications` to provide data on
        which the `Application` can ground its answers. This linkage of `Datastore` to
        `Application` is done through the `Create Application` or `Edit Application`
        APIs.

        Args:
          name: Name of the datastore

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/datastores",
            body=maybe_transform({"name": name}, datastore_create_params.DatastoreCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatastoreOutput,
        )

    def list(
        self,
        *,
        application_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDatastoresListPagination[DatastoreListResponse]:
        """
        List all the `Datastores`.

        Performs `cursor`-based pagination if the number of `Datastores` exceeds the
        requested `limit`. The returned `cursor` can be passed to the next
        `GET /datastores` call to retrieve the next set of `Datastores`.

        Args:
          application_id: ID of the application used to filter datastores. If provided, only datastores
              linked to this application will be returned.

          cursor: Cursor from the previous call to list datastores, used to retrieve the next set
              of results

          limit: Maximum number of datastores to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/datastores",
            page=SyncDatastoresListPagination[DatastoreListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application_id": application_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    datastore_list_params.DatastoreListParams,
                ),
            ),
            model=DatastoreListResponse,
        )

    def delete(
        self,
        datastore_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given `Datastore`, including all the documents ingested into it.

        This
        operation is irreversible.

        Args:
          datastore_id: Datastore ID of the datastore to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        return self._delete(
            f"/datastores/{datastore_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDatastoresResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatastoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatastoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatastoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncDatastoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatastoreOutput:
        """Create a new `Datastore`.

        A `Datastore` is a collection of documents.

        Documents can be ingested into and
        deleted from a `Datastore`.

        A `Datastore` can be linked to one or more `Applications` to provide data on
        which the `Application` can ground its answers. This linkage of `Datastore` to
        `Application` is done through the `Create Application` or `Edit Application`
        APIs.

        Args:
          name: Name of the datastore

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/datastores",
            body=await async_maybe_transform({"name": name}, datastore_create_params.DatastoreCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatastoreOutput,
        )

    def list(
        self,
        *,
        application_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DatastoreListResponse, AsyncDatastoresListPagination[DatastoreListResponse]]:
        """
        List all the `Datastores`.

        Performs `cursor`-based pagination if the number of `Datastores` exceeds the
        requested `limit`. The returned `cursor` can be passed to the next
        `GET /datastores` call to retrieve the next set of `Datastores`.

        Args:
          application_id: ID of the application used to filter datastores. If provided, only datastores
              linked to this application will be returned.

          cursor: Cursor from the previous call to list datastores, used to retrieve the next set
              of results

          limit: Maximum number of datastores to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/datastores",
            page=AsyncDatastoresListPagination[DatastoreListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application_id": application_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    datastore_list_params.DatastoreListParams,
                ),
            ),
            model=DatastoreListResponse,
        )

    async def delete(
        self,
        datastore_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given `Datastore`, including all the documents ingested into it.

        This
        operation is irreversible.

        Args:
          datastore_id: Datastore ID of the datastore to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        return await self._delete(
            f"/datastores/{datastore_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DatastoresResourceWithRawResponse:
    def __init__(self, datastores: DatastoresResource) -> None:
        self._datastores = datastores

        self.create = to_raw_response_wrapper(
            datastores.create,
        )
        self.list = to_raw_response_wrapper(
            datastores.list,
        )
        self.delete = to_raw_response_wrapper(
            datastores.delete,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._datastores.metadata)

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._datastores.documents)


class AsyncDatastoresResourceWithRawResponse:
    def __init__(self, datastores: AsyncDatastoresResource) -> None:
        self._datastores = datastores

        self.create = async_to_raw_response_wrapper(
            datastores.create,
        )
        self.list = async_to_raw_response_wrapper(
            datastores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datastores.delete,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._datastores.metadata)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._datastores.documents)


class DatastoresResourceWithStreamingResponse:
    def __init__(self, datastores: DatastoresResource) -> None:
        self._datastores = datastores

        self.create = to_streamed_response_wrapper(
            datastores.create,
        )
        self.list = to_streamed_response_wrapper(
            datastores.list,
        )
        self.delete = to_streamed_response_wrapper(
            datastores.delete,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._datastores.metadata)

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._datastores.documents)


class AsyncDatastoresResourceWithStreamingResponse:
    def __init__(self, datastores: AsyncDatastoresResource) -> None:
        self._datastores = datastores

        self.create = async_to_streamed_response_wrapper(
            datastores.create,
        )
        self.list = async_to_streamed_response_wrapper(
            datastores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datastores.delete,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._datastores.metadata)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._datastores.documents)
