# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["QueryResponse", "Attribution", "Message", "RetrievalContent"]


class Attribution(BaseModel):
    content_ids: List[str]
    """Content IDs of the sources for the attributed text"""

    end_idx: int
    """End index of the attributed text in the generated message"""

    start_idx: int
    """Start index of the attributed text in the generated message"""


class Message(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["user", "system", "assistant"]
    """Role of sender"""


class RetrievalContent(BaseModel):
    content_id: str
    """Unique identifier of the retrieved content"""

    doc_id: str
    """Unique identifier of the document"""

    doc_name: str
    """Name of the document"""

    format: Literal["pdf", "html"]
    """Format of the content, such as `pdf` or `html`"""

    number: int
    """Index of the retrieved item in the retrieval_contents list (starting from 1)"""

    type: str
    """Source type of the content.

    Will be `file` for any docs ingested through ingestion API.
    """

    extras: Optional[Dict[str, str]] = None
    """Reserved for extra metadata"""

    page: Optional[int] = None
    """Page number of the content in the document"""

    url: Optional[str] = None
    """URL of the source content, if applicable"""


class QueryResponse(BaseModel):
    attributions: List[Attribution]
    """Attributions for the response"""

    conversation_id: str
    """A unique identifier for the conversation.

    Can be passed to future `/query` calls to continue a conversation with the same
    message history.
    """

    message: Message
    """Response to the query request"""

    message_id: str
    """A unique identifier for this specific message"""

    retrieval_contents: List[RetrievalContent]
    """Relevant content retrieved to answer the query"""
