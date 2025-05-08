# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ParseJobResultsParams"]


class ParseJobResultsParams(TypedDict, total=False):
    output_types: List[Literal["markdown-document", "markdown-per-page", "blocks-per-page"]]
    """The desired output format(s) of the parsed file.

    Must be `markdown-document`, `markdown-per-page`, and/or `blocks-per-page`.
    `markdown-document` parses the whole document into a single concatenated
    markdown output. `markdown-per-page` provides markdown output per page.
    `blocks-per-page` provides a structured JSON representation of the content
    blocks on each page, sorted by reading order. Specify multiple values to get
    multiple formats in the response.
    """
