# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["EvaluateCreateParams"]


class EvaluateCreateParams(TypedDict, total=False):
    metrics: Required[List[Literal["equivalence", "groundedness"]]]
    """List of metrics to use.

    Supported metrics are `equivalence` and `groundedness`. Use comma-separated list
    to pass multiple values or use repeated keys.
    """

    evalset_file: FileTypes
    """
    Evalset file (CSV) to use for evaluation, containing the columns `prompt`
    (`question`), `reference` (`ground truth response`), and optional additional
    columns based on the selected metrics. Either `dataset_name` or `evalset_file`
    must be provided, but not both.
    """

    evalset_name: str
    """Name of the dataset to use for evaluation, created through the dataset API.

    Either `dataset_name` or `evalset_file` must be provided, but not both.
    """

    model_name: str
    """Model name of the tuned or aligned model to use.

    Defaults to the default model if not specified.
    """
