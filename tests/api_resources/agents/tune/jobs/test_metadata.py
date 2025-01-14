# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types.agents.tune import GetTuneJobResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ContextualAI) -> None:
        metadata = client.agents.tune.jobs.metadata.retrieve(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetTuneJobResponse, metadata, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ContextualAI) -> None:
        response = client.agents.tune.jobs.metadata.with_raw_response.retrieve(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(GetTuneJobResponse, metadata, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ContextualAI) -> None:
        with client.agents.tune.jobs.metadata.with_streaming_response.retrieve(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(GetTuneJobResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tune.jobs.metadata.with_raw_response.retrieve(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.agents.tune.jobs.metadata.with_raw_response.retrieve(
                job_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextualAI) -> None:
        metadata = await async_client.agents.tune.jobs.metadata.retrieve(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetTuneJobResponse, metadata, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.agents.tune.jobs.metadata.with_raw_response.retrieve(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(GetTuneJobResponse, metadata, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextualAI) -> None:
        async with async_client.agents.tune.jobs.metadata.with_streaming_response.retrieve(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(GetTuneJobResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tune.jobs.metadata.with_raw_response.retrieve(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.agents.tune.jobs.metadata.with_raw_response.retrieve(
                job_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )