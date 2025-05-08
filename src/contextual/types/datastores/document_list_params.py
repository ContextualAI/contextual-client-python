# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    cursor: str
    """
    Cursor from the previous call to list documents, used to retrieve the next set
    of results
    """

    ingestion_job_status: List[
        Literal[
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
    ]
    """
    Filters documents whose ingestion job status matches (one of) the provided
    status(es).
    """

    limit: int
    """Maximum number of documents to return"""

    uploaded_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters documents uploaded at or after specified timestamp."""

    uploaded_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters documents uploaded at or before specified timestamp."""
