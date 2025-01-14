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
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feedback(self, client: ContextualAI) -> None:
        query = client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_method_feedback_with_all_params(self, client: ContextualAI) -> None:
        query = client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
        )
        assert_matches_type(object, query, path=["response"])

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
        assert_matches_type(object, query, path=["response"])

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
            assert_matches_type(object, query, path=["response"])

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
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
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
    def test_method_start(self, client: ContextualAI) -> None:
        query = client.agents.query.start(
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
    def test_method_start_with_all_params(self, client: ContextualAI) -> None:
        query = client.agents.query.start(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            retrievals_only=True,
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model_id="model_id",
            stream=True,
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: ContextualAI) -> None:
        response = client.agents.query.with_raw_response.start(
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
    def test_streaming_response_start(self, client: ContextualAI) -> None:
        with client.agents.query.with_streaming_response.start(
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
    def test_path_params_start(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.query.with_raw_response.start(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "user",
                    }
                ],
            )


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feedback(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_method_feedback_with_all_params(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.feedback(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
        )
        assert_matches_type(object, query, path=["response"])

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
        assert_matches_type(object, query, path=["response"])

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
            assert_matches_type(object, query, path=["response"])

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
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
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
    async def test_method_start(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.start(
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
    async def test_method_start_with_all_params(self, async_client: AsyncContextualAI) -> None:
        query = await async_client.agents.query.start(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            retrievals_only=True,
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model_id="model_id",
            stream=True,
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.query.with_raw_response.start(
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
    async def test_streaming_response_start(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.query.with_streaming_response.start(
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
    async def test_path_params_start(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.query.with_raw_response.start(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "user",
                    }
                ],
            )
