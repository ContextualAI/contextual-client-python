# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import LMUnitCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLMUnit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        lmunit = client.lmunit.create(
            query="query",
            response="response",
            unit_test="unit_test",
        )
        assert_matches_type(LMUnitCreateResponse, lmunit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.lmunit.with_raw_response.create(
            query="query",
            response="response",
            unit_test="unit_test",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lmunit = response.parse()
        assert_matches_type(LMUnitCreateResponse, lmunit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.lmunit.with_streaming_response.create(
            query="query",
            response="response",
            unit_test="unit_test",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lmunit = response.parse()
            assert_matches_type(LMUnitCreateResponse, lmunit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLMUnit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        lmunit = await async_client.lmunit.create(
            query="query",
            response="response",
            unit_test="unit_test",
        )
        assert_matches_type(LMUnitCreateResponse, lmunit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.lmunit.with_raw_response.create(
            query="query",
            response="response",
            unit_test="unit_test",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lmunit = await response.parse()
        assert_matches_type(LMUnitCreateResponse, lmunit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.lmunit.with_streaming_response.create(
            query="query",
            response="response",
            unit_test="unit_test",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lmunit = await response.parse()
            assert_matches_type(LMUnitCreateResponse, lmunit, path=["response"])

        assert cast(Any, response.is_closed) is True
