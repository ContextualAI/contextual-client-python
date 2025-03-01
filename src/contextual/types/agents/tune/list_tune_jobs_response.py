# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .tune_job_metadata import TuneJobMetadata

__all__ = ["ListTuneJobsResponse"]


class ListTuneJobsResponse(BaseModel):
    jobs: List[TuneJobMetadata]
    """List of fine-tuning jobs for the agent"""

    total_count: int
    """Total number of jobs associated with the agent"""
