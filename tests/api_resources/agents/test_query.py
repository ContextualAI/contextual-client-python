# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual._utils import parse_datetime
from contextual.types.agents import (
    QueryResponse,
    QueryMetricsResponse,
    QueryFeedbackResponse,
    RetrievalInfoResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        query = client.agents.query.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        query = client.agents.query.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                    "custom_tags": ["string"],
                }
            ],
            include_retrieval_content_text=True,
            retrievals_only=True,
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            documents_filters={
                "filters": [
                    {
                        "field": "field1",
                        "operator": "equals",
                        "value": "value1",
                    }
                ],
                "operator": "AND",
            },
            llm_model_id="llm_model_id",
            override_configuration={
                "enable_filter": True,
                "enable_rerank": True,
                "filter_model": "filter_model",
                "filter_prompt": "filter_prompt",
                "lexical_alpha": 0,
                "max_new_tokens": 0,
                "model": "model",
                "rerank_instructions": "rerank_instructions",
                "reranker": "reranker",
                "reranker_score_filter_threshold": 0,
                "semantic_alpha": 0,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "top_k_reranked_chunks": 0,
                "top_k_retrieved_chunks": 0,
                "top_p": 0,
            },
            stream=True,
            structured_output={
                "json_schema": {"foo": "bar"},
                "type": "JSON",
            },
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.agents.query.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.agents.query.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.query.with_raw_response.create(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "user",
                    }
                ],
            )

    @parametrize
    def test_method_feedback(self, client: ContextualAI) -> None:
        query = client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(QueryFeedbackResponse, query, path=["response"])

    @parametrize
    def test_method_feedback_with_all_params(self, client: ContextualAI) -> None:
        query = client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
        )
        assert_matches_type(QueryFeedbackResponse, query, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: ContextualAI) -> None:
        response = client.agents.query.with_raw_response.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryFeedbackResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: ContextualAI) -> None:
        with client.agents.query.with_streaming_response.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryFeedbackResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.query.with_raw_response.feedback(
                agent_id="",
                feedback="thumbs_up",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_metrics(self, client: ContextualAI) -> None:
        query = client.agents.query.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(QueryMetricsResponse, query, path=["response"])

    @parametrize
    def test_method_metrics_with_all_params(self, client: ContextualAI) -> None:
        query = client.agents.query.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1000,
            offset=0,
            user_emails=["string"],
        )
        assert_matches_type(QueryMetricsResponse, query, path=["response"])

    @parametrize
    def test_raw_response_metrics(self, client: ContextualAI) -> None:
        response = client.agents.query.with_raw_response.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryMetricsResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_metrics(self, client: ContextualAI) -> None:
        with client.agents.query.with_streaming_response.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryMetricsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metrics(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.query.with_raw_response.metrics(
                agent_id="",
            )

    @parametrize
    def test_method_retrieval_info(self, client: ContextualAI) -> None:
        query = client.agents.query.retrieval_info(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(RetrievalInfoResponse, query, path=["response"])

    @parametrize
    def test_raw_response_retrieval_info(self, client: ContextualAI) -> None:
        response = client.agents.query.with_raw_response.retrieval_info(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(RetrievalInfoResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_retrieval_info(self, client: ContextualAI) -> None:
        with client.agents.query.with_streaming_response.retrieval_info(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(RetrievalInfoResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieval_info(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.query.with_raw_response.retrieval_info(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
                content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.query.with_raw_response.retrieval_info(
                message_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                    "custom_tags": ["string"],
                }
            ],
            include_retrieval_content_text=True,
            retrievals_only=True,
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            documents_filters={
                "filters": [
                    {
                        "field": "field1",
                        "operator": "equals",
                        "value": "value1",
                    }
                ],
                "operator": "AND",
            },
            llm_model_id="llm_model_id",
            override_configuration={
                "enable_filter": True,
                "enable_rerank": True,
                "filter_model": "filter_model",
                "filter_prompt": "filter_prompt",
                "lexical_alpha": 0,
                "max_new_tokens": 0,
                "model": "model",
                "rerank_instructions": "rerank_instructions",
                "reranker": "reranker",
                "reranker_score_filter_threshold": 0,
                "semantic_alpha": 0,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "top_k_reranked_chunks": 0,
                "top_k_retrieved_chunks": 0,
                "top_p": 0,
            },
            stream=True,
            structured_output={
                "json_schema": {"foo": "bar"},
                "type": "JSON",
            },
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.query.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.query.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.query.with_raw_response.create(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "user",
                    }
                ],
            )

    @parametrize
    async def test_method_feedback(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(QueryFeedbackResponse, query, path=["response"])

    @parametrize
    async def test_method_feedback_with_all_params(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
        )
        assert_matches_type(QueryFeedbackResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.query.with_raw_response.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryFeedbackResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.query.with_streaming_response.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryFeedbackResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.query.with_raw_response.feedback(
                agent_id="",
                feedback="thumbs_up",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_metrics(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(QueryMetricsResponse, query, path=["response"])

    @parametrize
    async def test_method_metrics_with_all_params(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1000,
            offset=0,
            user_emails=["string"],
        )
        assert_matches_type(QueryMetricsResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_metrics(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.query.with_raw_response.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryMetricsResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_metrics(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.query.with_streaming_response.metrics(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryMetricsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metrics(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.query.with_raw_response.metrics(
                agent_id="",
            )

    @parametrize
    async def test_method_retrieval_info(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.retrieval_info(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(RetrievalInfoResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_retrieval_info(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.query.with_raw_response.retrieval_info(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(RetrievalInfoResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_retrieval_info(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.query.with_streaming_response.retrieval_info(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(RetrievalInfoResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieval_info(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.query.with_raw_response.retrieval_info(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
                content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.query.with_raw_response.retrieval_info(
                message_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )
