# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.parsed_block import ParsedBlock

__all__ = ["DocumentGetParseResultResponse", "DocumentMetadata", "DocumentMetadataHierarchy", "Page"]


class DocumentMetadataHierarchy(BaseModel):
    """
    Hierarchy of the document, as both heading blocks and a markdown table of contents
    """

    blocks: Optional[List[ParsedBlock]] = None
    """Heading blocks which define the hierarchy of the document"""

    table_of_contents: Optional[str] = None
    """Markdown representation of the table of contents for this document"""


class DocumentMetadata(BaseModel):
    """Document-level metadata parsed from the document"""

    hierarchy: Optional[DocumentMetadataHierarchy] = None
    """
    Hierarchy of the document, as both heading blocks and a markdown table of
    contents
    """


class Page(BaseModel):
    """Per-page parse results."""

    index: int
    """The index of the parsed page (zero-indexed)"""

    blocks: Optional[List[ParsedBlock]] = None
    """The parsed, structured blocks of this page.

    Present if `blocks-per-page` was among the requested output types.
    """

    markdown: Optional[str] = None
    """The parsed, structured Markdown of this page.

    Present if `markdown-per-page` was among the requested output types.
    """


class DocumentGetParseResultResponse(BaseModel):
    """/parse results reponse object."""

    file_name: str
    """The name of the file that was uploaded for parsing"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """The current status of the parse job"""

    document_metadata: Optional[DocumentMetadata] = None
    """Document-level metadata parsed from the document"""

    markdown_document: Optional[str] = None
    """The parsed, structured Markdown of the input file.

    Only present if `markdown-document` was among the requested output types.
    """

    pages: Optional[List[Page]] = None
    """
    Per-page parse results, containing per-page Markdown (if `markdown-per-page` was
    requested) and/or per-page `ParsedBlock`s (if `blocks-per-page` was requested).
    """
