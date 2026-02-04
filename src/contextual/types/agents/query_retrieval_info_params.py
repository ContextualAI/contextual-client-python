# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["QueryRetrievalInfoParams"]


class QueryRetrievalInfoParams(TypedDict, total=False):
    agent_id: Required[str]
    """ID of the agent which sent the provided message."""

    content_ids: Required[SequenceNotStr[str]]
    """List of content ids for which to get the metadata."""
