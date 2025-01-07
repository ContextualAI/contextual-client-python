# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DatastoresResponse", "Datastore"]


class Datastore(BaseModel):
    id: str
    """ID of the datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created"""

    name: str
    """Name of the datastore"""


class DatastoresResponse(BaseModel):
    datastores: List[Datastore]
    """List of all datastores"""

    total_count: int
    """Total number of available datastores"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more datastores to retrieve.
    """
