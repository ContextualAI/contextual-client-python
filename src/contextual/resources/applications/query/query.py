# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
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
from ....types.applications import query_start_params, query_feedback_params, query_form_filling_params
from ....types.applications.query_response import QueryResponse
from ....types.applications.query_form_filling_response import QueryFormFillingResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

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

    def feedback(
        self,
        application_id: str,
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
        overall `Application` performance through the `Feedback` page in the Contextual
        UI, and as a basis for model fine-tuning.

        If providing feedback on a retrieval, include the `message_id` from the `/query`
        response, and a `content_id` returned in the query's `retrieval_contents` list.

        For feedback on generations, include `message_id` and do not include a
        `content_id`.

        Args:
          application_id: Application ID of the application to provide feedback for

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            f"/applications/{application_id}/feedback",
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

    def form_filling(
        self,
        application_id: str,
        *,
        queries: Iterable[query_form_filling_params.Query],
        scope_metadata: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryFormFillingResponse:
        """
        Start a conversation with an application and receive its generated response and
        attributions.

        Args:
          application_id: Application ID of the application to query

          queries: Queries used to fill the form

          scope_metadata: Scope of the form filling. This is the metadata that is used to determine the
              form filling strategy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            f"/applications/{application_id}/form_filling",
            body=maybe_transform(
                {
                    "queries": queries,
                    "scope_metadata": scope_metadata,
                },
                query_form_filling_params.QueryFormFillingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryFormFillingResponse,
        )

    def start(
        self,
        application_id: str,
        *,
        messages: Iterable[query_start_params.Message],
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
        Start a conversation with an `Application` and receive its generated response,
        along with relevant retrieved data and attributions.

        Args:
          application_id: Application ID of the application to query

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            f"/applications/{application_id}/query",
            body=maybe_transform(
                {
                    "messages": messages,
                    "conversation_id": conversation_id,
                    "model_id": model_id,
                    "stream": stream,
                },
                query_start_params.QueryStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"retrievals_only": retrievals_only}, query_start_params.QueryStartParams),
            ),
            cast_to=QueryResponse,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

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

    async def feedback(
        self,
        application_id: str,
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
        overall `Application` performance through the `Feedback` page in the Contextual
        UI, and as a basis for model fine-tuning.

        If providing feedback on a retrieval, include the `message_id` from the `/query`
        response, and a `content_id` returned in the query's `retrieval_contents` list.

        For feedback on generations, include `message_id` and do not include a
        `content_id`.

        Args:
          application_id: Application ID of the application to provide feedback for

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            f"/applications/{application_id}/feedback",
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

    async def form_filling(
        self,
        application_id: str,
        *,
        queries: Iterable[query_form_filling_params.Query],
        scope_metadata: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryFormFillingResponse:
        """
        Start a conversation with an application and receive its generated response and
        attributions.

        Args:
          application_id: Application ID of the application to query

          queries: Queries used to fill the form

          scope_metadata: Scope of the form filling. This is the metadata that is used to determine the
              form filling strategy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            f"/applications/{application_id}/form_filling",
            body=await async_maybe_transform(
                {
                    "queries": queries,
                    "scope_metadata": scope_metadata,
                },
                query_form_filling_params.QueryFormFillingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryFormFillingResponse,
        )

    async def start(
        self,
        application_id: str,
        *,
        messages: Iterable[query_start_params.Message],
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
        Start a conversation with an `Application` and receive its generated response,
        along with relevant retrieved data and attributions.

        Args:
          application_id: Application ID of the application to query

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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            f"/applications/{application_id}/query",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "conversation_id": conversation_id,
                    "model_id": model_id,
                    "stream": stream,
                },
                query_start_params.QueryStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"retrievals_only": retrievals_only}, query_start_params.QueryStartParams
                ),
            ),
            cast_to=QueryResponse,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.feedback = to_raw_response_wrapper(
            query.feedback,
        )
        self.form_filling = to_raw_response_wrapper(
            query.form_filling,
        )
        self.start = to_raw_response_wrapper(
            query.start,
        )

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._query.metrics)


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.feedback = async_to_raw_response_wrapper(
            query.feedback,
        )
        self.form_filling = async_to_raw_response_wrapper(
            query.form_filling,
        )
        self.start = async_to_raw_response_wrapper(
            query.start,
        )

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._query.metrics)


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.feedback = to_streamed_response_wrapper(
            query.feedback,
        )
        self.form_filling = to_streamed_response_wrapper(
            query.form_filling,
        )
        self.start = to_streamed_response_wrapper(
            query.start,
        )

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._query.metrics)


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.feedback = async_to_streamed_response_wrapper(
            query.feedback,
        )
        self.form_filling = async_to_streamed_response_wrapper(
            query.form_filling,
        )
        self.start = async_to_streamed_response_wrapper(
            query.start,
        )

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._query.metrics)