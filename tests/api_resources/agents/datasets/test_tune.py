# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from contextual.types.agents import DatasetResponse, ListDatasetsResponse, CreateDatasetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTune:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.agents.datasets.tune.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = response.parse()
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.agents.datasets.tune.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="tuning_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = response.parse()
            assert_matches_type(CreateDatasetResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.tune.with_raw_response.create(
                agent_id="",
                dataset_name="dataset_name",
                dataset_type="tuning_set",
                file=b"raw file contents",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tune = client.agents.datasets.tune.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tune.is_closed
        assert tune.json() == {"foo": "bar"}
        assert cast(Any, tune.is_closed) is True
        assert isinstance(tune, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_with_all_params(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tune = client.agents.datasets.tune.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            batch_size=1,
            version="version",
        )
        assert tune.is_closed
        assert tune.json() == {"foo": "bar"}
        assert cast(Any, tune.is_closed) is True
        assert isinstance(tune, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tune = client.agents.datasets.tune.with_raw_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert tune.is_closed is True
        assert tune.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tune.json() == {"foo": "bar"}
        assert isinstance(tune, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.agents.datasets.tune.with_streaming_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as tune:
            assert not tune.is_closed
            assert tune.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tune.json() == {"foo": "bar"}
            assert cast(Any, tune.is_closed) is True
            assert isinstance(tune, StreamedBinaryAPIResponse)

        assert cast(Any, tune.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.tune.with_raw_response.retrieve(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.tune.with_raw_response.retrieve(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ContextualAI) -> None:
        response = client.agents.datasets.tune.with_raw_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = response.parse()
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ContextualAI) -> None:
        with client.agents.datasets.tune.with_streaming_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="tuning_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = response.parse()
            assert_matches_type(CreateDatasetResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.tune.with_raw_response.update(
                dataset_name="dataset_name",
                agent_id="",
                dataset_type="tuning_set",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.tune.with_raw_response.update(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dataset_type="tuning_set",
                file=b"raw file contents",
            )

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListDatasetsResponse, tune, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(ListDatasetsResponse, tune, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.agents.datasets.tune.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = response.parse()
        assert_matches_type(ListDatasetsResponse, tune, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.agents.datasets.tune.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = response.parse()
            assert_matches_type(ListDatasetsResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.tune.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, tune, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.agents.datasets.tune.with_raw_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = response.parse()
        assert_matches_type(object, tune, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.agents.datasets.tune.with_streaming_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = response.parse()
            assert_matches_type(object, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.tune.with_raw_response.delete(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.tune.with_raw_response.delete(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_metadata(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetResponse, tune, path=["response"])

    @parametrize
    def test_method_metadata_with_all_params(self, client: ContextualAI) -> None:
        tune = client.agents.datasets.tune.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(DatasetResponse, tune, path=["response"])

    @parametrize
    def test_raw_response_metadata(self, client: ContextualAI) -> None:
        response = client.agents.datasets.tune.with_raw_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = response.parse()
        assert_matches_type(DatasetResponse, tune, path=["response"])

    @parametrize
    def test_streaming_response_metadata(self, client: ContextualAI) -> None:
        with client.agents.datasets.tune.with_streaming_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = response.parse()
            assert_matches_type(DatasetResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.tune.with_raw_response.metadata(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.tune.with_raw_response.metadata(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTune:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.tune.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = await response.parse()
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.tune.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="tuning_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = await response.parse()
            assert_matches_type(CreateDatasetResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.create(
                agent_id="",
                dataset_name="dataset_name",
                dataset_type="tuning_set",
                file=b"raw file contents",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tune = await async_client.agents.datasets.tune.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tune.is_closed
        assert await tune.json() == {"foo": "bar"}
        assert cast(Any, tune.is_closed) is True
        assert isinstance(tune, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_with_all_params(
        self, async_client: AsyncContextualAI, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tune = await async_client.agents.datasets.tune.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            batch_size=1,
            version="version",
        )
        assert tune.is_closed
        assert await tune.json() == {"foo": "bar"}
        assert cast(Any, tune.is_closed) is True
        assert isinstance(tune, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tune = await async_client.agents.datasets.tune.with_raw_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert tune.is_closed is True
        assert tune.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tune.json() == {"foo": "bar"}
        assert isinstance(tune, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/tune/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.agents.datasets.tune.with_streaming_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as tune:
            assert not tune.is_closed
            assert tune.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tune.json() == {"foo": "bar"}
            assert cast(Any, tune.is_closed) is True
            assert isinstance(tune, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tune.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.retrieve(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.retrieve(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.tune.with_raw_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="tuning_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = await response.parse()
        assert_matches_type(CreateDatasetResponse, tune, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.tune.with_streaming_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="tuning_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = await response.parse()
            assert_matches_type(CreateDatasetResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.update(
                dataset_name="dataset_name",
                agent_id="",
                dataset_type="tuning_set",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.update(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dataset_type="tuning_set",
                file=b"raw file contents",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListDatasetsResponse, tune, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(ListDatasetsResponse, tune, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.tune.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = await response.parse()
        assert_matches_type(ListDatasetsResponse, tune, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.tune.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = await response.parse()
            assert_matches_type(ListDatasetsResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, tune, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.tune.with_raw_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = await response.parse()
        assert_matches_type(object, tune, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.tune.with_streaming_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = await response.parse()
            assert_matches_type(object, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.delete(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.delete(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetResponse, tune, path=["response"])

    @parametrize
    async def test_method_metadata_with_all_params(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.agents.datasets.tune.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(DatasetResponse, tune, path=["response"])

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.tune.with_raw_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = await response.parse()
        assert_matches_type(DatasetResponse, tune, path=["response"])

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.tune.with_streaming_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = await response.parse()
            assert_matches_type(DatasetResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.metadata(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.tune.with_raw_response.metadata(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
