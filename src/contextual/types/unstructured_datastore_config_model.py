# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .html_configuration import HTMLConfiguration
from .chunking_configuration import ChunkingConfiguration
from .datastore_parse_configuration import DatastoreParseConfiguration

__all__ = ["UnstructuredDatastoreConfigModel"]


class UnstructuredDatastoreConfigModel(BaseModel):
    """Configuration for unstructured datastores."""

    chunking: Optional[ChunkingConfiguration] = None
    """Configuration for document chunking"""

    html_config: Optional[HTMLConfiguration] = None
    """Configuration for HTML Extraction"""

    parsing: Optional[DatastoreParseConfiguration] = None
    """Configuration for document parsing"""
