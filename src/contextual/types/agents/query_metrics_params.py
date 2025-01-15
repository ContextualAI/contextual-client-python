# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QueryMetricsParams"]


class QueryMetricsParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters messages that are created before specified timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters messages that are created after specified timestamp."""

    limit: int
    """Limits the number of messages to return."""

    offset: int
    """Offset for pagination."""
