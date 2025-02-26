# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["DocumentIngestParams"]


class DocumentIngestParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to ingest"""

    metadata: str
    """Metadata in `JSON` format.

    Metadata should be passed in a nested dictionary structure of `str` metadata
    type to `Dict` mapping `str` metadata keys to `str`, `bool`, `float` or `int`
    values. Currently, `custom_metadata` is the only supported metadata type.Example
    `metadata` dictionary: {"metadata": {"custom_metadata": {"customKey1": "value3",
    "\\__filterKey": "filterValue3"}}
    """
