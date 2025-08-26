# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    Datastore,
    DatastoreMetadata,
    CreateDatastoreResponse,
)
from contextual.pagination import SyncDatastoresPage, AsyncDatastoresPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatastores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        datastore = client.datastores.create(
            name="name",
        )
        assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        datastore = client.datastores.create(
            name="name",
            configuration={
                "chunking": {
                    "chunking_mode": "hierarchy_depth",
                    "enable_hierarchy_based_contextualization": True,
                    "max_chunk_length_tokens": 512,
                    "min_chunk_length_tokens": 128,
                },
                "html_config": {"max_chunk_length_tokens": 512},
                "parsing": {
                    "enable_split_tables": True,
                    "figure_caption_mode": "default",
                    "figure_captioning_prompt": "figure_captioning_prompt",
                    "max_split_table_cells": 0,
                },
            },
        )
        assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.datastores.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = response.parse()
        assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.datastores.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = response.parse()
            assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        datastore = client.datastores.list()
        assert_matches_type(SyncDatastoresPage[Datastore], datastore, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        datastore = client.datastores.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncDatastoresPage[Datastore], datastore, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.datastores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = response.parse()
        assert_matches_type(SyncDatastoresPage[Datastore], datastore, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.datastores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = response.parse()
            assert_matches_type(SyncDatastoresPage[Datastore], datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        datastore = client.datastores.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.datastores.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = response.parse()
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.datastores.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = response.parse()
            assert_matches_type(object, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_metadata(self, client: ContextualAI) -> None:
        datastore = client.datastores.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatastoreMetadata, datastore, path=["response"])

    @parametrize
    def test_raw_response_metadata(self, client: ContextualAI) -> None:
        response = client.datastores.with_raw_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = response.parse()
        assert_matches_type(DatastoreMetadata, datastore, path=["response"])

    @parametrize
    def test_streaming_response_metadata(self, client: ContextualAI) -> None:
        with client.datastores.with_streaming_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = response.parse()
            assert_matches_type(DatastoreMetadata, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.with_raw_response.metadata(
                "",
            )

    @parametrize
    def test_method_reset(self, client: ContextualAI) -> None:
        datastore = client.datastores.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: ContextualAI) -> None:
        response = client.datastores.with_raw_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = response.parse()
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: ContextualAI) -> None:
        with client.datastores.with_streaming_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = response.parse()
            assert_matches_type(object, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.with_raw_response.reset(
                "",
            )


class TestAsyncDatastores:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.create(
            name="name",
        )
        assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.create(
            name="name",
            configuration={
                "chunking": {
                    "chunking_mode": "hierarchy_depth",
                    "enable_hierarchy_based_contextualization": True,
                    "max_chunk_length_tokens": 512,
                    "min_chunk_length_tokens": 128,
                },
                "html_config": {"max_chunk_length_tokens": 512},
                "parsing": {
                    "enable_split_tables": True,
                    "figure_caption_mode": "default",
                    "figure_captioning_prompt": "figure_captioning_prompt",
                    "max_split_table_cells": 0,
                },
            },
        )
        assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = await response.parse()
        assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = await response.parse()
            assert_matches_type(CreateDatastoreResponse, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.list()
        assert_matches_type(AsyncDatastoresPage[Datastore], datastore, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncDatastoresPage[Datastore], datastore, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = await response.parse()
        assert_matches_type(AsyncDatastoresPage[Datastore], datastore, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = await response.parse()
            assert_matches_type(AsyncDatastoresPage[Datastore], datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = await response.parse()
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = await response.parse()
            assert_matches_type(object, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatastoreMetadata, datastore, path=["response"])

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.with_raw_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = await response.parse()
        assert_matches_type(DatastoreMetadata, datastore, path=["response"])

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.with_streaming_response.metadata(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = await response.parse()
            assert_matches_type(DatastoreMetadata, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.with_raw_response.metadata(
                "",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncContextualAI) -> None:
        datastore = await async_client.datastores.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.with_raw_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datastore = await response.parse()
        assert_matches_type(object, datastore, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.with_streaming_response.reset(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datastore = await response.parse()
            assert_matches_type(object, datastore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.with_raw_response.reset(
                "",
            )
