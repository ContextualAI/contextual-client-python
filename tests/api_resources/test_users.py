# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    ListUsersResponse,
    InviteUsersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: ContextualAI) -> None:
        user = client.users.update(
            email="email",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ContextualAI) -> None:
        user = client.users.update(
            email="email",
            is_tenant_admin=True,
            per_agent_roles=[
                {
                    "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "grant": True,
                    "roles": ["AGENT_USER"],
                }
            ],
            roles=["AGENT_USER"],
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ContextualAI) -> None:
        response = client.users.with_raw_response.update(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ContextualAI) -> None:
        with client.users.with_streaming_response.update(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        user = client.users.list()
        assert_matches_type(ListUsersResponse, user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        user = client.users.list(
            cursor="cursor",
            deactivated=True,
            limit=0,
            search="search",
        )
        assert_matches_type(ListUsersResponse, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ListUsersResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ListUsersResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_deactivate(self, client: ContextualAI) -> None:
        user = client.users.deactivate(
            email="email",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_deactivate(self, client: ContextualAI) -> None:
        response = client.users.with_raw_response.deactivate(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_deactivate(self, client: ContextualAI) -> None:
        with client.users.with_streaming_response.deactivate(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_invite(self, client: ContextualAI) -> None:
        user = client.users.invite(
            new_users=[{"email": "email"}],
            tenant_short_name="tenant_short_name",
        )
        assert_matches_type(InviteUsersResponse, user, path=["response"])

    @parametrize
    def test_raw_response_invite(self, client: ContextualAI) -> None:
        response = client.users.with_raw_response.invite(
            new_users=[{"email": "email"}],
            tenant_short_name="tenant_short_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(InviteUsersResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_invite(self, client: ContextualAI) -> None:
        with client.users.with_streaming_response.invite(
            new_users=[{"email": "email"}],
            tenant_short_name="tenant_short_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(InviteUsersResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncContextualAI) -> None:
        user = await async_client.users.update(
            email="email",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncContextualAI) -> None:
        user = await async_client.users.update(
            email="email",
            is_tenant_admin=True,
            per_agent_roles=[
                {
                    "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "grant": True,
                    "roles": ["AGENT_USER"],
                }
            ],
            roles=["AGENT_USER"],
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.users.with_raw_response.update(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextualAI) -> None:
        async with async_client.users.with_streaming_response.update(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        user = await async_client.users.list()
        assert_matches_type(ListUsersResponse, user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        user = await async_client.users.list(
            cursor="cursor",
            deactivated=True,
            limit=0,
            search="search",
        )
        assert_matches_type(ListUsersResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ListUsersResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ListUsersResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncContextualAI) -> None:
        user = await async_client.users.deactivate(
            email="email",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.users.with_raw_response.deactivate(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncContextualAI) -> None:
        async with async_client.users.with_streaming_response.deactivate(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_invite(self, async_client: AsyncContextualAI) -> None:
        user = await async_client.users.invite(
            new_users=[{"email": "email"}],
            tenant_short_name="tenant_short_name",
        )
        assert_matches_type(InviteUsersResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.users.with_raw_response.invite(
            new_users=[{"email": "email"}],
            tenant_short_name="tenant_short_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(InviteUsersResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncContextualAI) -> None:
        async with async_client.users.with_streaming_response.invite(
            new_users=[{"email": "email"}],
            tenant_short_name="tenant_short_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(InviteUsersResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
