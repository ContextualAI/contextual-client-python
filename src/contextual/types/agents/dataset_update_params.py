# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    agent_id: Required[str]
    """Agent ID associated with the dataset"""

    dataset_type: Required[Literal["evaluation_set"]]
    """Type of dataset which determines its schema and validation rules.

    Must match the `dataset_type` used at dataset creation time.
    """

    file: Required[FileTypes]
    """JSONL file containing the dataset"""
