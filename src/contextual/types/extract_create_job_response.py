# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractCreateJobResponse"]


class ExtractCreateJobResponse(BaseModel):
    """Response model for extraction job creation."""

    created_at: str
    """Timestamp when the job was created"""

    estimated_completion: str
    """Estimated completion time"""

    job_id: str
    """Unique ID of the extraction job"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Current status of the job"""
