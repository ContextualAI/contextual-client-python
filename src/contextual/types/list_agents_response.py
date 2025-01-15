# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .agent import Agent
from .._models import BaseModel

__all__ = ["ListAgentsResponse"]


class ListAgentsResponse(BaseModel):
    total_count: int
    """Total number of available agents"""

    data: Optional[List[Agent]] = None
    """List of active agents"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more agents to retrieve.
    """
