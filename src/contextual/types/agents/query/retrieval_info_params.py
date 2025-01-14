# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RetrievalInfoParams"]


class RetrievalInfoParams(TypedDict, total=False):
    agent_id: Required[str]
    """Agent ID of the agent which sent the provided message."""

    content_ids: Required[List[str]]
    """List of content ids for which to get the metadata."""
