# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    email: Required[str]
    """The email of the user"""

    is_tenant_admin: bool
    """Flag indicating if the user is a tenant admin"""

    roles: List[
        Literal[
            "VISITOR",
            "AGENT_USER",
            "CUSTOMER_INTERNAL_USER",
            "CONTEXTUAL_STAFF_USER",
            "CONTEXTUAL_EXTERNAL_STAFF_USER",
            "CONTEXTUAL_INTERNAL_STAFF_USER",
            "TENANT_ADMIN",
            "SUPER_ADMIN",
        ]
    ]
    """The user level roles of the user."""
