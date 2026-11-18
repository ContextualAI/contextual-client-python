# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillingRetrieveMonthlyUsageParams"]


class BillingRetrieveMonthlyUsageParams(TypedDict, total=False):
    month: Required[int]

    year: Required[int]

    resource_id: object
