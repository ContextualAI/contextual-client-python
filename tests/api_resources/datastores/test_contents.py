# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.pagination import SyncContentsPage, AsyncContentsPage
from contextual.types.datastores import (
    ContentListResponse,
    ContentMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        content = client.datastores.contents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncContentsPage[ContentListResponse], content, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        content = client.datastores.contents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            search="search",
        )
        assert_matches_type(SyncContentsPage[ContentListResponse], content, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.datastores.contents.with_raw_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(SyncContentsPage[ContentListResponse], content, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.datastores.contents.with_streaming_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(SyncContentsPage[ContentListResponse], content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.contents.with_raw_response.list(
                datastore_id="",
            )

    @parametrize
    def test_method_metadata(self, client: ContextualAI) -> None:
        content = client.datastores.contents.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContentMetadataResponse, content, path=["response"])

    @parametrize
    def test_method_metadata_with_all_params(self, client: ContextualAI) -> None:
        content = client.datastores.contents.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
        )
        assert_matches_type(ContentMetadataResponse, content, path=["response"])

    @parametrize
    def test_raw_response_metadata(self, client: ContextualAI) -> None:
        response = client.datastores.contents.with_raw_response.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(ContentMetadataResponse, content, path=["response"])

    @parametrize
    def test_streaming_response_metadata(self, client: ContextualAI) -> None:
        with client.datastores.contents.with_streaming_response.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(ContentMetadataResponse, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.contents.with_raw_response.metadata(
                content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `content_id` but received ''"):
            client.datastores.contents.with_raw_response.metadata(
                content_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncContents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        content = await async_client.datastores.contents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncContentsPage[ContentListResponse], content, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        content = await async_client.datastores.contents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            search="search",
        )
        assert_matches_type(AsyncContentsPage[ContentListResponse], content, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.contents.with_raw_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(AsyncContentsPage[ContentListResponse], content, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.contents.with_streaming_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(AsyncContentsPage[ContentListResponse], content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.contents.with_raw_response.list(
                datastore_id="",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncContextualAI) -> None:
        content = await async_client.datastores.contents.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContentMetadataResponse, content, path=["response"])

    @parametrize
    async def test_method_metadata_with_all_params(self, async_client: AsyncContextualAI) -> None:
        content = await async_client.datastores.contents.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
        )
        assert_matches_type(ContentMetadataResponse, content, path=["response"])

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.contents.with_raw_response.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(ContentMetadataResponse, content, path=["response"])

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.contents.with_streaming_response.metadata(
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(ContentMetadataResponse, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.contents.with_raw_response.metadata(
                content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `content_id` but received ''"):
            await async_client.datastores.contents.with_raw_response.metadata(
                content_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
