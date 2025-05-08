# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GlobalConfig"]


class GlobalConfig(BaseModel):
    enable_filter: Optional[bool] = None
    """Enables filtering of retrieved chunks with a separate LLM"""

    enable_multi_turn: Optional[bool] = None
    """Enables multi-turn conversations.

    This feature is currently experimental and will be improved.
    """

    enable_rerank: Optional[bool] = None
    """Enables reranking of retrieved chunks"""

    should_check_retrieval_need: Optional[bool] = None
    """Enables checking if retrieval is needed for the query.

    This feature is currently experimental and will be improved.
    """
