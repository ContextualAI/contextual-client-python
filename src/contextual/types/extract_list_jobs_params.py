# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractListJobsParams"]


class ExtractListJobsParams(TypedDict, total=False):
    cursor: object

    job_status: object

    limit: int

    search: object
