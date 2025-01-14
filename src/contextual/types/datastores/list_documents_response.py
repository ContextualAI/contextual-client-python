# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .document_metadata import DocumentMetadata

__all__ = ["ListDocumentsResponse"]


class ListDocumentsResponse(BaseModel):
    documents: List[DocumentMetadata]
    """List of documents retrieved based on the user's GET request"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Ommitted if there are no more documents after these ones, or if job_id was set in the request.
    """

    total_count: Optional[int] = None
    """
    Total number of available documents which would be returned by the request if no
    limit were specified. Ommitted if job_id was set in the request.
    """
