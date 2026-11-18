# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ExtractListSchemasResponse", "Schema"]


class Schema(BaseModel):
    """Response model for schema information."""

    created_at: str
    """Timestamp when the schema was created"""

    description: Optional[str] = None
    """Description of the schema"""

    metadata: Dict[str, object]
    """Schema metadata"""

    name: str
    """Name of the schema"""

    schema_definition: Dict[str, object]
    """JSON schema definition"""

    schema_id: str
    """Unique ID of the schema"""

    updated_at: str
    """Timestamp when the schema was last updated"""


class ExtractListSchemasResponse(BaseModel):
    """Response model for schema listing."""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination. Omitted if there are no more schemas to retrieve."""

    prev_cursor: Optional[str] = None
    """Previous cursor to go back in pagination. Omitted if this is the first page."""

    schemas: List[Schema]
    """List of schemas"""

    total_count: int
    """Total number of schemas"""
