# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExtractRetrieveDocumentResponse"]


class ExtractRetrieveDocumentResponse(BaseModel):
    """Response model for document information."""

    document_id: str
    """Unique ID of the document"""

    file_name: str
    """Original filename"""

    file_size: int
    """File size in bytes"""

    page_count: int
    """Number of pages in the document"""

    signed_url: Optional[str] = None
    """Presigned download URL for the document (valid for 1 hour). Only available for GCS and S3 storage backends."""

    status: str
    """Document status"""

    uploaded_at: str
    """Timestamp when the document was uploaded"""
