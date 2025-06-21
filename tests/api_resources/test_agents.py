# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    Agent,
    CreateAgentOutput,
    AgentMetadataResponse,
)
from contextual.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        agent = client.agents.create(
            name="xxx",
        )
        assert_matches_type(CreateAgentOutput, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        agent = client.agents.create(
            name="xxx",
            agent_configs={
                "filter_and_rerank_config": {
                    "rerank_instructions": "rerank_instructions",
                    "reranker_score_filter_threshold": 0,
                    "top_k_reranked_chunks": 0,
                },
                "generate_response_config": {
                    "avoid_commentary": True,
                    "calculate_groundedness": True,
                    "frequency_penalty": 0,
                    "max_new_tokens": 0,
                    "seed": 0,
                    "temperature": 0,
                    "top_p": 0,
                },
                "global_config": {
                    "enable_filter": True,
                    "enable_multi_turn": True,
                    "enable_rerank": True,
                    "should_check_retrieval_need": True,
                },
                "retrieval_config": {
                    "lexical_alpha": 0,
                    "semantic_alpha": 0,
                    "top_k_retrieved_chunks": 0,
                },
            },
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            filter_prompt="filter_prompt",
            no_retrieval_system_prompt="no_retrieval_system_prompt",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(CreateAgentOutput, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.agents.with_raw_response.create(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(CreateAgentOutput, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.agents.with_streaming_response.create(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(CreateAgentOutput, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ContextualAI) -> None:
        agent = client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ContextualAI) -> None:
        agent = client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_configs={
                "filter_and_rerank_config": {
                    "rerank_instructions": "rerank_instructions",
                    "reranker_score_filter_threshold": 0,
                    "top_k_reranked_chunks": 0,
                },
                "generate_response_config": {
                    "avoid_commentary": True,
                    "calculate_groundedness": True,
                    "frequency_penalty": 0,
                    "max_new_tokens": 0,
                    "seed": 0,
                    "temperature": 0,
                    "top_p": 0,
                },
                "global_config": {
                    "enable_filter": True,
                    "enable_multi_turn": True,
                    "enable_rerank": True,
                    "should_check_retrieval_need": True,
                },
                "retrieval_config": {
                    "lexical_alpha": 0,
                    "semantic_alpha": 0,
                    "top_k_retrieved_chunks": 0,
                },
            },
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            filter_prompt="filter_prompt",
            llm_model_id="llm_model_id",
            no_retrieval_system_prompt="no_retrieval_system_prompt",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ContextualAI) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ContextualAI) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        agent = client.agents.list()
        assert_matches_type(SyncPage[Agent], agent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        agent = client.agents.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[Agent], agent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(SyncPage[Agent], agent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(SyncPage[Agent], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        agent = client.agents.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.agents.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.agents.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_metadata(self, client: ContextualAI) -> None:
        agent = client.agents.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentMetadataResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_metadata(self, client: ContextualAI) -> None:
        response = client.agents.with_raw_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentMetadataResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_metadata(self, client: ContextualAI) -> None:
        with client.agents.with_streaming_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentMetadataResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.metadata(
                "",
            )

    @parametrize
    def test_method_reset(self, client: ContextualAI) -> None:
        agent = client.agents.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: ContextualAI) -> None:
        response = client.agents.with_raw_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: ContextualAI) -> None:
        with client.agents.with_streaming_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.reset(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.create(
            name="xxx",
        )
        assert_matches_type(CreateAgentOutput, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.create(
            name="xxx",
            agent_configs={
                "filter_and_rerank_config": {
                    "rerank_instructions": "rerank_instructions",
                    "reranker_score_filter_threshold": 0,
                    "top_k_reranked_chunks": 0,
                },
                "generate_response_config": {
                    "avoid_commentary": True,
                    "calculate_groundedness": True,
                    "frequency_penalty": 0,
                    "max_new_tokens": 0,
                    "seed": 0,
                    "temperature": 0,
                    "top_p": 0,
                },
                "global_config": {
                    "enable_filter": True,
                    "enable_multi_turn": True,
                    "enable_rerank": True,
                    "should_check_retrieval_need": True,
                },
                "retrieval_config": {
                    "lexical_alpha": 0,
                    "semantic_alpha": 0,
                    "top_k_retrieved_chunks": 0,
                },
            },
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            filter_prompt="filter_prompt",
            no_retrieval_system_prompt="no_retrieval_system_prompt",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(CreateAgentOutput, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.with_raw_response.create(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(CreateAgentOutput, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.with_streaming_response.create(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(CreateAgentOutput, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_configs={
                "filter_and_rerank_config": {
                    "rerank_instructions": "rerank_instructions",
                    "reranker_score_filter_threshold": 0,
                    "top_k_reranked_chunks": 0,
                },
                "generate_response_config": {
                    "avoid_commentary": True,
                    "calculate_groundedness": True,
                    "frequency_penalty": 0,
                    "max_new_tokens": 0,
                    "seed": 0,
                    "temperature": 0,
                    "top_p": 0,
                },
                "global_config": {
                    "enable_filter": True,
                    "enable_multi_turn": True,
                    "enable_rerank": True,
                    "should_check_retrieval_need": True,
                },
                "retrieval_config": {
                    "lexical_alpha": 0,
                    "semantic_alpha": 0,
                    "top_k_retrieved_chunks": 0,
                },
            },
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            filter_prompt="filter_prompt",
            llm_model_id="llm_model_id",
            no_retrieval_system_prompt="no_retrieval_system_prompt",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AsyncPage[Agent], agent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[Agent], agent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AsyncPage[Agent], agent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AsyncPage[Agent], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentMetadataResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.with_raw_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentMetadataResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.with_streaming_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentMetadataResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.metadata(
                "",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncContextualAI) -> None:
        agent = await async_client.agents.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.with_raw_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.with_streaming_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.reset(
                "",
            )
