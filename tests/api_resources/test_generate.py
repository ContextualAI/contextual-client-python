# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import GenerateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        generate = client.generate.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        generate = client.generate.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            avoid_commentary=True,
            max_new_tokens=1,
            system_prompt="system_prompt",
            temperature=0,
            top_p=1,
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.generate.with_raw_response.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.generate.with_streaming_response.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateCreateResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        generate = await async_client.generate.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        generate = await async_client.generate.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            avoid_commentary=True,
            max_new_tokens=1,
            system_prompt="system_prompt",
            temperature=0,
            top_p=1,
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.generate.with_raw_response.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.generate.with_streaming_response.create(
            knowledge=["string"],
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateCreateResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
