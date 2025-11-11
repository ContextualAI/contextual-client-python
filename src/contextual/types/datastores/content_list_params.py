# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContentListParams"]


class ContentListParams(TypedDict, total=False):
    document_id: str
    """Document ID of the document to retrieve details for"""

    limit: int
    """The number of content ids to be returned"""

    offset: int
    """The offset to start retrieving content ids"""

    search: str
    """The query to search keywords for"""
