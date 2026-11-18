# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BillingListTopUpsResponse", "TopUp"]


class TopUp(BaseModel):
    """Individual top-up entry"""

    amount: float
    """Amount of the top-up"""

    created_at: datetime
    """Date when the top-up was created"""

    description: str
    """Description of the top-up"""

    ending_balance: float
    """Ending balance after the top-up"""

    starting_balance: float
    """Starting balance before the top-up"""


class BillingListTopUpsResponse(BaseModel):
    """Response to GET /billing/free-credit request"""

    cursor: Optional[str] = None
    """Cursor for next page"""

    has_more: bool
    """Whether there are more top-ups to fetch"""

    top_ups: List[TopUp]
    """List of top-ups"""
