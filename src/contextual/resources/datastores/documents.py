# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDocumentsPage, AsyncDocumentsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.datastores import document_list_params, document_create_params
from ...types.datastores.ingestion_response import IngestionResponse
from ...types.datastores.document_description import DocumentDescription

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        datastore_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IngestionResponse:
        """Ingest a document into a given `Datastore`.

        Ingestion is an asynchronous task.

        Returns a document `id` which can be used to
        track the status of the ingestion job through calls to the
        `GET /datastores/{datastore_id}/documents/{document_id}/metadata` API.

        This `id` can also be used to delete the document through the
        `DELETE /datastores/{datastore_id}/documents/{document_id}` API.

        `file` must be a PDF or HTML file.

        Args:
          datastore_id: Datastore ID of the datastore in which to ingest the document

          file: File to ingest

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/datastores/{datastore_id}/documents",
            body=maybe_transform(body, document_create_params.DocumentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestionResponse,
        )

    def retrieve(
        self,
        document_id: str,
        *,
        datastore_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentDescription:
        """
        Get details of a given document, including its `name` and ingestion job
        `status`.

        Args:
          datastore_id: Datastore ID of the datastore from which to retrieve the document

          document_id: Document ID of the document to retrieve details for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            f"/datastores/{datastore_id}/documents/{document_id}/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDescription,
        )

    def list(
        self,
        datastore_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        ingestion_job_status: List[Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]]
        | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        uploaded_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        uploaded_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDocumentsPage[DocumentDescription]:
        """
        Get list of documents in a given `Datastore`, including document `id`, `name`,
        and ingestion job `status`.

        Performs `cursor`-based pagination if the number of documents exceeds the
        requested `limit`. The returned `cursor` can be passed to the next
        `GET /datastores/{datastore_id}/documents` call to retrieve the next set of
        documents.

        Args:
          datastore_id: Datastore ID of the datastore to retrieve documents for

          cursor: Cursor from the previous call to list documents, used to retrieve the next set
              of results

          ingestion_job_status: Filters documents whose ingestion job status matches (one of) the provided
              status(es).

          limit: Maximum number of documents to return

          uploaded_after: Filters documents uploaded at or after specified timestamp.

          uploaded_before: Filters documents uploaded at or before specified timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        return self._get_api_list(
            f"/datastores/{datastore_id}/documents",
            page=SyncDocumentsPage[DocumentDescription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ingestion_job_status": ingestion_job_status,
                        "limit": limit,
                        "uploaded_after": uploaded_after,
                        "uploaded_before": uploaded_before,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=DocumentDescription,
        )

    def delete(
        self,
        document_id: str,
        *,
        datastore_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given document from its `Datastore`.

        This operation is irreversible.

        Args:
          datastore_id: Datastore ID of the datastore from which to delete the document

          document_id: Document ID of the document to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._delete(
            f"/datastores/{datastore_id}/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        datastore_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IngestionResponse:
        """Ingest a document into a given `Datastore`.

        Ingestion is an asynchronous task.

        Returns a document `id` which can be used to
        track the status of the ingestion job through calls to the
        `GET /datastores/{datastore_id}/documents/{document_id}/metadata` API.

        This `id` can also be used to delete the document through the
        `DELETE /datastores/{datastore_id}/documents/{document_id}` API.

        `file` must be a PDF or HTML file.

        Args:
          datastore_id: Datastore ID of the datastore in which to ingest the document

          file: File to ingest

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/datastores/{datastore_id}/documents",
            body=await async_maybe_transform(body, document_create_params.DocumentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestionResponse,
        )

    async def retrieve(
        self,
        document_id: str,
        *,
        datastore_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentDescription:
        """
        Get details of a given document, including its `name` and ingestion job
        `status`.

        Args:
          datastore_id: Datastore ID of the datastore from which to retrieve the document

          document_id: Document ID of the document to retrieve details for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            f"/datastores/{datastore_id}/documents/{document_id}/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDescription,
        )

    def list(
        self,
        datastore_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        ingestion_job_status: List[Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]]
        | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        uploaded_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        uploaded_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DocumentDescription, AsyncDocumentsPage[DocumentDescription]]:
        """
        Get list of documents in a given `Datastore`, including document `id`, `name`,
        and ingestion job `status`.

        Performs `cursor`-based pagination if the number of documents exceeds the
        requested `limit`. The returned `cursor` can be passed to the next
        `GET /datastores/{datastore_id}/documents` call to retrieve the next set of
        documents.

        Args:
          datastore_id: Datastore ID of the datastore to retrieve documents for

          cursor: Cursor from the previous call to list documents, used to retrieve the next set
              of results

          ingestion_job_status: Filters documents whose ingestion job status matches (one of) the provided
              status(es).

          limit: Maximum number of documents to return

          uploaded_after: Filters documents uploaded at or after specified timestamp.

          uploaded_before: Filters documents uploaded at or before specified timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        return self._get_api_list(
            f"/datastores/{datastore_id}/documents",
            page=AsyncDocumentsPage[DocumentDescription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ingestion_job_status": ingestion_job_status,
                        "limit": limit,
                        "uploaded_after": uploaded_after,
                        "uploaded_before": uploaded_before,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=DocumentDescription,
        )

    async def delete(
        self,
        document_id: str,
        *,
        datastore_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given document from its `Datastore`.

        This operation is irreversible.

        Args:
          datastore_id: Datastore ID of the datastore from which to delete the document

          document_id: Document ID of the document to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._delete(
            f"/datastores/{datastore_id}/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_raw_response_wrapper(
            documents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            documents.list,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_raw_response_wrapper(
            documents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )