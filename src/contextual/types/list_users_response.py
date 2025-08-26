# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ListUsersResponse", "User", "UserPerAgentRole"]


class UserPerAgentRole(BaseModel):
    agent_id: str
    """ID of the agent on which to grant/revoke the role."""

    grant: bool
    """When set to true, the roles will be granted o/w revoked."""

    roles: List[Literal["AGENT_LEVEL_USER"]]
    """The roles that are granted/revoked"""


class User(BaseModel):
    id: str

    email: str
    """The email of the user"""

    agent_level_roles: Optional[List[Literal["AGENT_LEVEL_USER"]]] = None
    """The user level roles of the user for agent level roles."""

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
                "SERVICE_ACCOUNT",
            ]
        ]
    ] = None
    """The effective roles of the user."""

    is_tenant_admin: Optional[bool] = None
    """Flag indicating if the user is a tenant admin"""

    per_agent_roles: Optional[List[UserPerAgentRole]] = None
    """Per agent level roles for the user.

    If a user is granted any role under `agent_level_roles`, then the user has that
    role for all the agents. Only the roles that need to be updated should be part
    of this.
    """

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
                "SERVICE_ACCOUNT",
            ]
        ]
    ] = None
    """The user level roles of the user."""


class ListUsersResponse(BaseModel):
    users: List[User]
    """List of users"""

    next_cursor: Optional[str] = None
    """Cursor for the beginning of the next page"""
