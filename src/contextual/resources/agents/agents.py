# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, cast

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
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
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
from ...types.create_agent_output import CreateAgentOutput
from ...types.agent_metadata_response import AgentMetadataResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        agent_configs: agent_create_params.AgentConfigs | NotGiven = NOT_GIVEN,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        filter_prompt: str | NotGiven = NOT_GIVEN,
        multiturn_system_prompt: str | NotGiven = NOT_GIVEN,
        no_retrieval_system_prompt: str | NotGiven = NOT_GIVEN,
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

        This creates a specialized RAG `Agent` which queries over one or multiple
        `Datastores` to retrieve relevant data on which its generations are grounded.

        Retrieval and generation parameters are defined in the provided `Agent`
        configuration.

        If no `datastore_id` is provided in the configuration, this API automatically
        creates an empty `Datastore` and configures the `Agent` to use the newly created
        `Datastore`.

        > Note that self-serve users are currently required to create agents through our
        > UI. Otherwise, they will receive the following message: "This endpoint is
        > disabled as you need to go through checkout. Please use the UI to make this
        > request."

        Args:
          name: Name of the agent

          agent_configs: The following advanced parameters are experimental and subject to change.

          datastore_ids: The IDs of the datastore to associate with this agent.

          description: Description of the agent

          filter_prompt: The prompt to an LLM which determines whether retrieved chunks are relevant to a
              given query and filters out irrelevant chunks.

          multiturn_system_prompt: Instructions on how the agent should handle multi-turn conversations.

          no_retrieval_system_prompt: Instructions on how the agent should respond when there are no relevant
              retrievals that can be used to answer a query.

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle. The max length of all the suggested queries is 1000.

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
                    "agent_configs": agent_configs,
                    "datastore_ids": datastore_ids,
                    "description": description,
                    "filter_prompt": filter_prompt,
                    "multiturn_system_prompt": multiturn_system_prompt,
                    "no_retrieval_system_prompt": no_retrieval_system_prompt,
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
        agent_configs: agent_update_params.AgentConfigs | NotGiven = NOT_GIVEN,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        filter_prompt: str | NotGiven = NOT_GIVEN,
        llm_model_id: str | NotGiven = NOT_GIVEN,
        multiturn_system_prompt: str | NotGiven = NOT_GIVEN,
        no_retrieval_system_prompt: str | NotGiven = NOT_GIVEN,
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
          agent_id: ID of the agent to edit

          agent_configs: The following advanced parameters are experimental and subject to change.

          datastore_ids: IDs of the datastore to associate with the agent.

          filter_prompt: The prompt to an LLM which determines whether retrieved chunks are relevant to a
              given query and filters out irrelevant chunks.

          llm_model_id: The model ID to use for generation. Tuned models can only be used for the agents
              on which they were tuned. If no model is specified, the default model is used.
              Set to `default` to switch from a tuned model to the default model.

          multiturn_system_prompt: Instructions on how the agent should handle multi-turn conversations.

          no_retrieval_system_prompt: Instructions on how the agent should respond when there are no relevant
              retrievals that can be used to answer a query.

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle. The max length of all the suggested queries is 1000.

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
                    "agent_configs": agent_configs,
                    "datastore_ids": datastore_ids,
                    "filter_prompt": filter_prompt,
                    "llm_model_id": llm_model_id,
                    "multiturn_system_prompt": multiturn_system_prompt,
                    "no_retrieval_system_prompt": no_retrieval_system_prompt,
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
          agent_id: ID of the agent to delete

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
    ) -> AgentMetadataResponse:
        """
        Get metadata and configuration of a given `Agent`.

        Args:
          agent_id: ID of the agent for which to retrieve details

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return cast(
            AgentMetadataResponse,
            self._get(
                f"/agents/{agent_id}/metadata",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AgentMetadataResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def reset(
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
        """
        Reset a given `Agent` to default configuration.

        Args:
          agent_id: ID of the agent to reset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/agents/{agent_id}/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        agent_configs: agent_create_params.AgentConfigs | NotGiven = NOT_GIVEN,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        filter_prompt: str | NotGiven = NOT_GIVEN,
        multiturn_system_prompt: str | NotGiven = NOT_GIVEN,
        no_retrieval_system_prompt: str | NotGiven = NOT_GIVEN,
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

        This creates a specialized RAG `Agent` which queries over one or multiple
        `Datastores` to retrieve relevant data on which its generations are grounded.

        Retrieval and generation parameters are defined in the provided `Agent`
        configuration.

        If no `datastore_id` is provided in the configuration, this API automatically
        creates an empty `Datastore` and configures the `Agent` to use the newly created
        `Datastore`.

        > Note that self-serve users are currently required to create agents through our
        > UI. Otherwise, they will receive the following message: "This endpoint is
        > disabled as you need to go through checkout. Please use the UI to make this
        > request."

        Args:
          name: Name of the agent

          agent_configs: The following advanced parameters are experimental and subject to change.

          datastore_ids: The IDs of the datastore to associate with this agent.

          description: Description of the agent

          filter_prompt: The prompt to an LLM which determines whether retrieved chunks are relevant to a
              given query and filters out irrelevant chunks.

          multiturn_system_prompt: Instructions on how the agent should handle multi-turn conversations.

          no_retrieval_system_prompt: Instructions on how the agent should respond when there are no relevant
              retrievals that can be used to answer a query.

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle. The max length of all the suggested queries is 1000.

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
                    "agent_configs": agent_configs,
                    "datastore_ids": datastore_ids,
                    "description": description,
                    "filter_prompt": filter_prompt,
                    "multiturn_system_prompt": multiturn_system_prompt,
                    "no_retrieval_system_prompt": no_retrieval_system_prompt,
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
        agent_configs: agent_update_params.AgentConfigs | NotGiven = NOT_GIVEN,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        filter_prompt: str | NotGiven = NOT_GIVEN,
        llm_model_id: str | NotGiven = NOT_GIVEN,
        multiturn_system_prompt: str | NotGiven = NOT_GIVEN,
        no_retrieval_system_prompt: str | NotGiven = NOT_GIVEN,
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
          agent_id: ID of the agent to edit

          agent_configs: The following advanced parameters are experimental and subject to change.

          datastore_ids: IDs of the datastore to associate with the agent.

          filter_prompt: The prompt to an LLM which determines whether retrieved chunks are relevant to a
              given query and filters out irrelevant chunks.

          llm_model_id: The model ID to use for generation. Tuned models can only be used for the agents
              on which they were tuned. If no model is specified, the default model is used.
              Set to `default` to switch from a tuned model to the default model.

          multiturn_system_prompt: Instructions on how the agent should handle multi-turn conversations.

          no_retrieval_system_prompt: Instructions on how the agent should respond when there are no relevant
              retrievals that can be used to answer a query.

          suggested_queries: These queries will show up as suggestions in the Contextual UI when users load
              the agent. We recommend including common queries that users will ask, as well as
              complex queries so users understand the types of complex queries the system can
              handle. The max length of all the suggested queries is 1000.

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
                    "agent_configs": agent_configs,
                    "datastore_ids": datastore_ids,
                    "filter_prompt": filter_prompt,
                    "llm_model_id": llm_model_id,
                    "multiturn_system_prompt": multiturn_system_prompt,
                    "no_retrieval_system_prompt": no_retrieval_system_prompt,
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
          agent_id: ID of the agent to delete

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
    ) -> AgentMetadataResponse:
        """
        Get metadata and configuration of a given `Agent`.

        Args:
          agent_id: ID of the agent for which to retrieve details

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return cast(
            AgentMetadataResponse,
            await self._get(
                f"/agents/{agent_id}/metadata",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AgentMetadataResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def reset(
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
        """
        Reset a given `Agent` to default configuration.

        Args:
          agent_id: ID of the agent to reset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/agents/{agent_id}/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        self.reset = to_raw_response_wrapper(
            agents.reset,
        )

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._agents.query)


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
        self.reset = async_to_raw_response_wrapper(
            agents.reset,
        )

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._agents.query)


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
        self.reset = to_streamed_response_wrapper(
            agents.reset,
        )

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._agents.query)


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
        self.reset = async_to_streamed_response_wrapper(
            agents.reset,
        )

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._agents.query)
