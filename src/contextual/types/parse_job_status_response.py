# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParseJobStatusResponse"]


class ParseJobStatusResponse(BaseModel):
    file_name: str
    """The name of the file that was uploaded for parsing"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """The current status of the parse job"""
