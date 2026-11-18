# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["BillingRetrieveAclUsageResponse", "Usage"]


class Usage(BaseModel):
    """
    Single day's Agent Composer usage for a specific step.

    Represents aggregated usage data for a pipeline step on a specific date, summing across all models used by that step.
    """

    date: str
    """Date in ISO format (YYYY-MM-DD)"""

    input_tokens: int
    """Total input tokens for this step"""

    output_tokens: int
    """Total output tokens for this step"""

    step_name: str
    """Name of the pipeline step"""

    total_cost: float
    """Total cost in USD for this step"""


class BillingRetrieveAclUsageResponse(BaseModel):
    """
    Response containing daily usages of advance queries grouped by steps.

    This API returns step-level breakdown of Agent Composer usage for visualization purposes. The costs in this response are already included in the ACL_COST entry from the daily_usages table and should not be double-counted.
    """

    usages: List[Usage]
    """List of Agent Composer step usages aggregated by step and date"""
