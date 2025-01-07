# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .application import Application

__all__ = ["ApplicationsResponse"]


class ApplicationsResponse(BaseModel):
    total_count: int
    """Total number of available applications"""

    applications: Optional[List[Application]] = None
    """List of active applications"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more applications to retrieve.
    """
