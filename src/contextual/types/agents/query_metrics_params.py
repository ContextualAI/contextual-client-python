# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["QueryMetricsParams"]


class QueryMetricsParams(TypedDict, total=False):
    conversation_ids: SequenceNotStr[str]
    """Filter messages by conversation ids."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters messages that are created after the specified timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters messages that are created before specified timestamp.

    If both `created_after` and `created_before` are not provided, then
    `created_before` will be set to the current time and `created_after` will be set
    to the `created_before` - 2 days. If only `created_after` is provided, then
    `created_before` will be set to the `created_after` + 2 days. If only
    `created_before` is provided, then `created_after` will be set to the
    `created_before` - 2 days. If both `created_after` and `created_before` are
    provided, and the difference between them is more than 2 days, then
    `created_after` will be set to the `created_before` - 2 days.
    """

    limit: int
    """Limits the number of messages to return."""

    offset: int
    """Offset for pagination."""

    user_emails: SequenceNotStr[str]
    """Filter messages by users."""
