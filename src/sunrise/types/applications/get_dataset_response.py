# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GetDatasetResponse"]


class GetDatasetResponse(BaseModel):
    created_at: datetime
    """Timestamp indicating when the dataset was created"""

    num_samples: int
    """Number of samples in the dataset"""

    schema_: object = FieldInfo(alias="schema")
    """Schema of the dataset"""

    status: Literal["validated", "validating", "failed"]
    """Validation status of the dataset"""

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
    """Version of the dataset"""
