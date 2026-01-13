# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .unstructured_datastore_config_model import UnstructuredDatastoreConfigModel

__all__ = ["Datastore"]


class Datastore(BaseModel):
    """Datastore output entry with additional fields for public API."""

    id: str
    """ID of the datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created, in ISO format"""

    datastore_type: Literal["UNSTRUCTURED"]
    """Type of the datastore"""

    name: str
    """Name of the datastore"""

    configuration: Optional[UnstructuredDatastoreConfigModel] = None
    """Configuration of the datastore"""
