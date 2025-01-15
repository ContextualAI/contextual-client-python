# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["EvaluateCreateParams"]


class EvaluateCreateParams(TypedDict, total=False):
    metrics: Required[List[Literal["equivalence", "groundedness"]]]
    """List of metrics to use. Supported metrics are `equivalence` and `groundedness`."""

    evalset_file: FileTypes
    """Evalset file (CSV) to use for evaluation, containing the columns `prompt` (i.e.

    question) and `reference` (i.e. ground truth response). Either `evalset_name` or
    `evalset_file` must be provided, but not both.
    """

    evalset_name: str
    """
    Name of the Dataset to use for evaluation, created through the
    `/datasets/evaluate` API. Either `evalset_name` or `evalset_file` must be
    provided, but not both.
    """

    llm_model_id: Optional[str]
    """ID of the model to evaluate. Uses the default model if not specified."""
