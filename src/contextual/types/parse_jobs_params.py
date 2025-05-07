# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParseJobsParams"]


class ParseJobsParams(TypedDict, total=False):
    uploaded_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
