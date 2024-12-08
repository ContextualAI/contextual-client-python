# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetRetrieveParams"]


class DatasetRetrieveParams(TypedDict, total=False):
    application_id: Required[str]
    """Application ID associated with the dataset"""

    batch_size: int
    """Batch size for processing"""

    version: str
    """Version number of the dataset to retrieve.

    Defaults to the latest version if not specified.
    """
