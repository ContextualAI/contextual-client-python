# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["DocumentDescription"]


class DocumentDescription(BaseModel):
    id: str
    """ID of the document that was ingested"""

    name: str
    """User specified name of the document"""

    status: str
    """Status of this document's ingestion job"""
