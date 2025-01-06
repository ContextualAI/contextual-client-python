# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import StandaloneLmunitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStandalone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_lmunit(self, client: ContextualAI) -> None:
        standalone = client.standalone.lmunit(
            query="query",
            response="response",
            unit_test="unit_test",
        )
        assert_matches_type(StandaloneLmunitResponse, standalone, path=["response"])

    @parametrize
    def test_raw_response_lmunit(self, client: ContextualAI) -> None:
        response = client.standalone.with_raw_response.lmunit(
            query="query",
            response="response",
            unit_test="unit_test",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standalone = response.parse()
        assert_matches_type(StandaloneLmunitResponse, standalone, path=["response"])

    @parametrize
    def test_streaming_response_lmunit(self, client: ContextualAI) -> None:
        with client.standalone.with_streaming_response.lmunit(
            query="query",
            response="response",
            unit_test="unit_test",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standalone = response.parse()
            assert_matches_type(StandaloneLmunitResponse, standalone, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStandalone:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_lmunit(self, async_client: AsyncContextualAI) -> None:
        standalone = await async_client.standalone.lmunit(
            query="query",
            response="response",
            unit_test="unit_test",
        )
        assert_matches_type(StandaloneLmunitResponse, standalone, path=["response"])

    @parametrize
    async def test_raw_response_lmunit(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.standalone.with_raw_response.lmunit(
            query="query",
            response="response",
            unit_test="unit_test",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standalone = await response.parse()
        assert_matches_type(StandaloneLmunitResponse, standalone, path=["response"])

    @parametrize
    async def test_streaming_response_lmunit(self, async_client: AsyncContextualAI) -> None:
        async with async_client.standalone.with_streaming_response.lmunit(
            query="query",
            response="response",
            unit_test="unit_test",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standalone = await response.parse()
            assert_matches_type(StandaloneLmunitResponse, standalone, path=["response"])

        assert cast(Any, response.is_closed) is True
