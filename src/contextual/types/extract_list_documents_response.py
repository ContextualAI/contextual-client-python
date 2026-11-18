# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ExtractListDocumentsResponse", "Document"]


class Document(BaseModel):
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


class ExtractListDocumentsResponse(BaseModel):
    """Response model for document listing."""

    documents: List[Document]
    """List of documents"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination. Omitted if there are no more documents to retrieve."""

    prev_cursor: Optional[str] = None
    """Previous cursor to go back in pagination. Omitted if this is the first page."""

    total_count: int
    """Total number of documents"""
