# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DatastoreMetadata", "DatastoreUsages"]


class DatastoreUsages(BaseModel):
    size_gb: float
    """Actual size of the datastore in GB"""


class DatastoreMetadata(BaseModel):
    agent_ids: List[str]
    """List of agents using this datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created"""

    name: str
    """Name of the datastore"""

    datastore_usages: Optional[DatastoreUsages] = None
    """Datastore usage"""
