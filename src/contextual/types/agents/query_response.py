# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QueryResponse",
    "RetrievalContent",
    "RetrievalContentCtxlMetadata",
    "RetrievalContentCustomMetadataConfig",
    "Attribution",
    "GroundednessScore",
    "Message",
]


class RetrievalContentCtxlMetadata(BaseModel):
    chunk_id: Optional[str] = None
    """Unique identifier for the chunk."""

    chunk_size: Optional[int] = None
    """Size of the chunk in tokens or characters."""

    date_created: Optional[str] = None
    """Date when the document or chunk was created."""

    document_title: Optional[str] = None
    """Title of the document."""

    file_format: Optional[str] = None
    """Format of the file (e.g., PDF, DOCX)."""

    file_name: Optional[str] = None
    """Name of the source file."""

    is_figure: Optional[bool] = None
    """Whether this chunk represents a figure."""

    page: Optional[int] = None
    """Page number in the source document."""

    section_id: Optional[str] = None
    """The HTML id of the nearest element of the chunk"""

    section_title: Optional[str] = None
    """Title of the section."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class RetrievalContentCustomMetadataConfig(BaseModel):
    filterable: Optional[bool] = None
    """Whether to use in filtering. Defaults to True"""

    in_chunks: Optional[bool] = None
    """Whether to add in chunks.

    Defaults to True. The maximum amount of characters per metadata field that can
    be added to the prompt or rerank is 400. The maximum amount of metadata fields
    that can be added for prompt or retrieval is 10. Contact support@contextual.ai
    to request quota increases.
    """

    returned_in_response: Optional[bool] = None
    """Whether to add in response. Defaults to False"""


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

    ctxl_metadata: Optional[RetrievalContentCtxlMetadata] = None
    """Default metadata from the retrieval"""

    custom_metadata: Optional[Dict[str, Union[bool, float, str, List[float]]]] = None
    """
    Custom metadata for the document, provided by the user at ingestion time.Must be
    a JSON-serializable dictionary with string keys and simple primitive values
    (str, int, float, bool). The total size must not exceed 2 KB.The strings with
    date format must stay in date format or be avodied if not in date format.The
    'custom_metadata.url' field is automatically included in returned attributions
    during query time, if provided.The default maximum metadata fields that can be
    used is 15, contact support if more is needed.
    """

    custom_metadata_config: Optional[Dict[str, RetrievalContentCustomMetadataConfig]] = None
    """
    A dictionary mapping metadata field names to the configuration to use for each
    field. If a metadata field is not present in the dictionary, the default
    configuration will be used. If the dictionary is not provided, metadata will be
    added in context for rerank and generation but will not be returned back to the
    user in retrievals in query API. Limits: - Maximum characters per metadata field
    (for prompt or rerank): **400** - Maximum number of metadata fields (for prompt
    or retrieval): **10** Contact support@contextual.ai to request quota increases.
    """

    datastore_id: Optional[str] = None
    """Unique identifier of the datastore"""

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

    custom_tags: Optional[List[str]] = None
    """Custom tags for the message"""


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
