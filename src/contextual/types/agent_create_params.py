# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the agent"""

    agent_configs: "AgentConfigsParam"
    """The following advanced parameters are experimental and subject to change."""

    datastore_ids: SequenceNotStr[str]
    """The IDs of the datastore to associate with this agent."""

    description: str
    """Description of the agent"""

    filter_prompt: str
    """
    The prompt to an LLM which determines whether retrieved chunks are relevant to a
    given query and filters out irrelevant chunks.
    """

    multiturn_system_prompt: str
    """Instructions on how the agent should handle multi-turn conversations."""

    no_retrieval_system_prompt: str
    """
    Instructions on how the agent should respond when there are no relevant
    retrievals that can be used to answer a query.
    """

    suggested_queries: SequenceNotStr[str]
    """
    These queries will show up as suggestions in the Contextual UI when users load
    the agent. We recommend including common queries that users will ask, as well as
    complex queries so users understand the types of complex queries the system can
    handle. The max length of all the suggested queries is 1000.
    """

    system_prompt: str
    """Instructions that your agent references when generating responses.

    Note that we do not guarantee that the system will follow these instructions
    exactly.
    """


from .agent_configs_param import AgentConfigsParam
