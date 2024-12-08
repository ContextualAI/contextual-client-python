# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MetadataRetrieveParams"]


class MetadataRetrieveParams(TypedDict, total=False):
    application_id: Required[str]
    """Application ID associated with dataset"""

    version: str
    """Version number of the dataset. Defaults to the latest version if not specified."""
