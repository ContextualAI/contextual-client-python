# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    WorkspaceUpdateConsentResponse,
    WorkspaceRetrieveConsentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_consent(self, client: ContextualAI) -> None:
        workspace = client.workspaces.retrieve_consent()
        assert_matches_type(WorkspaceRetrieveConsentResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_retrieve_consent(self, client: ContextualAI) -> None:
        response = client.workspaces.with_raw_response.retrieve_consent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceRetrieveConsentResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_consent(self, client: ContextualAI) -> None:
        with client.workspaces.with_streaming_response.retrieve_consent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceRetrieveConsentResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_consent(self, client: ContextualAI) -> None:
        workspace = client.workspaces.update_consent(
            type="CONSENT_FULL",
        )
        assert_matches_type(WorkspaceUpdateConsentResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_update_consent(self, client: ContextualAI) -> None:
        response = client.workspaces.with_raw_response.update_consent(
            type="CONSENT_FULL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceUpdateConsentResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_update_consent(self, client: ContextualAI) -> None:
        with client.workspaces.with_streaming_response.update_consent(
            type="CONSENT_FULL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceUpdateConsentResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_consent(self, async_client: AsyncContextualAI) -> None:
        workspace = await async_client.workspaces.retrieve_consent()
        assert_matches_type(WorkspaceRetrieveConsentResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_consent(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.workspaces.with_raw_response.retrieve_consent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceRetrieveConsentResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_consent(self, async_client: AsyncContextualAI) -> None:
        async with async_client.workspaces.with_streaming_response.retrieve_consent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceRetrieveConsentResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_consent(self, async_client: AsyncContextualAI) -> None:
        workspace = await async_client.workspaces.update_consent(
            type="CONSENT_FULL",
        )
        assert_matches_type(WorkspaceUpdateConsentResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_update_consent(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.workspaces.with_raw_response.update_consent(
            type="CONSENT_FULL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceUpdateConsentResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_update_consent(self, async_client: AsyncContextualAI) -> None:
        async with async_client.workspaces.with_streaming_response.update_consent(
            type="CONSENT_FULL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceUpdateConsentResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True
