# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentMetadata"]


class AgentMetadata(BaseModel):
    datastore_ids: List[str]
    """The IDs of the datastore(s) associated with the agent"""

    name: str
    """Name of the agent"""

    description: Optional[str] = None
    """Description of the agent"""

    llm_model_id: Optional[str] = None
    """The model ID to use for generation.

    Tuned models can only be used for the agents on which they were tuned. If no
    model is specified, the default model is used. Set to `default` to switch from a
    tuned model to the default model.
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
