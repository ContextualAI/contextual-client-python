# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    billing_list_top_ups_params,
    billing_retrieve_acl_usage_params,
    billing_retrieve_monthly_usage_params,
    billing_retrieve_billing_mode_history_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.billing_list_top_ups_response import BillingListTopUpsResponse
from ..types.billing_retrieve_balance_response import BillingRetrieveBalanceResponse
from ..types.billing_retrieve_metadata_response import BillingRetrieveMetadataResponse
from ..types.billing_retrieve_acl_usage_response import BillingRetrieveAclUsageResponse
from ..types.billing_retrieve_monthly_usage_response import BillingRetrieveMonthlyUsageResponse
from ..types.billing_retrieve_earliest_usage_date_response import BillingRetrieveEarliestUsageDateResponse
from ..types.billing_retrieve_billing_mode_history_response import BillingRetrieveBillingModeHistoryResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveBalanceResponse:
        """
        Get the remaining balance for a tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveBalanceResponse,
        )

    def list_top_ups(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListTopUpsResponse:
        """
        Get the top-up history for a tenant. Paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/balance/top-ups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                    },
                    billing_list_top_ups_params.BillingListTopUpsParams,
                ),
            ),
            cast_to=BillingListTopUpsResponse,
        )

    def retrieve_billing_mode_history(
        self,
        *,
        year: int,
        month: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveBillingModeHistoryResponse:
        """
        Get the billing mode history for a tenant for a specific month.

        Args: request: Request object containing year and month with validation user_context: User context with tenant admin permissions

        Returns: Billing mode history records for the specified month and year Returns at least one entry which is the mode of the first date of the given month, with potential mode changes in the middle of the month. If no record found, defaults to LEGACY mode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/billing_mode/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "year": year,
                        "month": month,
                    },
                    billing_retrieve_billing_mode_history_params.BillingRetrieveBillingModeHistoryParams,
                ),
            ),
            cast_to=BillingRetrieveBillingModeHistoryResponse,
        )

    def retrieve_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveMetadataResponse:
        """
        Non admin endpoint for getting the billing metadata for a tenant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveMetadataResponse,
        )

    def retrieve_acl_usage(
        self,
        *,
        year: int,
        month: int,
        resource_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveAclUsageResponse:
        """
        Get Agent Composer step-level usage data for a specific month.

        This API returns daily usages of advance queries grouped by steps. The data is used for visualization purposes to show users which Agent Composer steps were executed and their associated costs and token consumption.

        Note: The costs returned here are already included in the ACL_COST entry from the daily_usages table and should not be double-counted in billing.

        Args: request: Request object containing year, month, and optional resource_id user_context: User context with tenant admin permissions

        Returns: Agent Composer step usage data aggregated by step and date

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/usages/acl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "year": year,
                        "month": month,
                        "resource_id": resource_id,
                    },
                    billing_retrieve_acl_usage_params.BillingRetrieveAclUsageParams,
                ),
            ),
            cast_to=BillingRetrieveAclUsageResponse,
        )

    def retrieve_earliest_usage_date(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveEarliestUsageDateResponse:
        """
        Get the earliest usage date for a tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/usages/earliest_date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveEarliestUsageDateResponse,
        )

    def retrieve_monthly_usage(
        self,
        *,
        year: int,
        month: int,
        resource_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveMonthlyUsageResponse:
        """
        Get monthly usage data for a tenant with validation for year and month parameters.

        Args: request: Request object containing year and month with validation user_context: User context with tenant admin permissions resource_id: Optional[UUID]. If provided, get usage data for a specific resource. Otherwise, get aggregated usage data across all resources.

        Returns: Monthly usage records for the specified month and year

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing/usages/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "year": year,
                        "month": month,
                        "resource_id": resource_id,
                    },
                    billing_retrieve_monthly_usage_params.BillingRetrieveMonthlyUsageParams,
                ),
            ),
            cast_to=BillingRetrieveMonthlyUsageResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveBalanceResponse:
        """
        Get the remaining balance for a tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveBalanceResponse,
        )

    async def list_top_ups(
        self,
        *,
        limit: int | Omit = omit,
        cursor: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListTopUpsResponse:
        """
        Get the top-up history for a tenant. Paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/balance/top-ups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                    },
                    billing_list_top_ups_params.BillingListTopUpsParams,
                ),
            ),
            cast_to=BillingListTopUpsResponse,
        )

    async def retrieve_billing_mode_history(
        self,
        *,
        year: int,
        month: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveBillingModeHistoryResponse:
        """
        Get the billing mode history for a tenant for a specific month.

        Args: request: Request object containing year and month with validation user_context: User context with tenant admin permissions

        Returns: Billing mode history records for the specified month and year Returns at least one entry which is the mode of the first date of the given month, with potential mode changes in the middle of the month. If no record found, defaults to LEGACY mode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/billing_mode/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "year": year,
                        "month": month,
                    },
                    billing_retrieve_billing_mode_history_params.BillingRetrieveBillingModeHistoryParams,
                ),
            ),
            cast_to=BillingRetrieveBillingModeHistoryResponse,
        )

    async def retrieve_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveMetadataResponse:
        """
        Non admin endpoint for getting the billing metadata for a tenant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveMetadataResponse,
        )

    async def retrieve_acl_usage(
        self,
        *,
        year: int,
        month: int,
        resource_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveAclUsageResponse:
        """
        Get Agent Composer step-level usage data for a specific month.

        This API returns daily usages of advance queries grouped by steps. The data is used for visualization purposes to show users which Agent Composer steps were executed and their associated costs and token consumption.

        Note: The costs returned here are already included in the ACL_COST entry from the daily_usages table and should not be double-counted in billing.

        Args: request: Request object containing year, month, and optional resource_id user_context: User context with tenant admin permissions

        Returns: Agent Composer step usage data aggregated by step and date

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/usages/acl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "year": year,
                        "month": month,
                        "resource_id": resource_id,
                    },
                    billing_retrieve_acl_usage_params.BillingRetrieveAclUsageParams,
                ),
            ),
            cast_to=BillingRetrieveAclUsageResponse,
        )

    async def retrieve_earliest_usage_date(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveEarliestUsageDateResponse:
        """
        Get the earliest usage date for a tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/usages/earliest_date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveEarliestUsageDateResponse,
        )

    async def retrieve_monthly_usage(
        self,
        *,
        year: int,
        month: int,
        resource_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveMonthlyUsageResponse:
        """
        Get monthly usage data for a tenant with validation for year and month parameters.

        Args: request: Request object containing year and month with validation user_context: User context with tenant admin permissions resource_id: Optional[UUID]. If provided, get usage data for a specific resource. Otherwise, get aggregated usage data across all resources.

        Returns: Monthly usage records for the specified month and year

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing/usages/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "year": year,
                        "month": month,
                        "resource_id": resource_id,
                    },
                    billing_retrieve_monthly_usage_params.BillingRetrieveMonthlyUsageParams,
                ),
            ),
            cast_to=BillingRetrieveMonthlyUsageResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.retrieve_balance = to_raw_response_wrapper(
            billing.retrieve_balance,
        )
        self.list_top_ups = to_raw_response_wrapper(
            billing.list_top_ups,
        )
        self.retrieve_billing_mode_history = to_raw_response_wrapper(
            billing.retrieve_billing_mode_history,
        )
        self.retrieve_metadata = to_raw_response_wrapper(
            billing.retrieve_metadata,
        )
        self.retrieve_acl_usage = to_raw_response_wrapper(
            billing.retrieve_acl_usage,
        )
        self.retrieve_earliest_usage_date = to_raw_response_wrapper(
            billing.retrieve_earliest_usage_date,
        )
        self.retrieve_monthly_usage = to_raw_response_wrapper(
            billing.retrieve_monthly_usage,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.retrieve_balance = async_to_raw_response_wrapper(
            billing.retrieve_balance,
        )
        self.list_top_ups = async_to_raw_response_wrapper(
            billing.list_top_ups,
        )
        self.retrieve_billing_mode_history = async_to_raw_response_wrapper(
            billing.retrieve_billing_mode_history,
        )
        self.retrieve_metadata = async_to_raw_response_wrapper(
            billing.retrieve_metadata,
        )
        self.retrieve_acl_usage = async_to_raw_response_wrapper(
            billing.retrieve_acl_usage,
        )
        self.retrieve_earliest_usage_date = async_to_raw_response_wrapper(
            billing.retrieve_earliest_usage_date,
        )
        self.retrieve_monthly_usage = async_to_raw_response_wrapper(
            billing.retrieve_monthly_usage,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.retrieve_balance = to_streamed_response_wrapper(
            billing.retrieve_balance,
        )
        self.list_top_ups = to_streamed_response_wrapper(
            billing.list_top_ups,
        )
        self.retrieve_billing_mode_history = to_streamed_response_wrapper(
            billing.retrieve_billing_mode_history,
        )
        self.retrieve_metadata = to_streamed_response_wrapper(
            billing.retrieve_metadata,
        )
        self.retrieve_acl_usage = to_streamed_response_wrapper(
            billing.retrieve_acl_usage,
        )
        self.retrieve_earliest_usage_date = to_streamed_response_wrapper(
            billing.retrieve_earliest_usage_date,
        )
        self.retrieve_monthly_usage = to_streamed_response_wrapper(
            billing.retrieve_monthly_usage,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.retrieve_balance = async_to_streamed_response_wrapper(
            billing.retrieve_balance,
        )
        self.list_top_ups = async_to_streamed_response_wrapper(
            billing.list_top_ups,
        )
        self.retrieve_billing_mode_history = async_to_streamed_response_wrapper(
            billing.retrieve_billing_mode_history,
        )
        self.retrieve_metadata = async_to_streamed_response_wrapper(
            billing.retrieve_metadata,
        )
        self.retrieve_acl_usage = async_to_streamed_response_wrapper(
            billing.retrieve_acl_usage,
        )
        self.retrieve_earliest_usage_date = async_to_streamed_response_wrapper(
            billing.retrieve_earliest_usage_date,
        )
        self.retrieve_monthly_usage = async_to_streamed_response_wrapper(
            billing.retrieve_monthly_usage,
        )
