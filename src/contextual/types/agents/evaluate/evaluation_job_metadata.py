# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["EvaluationJobMetadata", "JobMetadata"]


class JobMetadata(BaseModel):
    num_failed_predictions: Optional[int] = None
    """Number of predictions that failed during the evaluation job"""

    num_predictions: Optional[int] = None
    """Total number of predictions made during the evaluation job"""

    num_processed_predictions: Optional[int] = None
    """Number of predictions that were processed during the evaluation job"""

    num_successful_predictions: Optional[int] = None
    """Number of predictions that were successful during the evaluation job"""


class EvaluationJobMetadata(BaseModel):
    dataset_name: str
    """Dataset name containing the individual results of the evaluation round"""

    job_metadata: JobMetadata
    """
    Metadata of the evaluation round with the number of predictions, failed
    predictions, and successful predictions.
    """

    metrics: object
    """Results of the evaluation round, grouped by each metric"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Status of the evaluation round"""
