# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .unstructured_datastore_config_model import UnstructuredDatastoreConfigModel

__all__ = ["DatastoreMetadata", "DatastoreUsages"]


class DatastoreUsages(BaseModel):
    """Datastore usage"""

    size_gb: float
    """Actual size of the datastore in GB"""


class DatastoreMetadata(BaseModel):
    agent_ids: List[str]
    """List of agents using this datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created"""

    name: str
    """Name of the datastore"""

    configuration: Optional[UnstructuredDatastoreConfigModel] = None
    """Configuration for unstructured datastores."""

    datastore_type: Optional[Literal["UNSTRUCTURED"]] = None
    """Type of the datastore"""

    datastore_usages: Optional[DatastoreUsages] = None
    """Datastore usage"""
