# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sunrise import Sunrise, AsyncSunrise
from tests.utils import assert_matches_type
from sunrise.types.datastores import GetDatastoreResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sunrise) -> None:
        metadata = client.datastores.metadata.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetDatastoreResponse, metadata, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sunrise) -> None:
        response = client.datastores.metadata.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(GetDatastoreResponse, metadata, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sunrise) -> None:
        with client.datastores.metadata.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(GetDatastoreResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sunrise) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.metadata.with_raw_response.retrieve(
                "",
            )


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSunrise) -> None:
        metadata = await async_client.datastores.metadata.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetDatastoreResponse, metadata, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSunrise) -> None:
        response = await async_client.datastores.metadata.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(GetDatastoreResponse, metadata, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSunrise) -> None:
        async with async_client.datastores.metadata.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(GetDatastoreResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSunrise) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.metadata.with_raw_response.retrieve(
                "",
            )
