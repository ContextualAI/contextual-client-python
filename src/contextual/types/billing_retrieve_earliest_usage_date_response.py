# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from .._models import BaseModel

__all__ = ["BillingRetrieveEarliestUsageDateResponse"]


class BillingRetrieveEarliestUsageDateResponse(BaseModel):
    """Response to GET /billing/usage/earliest_date request"""

    date: Optional[datetime.date] = None
    """Earliest usage date"""
