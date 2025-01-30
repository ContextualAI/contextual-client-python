# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import generate_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.generate_create_response import GenerateCreateResponse

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_extra_body: generate_create_params.ExtraBody,
        messages: Iterable[generate_create_params.Message],
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateCreateResponse:
        """
        Generate a response using Contextual's Grounded Language Model (GLM), an LLM
        engineered specifically to prioritize faithfulness to in-context retrievals over
        parametric knowledge to reduce hallucinations in Retrieval-Augmented Generation.

        The total request cannot exceed 6,100 tokens.

        Args:
          api_extra_body: Extra parameters to be passed to Contextual's GLM

          messages: List of messages in the conversation so far. The last message must be from the
              user.

          model: The version of the Contextual's GLM to use. Currently, we just have "v1".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generate",
            body=maybe_transform(
                {
                    "api_extra_body": api_extra_body,
                    "messages": messages,
                    "model": model,
                },
                generate_create_params.GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateCreateResponse,
        )


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_extra_body: generate_create_params.ExtraBody,
        messages: Iterable[generate_create_params.Message],
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateCreateResponse:
        """
        Generate a response using Contextual's Grounded Language Model (GLM), an LLM
        engineered specifically to prioritize faithfulness to in-context retrievals over
        parametric knowledge to reduce hallucinations in Retrieval-Augmented Generation.

        The total request cannot exceed 6,100 tokens.

        Args:
          api_extra_body: Extra parameters to be passed to Contextual's GLM

          messages: List of messages in the conversation so far. The last message must be from the
              user.

          model: The version of the Contextual's GLM to use. Currently, we just have "v1".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generate",
            body=await async_maybe_transform(
                {
                    "api_extra_body": api_extra_body,
                    "messages": messages,
                    "model": model,
                },
                generate_create_params.GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateCreateResponse,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.create = to_raw_response_wrapper(
            generate.create,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.create = async_to_raw_response_wrapper(
            generate.create,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.create = to_streamed_response_wrapper(
            generate.create,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.create = async_to_streamed_response_wrapper(
            generate.create,
        )
