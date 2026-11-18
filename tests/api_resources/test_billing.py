# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    BillingListTopUpsResponse,
    BillingRetrieveBalanceResponse,
    BillingRetrieveAclUsageResponse,
    BillingRetrieveMetadataResponse,
    BillingRetrieveMonthlyUsageResponse,
    BillingRetrieveEarliestUsageDateResponse,
    BillingRetrieveBillingModeHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_balance(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_balance()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_retrieve_balance(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_balance(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_top_ups(self, client: ContextualAI) -> None:
        billing = client.billing.list_top_ups()
        assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

    @parametrize
    def test_method_list_top_ups_with_all_params(self, client: ContextualAI) -> None:
        billing = client.billing.list_top_ups(
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_list_top_ups(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.list_top_ups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_list_top_ups(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.list_top_ups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_billing_mode_history(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_billing_mode_history(
            year=2025,
            month=1,
        )
        assert_matches_type(BillingRetrieveBillingModeHistoryResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_retrieve_billing_mode_history(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.retrieve_billing_mode_history(
            year=2025,
            month=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveBillingModeHistoryResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_billing_mode_history(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.retrieve_billing_mode_history(
            year=2025,
            month=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveBillingModeHistoryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_metadata(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_metadata()
        assert_matches_type(BillingRetrieveMetadataResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_retrieve_metadata(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.retrieve_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveMetadataResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_metadata(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.retrieve_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveMetadataResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_acl_usage(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_acl_usage(
            year=2025,
            month=1,
        )
        assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

    @parametrize
    def test_method_retrieve_acl_usage_with_all_params(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_acl_usage(
            year=2025,
            month=1,
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_retrieve_acl_usage(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.retrieve_acl_usage(
            year=2025,
            month=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_acl_usage(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.retrieve_acl_usage(
            year=2025,
            month=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_earliest_usage_date(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_earliest_usage_date()
        assert_matches_type(BillingRetrieveEarliestUsageDateResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_retrieve_earliest_usage_date(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.retrieve_earliest_usage_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveEarliestUsageDateResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_earliest_usage_date(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.retrieve_earliest_usage_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveEarliestUsageDateResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_monthly_usage(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_monthly_usage(
            year=2025,
            month=1,
        )
        assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

    @parametrize
    def test_method_retrieve_monthly_usage_with_all_params(self, client: ContextualAI) -> None:
        billing = client.billing.retrieve_monthly_usage(
            year=2025,
            month=1,
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_retrieve_monthly_usage(self, client: ContextualAI) -> None:
        response = client.billing.with_raw_response.retrieve_monthly_usage(
            year=2025,
            month=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_monthly_usage(self, client: ContextualAI) -> None:
        with client.billing.with_streaming_response.retrieve_monthly_usage(
            year=2025,
            month=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_balance()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_top_ups(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.list_top_ups()
        assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

    @parametrize
    async def test_method_list_top_ups_with_all_params(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.list_top_ups(
            limit=1,
            cursor="cursor",
        )
        assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_list_top_ups(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.list_top_ups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_list_top_ups(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.list_top_ups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingListTopUpsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_billing_mode_history(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_billing_mode_history(
            year=2025,
            month=1,
        )
        assert_matches_type(BillingRetrieveBillingModeHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_billing_mode_history(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_billing_mode_history(
            year=2025,
            month=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveBillingModeHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_billing_mode_history(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_billing_mode_history(
            year=2025,
            month=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveBillingModeHistoryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_metadata(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_metadata()
        assert_matches_type(BillingRetrieveMetadataResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveMetadataResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveMetadataResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_acl_usage(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_acl_usage(
            year=2025,
            month=1,
        )
        assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

    @parametrize
    async def test_method_retrieve_acl_usage_with_all_params(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_acl_usage(
            year=2025,
            month=1,
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_acl_usage(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_acl_usage(
            year=2025,
            month=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_acl_usage(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_acl_usage(
            year=2025,
            month=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveAclUsageResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_earliest_usage_date(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_earliest_usage_date()
        assert_matches_type(BillingRetrieveEarliestUsageDateResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_earliest_usage_date(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_earliest_usage_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveEarliestUsageDateResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_earliest_usage_date(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_earliest_usage_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveEarliestUsageDateResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_monthly_usage(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_monthly_usage(
            year=2025,
            month=1,
        )
        assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

    @parametrize
    async def test_method_retrieve_monthly_usage_with_all_params(self, async_client: AsyncContextualAI) -> None:
        billing = await async_client.billing.retrieve_monthly_usage(
            year=2025,
            month=1,
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_monthly_usage(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_monthly_usage(
            year=2025,
            month=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_monthly_usage(self, async_client: AsyncContextualAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_monthly_usage(
            year=2025,
            month=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveMonthlyUsageResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True
