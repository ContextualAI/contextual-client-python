# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    cursor: str
    """
    Cursor from the previous call to list applications, used to retrieve the next
    set of results
    """

    limit: int
    """Maximum number of applications to return"""
