# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GlobalConfigParam"]


class GlobalConfigParam(TypedDict, total=False):
    enable_filter: bool
    """Enables filtering of retrieved chunks with a separate LLM"""

    enable_multi_turn: bool
    """Enables multi-turn conversations.

    This feature is currently experimental and will be improved.
    """

    enable_rerank: bool
    """Enables reranking of retrieved chunks"""

    should_check_retrieval_need: bool
    """Enables checking if retrieval is needed for the query.

    This feature is currently experimental and will be improved.
    """
