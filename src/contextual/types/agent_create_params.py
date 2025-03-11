# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = [
    "AgentCreateParams",
    "AgentConfigs",
    "AgentConfigsFilterAndRerankConfig",
    "AgentConfigsGenerateResponseConfig",
    "AgentConfigsGlobalConfig",
    "AgentConfigsRetrievalConfig",
]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the agent"""

    agent_configs: AgentConfigs
    """The following advanced parameters are experimental and subject to change."""

    datastore_ids: List[str]
    """The IDs of the datastore to associate with this agent."""

    description: str
    """Description of the agent"""

    filter_prompt: str
    """
    The prompt to an LLM which determines whether retrieved chunks are relevant to a
    given query and filters out irrelevant chunks.
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


class AgentConfigsFilterAndRerankConfig(TypedDict, total=False):
    top_k_reranked_chunks: int
    """The number of highest ranked chunks after reranking to be used"""


class AgentConfigsGenerateResponseConfig(TypedDict, total=False):
    calculate_groundedness: bool
    """This parameter controls generation of groundedness scores."""

    frequency_penalty: float
    """
    This parameter adjusts how the model treats repeated tokens during text
    generation.
    """

    max_new_tokens: int
    """The maximum number of tokens the model can generate in a response."""

    seed: int
    """
    This parameter controls the randomness of how the model selects the next tokens
    during text generation.
    """

    temperature: float
    """The sampling temperature, which affects the randomness in the response."""

    top_p: float
    """
    A parameter for nucleus sampling, an alternative to `temperature` which also
    affects the randomness of the response.
    """


class AgentConfigsGlobalConfig(TypedDict, total=False):
    enable_filter: bool
    """Enables filtering of retrieved chunks with a separate LLM"""

    enable_multi_turn: bool
    """Enables multi-turn conversations.

    This feature is currently experimental and will be improved.
    """

    enable_rerank: bool
    """Enables reranking of retrieved chunks"""


class AgentConfigsRetrievalConfig(TypedDict, total=False):
    lexical_alpha: float
    """The weight of lexical search during retrieval"""

    semantic_alpha: float
    """The weight of semantic search during retrieval"""

    top_k_retrieved_chunks: int
    """The maximum number of retrieved chunks from the datastore."""


class AgentConfigs(TypedDict, total=False):
    filter_and_rerank_config: AgentConfigsFilterAndRerankConfig
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: AgentConfigsGenerateResponseConfig
    """Parameters that affect response generation"""

    global_config: AgentConfigsGlobalConfig
    """Parameters that affect the agent's overall RAG workflow"""

    retrieval_config: AgentConfigsRetrievalConfig
    """Parameters that affect how the agent retrieves from datastore(s)"""
