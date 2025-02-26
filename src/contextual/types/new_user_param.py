# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewUserParam", "PerAgentRole"]


class PerAgentRole(TypedDict, total=False):
    agent_id: Required[str]
    """ID of the agent on which to grant/revoke the role."""

    grant: Required[bool]
    """When set to true, the roles will be granted o/w revoked."""

    roles: Required[List[Literal["AGENT_USER"]]]
    """The roles that are granted/revoked"""


class NewUserParam(TypedDict, total=False):
    email: Required[str]
    """The email of the user"""

    is_tenant_admin: bool
    """Flag indicating if the user is a tenant admin"""

    per_agent_roles: Iterable[PerAgentRole]
    """Per agent level roles for the user.

    If a user is granted any role under `roles`, then the user has that role for all
    the agents. Only the roles that need to be updated should be part of this.
    """

    roles: List[Literal["AGENT_USER"]]
    """The user level roles of the user."""
