# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from contextual_sdk import ContextualAI, AsyncContextualAI
from contextual_sdk.types.applications import TuneResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTune:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        tune = client.applications.tune.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
        )
        assert_matches_type(TuneResponse, tune, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        tune = client.applications.tune.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
            model_id="model_id",
            test_file=b"raw file contents",
        )
        assert_matches_type(TuneResponse, tune, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.applications.tune.with_raw_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = response.parse()
        assert_matches_type(TuneResponse, tune, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.applications.tune.with_streaming_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = response.parse()
            assert_matches_type(TuneResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.tune.with_raw_response.create(
                application_id="",
                training_file=b"raw file contents",
            )


class TestAsyncTune:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.applications.tune.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
        )
        assert_matches_type(TuneResponse, tune, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        tune = await async_client.applications.tune.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
            model_id="model_id",
            test_file=b"raw file contents",
        )
        assert_matches_type(TuneResponse, tune, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.tune.with_raw_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tune = await response.parse()
        assert_matches_type(TuneResponse, tune, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.tune.with_streaming_response.create(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            training_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tune = await response.parse()
            assert_matches_type(TuneResponse, tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.tune.with_raw_response.create(
                application_id="",
                training_file=b"raw file contents",
            )
