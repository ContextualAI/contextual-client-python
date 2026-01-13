# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .html_configuration_param import HTMLConfigurationParam
from .chunking_configuration_param import ChunkingConfigurationParam
from .datastore_parse_configuration_param import DatastoreParseConfigurationParam

__all__ = ["UnstructuredDatastoreConfigModelParam"]


class UnstructuredDatastoreConfigModelParam(TypedDict, total=False):
    """Configuration for unstructured datastores."""

    chunking: ChunkingConfigurationParam
    """Configuration for document chunking"""

    html_config: HTMLConfigurationParam
    """Configuration for HTML Extraction"""

    parsing: DatastoreParseConfigurationParam
    """Configuration for document parsing"""
