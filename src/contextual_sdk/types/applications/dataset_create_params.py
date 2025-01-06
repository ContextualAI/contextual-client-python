# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    dataset_name: Required[str]
    """Name of the dataset"""

    dataset_type: Required[Literal["evaluation_set"]]
    """Type of dataset which determines its schema and validation rules."""

    file: Required[FileTypes]
    """JSONL file containing the dataset"""
