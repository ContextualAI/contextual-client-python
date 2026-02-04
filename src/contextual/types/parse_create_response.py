# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ParseCreateResponse"]


class ParseCreateResponse(BaseModel):
    """/parse response object."""

    job_id: str
    """Unique ID of the parse job"""
