# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "AgentMetadata",
    "AgentConfigs",
    "AgentConfigsFilterAndRerankConfig",
    "AgentConfigsGenerateResponseConfig",
    "AgentConfigsGlobalConfig",
    "AgentConfigsRetrievalConfig",
]


class AgentConfigsFilterAndRerankConfig(BaseModel):
    top_k_reranked_chunks: Optional[int] = None
    """The number of highest ranked chunks after reranking to be used"""


class AgentConfigsGenerateResponseConfig(BaseModel):
    calculate_groundedness: Optional[bool] = None
    """This parameter controls generation of groundedness scores."""

    frequency_penalty: Optional[float] = None
    """
    This parameter adjusts how the model treats repeated tokens during text
    generation.
    """

    max_new_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate in a response."""

    seed: Optional[int] = None
    """
    This parameter controls the randomness of how the model selects the next tokens
    during text generation.
    """

    temperature: Optional[float] = None
    """The sampling temperature, which affects the randomness in the response."""

    top_p: Optional[float] = None
    """
    A parameter for nucleus sampling, an alternative to `temperature` which also
    affects the randomness of the response.
    """


class AgentConfigsGlobalConfig(BaseModel):
    enable_filter: Optional[bool] = None
    """Enables filtering of retrieved chunks with a separate LLM"""

    enable_multi_turn: Optional[bool] = None
    """Enables multi-turn conversations.

    This feature is currently experimental and will be improved.
    """

    enable_rerank: Optional[bool] = None
    """Enables reranking of retrieved chunks"""


class AgentConfigsRetrievalConfig(BaseModel):
    lexical_alpha: Optional[float] = None
    """The weight of lexical search during retrieval"""

    semantic_alpha: Optional[float] = None
    """The weight of semantic search during retrieval"""

    top_k_retrieved_chunks: Optional[int] = None
    """The maximum number of retrieved chunks from the datastore."""


class AgentConfigs(BaseModel):
    filter_and_rerank_config: Optional[AgentConfigsFilterAndRerankConfig] = None
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: Optional[AgentConfigsGenerateResponseConfig] = None
    """Parameters that affect response generation"""

    global_config: Optional[AgentConfigsGlobalConfig] = None
    """Parameters that affect the agent's overall RAG workflow"""

    retrieval_config: Optional[AgentConfigsRetrievalConfig] = None
    """Parameters that affect how the agent retrieves from datastore(s)"""


class AgentMetadata(BaseModel):
    datastore_ids: List[str]
    """The IDs of the datastore(s) associated with the agent"""

    name: str
    """Name of the agent"""

    agent_configs: Optional[AgentConfigs] = None
    """The following advanced parameters are experimental and subject to change."""

    description: Optional[str] = None
    """Description of the agent"""

    filter_prompt: Optional[str] = None
    """
    The prompt to an LLM which determines whether retrieved chunks are relevant to a
    given query and filters out irrelevant chunks. This prompt is applied per chunk.
    """

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
