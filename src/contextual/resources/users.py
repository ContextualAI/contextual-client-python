# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import user_list_params, user_invite_params, user_update_params, user_deactivate_params
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
from ..pagination import SyncUsersPage, AsyncUsersPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.new_user_param import NewUserParam
from ..types.list_users_response import User
from ..types.invite_users_response import InviteUsersResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        email: str,
        agent_level_roles: List[Literal["AGENT_LEVEL_USER"]] | Omit = omit,
        is_tenant_admin: bool | Omit = omit,
        per_agent_roles: Iterable[user_update_params.PerAgentRole] | Omit = omit,
        roles: List[
            Literal[
                "VISITOR",
                "AGENT_USER",
                "CUSTOMER_USER",
                "CUSTOMER_INTERNAL_USER",
                "CONTEXTUAL_STAFF_USER",
                "CONTEXTUAL_EXTERNAL_STAFF_USER",
                "CONTEXTUAL_INTERNAL_STAFF_USER",
                "TENANT_ADMIN",
                "CUSTOMER_ADMIN",
                "CONTEXTUAL_ADMIN",
                "SUPER_ADMIN",
                "SERVICE_ACCOUNT",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Modify a given `User`.

        Fields not included in the request body will not be modified.

        Args:
          email: The email of the user

          agent_level_roles: The user level roles of the user for agent level roles.

          is_tenant_admin: Flag indicating if the user is a tenant admin

          per_agent_roles: Per agent level roles for the user. If a user is granted any role under
              `agent_level_roles`, then the user has that role for all the agents. Only the
              roles that need to be updated should be part of this.

          roles: The user level roles of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/users",
            body=maybe_transform(
                {
                    "email": email,
                    "agent_level_roles": agent_level_roles,
                    "is_tenant_admin": is_tenant_admin,
                    "per_agent_roles": per_agent_roles,
                    "roles": roles,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        deactivated: bool | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncUsersPage[User]:
        """
        Retrieve a list of `users`.

        Args:
          cursor: Cursor for the beginning of the current page

          deactivated: When set to true, return deactivated users instead.

          limit: Number of users to return

          search: Query to filter users by email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users",
            page=SyncUsersPage[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deactivated": deactivated,
                        "limit": limit,
                        "search": search,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    def deactivate(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a given `user`.

        Args:
          email: The email of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/users",
            body=maybe_transform({"email": email}, user_deactivate_params.UserDeactivateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def invite(
        self,
        *,
        new_users: Iterable[NewUserParam],
        tenant_short_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteUsersResponse:
        """Invite users to the tenant.

        This checks if the user is already in the tenant and
        if not, creates the user. We will return a list of user emails that were
        successfully created (including existing users).

        Args:
          new_users: List of new users to be invited

          tenant_short_name: The short name of the tenant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users",
            body=maybe_transform(
                {
                    "new_users": new_users,
                    "tenant_short_name": tenant_short_name,
                },
                user_invite_params.UserInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteUsersResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        email: str,
        agent_level_roles: List[Literal["AGENT_LEVEL_USER"]] | Omit = omit,
        is_tenant_admin: bool | Omit = omit,
        per_agent_roles: Iterable[user_update_params.PerAgentRole] | Omit = omit,
        roles: List[
            Literal[
                "VISITOR",
                "AGENT_USER",
                "CUSTOMER_USER",
                "CUSTOMER_INTERNAL_USER",
                "CONTEXTUAL_STAFF_USER",
                "CONTEXTUAL_EXTERNAL_STAFF_USER",
                "CONTEXTUAL_INTERNAL_STAFF_USER",
                "TENANT_ADMIN",
                "CUSTOMER_ADMIN",
                "CONTEXTUAL_ADMIN",
                "SUPER_ADMIN",
                "SERVICE_ACCOUNT",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Modify a given `User`.

        Fields not included in the request body will not be modified.

        Args:
          email: The email of the user

          agent_level_roles: The user level roles of the user for agent level roles.

          is_tenant_admin: Flag indicating if the user is a tenant admin

          per_agent_roles: Per agent level roles for the user. If a user is granted any role under
              `agent_level_roles`, then the user has that role for all the agents. Only the
              roles that need to be updated should be part of this.

          roles: The user level roles of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "agent_level_roles": agent_level_roles,
                    "is_tenant_admin": is_tenant_admin,
                    "per_agent_roles": per_agent_roles,
                    "roles": roles,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        deactivated: bool | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[User, AsyncUsersPage[User]]:
        """
        Retrieve a list of `users`.

        Args:
          cursor: Cursor for the beginning of the current page

          deactivated: When set to true, return deactivated users instead.

          limit: Number of users to return

          search: Query to filter users by email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users",
            page=AsyncUsersPage[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deactivated": deactivated,
                        "limit": limit,
                        "search": search,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    async def deactivate(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a given `user`.

        Args:
          email: The email of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/users",
            body=await async_maybe_transform({"email": email}, user_deactivate_params.UserDeactivateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def invite(
        self,
        *,
        new_users: Iterable[NewUserParam],
        tenant_short_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteUsersResponse:
        """Invite users to the tenant.

        This checks if the user is already in the tenant and
        if not, creates the user. We will return a list of user emails that were
        successfully created (including existing users).

        Args:
          new_users: List of new users to be invited

          tenant_short_name: The short name of the tenant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users",
            body=await async_maybe_transform(
                {
                    "new_users": new_users,
                    "tenant_short_name": tenant_short_name,
                },
                user_invite_params.UserInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteUsersResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.deactivate = to_raw_response_wrapper(
            users.deactivate,
        )
        self.invite = to_raw_response_wrapper(
            users.invite,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            users.deactivate,
        )
        self.invite = async_to_raw_response_wrapper(
            users.invite,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            users.deactivate,
        )
        self.invite = to_streamed_response_wrapper(
            users.invite,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            users.deactivate,
        )
        self.invite = async_to_streamed_response_wrapper(
            users.invite,
        )
