# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Datastore"]


class Datastore(BaseModel):
    id: str
    """ID of the datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created"""

    name: str
    """Name of the datastore"""
