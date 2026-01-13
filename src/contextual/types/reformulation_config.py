# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReformulationConfig"]


class ReformulationConfig(BaseModel):
    """Captures Query Reformulation configurations for an Agent"""

    enable_query_decomposition: Optional[bool] = None
    """Whether to enable query decomposition."""

    enable_query_expansion: Optional[bool] = None
    """Whether to enable query expansion."""

    query_decomposition_prompt: Optional[str] = None
    """The prompt to use for query decomposition."""

    query_expansion_prompt: Optional[str] = None
    """The prompt to use for query expansion."""
