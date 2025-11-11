# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncContentsPage, AsyncContentsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.datastores import content_list_params, content_metadata_params
from ...types.datastores.content_list_response import ContentListResponse
from ...types.datastores.content_metadata_response import ContentMetadataResponse

__all__ = ["ContentsResource", "AsyncContentsResource"]


class ContentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return ContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return ContentsResourceWithStreamingResponse(self)

    def list(
        self,
        datastore_id: str,
        *,
        document_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncContentsPage[ContentListResponse]:
        """
        Get Document Contents

        Args:
          datastore_id: Datastore ID of the datastore from which to retrieve the document

          document_id: Document ID of the document to retrieve details for

          limit: The number of content ids to be returned

          offset: The offset to start retrieving content ids

          search: The query to search keywords for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        return self._get_api_list(
            f"/datastores/{datastore_id}/contents",
            page=SyncContentsPage[ContentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "document_id": document_id,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    content_list_params.ContentListParams,
                ),
            ),
            model=cast(Any, ContentListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def metadata(
        self,
        content_id: str,
        *,
        datastore_id: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentMetadataResponse:
        """
        Get Content Metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        if not content_id:
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return cast(
            ContentMetadataResponse,
            self._get(
                f"/datastores/{datastore_id}/contents/{content_id}/metadata",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"cursor": cursor}, content_metadata_params.ContentMetadataParams),
                ),
                cast_to=cast(
                    Any, ContentMetadataResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncContentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncContentsResourceWithStreamingResponse(self)

    def list(
        self,
        datastore_id: str,
        *,
        document_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContentListResponse, AsyncContentsPage[ContentListResponse]]:
        """
        Get Document Contents

        Args:
          datastore_id: Datastore ID of the datastore from which to retrieve the document

          document_id: Document ID of the document to retrieve details for

          limit: The number of content ids to be returned

          offset: The offset to start retrieving content ids

          search: The query to search keywords for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        return self._get_api_list(
            f"/datastores/{datastore_id}/contents",
            page=AsyncContentsPage[ContentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "document_id": document_id,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    content_list_params.ContentListParams,
                ),
            ),
            model=cast(Any, ContentListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def metadata(
        self,
        content_id: str,
        *,
        datastore_id: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentMetadataResponse:
        """
        Get Content Metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datastore_id:
            raise ValueError(f"Expected a non-empty value for `datastore_id` but received {datastore_id!r}")
        if not content_id:
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return cast(
            ContentMetadataResponse,
            await self._get(
                f"/datastores/{datastore_id}/contents/{content_id}/metadata",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"cursor": cursor}, content_metadata_params.ContentMetadataParams
                    ),
                ),
                cast_to=cast(
                    Any, ContentMetadataResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ContentsResourceWithRawResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.list = to_raw_response_wrapper(
            contents.list,
        )
        self.metadata = to_raw_response_wrapper(
            contents.metadata,
        )


class AsyncContentsResourceWithRawResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.list = async_to_raw_response_wrapper(
            contents.list,
        )
        self.metadata = async_to_raw_response_wrapper(
            contents.metadata,
        )


class ContentsResourceWithStreamingResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.list = to_streamed_response_wrapper(
            contents.list,
        )
        self.metadata = to_streamed_response_wrapper(
            contents.metadata,
        )


class AsyncContentsResourceWithStreamingResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.list = async_to_streamed_response_wrapper(
            contents.list,
        )
        self.metadata = async_to_streamed_response_wrapper(
            contents.metadata,
        )
