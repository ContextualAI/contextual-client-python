# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocumentGetParseResultParams"]


class DocumentGetParseResultParams(TypedDict, total=False):
    datastore_id: Required[str]
    """Datastore ID of the datastore from which to retrieve the document"""

    output_types: List[Literal["markdown-document", "markdown-per-page", "blocks-per-page"]]
    """The desired output format(s) of the parsed file.

    Must be `markdown-document`, `markdown-per-page`, and/or `blocks-per-page`.
    Specify multiple values to get multiple formats in the response.
    `markdown-document` parses the whole document into a single concatenated
    markdown output. `markdown-per-page` provides markdown output per page.
    `blocks-per-page` provides a structured JSON representation of the content
    blocks on each page, sorted by reading order.
    """
