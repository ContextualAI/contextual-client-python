# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from contextual_sdk import ContextualAI, AsyncContextualAI
from contextual_sdk.types.applications import (
    ListDatasetResponse,
    CreateDatasetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.applications.datasets.with_raw_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.applications.datasets.with_streaming_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.datasets.with_raw_response.create(
                application_id="",
                dataset_name="dataset_name",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    def test_method_retrieve(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            batch_size=1,
            version="version",
        )
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ContextualAI) -> None:
        response = client.applications.datasets.with_raw_response.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ContextualAI) -> None:
        with client.applications.datasets.with_streaming_response.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.datasets.with_raw_response.retrieve(
                dataset_name="dataset_name",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.applications.datasets.with_raw_response.retrieve(
                dataset_name="",
                application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.update(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ContextualAI) -> None:
        response = client.applications.datasets.with_raw_response.update(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ContextualAI) -> None:
        with client.applications.datasets.with_streaming_response.update(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.datasets.with_raw_response.update(
                dataset_name="dataset_name",
                application_id="",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.applications.datasets.with_raw_response.update(
                dataset_name="",
                application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(ListDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.applications.datasets.with_raw_response.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(ListDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.applications.datasets.with_streaming_response.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(ListDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.datasets.with_raw_response.list(
                application_id="",
            )

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        dataset = client.applications.datasets.delete(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.applications.datasets.with_raw_response.delete(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.applications.datasets.with_streaming_response.delete(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.datasets.with_raw_response.delete(
                dataset_name="dataset_name",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.applications.datasets.with_raw_response.delete(
                dataset_name="",
                application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.datasets.with_raw_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.datasets.with_streaming_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.datasets.with_raw_response.create(
                application_id="",
                dataset_name="dataset_name",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            batch_size=1,
            version="version",
        )
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.datasets.with_raw_response.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.datasets.with_streaming_response.retrieve(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.datasets.with_raw_response.retrieve(
                dataset_name="dataset_name",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.applications.datasets.with_raw_response.retrieve(
                dataset_name="",
                application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.update(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.datasets.with_raw_response.update(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.datasets.with_streaming_response.update(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.datasets.with_raw_response.update(
                dataset_name="dataset_name",
                application_id="",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.applications.datasets.with_raw_response.update(
                dataset_name="",
                application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(ListDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.datasets.with_raw_response.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(ListDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.datasets.with_streaming_response.list(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(ListDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.datasets.with_raw_response.list(
                application_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        dataset = await async_client.applications.datasets.delete(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.datasets.with_raw_response.delete(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.datasets.with_streaming_response.delete(
            dataset_name="dataset_name",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.datasets.with_raw_response.delete(
                dataset_name="dataset_name",
                application_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.applications.datasets.with_raw_response.delete(
                dataset_name="",
                application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
