# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["GetDatastoreResponse"]


class GetDatastoreResponse(BaseModel):
    agent_ids: List[str]
    """List of agents using this datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created"""

    name: str
    """Name of the datastore"""
