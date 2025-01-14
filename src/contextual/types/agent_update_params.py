# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    datastore_ids: List[str]
    """IDs of the datastore to associate with the agent."""

    llm_model_id: str
    """Optional model ID of a tuned model to use for generation.

    Model must have been tuned on this agent; tuned models cannot be used across
    agents. Uses default model if none is specified. Set to `default` to deactivate
    the tuned model and use the default model.
    """

    suggested_queries: List[str]
    """
    These queries will show up as suggestions in the Contextual UI when users load
    the agent. We recommend including common queries that users will ask, as well as
    complex queries so users understand the types of complex queries the system can
    handle.
    """

    system_prompt: str
    """Instructions that your agent references when generating responses.

    Note that we do not guarantee that the system will follow these instructions
    exactly.
    """
