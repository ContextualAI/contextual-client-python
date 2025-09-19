# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import rerank_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.rerank_create_response import RerankCreateResponse

__all__ = ["RerankResource", "AsyncRerankResource"]


class RerankResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RerankResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return RerankResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RerankResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return RerankResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        documents: SequenceNotStr[str],
        model: str,
        query: str,
        instruction: str | Omit = omit,
        metadata: SequenceNotStr[str] | Omit = omit,
        top_n: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RerankCreateResponse:
        """
        Rank a list of documents according to their relevance to a query primarily and
        your custom instructions secondarily. We evaluated the model on instructions for
        recency, document type, source, and metadata, and it can generalize to other
        instructions as well. The reranker supports multilinguality.

        The total request cannot exceed 400,000 tokens. The combined length of the
        query, instruction and any document with its metadata must not exceed 8,000
        tokens.

        See our
        [blog post](https://contextual.ai/blog/introducing-instruction-following-reranker/)
        and
        [code examples](https://colab.research.google.com/github/ContextualAI/examples/blob/main/03-standalone-api/03-rerank/rerank.ipynb).
        Email [rerank-feedback@contextual.ai](mailto:rerank-feedback@contextual.ai) with
        any feedback or questions.

        Args:
          documents: The texts to be reranked according to their relevance to the query and the
              optional instruction

          model:
              The version of the reranker to use. Currently, we have:
              "ctxl-rerank-v2-instruct-multilingual",
              "ctxl-rerank-v2-instruct-multilingual-mini", "ctxl-rerank-v1-instruct".

          query: The string against which documents will be ranked for relevance

          instruction: Instructions that the reranker references when ranking documents, after
              considering relevance. We evaluated the model on instructions for recency,
              document type, source, and metadata, and it can generalize to other instructions
              as well. For instructions related to recency and timeframe, specify the
              timeframe (e.g., instead of saying "this year") because the reranker doesn't
              know the current date. Example: "Prioritize internal sales documents over market
              analysis reports. More recent documents should be weighted higher. Enterprise
              portal content supersedes distributor communications."

          metadata: Metadata for documents being passed to the reranker. Must be the same length as
              the documents list. If a document does not have metadata, add an empty string.

          top_n: The number of top-ranked results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/rerank",
            body=maybe_transform(
                {
                    "documents": documents,
                    "model": model,
                    "query": query,
                    "instruction": instruction,
                    "metadata": metadata,
                    "top_n": top_n,
                },
                rerank_create_params.RerankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankCreateResponse,
        )


class AsyncRerankResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRerankResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRerankResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRerankResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncRerankResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        documents: SequenceNotStr[str],
        model: str,
        query: str,
        instruction: str | Omit = omit,
        metadata: SequenceNotStr[str] | Omit = omit,
        top_n: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RerankCreateResponse:
        """
        Rank a list of documents according to their relevance to a query primarily and
        your custom instructions secondarily. We evaluated the model on instructions for
        recency, document type, source, and metadata, and it can generalize to other
        instructions as well. The reranker supports multilinguality.

        The total request cannot exceed 400,000 tokens. The combined length of the
        query, instruction and any document with its metadata must not exceed 8,000
        tokens.

        See our
        [blog post](https://contextual.ai/blog/introducing-instruction-following-reranker/)
        and
        [code examples](https://colab.research.google.com/github/ContextualAI/examples/blob/main/03-standalone-api/03-rerank/rerank.ipynb).
        Email [rerank-feedback@contextual.ai](mailto:rerank-feedback@contextual.ai) with
        any feedback or questions.

        Args:
          documents: The texts to be reranked according to their relevance to the query and the
              optional instruction

          model:
              The version of the reranker to use. Currently, we have:
              "ctxl-rerank-v2-instruct-multilingual",
              "ctxl-rerank-v2-instruct-multilingual-mini", "ctxl-rerank-v1-instruct".

          query: The string against which documents will be ranked for relevance

          instruction: Instructions that the reranker references when ranking documents, after
              considering relevance. We evaluated the model on instructions for recency,
              document type, source, and metadata, and it can generalize to other instructions
              as well. For instructions related to recency and timeframe, specify the
              timeframe (e.g., instead of saying "this year") because the reranker doesn't
              know the current date. Example: "Prioritize internal sales documents over market
              analysis reports. More recent documents should be weighted higher. Enterprise
              portal content supersedes distributor communications."

          metadata: Metadata for documents being passed to the reranker. Must be the same length as
              the documents list. If a document does not have metadata, add an empty string.

          top_n: The number of top-ranked results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/rerank",
            body=await async_maybe_transform(
                {
                    "documents": documents,
                    "model": model,
                    "query": query,
                    "instruction": instruction,
                    "metadata": metadata,
                    "top_n": top_n,
                },
                rerank_create_params.RerankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankCreateResponse,
        )


class RerankResourceWithRawResponse:
    def __init__(self, rerank: RerankResource) -> None:
        self._rerank = rerank

        self.create = to_raw_response_wrapper(
            rerank.create,
        )


class AsyncRerankResourceWithRawResponse:
    def __init__(self, rerank: AsyncRerankResource) -> None:
        self._rerank = rerank

        self.create = async_to_raw_response_wrapper(
            rerank.create,
        )


class RerankResourceWithStreamingResponse:
    def __init__(self, rerank: RerankResource) -> None:
        self._rerank = rerank

        self.create = to_streamed_response_wrapper(
            rerank.create,
        )


class AsyncRerankResourceWithStreamingResponse:
    def __init__(self, rerank: AsyncRerankResource) -> None:
        self._rerank = rerank

        self.create = async_to_streamed_response_wrapper(
            rerank.create,
        )
