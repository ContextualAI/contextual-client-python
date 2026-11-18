# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ExtractUploadDocumentResponse"]


class ExtractUploadDocumentResponse(BaseModel):
    """Response model for document upload."""

    document_id: str
    """Unique ID of the uploaded document"""

    file_name: str
    """Original filename of the uploaded document"""

    file_size: int
    """File size in bytes"""

    page_count: int
    """Number of pages in the document"""

    status: str
    """Upload status"""

    uploaded_at: str
    """Timestamp when the document was uploaded"""
