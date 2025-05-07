# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ListEvaluationJobsResponse", "EvaluationRound"]


class EvaluationRound(BaseModel):
    id: str
    """ID of the evaluation round"""

    created_at: datetime
    """Timestamp indicating when the evaluation round was created"""

    status: Literal[
        "pending",
        "processing",
        "retrying",
        "completed",
        "failed",
        "cancelled",
        "failed_to_provision",
        "generating_data",
        "training_in_progress",
        "failed_to_generate_data",
        "provisioning",
    ]
    """Status of the evaluation round"""

    user_email: str
    """Email of the user who launched the evaluation round"""

    finished_at: Optional[datetime] = None
    """Timestamp indicating when the evaluation round finished processing"""

    notes: Optional[str] = None
    """User notes for the evaluation job"""

    num_failed_predictions: Optional[int] = None
    """Number of predictions that failed during the evaluation round"""

    num_predictions: Optional[int] = None
    """Total number of predictions made during the evaluation round"""

    num_processed_predictions: Optional[int] = None
    """Number of predictions that have been processed during the evaluation round"""

    num_successful_predictions: Optional[int] = None
    """Number of predictions that were successful during the evaluation round"""

    processing_started_at: Optional[datetime] = None
    """Timestamp indicating when the evaluation round started processing"""

    results_dataset_name: Optional[str] = None
    """Name of the dataset with the evaluation results"""

    summary_results: Optional[object] = None
    """Score of the evaluation round"""


class ListEvaluationJobsResponse(BaseModel):
    evaluation_rounds: List[EvaluationRound]
    """List of evaluation results"""
