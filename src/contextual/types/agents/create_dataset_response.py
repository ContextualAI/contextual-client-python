# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreateDatasetResponse"]


class CreateDatasetResponse(BaseModel):
    name: str
    """Name of the dataset"""

    type: Literal["tuning_set", "evaluation_set", "evaluation_set_prediction", "evaluation_run_result"]
    """Type of the dataset"""

    version: str
    """Version number of the dataset"""
