# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CreateAgentOutput"]


class CreateAgentOutput(BaseModel):
    id: str
    """ID of the agent"""

    datastore_ids: List[str]
    """IDs of the datastores associated with the agent.

    If no datastore was provided as part of the request, this is a singleton list
    containing the ID of the automatically created datastore.
    """
