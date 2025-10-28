# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentMetadata", "AgentUsages"]


class AgentUsages(BaseModel):
    eval: int
    """eval request count"""

    query: int
    """query request count"""

    tune: int
    """tune request count"""


class AgentMetadata(BaseModel):
    datastore_ids: List[str]
    """The IDs of the datastore(s) associated with the agent"""

    name: str
    """Name of the agent"""

    template_name: str
    """The template used to create this agent."""

    agent_configs: Optional["AgentConfigs"] = None
    """The following advanced parameters are experimental and subject to change."""

    agent_usages: Optional[AgentUsages] = None
    """Total API request counts for the agent."""

    description: Optional[str] = None
    """Description of the agent"""

    filter_prompt: Optional[str] = None
    """
    The prompt to an LLM which determines whether retrieved chunks are relevant to a
    given query and filters out irrelevant chunks. This prompt is applied per chunk.
    """

    multiturn_system_prompt: Optional[str] = None
    """Instructions on how the agent should handle multi-turn conversations."""

    no_retrieval_system_prompt: Optional[str] = None
    """
    Instructions on how the agent should respond when there are no relevant
    retrievals that can be used to answer a query.
    """

    suggested_queries: Optional[List[str]] = None
    """
    These queries will show up as suggestions in the Contextual UI when users load
    the agent. We recommend including common queries that users will ask, as well as
    complex queries so users understand the types of complex queries the system can
    handle. The max length of all the suggested queries is 1000.
    """

    system_prompt: Optional[str] = None
    """Instructions that your agent references when generating responses.

    Note that we do not guarantee that the system will follow these instructions
    exactly.
    """


from .agent_configs import AgentConfigs
