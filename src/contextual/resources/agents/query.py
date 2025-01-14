# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ..._base_client import make_request_options
from ...types.agents import (
    query_create_params,
    query_metrics_params,
    query_feedback_params,
    query_retrieval_info_params,
)
from ...types.agents.query_response import QueryResponse
from ...types.agents.query_metrics_response import QueryMetricsResponse
from ...types.agents.retrieval_info_response import RetrievalInfoResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return QueryResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        messages: Iterable[query_create_params.Message],
        retrievals_only: bool | NotGiven = NOT_GIVEN,
        conversation_id: str | NotGiven = NOT_GIVEN,
        model_id: str | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryResponse:
        """
        Start a conversation with an `Agent` and receive its generated response, along
        with relevant retrieved data and attributions.

        Args:
          agent_id: Agent ID of the agent to query

          messages: Message objects in the conversation

          retrievals_only: Set to `true` to skip generation of the response.

          conversation_id: Conversation ID. An optional alternative to providing message history in the
              `messages` field. If provided, history in the `messages` field will be ignored.

          model_id: Model ID of the specific fine-tuned or aligned model to use. Defaults to base
              model if not specified.

          stream: Set to `true` to receive a streamed response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/query",
            body=maybe_transform(
                {
                    "messages": messages,
                    "conversation_id": conversation_id,
                    "model_id": model_id,
                    "stream": stream,
                },
                query_create_params.QueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"retrievals_only": retrievals_only}, query_create_params.QueryCreateParams),
            ),
            cast_to=QueryResponse,
        )

    def feedback(
        self,
        agent_id: str,
        *,
        feedback: Literal["thumbs_up", "thumbs_down", "flagged", "removed"],
        message_id: str,
        content_id: str | NotGiven = NOT_GIVEN,
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Provide feedback for a generation or a retrieval.

        Feedback can be used to track
        overall `Agent` performance through the `Feedback` page in the Contextual UI,
        and as a basis for model fine-tuning.

        If providing feedback on a retrieval, include the `message_id` from the `/query`
        response, and a `content_id` returned in the query's `retrieval_contents` list.

        For feedback on generations, include `message_id` and do not include a
        `content_id`.

        Args:
          agent_id: Agent ID of the agent to provide feedback for

          feedback: Feedback to provide on the message. Set to "removed" to undo previously provided
              feedback.

          message_id: ID of the message to provide feedback on.

          content_id: Content ID to provide feedback on, if feedback is on retrieval. Set to None for
              generation feedback.

          explanation: Optional explanation for the feedback.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/feedback",
            body=maybe_transform(
                {
                    "feedback": feedback,
                    "message_id": message_id,
                    "content_id": content_id,
                    "explanation": explanation,
                },
                query_feedback_params.QueryFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def metrics(
        self,
        agent_id: str,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryMetricsResponse:
        """
        Get feedbacks a given agent.

        Args:
          agent_id: Agent ID of the agent to get metrics for

          created_after: Filters messages that are created before specified timestamp.

          created_before: Filters messages that are created after specified timestamp.

          limit: Limits the number of messages to return.

          offset: Offset for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "limit": limit,
                        "offset": offset,
                    },
                    query_metrics_params.QueryMetricsParams,
                ),
            ),
            cast_to=QueryMetricsResponse,
        )

    def retrieval_info(
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
                query=maybe_transform(
                    {"content_ids": content_ids}, query_retrieval_info_params.QueryRetrievalInfoParams
                ),
            ),
            cast_to=RetrievalInfoResponse,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncQueryResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        messages: Iterable[query_create_params.Message],
        retrievals_only: bool | NotGiven = NOT_GIVEN,
        conversation_id: str | NotGiven = NOT_GIVEN,
        model_id: str | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryResponse:
        """
        Start a conversation with an `Agent` and receive its generated response, along
        with relevant retrieved data and attributions.

        Args:
          agent_id: Agent ID of the agent to query

          messages: Message objects in the conversation

          retrievals_only: Set to `true` to skip generation of the response.

          conversation_id: Conversation ID. An optional alternative to providing message history in the
              `messages` field. If provided, history in the `messages` field will be ignored.

          model_id: Model ID of the specific fine-tuned or aligned model to use. Defaults to base
              model if not specified.

          stream: Set to `true` to receive a streamed response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/query",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "conversation_id": conversation_id,
                    "model_id": model_id,
                    "stream": stream,
                },
                query_create_params.QueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"retrievals_only": retrievals_only}, query_create_params.QueryCreateParams
                ),
            ),
            cast_to=QueryResponse,
        )

    async def feedback(
        self,
        agent_id: str,
        *,
        feedback: Literal["thumbs_up", "thumbs_down", "flagged", "removed"],
        message_id: str,
        content_id: str | NotGiven = NOT_GIVEN,
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Provide feedback for a generation or a retrieval.

        Feedback can be used to track
        overall `Agent` performance through the `Feedback` page in the Contextual UI,
        and as a basis for model fine-tuning.

        If providing feedback on a retrieval, include the `message_id` from the `/query`
        response, and a `content_id` returned in the query's `retrieval_contents` list.

        For feedback on generations, include `message_id` and do not include a
        `content_id`.

        Args:
          agent_id: Agent ID of the agent to provide feedback for

          feedback: Feedback to provide on the message. Set to "removed" to undo previously provided
              feedback.

          message_id: ID of the message to provide feedback on.

          content_id: Content ID to provide feedback on, if feedback is on retrieval. Set to None for
              generation feedback.

          explanation: Optional explanation for the feedback.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/feedback",
            body=await async_maybe_transform(
                {
                    "feedback": feedback,
                    "message_id": message_id,
                    "content_id": content_id,
                    "explanation": explanation,
                },
                query_feedback_params.QueryFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def metrics(
        self,
        agent_id: str,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryMetricsResponse:
        """
        Get feedbacks a given agent.

        Args:
          agent_id: Agent ID of the agent to get metrics for

          created_after: Filters messages that are created before specified timestamp.

          created_before: Filters messages that are created after specified timestamp.

          limit: Limits the number of messages to return.

          offset: Offset for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "limit": limit,
                        "offset": offset,
                    },
                    query_metrics_params.QueryMetricsParams,
                ),
            ),
            cast_to=QueryMetricsResponse,
        )

    async def retrieval_info(
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
                    {"content_ids": content_ids}, query_retrieval_info_params.QueryRetrievalInfoParams
                ),
            ),
            cast_to=RetrievalInfoResponse,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.create = to_raw_response_wrapper(
            query.create,
        )
        self.feedback = to_raw_response_wrapper(
            query.feedback,
        )
        self.metrics = to_raw_response_wrapper(
            query.metrics,
        )
        self.retrieval_info = to_raw_response_wrapper(
            query.retrieval_info,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.create = async_to_raw_response_wrapper(
            query.create,
        )
        self.feedback = async_to_raw_response_wrapper(
            query.feedback,
        )
        self.metrics = async_to_raw_response_wrapper(
            query.metrics,
        )
        self.retrieval_info = async_to_raw_response_wrapper(
            query.retrieval_info,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.create = to_streamed_response_wrapper(
            query.create,
        )
        self.feedback = to_streamed_response_wrapper(
            query.feedback,
        )
        self.metrics = to_streamed_response_wrapper(
            query.metrics,
        )
        self.retrieval_info = to_streamed_response_wrapper(
            query.retrieval_info,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.create = async_to_streamed_response_wrapper(
            query.create,
        )
        self.feedback = async_to_streamed_response_wrapper(
            query.feedback,
        )
        self.metrics = async_to_streamed_response_wrapper(
            query.metrics,
        )
        self.retrieval_info = async_to_streamed_response_wrapper(
            query.retrieval_info,
        )
