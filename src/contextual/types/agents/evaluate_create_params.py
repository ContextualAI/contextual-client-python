# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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

    llm_model_id: str
    """ID of the model to evaluate. Uses the default model if not specified."""

    notes: str
    """User notes for the evaluation job."""

    override_configuration: str
    """Override the configuration for the query.

    This will override the configuration for the agent during evaluation.
    """
