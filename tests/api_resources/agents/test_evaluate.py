# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types.agents import CreateEvaluationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        evaluate = client.agents.evaluate.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
        )
        assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        evaluate = client.agents.evaluate.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
            evalset_file=b"raw file contents",
            evalset_name="evalset_name",
            llm_model_id="llm_model_id",
        )
        assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.agents.evaluate.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.agents.evaluate.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.evaluate.with_raw_response.create(
                agent_id="",
                metrics=["equivalence"],
            )


class TestAsyncEvaluate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.evaluate.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
        )
        assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.evaluate.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
            evalset_file=b"raw file contents",
            evalset_name="evalset_name",
            llm_model_id="llm_model_id",
        )
        assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.evaluate.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.evaluate.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metrics=["equivalence"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(CreateEvaluationResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.evaluate.with_raw_response.create(
                agent_id="",
                metrics=["equivalence"],
            )
