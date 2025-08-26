# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .global_config_param import GlobalConfigParam
from .retrieval_config_param import RetrievalConfigParam
from .generate_response_config_param import GenerateResponseConfigParam

__all__ = [
    "AgentCreateParams",
    "AgentConfigs",
    "AgentConfigsFilterAndRerankConfig",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFilters",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersBaseMetadataFilter",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInput",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInputFilter",
    "AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInputFilterBaseMetadataFilter",
    "AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFilters",
    "AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilter",
    "AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilterBaseMetadataFilter",
    "AgentConfigsReformulationConfig",
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

    multiturn_system_prompt: str
    """Instructions on how the agent should handle multi-turn conversations."""

    no_retrieval_system_prompt: str
    """
    Instructions on how the agent should respond when there are no relevant
    retrievals that can be used to answer a query.
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


class AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersBaseMetadataFilter(TypedDict, total=False):
    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal[
            "equals",
            "containsany",
            "exists",
            "startswith",
            "gt",
            "gte",
            "lt",
            "lte",
            "notequals",
            "between",
            "wildcard",
        ]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


class AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInputFilterBaseMetadataFilter(
    TypedDict, total=False
):
    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal[
            "equals",
            "containsany",
            "exists",
            "startswith",
            "gt",
            "gte",
            "lt",
            "lte",
            "notequals",
            "between",
            "wildcard",
        ]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInputFilter: TypeAlias = Union[
    AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInputFilterBaseMetadataFilter, object
]


class AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInput(TypedDict, total=False):
    filters: Required[
        Iterable[AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInputFilter]
    ]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]]
    """Composite operator to be used to combine filters"""


AgentConfigsFilterAndRerankConfigDefaultMetadataFilters: TypeAlias = Union[
    AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersBaseMetadataFilter,
    AgentConfigsFilterAndRerankConfigDefaultMetadataFiltersCompositeMetadataFilterInput,
]


class AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilterBaseMetadataFilter(TypedDict, total=False):
    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal[
            "equals",
            "containsany",
            "exists",
            "startswith",
            "gt",
            "gte",
            "lt",
            "lte",
            "notequals",
            "between",
            "wildcard",
        ]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilter: TypeAlias = Union[
    AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilterBaseMetadataFilter, object
]


class AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFilters(TypedDict, total=False):
    filters: Required[Iterable[AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFiltersFilter]]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]]
    """Composite operator to be used to combine filters"""


class AgentConfigsFilterAndRerankConfig(TypedDict, total=False):
    default_metadata_filters: AgentConfigsFilterAndRerankConfigDefaultMetadataFilters
    """
    Optional metadata filter which is applied while retrieving from every datastore
    linked to this agent.
    """

    per_datastore_metadata_filters: Dict[str, AgentConfigsFilterAndRerankConfigPerDatastoreMetadataFilters]
    """Defines an optional custom metadata filter per datastore ID.

    Each entry in the dictionary should have a datastore UUID as the key, and the
    value should be a metadata filter definition. The filter will be applied in
    addition to filter(s) specified in `default_metadata_filters` and in the
    `documents_filters` field in the `/query` request during retrieval.
    """

    rerank_instructions: str
    """Instructions that the reranker references when ranking retrievals.

    Note that we do not guarantee that the reranker will follow these instructions
    exactly. Examples: "Prioritize internal sales documents over market analysis
    reports. More recent documents should be weighted higher. Enterprise portal
    content supersedes distributor communications." and "Emphasize forecasts from
    top-tier investment banks. Recent analysis should take precedence. Disregard
    aggregator sites and favor detailed research notes over news summaries."
    """

    reranker_score_filter_threshold: float
    """
    If the reranker relevance score associated with a chunk is below this threshold,
    then the chunk will be filtered out and not used for generation. Scores are
    between 0 and 1, with scores closer to 1 being more relevant. Set the value to 0
    to disable the reranker score filtering.
    """

    top_k_reranked_chunks: int
    """The number of highest ranked chunks after reranking to be used"""


class AgentConfigsReformulationConfig(TypedDict, total=False):
    enable_query_decomposition: bool
    """Whether to enable query decomposition."""

    enable_query_expansion: bool
    """Whether to enable query expansion."""

    query_decomposition_prompt: str
    """The prompt to use for query decomposition."""

    query_expansion_prompt: str
    """The prompt to use for query expansion."""


class AgentConfigs(TypedDict, total=False):
    filter_and_rerank_config: AgentConfigsFilterAndRerankConfig
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: GenerateResponseConfigParam
    """Parameters that affect response generation"""

    global_config: GlobalConfigParam
    """Parameters that affect the agent's overall RAG workflow"""

    reformulation_config: AgentConfigsReformulationConfig
    """Parameters that affect the agent's query reformulation"""

    retrieval_config: RetrievalConfigParam
    """Parameters that affect how the agent retrieves from datastore(s)"""
