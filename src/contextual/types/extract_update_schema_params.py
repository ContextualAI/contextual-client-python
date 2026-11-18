# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractUpdateSchemaParams"]


class ExtractUpdateSchemaParams(TypedDict, total=False):
    description: object
    """Description of the schema"""

    metadata: object
    """Additional metadata"""

    name: object
    """Name of the schema"""

    schema_definition: object
    """JSON schema definition"""
