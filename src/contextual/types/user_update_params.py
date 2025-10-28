# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserUpdateParams", "PerAgentRole"]


class UserUpdateParams(TypedDict, total=False):
    email: Required[str]
    """The email of the user"""

    agent_level_roles: List[Literal["AGENT_LEVEL_USER"]]
    """The user level roles of the user for agent level roles."""

    is_tenant_admin: bool
    """Flag indicating if the user is a tenant admin"""

    per_agent_roles: Iterable[PerAgentRole]
    """Per agent level roles for the user.

    If a user is granted any role under `agent_level_roles`, then the user has that
    role for all the agents. Only the roles that need to be updated should be part
    of this.
    """

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
    """The user level roles of the user."""


class PerAgentRole(TypedDict, total=False):
    agent_id: Required[str]
    """ID of the agent on which to grant/revoke the role."""

    grant: Required[bool]
    """When set to true, the roles will be granted o/w revoked."""

    roles: Required[List[Literal["AGENT_LEVEL_USER"]]]
    """The roles that are granted/revoked"""
