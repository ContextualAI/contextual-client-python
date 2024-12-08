# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreateDatasetResponse"]


class CreateDatasetResponse(BaseModel):
    name: str
    """Name of the dataset"""

    type: Literal[
        "response_generation_train",
        "grounded_generation_train",
        "response_generation_validation",
        "grounded_generation_validation",
        "evaluation_run",
        "evaluation_set",
        "evaluation_set_prediction",
        "evaluation_run_result",
    ]
    """Type of the dataset"""

    version: str
    """Version number of the dataset"""
