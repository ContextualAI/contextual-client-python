# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParseJobsParams"]


class ParseJobsParams(TypedDict, total=False):
    cursor: str
    """
    Cursor from the previous call to list parse jobs, used to retrieve the next set
    of results
    """

    limit: int
    """Maximum number of parse jobs to return"""

    uploaded_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Filters to only documents uploaded to `/parse` at or after specified UTC
    timestamp. If not provided, or if the provided timestamp is before the maximum
    parse job retention period (30 days), the maximum retention period will be used
    instead.
    """
