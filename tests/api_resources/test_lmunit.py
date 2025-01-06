# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from contextual_sdk import ContextualAI, AsyncContextualAI
from contextual_sdk.types import LmunitScoreResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLmunit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_score(self, client: ContextualAI) -> None:
        lmunit = client.lmunit.score(
            query="query",
            response="response",
            unit_test="unit_test",
        )
        assert_matches_type(LmunitScoreResponse, lmunit, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: ContextualAI) -> None:
        response = client.lmunit.with_raw_response.score(
            query="query",
            response="response",
            unit_test="unit_test",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lmunit = response.parse()
        assert_matches_type(LmunitScoreResponse, lmunit, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: ContextualAI) -> None:
        with client.lmunit.with_streaming_response.score(
            query="query",
            response="response",
            unit_test="unit_test",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lmunit = response.parse()
            assert_matches_type(LmunitScoreResponse, lmunit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLmunit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_score(self, async_client: AsyncContextualAI) -> None:
        lmunit = await async_client.lmunit.score(
            query="query",
            response="response",
            unit_test="unit_test",
        )
        assert_matches_type(LmunitScoreResponse, lmunit, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.lmunit.with_raw_response.score(
            query="query",
            response="response",
            unit_test="unit_test",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lmunit = await response.parse()
        assert_matches_type(LmunitScoreResponse, lmunit, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncContextualAI) -> None:
        async with async_client.lmunit.with_streaming_response.score(
            query="query",
            response="response",
            unit_test="unit_test",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lmunit = await response.parse()
            assert_matches_type(LmunitScoreResponse, lmunit, path=["response"])

        assert cast(Any, response.is_closed) is True
