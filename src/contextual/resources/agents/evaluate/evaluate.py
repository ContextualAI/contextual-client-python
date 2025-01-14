# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Mapping, cast
from typing_extensions import Literal

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
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
from ....types.agents import evaluate_create_params
from ....types.agents.create_evaluation_response import CreateEvaluationResponse

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return EvaluateResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        metrics: List[Literal["equivalence", "groundedness"]],
        evalset_file: FileTypes | NotGiven = NOT_GIVEN,
        evalset_name: str | NotGiven = NOT_GIVEN,
        model_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateEvaluationResponse:
        """
        Launch an `Evaluation` round.

        An `Evaluation` is an asynchronous operation which evaluates an `Agent` on a set
        of test questions and reference answers. An `Evaluation` can select one or more
        metrics to assess the quality of generated answers. These metrics include
        `equivalence` and `groundedness`.

        `Evaluation` test set data can be provided in one of two forms: - A CSV
        `evalset_file` containing the columns `prompt`, `reference` (i.e. gold-answers),
        and `knowledge` (optional `list[str]` of retrieved knowledge) - A `dataset_name`
        which refers to an `evaluation_set` `Dataset` created through the `Dataset` API.

        Args:
          agent_id: Agent ID of the agent to evaluate

          metrics: List of metrics to use. Supported metrics are `equivalence` and `groundedness`.
              Use comma-separated list to pass multiple values or use repeated keys.

          evalset_file: Evalset file (CSV) to use for evaluation, containing the columns `prompt`
              (`question`), `reference` (`ground truth response`), and optional additional
              columns based on the selected metrics. Either `dataset_name` or `evalset_file`
              must be provided, but not both.

          evalset_name: Name of the dataset to use for evaluation, created through the dataset API.
              Either `dataset_name` or `evalset_file` must be provided, but not both.

          model_name: Model name of the tuned or aligned model to use. Defaults to the default model
              if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        body = deepcopy_minimal(
            {
                "metrics": metrics,
                "evalset_file": evalset_file,
                "evalset_name": evalset_name,
                "model_name": model_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["evalset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/agents/{agent_id}/evaluate",
            body=maybe_transform(body, evaluate_create_params.EvaluateCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEvaluationResponse,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        metrics: List[Literal["equivalence", "groundedness"]],
        evalset_file: FileTypes | NotGiven = NOT_GIVEN,
        evalset_name: str | NotGiven = NOT_GIVEN,
        model_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateEvaluationResponse:
        """
        Launch an `Evaluation` round.

        An `Evaluation` is an asynchronous operation which evaluates an `Agent` on a set
        of test questions and reference answers. An `Evaluation` can select one or more
        metrics to assess the quality of generated answers. These metrics include
        `equivalence` and `groundedness`.

        `Evaluation` test set data can be provided in one of two forms: - A CSV
        `evalset_file` containing the columns `prompt`, `reference` (i.e. gold-answers),
        and `knowledge` (optional `list[str]` of retrieved knowledge) - A `dataset_name`
        which refers to an `evaluation_set` `Dataset` created through the `Dataset` API.

        Args:
          agent_id: Agent ID of the agent to evaluate

          metrics: List of metrics to use. Supported metrics are `equivalence` and `groundedness`.
              Use comma-separated list to pass multiple values or use repeated keys.

          evalset_file: Evalset file (CSV) to use for evaluation, containing the columns `prompt`
              (`question`), `reference` (`ground truth response`), and optional additional
              columns based on the selected metrics. Either `dataset_name` or `evalset_file`
              must be provided, but not both.

          evalset_name: Name of the dataset to use for evaluation, created through the dataset API.
              Either `dataset_name` or `evalset_file` must be provided, but not both.

          model_name: Model name of the tuned or aligned model to use. Defaults to the default model
              if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        body = deepcopy_minimal(
            {
                "metrics": metrics,
                "evalset_file": evalset_file,
                "evalset_name": evalset_name,
                "model_name": model_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["evalset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/agents/{agent_id}/evaluate",
            body=await async_maybe_transform(body, evaluate_create_params.EvaluateCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEvaluationResponse,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = to_raw_response_wrapper(
            evaluate.create,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._evaluate.jobs)


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = async_to_raw_response_wrapper(
            evaluate.create,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._evaluate.jobs)


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = to_streamed_response_wrapper(
            evaluate.create,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._evaluate.jobs)


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.create = async_to_streamed_response_wrapper(
            evaluate.create,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._evaluate.jobs)
