# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvaluateListParams"]


class EvaluateListParams(TypedDict, total=False):
    dataset_name: str
    """Optional dataset name to filter the results by.

    If provided, only versions from that dataset are listed.
    """
