# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    ApplicationListResponse,
    CreateApplicationOutput,
)
from contextual.pagination import SyncApplicationsListResponse, AsyncApplicationsListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        application = client.applications.create(
            name="xxx",
        )
        assert_matches_type(CreateApplicationOutput, application, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        application = client.applications.create(
            name="xxx",
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="xxx",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(CreateApplicationOutput, application, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.applications.with_raw_response.create(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(CreateApplicationOutput, application, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.applications.with_streaming_response.create(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(CreateApplicationOutput, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ContextualAI) -> None:
        application = client.applications.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ContextualAI) -> None:
        application = client.applications.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            llm_model_id="llm_model_id",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ContextualAI) -> None:
        response = client.applications.with_raw_response.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ContextualAI) -> None:
        with client.applications.with_streaming_response.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.update(
                application_id="",
            )

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        application = client.applications.list()
        assert_matches_type(SyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        application = client.applications.list(
            cursor="cursor",
            limit=1,
            search="search",
        )
        assert_matches_type(SyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(SyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(SyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        application = client.applications.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.applications.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.applications.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.delete(
                "",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.create(
            name="xxx",
        )
        assert_matches_type(CreateApplicationOutput, application, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.create(
            name="xxx",
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="xxx",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(CreateApplicationOutput, application, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.with_raw_response.create(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(CreateApplicationOutput, application, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.with_streaming_response.create(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(CreateApplicationOutput, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            llm_model_id="llm_model_id",
            suggested_queries=["string"],
            system_prompt="system_prompt",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.with_raw_response.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.with_streaming_response.update(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.update(
                application_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.list()
        assert_matches_type(AsyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.list(
            cursor="cursor",
            limit=1,
            search="search",
        )
        assert_matches_type(AsyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(AsyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(AsyncApplicationsListResponse[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        application = await async_client.applications.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.applications.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.applications.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.delete(
                "",
            )
