# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReformulationConfigParam"]


class ReformulationConfigParam(TypedDict, total=False):
    """Captures Query Reformulation configurations for an Agent"""

    enable_query_decomposition: bool
    """Whether to enable query decomposition."""

    enable_query_expansion: bool
    """Whether to enable query expansion."""

    query_decomposition_prompt: str
    """The prompt to use for query decomposition."""

    query_expansion_prompt: str
    """The prompt to use for query expansion."""
