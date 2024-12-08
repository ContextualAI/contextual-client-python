# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .documents.document_description import DocumentDescription

__all__ = ["GetDocumentsResponse"]


class GetDocumentsResponse(BaseModel):
    documents: List[DocumentDescription]
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
