# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["QueryMetricsResponse"]


class QueryMetricsResponse(BaseModel):
    total_count: int
    """Total number of messages."""

    messages: Optional[List[object]] = None
    """List of messages."""

    next_offset: Optional[int] = None
    """Offset for the next page.

    If there are no more messages to get, then this is not set.
    """
