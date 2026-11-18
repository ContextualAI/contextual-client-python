# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ExtractRetrieveSchemaResponse"]


class ExtractRetrieveSchemaResponse(BaseModel):
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
