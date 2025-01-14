# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
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
from ....types.agents.query import retrieval_info_params
from ....types.agents.query.retrieval_info_response import RetrievalInfoResponse

__all__ = ["RetrievalResource", "AsyncRetrievalResource"]


class RetrievalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return RetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return RetrievalResourceWithStreamingResponse(self)

    def info(
        self,
        message_id: str,
        *,
        agent_id: str,
        content_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrievalInfoResponse:
        """
        Return content metadata of the contents used to generate response for a given
        message.

        Args:
          agent_id: Agent ID of the agent which sent the provided message.

          message_id: Message ID for which the content metadata needs to be retrieved.

          content_ids: List of content ids for which to get the metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/agents/{agent_id}/query/{message_id}/retrieval/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"content_ids": content_ids}, retrieval_info_params.RetrievalInfoParams),
            ),
            cast_to=RetrievalInfoResponse,
        )


class AsyncRetrievalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncRetrievalResourceWithStreamingResponse(self)

    async def info(
        self,
        message_id: str,
        *,
        agent_id: str,
        content_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrievalInfoResponse:
        """
        Return content metadata of the contents used to generate response for a given
        message.

        Args:
          agent_id: Agent ID of the agent which sent the provided message.

          message_id: Message ID for which the content metadata needs to be retrieved.

          content_ids: List of content ids for which to get the metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/agents/{agent_id}/query/{message_id}/retrieval/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"content_ids": content_ids}, retrieval_info_params.RetrievalInfoParams
                ),
            ),
            cast_to=RetrievalInfoResponse,
        )


class RetrievalResourceWithRawResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.info = to_raw_response_wrapper(
            retrieval.info,
        )


class AsyncRetrievalResourceWithRawResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.info = async_to_raw_response_wrapper(
            retrieval.info,
        )


class RetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.info = to_streamed_response_wrapper(
            retrieval.info,
        )


class AsyncRetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.info = async_to_streamed_response_wrapper(
            retrieval.info,
        )
