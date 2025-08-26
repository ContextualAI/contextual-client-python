# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .global_config_param import GlobalConfigParam
from .retrieval_config_param import RetrievalConfigParam
from .generate_response_config_param import GenerateResponseConfigParam

__all__ = ["AgentConfigsParam", "ReformulationConfig"]


class ReformulationConfig(TypedDict, total=False):
    enable_query_decomposition: bool
    """Whether to enable query decomposition."""

    enable_query_expansion: bool
    """Whether to enable query expansion."""

    query_decomposition_prompt: str
    """The prompt to use for query decomposition."""

    query_expansion_prompt: str
    """The prompt to use for query expansion."""


class AgentConfigsParam(TypedDict, total=False):
    filter_and_rerank_config: "FilterAndRerankConfigParam"
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: GenerateResponseConfigParam
    """Parameters that affect response generation"""

    global_config: GlobalConfigParam
    """Parameters that affect the agent's overall RAG workflow"""

    reformulation_config: ReformulationConfig
    """Parameters that affect the agent's query reformulation"""

    retrieval_config: RetrievalConfigParam
    """Parameters that affect how the agent retrieves from datastore(s)"""


from .filter_and_rerank_config_param import FilterAndRerankConfigParam
