# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import FileTypes

__all__ = ["TuneCreateParams"]


class TuneCreateParams(TypedDict, total=False):
    dataset_name: Required[str]
    """Name of the tune dataset"""

    dataset_type: Required[Literal["tuning_set"]]
    """Type of tune dataset which determines its schema and validation rules."""

    file: Required[FileTypes]
    """JSONL file containing the tune dataset"""
