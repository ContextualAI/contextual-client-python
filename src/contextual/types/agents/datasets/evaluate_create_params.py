# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import FileTypes

__all__ = ["EvaluateCreateParams"]


class EvaluateCreateParams(TypedDict, total=False):
    dataset_name: Required[str]
    """Name of the evaluation dataset"""

    dataset_type: Required[Literal["evaluation_set"]]
    """Type of evaluation dataset which determines its schema and validation rules."""

    file: Required[FileTypes]
    """JSONL or CSV file containing the evaluation dataset"""
