# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "RetrievalInfoResponse",
    "ContentMetadata",
    "ContentMetadataUnstructuredContentMetadata",
    "ContentMetadataStructuredContentMetadata",
]


class ContentMetadataUnstructuredContentMetadata(BaseModel):
    content_id: str
    """Id of the content."""

    content_text: str
    """Text of the content."""

    document_id: str
    """Id of the document which the content belongs to."""

    height: float
    """Height of the image."""

    page: int
    """Page number of the content."""

    page_img: str
    """Image of the page on which the content occurs."""

    width: float
    """Width of the image."""

    x0: float
    """X coordinate of the top left corner on the bounding box."""

    x1: float
    """X coordinate of the bottom right corner on the bounding box."""

    y0: float
    """Y coordinate of the top left corner on the bounding box."""

    y1: float
    """Y coordinate of the bottom right corner on the bounding box."""

    content_type: Optional[Literal["unstructured"]] = None


class ContentMetadataStructuredContentMetadata(BaseModel):
    content_id: str
    """Id of the content."""

    content_text: object
    """Text of the content."""

    content_type: Optional[Literal["structured"]] = None


ContentMetadata: TypeAlias = Annotated[
    Union[ContentMetadataUnstructuredContentMetadata, ContentMetadataStructuredContentMetadata],
    PropertyInfo(discriminator="content_type"),
]


class RetrievalInfoResponse(BaseModel):
    content_metadatas: Optional[List[ContentMetadata]] = None
    """List of content metadatas."""
