# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ContextualAIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import parse, users, agents, lmunit, rerank, generate, datastores
    from .resources.parse import ParseResource, AsyncParseResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.lmunit import LMUnitResource, AsyncLMUnitResource
    from .resources.rerank import RerankResource, AsyncRerankResource
    from .resources.generate import GenerateResource, AsyncGenerateResource
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.datastores.datastores import DatastoresResource, AsyncDatastoresResource

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
    # client options
    api_key: str | None = None
    is_snowflake: bool = False
    is_snowflake_internal: bool = False

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
        """Construct a new synchronous ContextualAI client instance.

        This automatically infers the `api_key` argument from the `CONTEXTUAL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CONTEXTUAL_API_KEY")
        if api_key is None:
            if os.getenv('SNOWFLAKE_INTERNAL_API_SERVICE', False):
                self.is_snowflake_internal = True
            else:
                raise ContextualAIError(
                    "The api_key client option must be set either by passing api_key to the client or by setting the CONTEXTUAL_API_KEY environment variable"
                )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CONTEXTUAL_AI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.contextual.ai/v1"

        if 'snowflakecomputing.app' in str(base_url):
            self.is_snowflake = True

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

    @cached_property
    def datastores(self) -> DatastoresResource:
        from .resources.datastores import DatastoresResource

        return DatastoresResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def lmunit(self) -> LMUnitResource:
        from .resources.lmunit import LMUnitResource

        return LMUnitResource(self)

    @cached_property
    def rerank(self) -> RerankResource:
        from .resources.rerank import RerankResource

        return RerankResource(self)

    @cached_property
    def generate(self) -> GenerateResource:
        from .resources.generate import GenerateResource

        return GenerateResource(self)

    @cached_property
    def parse(self) -> ParseResource:
        from .resources.parse import ParseResource

        return ParseResource(self)

    @cached_property
    def with_raw_response(self) -> ContextualAIWithRawResponse:
        return ContextualAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextualAIWithStreamedResponse:
        return ContextualAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if self.is_snowflake:
            return {"Authorization": f"Snowflake Token={api_key}"}
        elif self.is_snowflake_internal:
            return {}
        else:
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
    # client options
    api_key: str | None = None
    is_snowflake: bool = False
    is_snowflake_internal: bool = False

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
        """Construct a new async AsyncContextualAI client instance.

        This automatically infers the `api_key` argument from the `CONTEXTUAL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CONTEXTUAL_API_KEY")
        if api_key is None:
            if os.getenv('SNOWFLAKE_INTERNAL_API_SERVICE', False):
                self.is_snowflake_internal = True
            else:
                raise ContextualAIError(
                    "The api_key client option must be set either by passing api_key to the client or by setting the CONTEXTUAL_API_KEY environment variable"
                )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CONTEXTUAL_AI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.contextual.ai/v1"

        if 'snowflakecomputing.app' in str(base_url):
            self.is_snowflake = True

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

    @cached_property
    def datastores(self) -> AsyncDatastoresResource:
        from .resources.datastores import AsyncDatastoresResource

        return AsyncDatastoresResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def lmunit(self) -> AsyncLMUnitResource:
        from .resources.lmunit import AsyncLMUnitResource

        return AsyncLMUnitResource(self)

    @cached_property
    def rerank(self) -> AsyncRerankResource:
        from .resources.rerank import AsyncRerankResource

        return AsyncRerankResource(self)

    @cached_property
    def generate(self) -> AsyncGenerateResource:
        from .resources.generate import AsyncGenerateResource

        return AsyncGenerateResource(self)

    @cached_property
    def parse(self) -> AsyncParseResource:
        from .resources.parse import AsyncParseResource

        return AsyncParseResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncContextualAIWithRawResponse:
        return AsyncContextualAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextualAIWithStreamedResponse:
        return AsyncContextualAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override 
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if self.is_snowflake:
            return {"Authorization": f"Snowflake Token={api_key}"}
        elif self.is_snowflake_internal:
            return {}
        else:
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
    _client: ContextualAI

    def __init__(self, client: ContextualAI) -> None:
        self._client = client

    @cached_property
    def datastores(self) -> datastores.DatastoresResourceWithRawResponse:
        from .resources.datastores import DatastoresResourceWithRawResponse

        return DatastoresResourceWithRawResponse(self._client.datastores)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def lmunit(self) -> lmunit.LMUnitResourceWithRawResponse:
        from .resources.lmunit import LMUnitResourceWithRawResponse

        return LMUnitResourceWithRawResponse(self._client.lmunit)

    @cached_property
    def rerank(self) -> rerank.RerankResourceWithRawResponse:
        from .resources.rerank import RerankResourceWithRawResponse

        return RerankResourceWithRawResponse(self._client.rerank)

    @cached_property
    def generate(self) -> generate.GenerateResourceWithRawResponse:
        from .resources.generate import GenerateResourceWithRawResponse

        return GenerateResourceWithRawResponse(self._client.generate)

    @cached_property
    def parse(self) -> parse.ParseResourceWithRawResponse:
        from .resources.parse import ParseResourceWithRawResponse

        return ParseResourceWithRawResponse(self._client.parse)


class AsyncContextualAIWithRawResponse:
    _client: AsyncContextualAI

    def __init__(self, client: AsyncContextualAI) -> None:
        self._client = client

    @cached_property
    def datastores(self) -> datastores.AsyncDatastoresResourceWithRawResponse:
        from .resources.datastores import AsyncDatastoresResourceWithRawResponse

        return AsyncDatastoresResourceWithRawResponse(self._client.datastores)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def lmunit(self) -> lmunit.AsyncLMUnitResourceWithRawResponse:
        from .resources.lmunit import AsyncLMUnitResourceWithRawResponse

        return AsyncLMUnitResourceWithRawResponse(self._client.lmunit)

    @cached_property
    def rerank(self) -> rerank.AsyncRerankResourceWithRawResponse:
        from .resources.rerank import AsyncRerankResourceWithRawResponse

        return AsyncRerankResourceWithRawResponse(self._client.rerank)

    @cached_property
    def generate(self) -> generate.AsyncGenerateResourceWithRawResponse:
        from .resources.generate import AsyncGenerateResourceWithRawResponse

        return AsyncGenerateResourceWithRawResponse(self._client.generate)

    @cached_property
    def parse(self) -> parse.AsyncParseResourceWithRawResponse:
        from .resources.parse import AsyncParseResourceWithRawResponse

        return AsyncParseResourceWithRawResponse(self._client.parse)


class ContextualAIWithStreamedResponse:
    _client: ContextualAI

    def __init__(self, client: ContextualAI) -> None:
        self._client = client

    @cached_property
    def datastores(self) -> datastores.DatastoresResourceWithStreamingResponse:
        from .resources.datastores import DatastoresResourceWithStreamingResponse

        return DatastoresResourceWithStreamingResponse(self._client.datastores)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def lmunit(self) -> lmunit.LMUnitResourceWithStreamingResponse:
        from .resources.lmunit import LMUnitResourceWithStreamingResponse

        return LMUnitResourceWithStreamingResponse(self._client.lmunit)

    @cached_property
    def rerank(self) -> rerank.RerankResourceWithStreamingResponse:
        from .resources.rerank import RerankResourceWithStreamingResponse

        return RerankResourceWithStreamingResponse(self._client.rerank)

    @cached_property
    def generate(self) -> generate.GenerateResourceWithStreamingResponse:
        from .resources.generate import GenerateResourceWithStreamingResponse

        return GenerateResourceWithStreamingResponse(self._client.generate)

    @cached_property
    def parse(self) -> parse.ParseResourceWithStreamingResponse:
        from .resources.parse import ParseResourceWithStreamingResponse

        return ParseResourceWithStreamingResponse(self._client.parse)


class AsyncContextualAIWithStreamedResponse:
    _client: AsyncContextualAI

    def __init__(self, client: AsyncContextualAI) -> None:
        self._client = client

    @cached_property
    def datastores(self) -> datastores.AsyncDatastoresResourceWithStreamingResponse:
        from .resources.datastores import AsyncDatastoresResourceWithStreamingResponse

        return AsyncDatastoresResourceWithStreamingResponse(self._client.datastores)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def lmunit(self) -> lmunit.AsyncLMUnitResourceWithStreamingResponse:
        from .resources.lmunit import AsyncLMUnitResourceWithStreamingResponse

        return AsyncLMUnitResourceWithStreamingResponse(self._client.lmunit)

    @cached_property
    def rerank(self) -> rerank.AsyncRerankResourceWithStreamingResponse:
        from .resources.rerank import AsyncRerankResourceWithStreamingResponse

        return AsyncRerankResourceWithStreamingResponse(self._client.rerank)

    @cached_property
    def generate(self) -> generate.AsyncGenerateResourceWithStreamingResponse:
        from .resources.generate import AsyncGenerateResourceWithStreamingResponse

        return AsyncGenerateResourceWithStreamingResponse(self._client.generate)

    @cached_property
    def parse(self) -> parse.AsyncParseResourceWithStreamingResponse:
        from .resources.parse import AsyncParseResourceWithStreamingResponse

        return AsyncParseResourceWithStreamingResponse(self._client.parse)


Client = ContextualAI

AsyncClient = AsyncContextualAI
