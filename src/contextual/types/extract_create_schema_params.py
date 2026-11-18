# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ExtractCreateSchemaParams"]


class ExtractCreateSchemaParams(TypedDict, total=False):
    name: Required[str]
    """Name of the schema"""

    schema_definition: Required[Dict[str, object]]
    """
    JSON Schema definition. Must be a valid JSON Schema that defines the structure of data to extract from documents. See the comprehensive schema guide in the API documentation for detailed examples and supported features.
    """

    description: object
    """Description of the schema"""

    metadata: object
    """Additional metadata for the schema"""
