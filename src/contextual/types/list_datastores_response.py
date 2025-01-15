# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .datastore import Datastore

__all__ = ["ListDatastoresResponse"]


class ListDatastoresResponse(BaseModel):
    datastores: List[Datastore]
    """List of all datastores"""

    total_count: int
    """Total number of available datastores"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more datastores to retrieve.
    """
