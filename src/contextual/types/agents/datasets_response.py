# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DatasetsResponse", "DatasetSummary"]


class DatasetSummary(BaseModel):
    created_at: datetime
    """Timestamp indicating when the dataset was created"""

    name: str
    """Name of the dataset"""

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


class DatasetsResponse(BaseModel):
    dataset_summaries: List[DatasetSummary]

    total_count: int
    """Total number of datasets"""
