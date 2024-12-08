# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ListGetTuneJobResponse", "Job"]


class Job(BaseModel):
    id: str
    """ID of the tune job"""

    job_status: str
    """Status of the tune job"""

    evaluation_results: Optional[Dict[str, float]] = None
    """
    Evaluation results of the tuned model, represented as an object mapping metric
    names (strings) to their scores (floats). Omitted if the tuning job failed or is
    still in progress.
    """

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """ID of the trained model.

    Omitted if the tuning job failed or is still in progress.
    """


class ListGetTuneJobResponse(BaseModel):
    jobs: List[Job]
    """List of tune jobs"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more specialization jobs.
    """

    total_count: Optional[int] = None
    """Total number of available specialization jobs"""
