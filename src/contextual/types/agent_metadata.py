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
    "AgentUsages",
]


class AgentConfigsFilterAndRerankConfig(BaseModel):
    rerank_instructions: Optional[str] = None
    """Instructions that the reranker references when ranking retrievals.

    Note that we do not guarantee that the reranker will follow these instructions
    exactly. Examples: "Prioritize internal sales documents over market analysis
    reports. More recent documents should be weighted higher. Enterprise portal
    content supersedes distributor communications." and "Emphasize forecasts from
    top-tier investment banks. Recent analysis should take precedence. Disregard
    aggregator sites and favor detailed research notes over news summaries."
    """

    reranker_score_filter_threshold: Optional[float] = None
    """
    If the reranker relevance score associated with a chunk is below this threshold,
    then the chunk will be filtered out and not used for generation. Scores are
    between 0 and 1, with scores closer to 1 being more relevant. Set the value to 0
    to disable the reranker score filtering.
    """

    top_k_reranked_chunks: Optional[int] = None
    """The number of highest ranked chunks after reranking to be used"""


class AgentConfigsGenerateResponseConfig(BaseModel):
    avoid_commentary: Optional[bool] = None
    """
    Flag to indicate whether the model should avoid providing additional commentary
    in responses. Commentary is conversational in nature and does not contain
    verifiable claims; therefore, commentary is not strictly grounded in available
    context. However, commentary may provide useful context which improves the
    helpfulness of responses.
    """

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

    should_check_retrieval_need: Optional[bool] = None
    """Enables checking if retrieval is needed for the query.

    This feature is currently experimental and will be improved.
    """


class AgentConfigsRetrievalConfig(BaseModel):
    lexical_alpha: Optional[float] = None
    """The weight of lexical search during retrieval.

    Must sum to 1 with semantic_alpha.
    """

    semantic_alpha: Optional[float] = None
    """The weight of semantic search during retrieval.

    Must sum to 1 with lexical_alpha.
    """

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

    agent_configs: Optional[AgentConfigs] = None
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

    llm_model_id: Optional[str] = None
    """The model ID to use for generation.

    Tuned models can only be used for the agents on which they were tuned. If no
    model is specified, the default model is used. Set to `default` to switch from a
    tuned model to the default model.
    """

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
