# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    cursor: str
    """
    Cursor from the previous call to list agents, used to retrieve the next set of
    results
    """

    limit: int
    """Maximum number of agents to return"""
