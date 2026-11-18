# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["BillingRetrieveMetadataResponse"]


class BillingRetrieveMetadataResponse(BaseModel):
    """Response to GET /billing/metadata request"""

    is_auto_top_up_enabled: bool
    """Whether auto top-up is enabled"""

    is_low_balance: bool
    """Whether the user is low on balance"""
