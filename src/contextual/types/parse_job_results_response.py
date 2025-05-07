# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ParseJobResultsResponse",
    "Page",
    "PageBlock",
    "PageBlockBoundingBox",
    "TableOfContents",
    "TableOfContentsBlock",
    "TableOfContentsBlockBoundingBox",
]


class PageBlockBoundingBox(BaseModel):
    x0: float
    """The x-coordinate of the top-left corner of the bounding box"""

    x1: float
    """The x-coordinate of the bottom-right corner of the bounding box"""

    y0: float
    """The y-coordinate of the top-left corner of the bounding box"""

    y1: float
    """The y-coordinate of the bottom-right corner of the bounding box"""


class PageBlock(BaseModel):
    id: str
    """Unique ID of the block"""

    bounding_box: PageBlockBoundingBox
    """
    The normalized bounding box of the block, as relative percentages of the page
    width and height
    """

    markdown: str
    """The Markdown representation of the block"""

    type: Literal["heading", "text", "table", "figure"]
    """The type of the block"""

    confidence_level: Optional[Literal["low", "medium", "high"]] = None
    """The confidence level of this block categorized as 'low', 'medium', or 'high'.

    Only available for blocks of type 'table' currently.
    """

    hierarchy_level: Optional[int] = None
    """
    The level of the block in the document hierarchy, starting at 0 for the
    root-level title block. Only present if `enable_document_hierarchy` was set to
    true in the request.
    """

    page_index: Optional[int] = None
    """The page (0-indexed) that this block belongs to.

    Only set for heading blocks that are returned in the table of contents.
    """

    parent_ids: Optional[List[str]] = None
    """
    The IDs of the parent in the document hierarchy, sorted from root-level to
    bottom. For root-level heading blocks, this will be an empty list. Only present
    if `enable_document_hierarchy` was set to true in the request.
    """


class Page(BaseModel):
    index: int
    """The index of the parsed page (zero-indexed)"""

    blocks: Optional[List[PageBlock]] = None
    """The parsed, structured blocks of this page.

    Present if `blocks-per-page` was among the requested output types.
    """

    markdown: Optional[str] = None
    """The parsed, structured Markdown of this page.

    Present if `markdown-per-page` was among the requested output types.
    """


class TableOfContentsBlockBoundingBox(BaseModel):
    x0: float
    """The x-coordinate of the top-left corner of the bounding box"""

    x1: float
    """The x-coordinate of the bottom-right corner of the bounding box"""

    y0: float
    """The y-coordinate of the top-left corner of the bounding box"""

    y1: float
    """The y-coordinate of the bottom-right corner of the bounding box"""


class TableOfContentsBlock(BaseModel):
    id: str
    """Unique ID of the block"""

    bounding_box: TableOfContentsBlockBoundingBox
    """
    The normalized bounding box of the block, as relative percentages of the page
    width and height
    """

    markdown: str
    """The Markdown representation of the block"""

    type: Literal["heading", "text", "table", "figure"]
    """The type of the block"""

    confidence_level: Optional[Literal["low", "medium", "high"]] = None
    """The confidence level of this block categorized as 'low', 'medium', or 'high'.

    Only available for blocks of type 'table' currently.
    """

    hierarchy_level: Optional[int] = None
    """
    The level of the block in the document hierarchy, starting at 0 for the
    root-level title block. Only present if `enable_document_hierarchy` was set to
    true in the request.
    """

    page_index: Optional[int] = None
    """The page (0-indexed) that this block belongs to.

    Only set for heading blocks that are returned in the table of contents.
    """

    parent_ids: Optional[List[str]] = None
    """
    The IDs of the parent in the document hierarchy, sorted from root-level to
    bottom. For root-level heading blocks, this will be an empty list. Only present
    if `enable_document_hierarchy` was set to true in the request.
    """


class TableOfContents(BaseModel):
    blocks: Optional[List[TableOfContentsBlock]] = None
    """Heading blocks that define the hierarchy of the document"""

    markdown: Optional[str] = None
    """
    Markdown representation of the table of contents that can be pre-pended to the
    markdown document.
    """


class ParseJobResultsResponse(BaseModel):
    file_name: str
    """The name of the file that was uploaded for parsing"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """The current status of the parse job"""

    markdown_document: Optional[str] = None
    """The parsed, structured Markdown of the input file.

    Only present if `markdown-document` was among the requested output types.
    """

    pages: Optional[List[Page]] = None
    """
    Per-page parse results, containing per-page Markdown (if `markdown-per-page` was
    requested) and/or per-page `ParsedBlock`s (if `blocks-per-page` was requested).
    """

    table_of_contents: Optional[TableOfContents] = None
    """The table of contents representing the document's heading hierarchy.

    Only present if `enable_document_hierarchy` was set to true in the parse
    request.
    """
