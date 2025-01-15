# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._compat import PYDANTIC_V2, ConfigDict
from ...._models import BaseModel

__all__ = ["ListTuneJobsResponse", "Job"]


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

    model_id: Optional[str] = None
    """ID of the trained model.

    Omitted if the tuning job failed or is still in progress.
    """

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ListTuneJobsResponse(BaseModel):
    jobs: List[Job]
    """List of tune jobs"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination.

    Omitted if there are no more specialization jobs.
    """

    total_count: Optional[int] = None
    """Total number of available specialization jobs"""
