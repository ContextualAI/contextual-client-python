# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Agent"]


class Agent(BaseModel):
    id: str
    """ID of the agent"""

    description: str
    """Description of the agent"""

    name: str
    """Name of the agent"""
