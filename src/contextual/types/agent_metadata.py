# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .global_config import GlobalConfig
from .retrieval_config import RetrievalConfig
from .generate_response_config import GenerateResponseConfig

__all__ = [
    "AgentMetadata",
    "AgentConfigs",
    "AgentConfigsFilterAndRerankConfig",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFilters",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersBaseMetadataFilter",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutput",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutputFilter",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutputFilterBaseMetadataFilter",
    "AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFilters",
    "AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilter",
    "AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilterBaseMetadataFilter",
    "AgentConfigsReformulationConfig",
    "AgentUsages",
]


class AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersBaseMetadataFilter(BaseModel):
    field: str
    """Field name to search for in the metadata"""

    operator: Literal[
        "equals", "containsany", "exists", "startswith", "gt", "gte", "lt", "lte", "notequals", "between", "wildcard"
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None] = None
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


class AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutputFilterBaseMetadataFilter(
    BaseModel
):
    field: str
    """Field name to search for in the metadata"""

    operator: Literal[
        "equals", "containsany", "exists", "startswith", "gt", "gte", "lt", "lte", "notequals", "between", "wildcard"
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None] = None
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutputFilter: TypeAlias = Union[
    AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutputFilterBaseMetadataFilter, object
]


class AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutput(BaseModel):
    filters: List[AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutputFilter]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]] = None
    """Composite operator to be used to combine filters"""


AgentConfigsFilterAndRerankConfigDefaultMetadataFilters: TypeAlias = Union[
    AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersBaseMetadataFilter,
    AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterOutput,
]


class AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilterBaseMetadataFilter(BaseModel):
    field: str
    """Field name to search for in the metadata"""

    operator: Literal[
        "equals", "containsany", "exists", "startswith", "gt", "gte", "lt", "lte", "notequals", "between", "wildcard"
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None] = None
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilter: TypeAlias = Union[
    AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilterBaseMetadataFilter, object
]


class AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFilters(BaseModel):
    filters: List[AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilter]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]] = None
    """Composite operator to be used to combine filters"""


class AgentConfigsFilterAndRerankConfig(BaseModel):
    default_metadata_filters: Optional[AgentConfigsFilterAndRerankConfigDefaultMetadataFilters] = None
    """
    Optional metadata filter which is applied while retrieving from every datastore
    linked to this agent.
    """

    per_datastore_metadata_filters: Optional[
        Dict[str, AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFilters]
    ] = None
    """Defines an optional custom metadata filter per datastore ID.

    Each entry in the dictionary should have a datastore UUID as the key, and the
    value should be a metadata filter definition. The filter will be applied in
    addition to filter(s) specified in `default_metadata_filters` and in the
    `documents_filters` field in the `/query` request during retrieval.
    """

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


class AgentConfigsReformulationConfig(BaseModel):
    enable_query_decomposition: Optional[bool] = None
    """Whether to enable query decomposition."""

    enable_query_expansion: Optional[bool] = None
    """Whether to enable query expansion."""

    query_decomposition_prompt: Optional[str] = None
    """The prompt to use for query decomposition."""

    query_expansion_prompt: Optional[str] = None
    """The prompt to use for query expansion."""


class AgentConfigs(BaseModel):
    filter_and_rerank_config: Optional[AgentConfigsFilterAndRerankConfig] = None
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: Optional[GenerateResponseConfig] = None
    """Parameters that affect response generation"""

    global_config: Optional[GlobalConfig] = None
    """Parameters that affect the agent's overall RAG workflow"""

    reformulation_config: Optional[AgentConfigsReformulationConfig] = None
    """Parameters that affect the agent's query reformulation"""

    retrieval_config: Optional[RetrievalConfig] = None
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

    template_name: str
    """The template used to create this agent."""

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
