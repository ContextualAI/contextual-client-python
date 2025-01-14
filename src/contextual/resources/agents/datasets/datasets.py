# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tune import (
    TuneResource,
    AsyncTuneResource,
    TuneResourceWithRawResponse,
    AsyncTuneResourceWithRawResponse,
    TuneResourceWithStreamingResponse,
    AsyncTuneResourceWithStreamingResponse,
)
from .evaluate import (
    EvaluateResource,
    AsyncEvaluateResource,
    EvaluateResourceWithRawResponse,
    AsyncEvaluateResourceWithRawResponse,
    EvaluateResourceWithStreamingResponse,
    AsyncEvaluateResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def tune(self) -> TuneResource:
        return TuneResource(self._client)

    @cached_property
    def evaluate(self) -> EvaluateResource:
        return EvaluateResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def tune(self) -> AsyncTuneResource:
        return AsyncTuneResource(self._client)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResource:
        return AsyncEvaluateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def tune(self) -> TuneResourceWithRawResponse:
        return TuneResourceWithRawResponse(self._datasets.tune)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self._datasets.evaluate)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def tune(self) -> AsyncTuneResourceWithRawResponse:
        return AsyncTuneResourceWithRawResponse(self._datasets.tune)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self._datasets.evaluate)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def tune(self) -> TuneResourceWithStreamingResponse:
        return TuneResourceWithStreamingResponse(self._datasets.tune)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self._datasets.evaluate)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def tune(self) -> AsyncTuneResourceWithStreamingResponse:
        return AsyncTuneResourceWithStreamingResponse(self._datasets.tune)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self._datasets.evaluate)
