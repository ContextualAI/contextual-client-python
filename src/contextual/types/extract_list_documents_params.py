# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractListDocumentsParams"]


class ExtractListDocumentsParams(TypedDict, total=False):
    cursor: object

    limit: int

    search: object
