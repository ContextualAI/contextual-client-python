# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["QueryResponse", "RetrievalContent", "Attribution", "GroundednessScore", "Message"]


class RetrievalContent(BaseModel):
    content_id: str
    """Unique identifier of the retrieved content"""

    doc_id: str
    """Unique identifier of the document"""

    doc_name: str
    """Name of the document"""

    format: Literal["pdf", "html", "htm", "mhtml", "doc", "docx", "ppt", "pptx"]
    """Format of the content, such as `pdf` or `html`"""

    type: str
    """Source type of the content.

    Will be `file` for any docs ingested through ingestion API.
    """

    content_text: Optional[str] = None
    """Text of the retrieved content.

    Included in response to a query if `include_retrieval_content_text` is True
    """

    number: Optional[int] = None
    """Index of the retrieved item in the retrieval_contents list (starting from 1)"""

    page: Optional[int] = None
    """Page number of the content in the document"""

    score: Optional[float] = None
    """Score of the retrieval, if applicable"""

    url: Optional[str] = None
    """URL of the source content, if applicable"""


class Attribution(BaseModel):
    content_ids: List[str]
    """Content IDs of the sources for the attributed text"""

    end_idx: int
    """End index of the attributed text in the generated message"""

    start_idx: int
    """Start index of the attributed text in the generated message"""


class GroundednessScore(BaseModel):
    end_idx: int
    """End index of the span in the generated message"""

    score: int
    """Groundedness score for the span"""

    start_idx: int
    """Start index of the span in the generated message"""


class Message(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["user", "system", "assistant", "knowledge"]
    """Role of the sender"""


class QueryResponse(BaseModel):
    conversation_id: str
    """A unique identifier for the conversation.

    Can be passed to future `/query` calls to continue a conversation with the same
    message history.
    """

    retrieval_contents: List[RetrievalContent]
    """Relevant content retrieved to answer the query"""

    attributions: Optional[List[Attribution]] = None
    """Attributions for the response"""

    groundedness_scores: Optional[List[GroundednessScore]] = None
    """Groundedness scores for the response"""

    message: Optional[Message] = None
    """Response to the query request"""

    message_id: Optional[str] = None
    """A unique identifier for this specific message"""
