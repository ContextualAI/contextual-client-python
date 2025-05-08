# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..types import generate_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
        knowledge: List[str],
        messages: Iterable[generate_create_params.Message],
        model: str,
        avoid_commentary: bool | NotGiven = NOT_GIVEN,
        max_new_tokens: int | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
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
        parametric knowledge to reduce hallucinations in Retrieval-Augmented Generation
        and agentic use cases.

        The total request cannot exceed 32,000 tokens.

        See our
        [blog post](https://contextual.ai/blog/introducing-grounded-language-model/) and
        [code examples](https://colab.research.google.com/github/ContextualAI/examples/blob/main/03-standalone-api/02-generate/generate.ipynb).
        Email [glm-feedback@contextual.ai](mailto:glm-feedback@contextual.ai) with any
        feedback or questions.

        Args:
          knowledge: The knowledge sources the model can use when generating a response.

          messages: List of messages in the conversation so far. The last message must be from the
              user.

          model: The version of the Contextual's GLM to use. Currently, we just have "v1".

          avoid_commentary: Flag to indicate whether the model should avoid providing additional commentary
              in responses. Commentary is conversational in nature and does not contain
              verifiable claims; therefore, commentary is not strictly grounded in available
              context. However, commentary may provide useful context which improves the
              helpfulness of responses.

          max_new_tokens: The maximum number of tokens that the model can generate in the response.

          system_prompt: Instructions that the model follows when generating responses. Note that we do
              not guarantee that the model follows these instructions exactly.

          temperature: The sampling temperature, which affects the randomness in the response. Note
              that higher temperature values can reduce groundedness.

          top_p: A parameter for nucleus sampling, an alternative to temperature which also
              affects the randomness of the response. Note that higher top_p values can reduce
              groundedness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generate",
            body=maybe_transform(
                {
                    "knowledge": knowledge,
                    "messages": messages,
                    "model": model,
                    "avoid_commentary": avoid_commentary,
                    "max_new_tokens": max_new_tokens,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "top_p": top_p,
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
        knowledge: List[str],
        messages: Iterable[generate_create_params.Message],
        model: str,
        avoid_commentary: bool | NotGiven = NOT_GIVEN,
        max_new_tokens: int | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
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
        parametric knowledge to reduce hallucinations in Retrieval-Augmented Generation
        and agentic use cases.

        The total request cannot exceed 32,000 tokens.

        See our
        [blog post](https://contextual.ai/blog/introducing-grounded-language-model/) and
        [code examples](https://colab.research.google.com/github/ContextualAI/examples/blob/main/03-standalone-api/02-generate/generate.ipynb).
        Email [glm-feedback@contextual.ai](mailto:glm-feedback@contextual.ai) with any
        feedback or questions.

        Args:
          knowledge: The knowledge sources the model can use when generating a response.

          messages: List of messages in the conversation so far. The last message must be from the
              user.

          model: The version of the Contextual's GLM to use. Currently, we just have "v1".

          avoid_commentary: Flag to indicate whether the model should avoid providing additional commentary
              in responses. Commentary is conversational in nature and does not contain
              verifiable claims; therefore, commentary is not strictly grounded in available
              context. However, commentary may provide useful context which improves the
              helpfulness of responses.

          max_new_tokens: The maximum number of tokens that the model can generate in the response.

          system_prompt: Instructions that the model follows when generating responses. Note that we do
              not guarantee that the model follows these instructions exactly.

          temperature: The sampling temperature, which affects the randomness in the response. Note
              that higher temperature values can reduce groundedness.

          top_p: A parameter for nucleus sampling, an alternative to temperature which also
              affects the randomness of the response. Note that higher top_p values can reduce
              groundedness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generate",
            body=await async_maybe_transform(
                {
                    "knowledge": knowledge,
                    "messages": messages,
                    "model": model,
                    "avoid_commentary": avoid_commentary,
                    "max_new_tokens": max_new_tokens,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "top_p": top_p,
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
