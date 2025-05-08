# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ListUsersResponse", "User"]


class User(BaseModel):
    id: str

    email: str
    """The email of the user"""

    effective_roles: Optional[
        List[
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
    ] = None
    """The effective roles of the user."""

    is_tenant_admin: Optional[bool] = None
    """Flag indicating if the user is a tenant admin"""

    roles: Optional[
        List[
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
    ] = None
    """The user level roles of the user."""


class ListUsersResponse(BaseModel):
    users: List[User]
    """List of users"""

    next_cursor: Optional[str] = None
    """Cursor for the beginning of the next page"""
