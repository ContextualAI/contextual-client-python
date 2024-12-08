# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ApplicationList", "Application"]


class Application(BaseModel):
    id: str
    """ID of the application"""

    description: str
    """Description of the application"""

    name: str
    """Name of the application"""


class ApplicationList(BaseModel):
    total_count: int
    """Total number of available applications"""

    applications: Optional[List[Application]] = None
    """List of active applications"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more applications to retrieve.
    """
