# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    datastore_ids: List[str]
    """IDs of the datastore to associate with the agent."""

    llm_model_id: str
    """The model ID to use for generation.

    Tuned models can only be used for the agents on which they were tuned. If no
    model is specified, the default model is used. Set to `default` to switch from a
    tuned model to the default model.
    """

    suggested_queries: List[str]
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
