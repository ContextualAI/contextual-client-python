# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_lmunit_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ContextualAIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.agents import agents
from .resources.datastores import datastores
from .types.lmunit_response import LMUnitResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ContextualAI",
    "AsyncContextualAI",
    "Client",
    "AsyncClient",
]


class ContextualAI(SyncAPIClient):
    datastores: datastores.DatastoresResource
    agents: agents.AgentsResource
    with_raw_response: ContextualAIWithRawResponse
    with_streaming_response: ContextualAIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Contextual AI client instance.

        This automatically infers the `api_key` argument from the `CONTEXTUAL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CONTEXTUAL_API_KEY")
        if api_key is None:
            raise ContextualAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CONTEXTUAL_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CONTEXTUAL_AI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.contextual.ai/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.datastores = datastores.DatastoresResource(self)
        self.agents = agents.AgentsResource(self)
        self.with_raw_response = ContextualAIWithRawResponse(self)
        self.with_streaming_response = ContextualAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def lmunit(
        self,
        *,
        query: str,
        response: str,
        unit_test: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LMUnitResponse:
        """
        Given a `query`, `response`, and a `unit_test`, return the response's `score` on
        the unit test on a 5-point continuous scale. The total input cannot exceed 7000
        tokens.

        See a code example in [our blog post](https://contextual.ai/news/lmunit/). Email
        [lmunit-feedback@contextual.ai](mailto:lmunit-feedback@contextual.ai) with any
        feedback or questions.

        > 🚀 Obtain an LMUnit API key by completing
        > [this form](https://contextual.ai/request-lmunit-api/)

        Args:
          query: The prompt to which the model responds

          response: The model response to evaluate

          unit_test: A natural language statement or question against which to evaluate the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/lmunit",
            body=maybe_transform(
                {
                    "query": query,
                    "response": response,
                    "unit_test": unit_test,
                },
                client_lmunit_params.ClientLMUnitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LMUnitResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncContextualAI(AsyncAPIClient):
    datastores: datastores.AsyncDatastoresResource
    agents: agents.AsyncAgentsResource
    with_raw_response: AsyncContextualAIWithRawResponse
    with_streaming_response: AsyncContextualAIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Contextual AI client instance.

        This automatically infers the `api_key` argument from the `CONTEXTUAL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CONTEXTUAL_API_KEY")
        if api_key is None:
            raise ContextualAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CONTEXTUAL_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CONTEXTUAL_AI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.contextual.ai/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.datastores = datastores.AsyncDatastoresResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.with_raw_response = AsyncContextualAIWithRawResponse(self)
        self.with_streaming_response = AsyncContextualAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def lmunit(
        self,
        *,
        query: str,
        response: str,
        unit_test: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LMUnitResponse:
        """
        Given a `query`, `response`, and a `unit_test`, return the response's `score` on
        the unit test on a 5-point continuous scale. The total input cannot exceed 7000
        tokens.

        See a code example in [our blog post](https://contextual.ai/news/lmunit/). Email
        [lmunit-feedback@contextual.ai](mailto:lmunit-feedback@contextual.ai) with any
        feedback or questions.

        > 🚀 Obtain an LMUnit API key by completing
        > [this form](https://contextual.ai/request-lmunit-api/)

        Args:
          query: The prompt to which the model responds

          response: The model response to evaluate

          unit_test: A natural language statement or question against which to evaluate the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/lmunit",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "response": response,
                    "unit_test": unit_test,
                },
                client_lmunit_params.ClientLMUnitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LMUnitResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ContextualAIWithRawResponse:
    def __init__(self, client: ContextualAI) -> None:
        self.datastores = datastores.DatastoresResourceWithRawResponse(client.datastores)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)

        self.lmunit = to_raw_response_wrapper(
            client.lmunit,
        )


class AsyncContextualAIWithRawResponse:
    def __init__(self, client: AsyncContextualAI) -> None:
        self.datastores = datastores.AsyncDatastoresResourceWithRawResponse(client.datastores)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)

        self.lmunit = async_to_raw_response_wrapper(
            client.lmunit,
        )


class ContextualAIWithStreamedResponse:
    def __init__(self, client: ContextualAI) -> None:
        self.datastores = datastores.DatastoresResourceWithStreamingResponse(client.datastores)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)

        self.lmunit = to_streamed_response_wrapper(
            client.lmunit,
        )


class AsyncContextualAIWithStreamedResponse:
    def __init__(self, client: AsyncContextualAI) -> None:
        self.datastores = datastores.AsyncDatastoresResourceWithStreamingResponse(client.datastores)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)

        self.lmunit = async_to_streamed_response_wrapper(
            client.lmunit,
        )


Client = ContextualAI

AsyncClient = AsyncContextualAI
