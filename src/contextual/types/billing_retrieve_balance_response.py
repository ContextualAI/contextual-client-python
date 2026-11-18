# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["BillingRetrieveBalanceResponse"]


class BillingRetrieveBalanceResponse(BaseModel):
    """Response to GET /billing/balance request"""

    balance: float
    """Balance of the user"""
