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
from contextual.types.agents import DatasetMetadata, ListDatasetsResponse, CreateDatasetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.agents.datasets.evaluate.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.agents.datasets.evaluate.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.create(
                agent_id="",
                dataset_name="dataset_name",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        evaluate = client.agents.datasets.evaluate.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert evaluate.is_closed
        assert evaluate.json() == {"foo": "bar"}
        assert cast(Any, evaluate.is_closed) is True
        assert isinstance(evaluate, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_with_all_params(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        evaluate = client.agents.datasets.evaluate.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            batch_size=1,
            version="version",
        )
        assert evaluate.is_closed
        assert evaluate.json() == {"foo": "bar"}
        assert cast(Any, evaluate.is_closed) is True
        assert isinstance(evaluate, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        evaluate = client.agents.datasets.evaluate.with_raw_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert evaluate.is_closed is True
        assert evaluate.http_request.headers.get("X-Stainless-Lang") == "python"
        assert evaluate.json() == {"foo": "bar"}
        assert isinstance(evaluate, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: ContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.agents.datasets.evaluate.with_streaming_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as evaluate:
            assert not evaluate.is_closed
            assert evaluate.http_request.headers.get("X-Stainless-Lang") == "python"

            assert evaluate.json() == {"foo": "bar"}
            assert cast(Any, evaluate.is_closed) is True
            assert isinstance(evaluate, StreamedBinaryAPIResponse)

        assert cast(Any, evaluate.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.retrieve(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.retrieve(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ContextualAI) -> None:
        response = client.agents.datasets.evaluate.with_raw_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ContextualAI) -> None:
        with client.agents.datasets.evaluate.with_streaming_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.update(
                dataset_name="dataset_name",
                agent_id="",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.update(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.agents.datasets.evaluate.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.agents.datasets.evaluate.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, evaluate, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.agents.datasets.evaluate.with_raw_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(object, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.agents.datasets.evaluate.with_streaming_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(object, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.delete(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.delete(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_metadata(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetMetadata, evaluate, path=["response"])

    @parametrize
    def test_method_metadata_with_all_params(self, client: ContextualAI) -> None:
        evaluate = client.agents.datasets.evaluate.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(DatasetMetadata, evaluate, path=["response"])

    @parametrize
    def test_raw_response_metadata(self, client: ContextualAI) -> None:
        response = client.agents.datasets.evaluate.with_raw_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(DatasetMetadata, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_metadata(self, client: ContextualAI) -> None:
        with client.agents.datasets.evaluate.with_streaming_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(DatasetMetadata, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.metadata(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            client.agents.datasets.evaluate.with_raw_response.metadata(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncEvaluate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.evaluate.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.evaluate.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.create(
                agent_id="",
                dataset_name="dataset_name",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        evaluate = await async_client.agents.datasets.evaluate.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert evaluate.is_closed
        assert await evaluate.json() == {"foo": "bar"}
        assert cast(Any, evaluate.is_closed) is True
        assert isinstance(evaluate, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_with_all_params(
        self, async_client: AsyncContextualAI, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        evaluate = await async_client.agents.datasets.evaluate.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            batch_size=1,
            version="version",
        )
        assert evaluate.is_closed
        assert await evaluate.json() == {"foo": "bar"}
        assert cast(Any, evaluate.is_closed) is True
        assert isinstance(evaluate, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        evaluate = await async_client.agents.datasets.evaluate.with_raw_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert evaluate.is_closed is True
        assert evaluate.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await evaluate.json() == {"foo": "bar"}
        assert isinstance(evaluate, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncContextualAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/datasets/evaluate/dataset_name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.agents.datasets.evaluate.with_streaming_response.retrieve(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as evaluate:
            assert not evaluate.is_closed
            assert evaluate.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await evaluate.json() == {"foo": "bar"}
            assert cast(Any, evaluate.is_closed) is True
            assert isinstance(evaluate, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, evaluate.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.retrieve(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.retrieve(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.evaluate.with_raw_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.evaluate.with_streaming_response.update(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_type="evaluation_set",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(CreateDatasetResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.update(
                dataset_name="dataset_name",
                agent_id="",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.update(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dataset_type="evaluation_set",
                file=b"raw file contents",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.evaluate.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.evaluate.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(ListDatasetsResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.evaluate.with_raw_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(object, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.evaluate.with_streaming_response.delete(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(object, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.delete(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.delete(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetMetadata, evaluate, path=["response"])

    @parametrize
    async def test_method_metadata_with_all_params(self, async_client: AsyncContextualAI) -> None:
        evaluate = await async_client.agents.datasets.evaluate.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(DatasetMetadata, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.datasets.evaluate.with_raw_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(DatasetMetadata, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.datasets.evaluate.with_streaming_response.metadata(
            dataset_name="dataset_name",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(DatasetMetadata, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.metadata(
                dataset_name="dataset_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_name` but received ''"):
            await async_client.agents.datasets.evaluate.with_raw_response.metadata(
                dataset_name="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
