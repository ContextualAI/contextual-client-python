# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingRetrieveBillingModeHistoryResponse", "BillingMode"]


class BillingMode(BaseModel):
    """Individual billing mode entry"""

    billing_mode: Literal["ON_DEMAND_PREPAID", "ON_DEMAND_PAY_ARREARS", "PROVISION_THROUGHPUT", "LEGACY"]
    """Billing mode"""

    date: datetime.date
    """Date (yyyy-mm-dd) when the billing mode became effective"""


class BillingRetrieveBillingModeHistoryResponse(BaseModel):
    """Response to GET /billing/billing_mode/history request"""

    billing_modes: List[BillingMode]
    """List of billing mode entries for the specified month"""
