# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["ParseCreateParams"]


class ParseCreateParams(TypedDict, total=False):
    raw_file: Required[FileTypes]
    """The file to be parsed. The file type must be PDF, DOC / DOCX, PPT / PPTX."""

    enable_document_hierarchy: bool
    """
    Adds a table of contents to the output with the structure of the entire parsed
    document. This feature is in beta. Controls parsing heading levels (e.g. H1, H2,
    H3) at higher quality. Not permitted in `basic` parsing_mode, or if page_range
    is not continuous and/or does not start from page zero.
    """

    enable_split_tables: bool
    """
    Controls whether tables are split into multiple tables by row with the headers
    propagated. Use for improving LLM comprehension of very large tables. Not
    permitted in `basic` parsing_mode.
    """

    figure_caption_mode: Literal["concise", "detailed"]
    """Controls how thorough figure captions are.

    `concise` is short and minimizes chances of hallucinations. `detailed` is more
    thorough and can include commentary; this mode is in beta. Not permitted in
    `basic` parsing_mode.
    """

    max_split_table_cells: int
    """
    Threshold number of table cells beyond which large tables are split if
    `enable_split_tables` is True. Not permitted in `basic` parsing_mode.
    """

    page_range: str
    """Optional string representing page range to be parsed.

    Format: comma-separated indexes (0-based, e.g. `0,1,2,5,6`), or ranges inclusive
    of both ends (e.g. `0-2,5,6`)
    """

    parse_mode: Literal["basic", "standard"]
    """The settings to use for parsing.

    `basic` is for simple, text-only documents. `standard` is for complex documents
    with images, complex hierarchy, and/or no natively encoded textual data (e.g.
    for scanned documents).
    """
