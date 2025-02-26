# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    cursor: str
    """Cursor for the beginning of the current page"""

    deactivated: bool
    """When set to true, return deactivated users instead."""

    limit: int
    """Number of users to return"""

    search: str
    """Query to filter users by email"""
