# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from ...types import agent_list_params, agent_create_params, agent_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .tune.tune import (
    TuneResource,
    AsyncTuneResource,
    TuneResourceWithRawResponse,
    AsyncTuneResourceWithRawResponse,
    TuneResourceWithStreamingResponse,
    AsyncTuneResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ...types.agent import Agent
from ..._base_client import AsyncPaginator, make_request_options
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .evaluate.evaluate import (
    EvaluateResource,
    AsyncEvaluateResource,
    EvaluateResourceWithRawResponse,
    AsyncEvaluateResourceWithRawResponse,
    EvaluateResourceWithStreamingResponse,
    AsyncEvaluateResourceWithStreamingResponse,
)
from ...types.agent_metadata import AgentMetadata
from ...types.create_agent_output import CreateAgentOutput

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def evaluate(self) -> EvaluateResource:
        return EvaluateResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def tune(self) -> TuneResource:
        return TuneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateAgentOutput:
        """
        Create a new `Agent` with a specific configuration.

        This creates a specialized RAG `Agent` which queries over a `Datastore` to
        retrieve relevant data on which its generations are grounded.

        Retrieval and generation parameters are defined in the provided `Agent`
        configuration.

        If no `datastore_id` is provided in the configuration, this API automatically
        creates an empty `Datastore` and configures the `Agent` to use the newly created
        `Datastore`.

        Args:
          name: Name of the agent

          datastore_ids: The IDs of the datastore associated with the agent. Leave empty to automatically
              create a new datastore.

          description: Description of the agent

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle.

          system_prompt: Instructions that your agent references when generating responses. Note that we
              do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents",
            body=maybe_transform(
                {
                    "name": name,
                    "datastore_ids": datastore_ids,
                    "description": description,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAgentOutput,
        )

    def update(
        self,
        agent_id: str,
        *,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        llm_model_id: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modify a given `Agent` to utilize the provided configuration.

        Fields not included in the request body will not be modified.

        Args:
          agent_id: Agent ID of the agent to edit

          datastore_ids: IDs of the datastore to associate with the agent.

          llm_model_id: Optional model ID of a tuned model to use for generation. Model must have been
              tuned on this agent; tuned models cannot be used across agents. Uses default
              model if none is specified. Set to `default` to deactivate the tuned model and
              use the default model.

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle.

          system_prompt: Instructions that your agent references when generating responses. Note that we
              do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/agents/{agent_id}",
            body=maybe_transform(
                {
                    "datastore_ids": datastore_ids,
                    "llm_model_id": llm_model_id,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Agent]:
        """
        Retrieve a list of all `Agents`.

        Args:
          cursor: Cursor from the previous call to list agents, used to retrieve the next set of
              results

          limit: Maximum number of agents to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agents",
            page=SyncPage[Agent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given `Agent`.

        This is an irreversible operation.

        Note: `Datastores` which are associated with the `Agent` will not be deleted,
        even if no other `Agent` is using them. To delete a `Datastore`, use the
        `DELETE /datastores/{datastore_id}` API.

        Args:
          agent_id: Agent ID of the agent to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def metadata(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentMetadata:
        """
        Get metadata and configuration of a given `Agent`.

        Args:
          agent_id: Agent ID of the agent to retrieve details for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentMetadata,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResource:
        return AsyncEvaluateResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def tune(self) -> AsyncTuneResource:
        return AsyncTuneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateAgentOutput:
        """
        Create a new `Agent` with a specific configuration.

        This creates a specialized RAG `Agent` which queries over a `Datastore` to
        retrieve relevant data on which its generations are grounded.

        Retrieval and generation parameters are defined in the provided `Agent`
        configuration.

        If no `datastore_id` is provided in the configuration, this API automatically
        creates an empty `Datastore` and configures the `Agent` to use the newly created
        `Datastore`.

        Args:
          name: Name of the agent

          datastore_ids: The IDs of the datastore associated with the agent. Leave empty to automatically
              create a new datastore.

          description: Description of the agent

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle.

          system_prompt: Instructions that your agent references when generating responses. Note that we
              do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "datastore_ids": datastore_ids,
                    "description": description,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAgentOutput,
        )

    async def update(
        self,
        agent_id: str,
        *,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        llm_model_id: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modify a given `Agent` to utilize the provided configuration.

        Fields not included in the request body will not be modified.

        Args:
          agent_id: Agent ID of the agent to edit

          datastore_ids: IDs of the datastore to associate with the agent.

          llm_model_id: Optional model ID of a tuned model to use for generation. Model must have been
              tuned on this agent; tuned models cannot be used across agents. Uses default
              model if none is specified. Set to `default` to deactivate the tuned model and
              use the default model.

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle.

          system_prompt: Instructions that your agent references when generating responses. Note that we
              do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "datastore_ids": datastore_ids,
                    "llm_model_id": llm_model_id,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Agent, AsyncPage[Agent]]:
        """
        Retrieve a list of all `Agents`.

        Args:
          cursor: Cursor from the previous call to list agents, used to retrieve the next set of
              results

          limit: Maximum number of agents to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agents",
            page=AsyncPage[Agent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given `Agent`.

        This is an irreversible operation.

        Note: `Datastores` which are associated with the `Agent` will not be deleted,
        even if no other `Agent` is using them. To delete a `Datastore`, use the
        `DELETE /datastores/{datastore_id}` API.

        Args:
          agent_id: Agent ID of the agent to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def metadata(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentMetadata:
        """
        Get metadata and configuration of a given `Agent`.

        Args:
          agent_id: Agent ID of the agent to retrieve details for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentMetadata,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.metadata = to_raw_response_wrapper(
            agents.metadata,
        )

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._agents.query)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self._agents.evaluate)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._agents.datasets)

    @cached_property
    def tune(self) -> TuneResourceWithRawResponse:
        return TuneResourceWithRawResponse(self._agents.tune)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.metadata = async_to_raw_response_wrapper(
            agents.metadata,
        )

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._agents.query)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self._agents.evaluate)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._agents.datasets)

    @cached_property
    def tune(self) -> AsyncTuneResourceWithRawResponse:
        return AsyncTuneResourceWithRawResponse(self._agents.tune)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.metadata = to_streamed_response_wrapper(
            agents.metadata,
        )

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._agents.query)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self._agents.evaluate)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._agents.datasets)

    @cached_property
    def tune(self) -> TuneResourceWithStreamingResponse:
        return TuneResourceWithStreamingResponse(self._agents.tune)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.metadata = async_to_streamed_response_wrapper(
            agents.metadata,
        )

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._agents.query)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self._agents.evaluate)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._agents.datasets)

    @cached_property
    def tune(self) -> AsyncTuneResourceWithStreamingResponse:
        return AsyncTuneResourceWithStreamingResponse(self._agents.tune)
