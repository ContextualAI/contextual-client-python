# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParseJobsResponse", "Job"]


class Job(BaseModel):
    id: str
    """Unique ID of the parse job"""

    file_name: str
    """The name of the file that was uploaded for parsing"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """The current status of the parse job"""


class ParseJobsResponse(BaseModel):
    jobs: List[Job]
    """List of parse jobs"""

    total_jobs: int
    """Total number of parse jobs"""
