# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .new_user_param import NewUserParam

__all__ = ["UserInviteParams"]


class UserInviteParams(TypedDict, total=False):
    new_users: Required[Iterable[NewUserParam]]
    """List of new users to be invited"""

    tenant_short_name: Required[str]
    """The short name of the tenant"""
