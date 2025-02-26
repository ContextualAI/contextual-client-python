# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DocumentMetadata"]


class DocumentMetadata(BaseModel):
    id: str
    """ID of the document that was ingested"""

    created_at: str
    """Timestamp of when the document was created in ISO format."""

    name: str
    """User specified name of the document"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Status of this document's ingestion job"""

    custom_metadata: Optional[Dict[str, Union[bool, float, str]]] = None

    updated_at: Optional[str] = None
    """Timestamp of when the document was modified in ISO format."""
