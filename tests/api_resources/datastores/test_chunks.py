# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types.datastores import ChunkUpdateContentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChunks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_content(self, client: ContextualAI) -> None:
        chunk = client.datastores.chunks.update_content(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )
        assert_matches_type(ChunkUpdateContentResponse, chunk, path=["response"])

    @parametrize
    def test_raw_response_update_content(self, client: ContextualAI) -> None:
        response = client.datastores.chunks.with_raw_response.update_content(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(ChunkUpdateContentResponse, chunk, path=["response"])

    @parametrize
    def test_streaming_response_update_content(self, client: ContextualAI) -> None:
        with client.datastores.chunks.with_streaming_response.update_content(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(ChunkUpdateContentResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_content(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.chunks.with_raw_response.update_content(
                content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `content_id` but received ''"):
            client.datastores.chunks.with_raw_response.update_content(
                content_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content="content",
            )


class TestAsyncChunks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update_content(self, async_client: AsyncContextualAI) -> None:
        chunk = await async_client.datastores.chunks.update_content(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )
        assert_matches_type(ChunkUpdateContentResponse, chunk, path=["response"])

    @parametrize
    async def test_raw_response_update_content(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.chunks.with_raw_response.update_content(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(ChunkUpdateContentResponse, chunk, path=["response"])

    @parametrize
    async def test_streaming_response_update_content(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.chunks.with_streaming_response.update_content(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(ChunkUpdateContentResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_content(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.chunks.with_raw_response.update_content(
                content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `content_id` but received ''"):
            await async_client.datastores.chunks.with_raw_response.update_content(
                content_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content="content",
            )
