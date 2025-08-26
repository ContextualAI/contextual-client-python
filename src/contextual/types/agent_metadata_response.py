# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AgentMetadataResponse", "GetTwilightAgentResponse", "GetTwilightAgentResponseAgentUsages"]


class GetTwilightAgentResponseAgentUsages(BaseModel):
    eval: int
    """eval request count"""

    query: int
    """query request count"""

    tune: int
    """tune request count"""


class GetTwilightAgentResponse(BaseModel):
    datastore_ids: List[str]
    """The IDs of the datastore(s) associated with the agent"""

    name: str
    """Name of the agent"""

    template_name: str

    agent_configs: Optional[object] = None
    """The following advanced parameters are experimental and subject to change."""

    agent_usages: Optional[GetTwilightAgentResponseAgentUsages] = None
    """Total API request counts for the agent."""

    description: Optional[str] = None
    """Description of the agent"""


AgentMetadataResponse: TypeAlias = Union["AgentMetadata", GetTwilightAgentResponse]

from .agent_metadata import AgentMetadata
