# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .global_config import GlobalConfig
from .retrieval_config import RetrievalConfig
from .generate_response_config import GenerateResponseConfig

__all__ = ["AgentConfigs", "ReformulationConfig"]


class ReformulationConfig(BaseModel):
    enable_query_decomposition: Optional[bool] = None
    """Whether to enable query decomposition."""

    enable_query_expansion: Optional[bool] = None
    """Whether to enable query expansion."""

    query_decomposition_prompt: Optional[str] = None
    """The prompt to use for query decomposition."""

    query_expansion_prompt: Optional[str] = None
    """The prompt to use for query expansion."""


class AgentConfigs(BaseModel):
    filter_and_rerank_config: Optional["FilterAndRerankConfig"] = None
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: Optional[GenerateResponseConfig] = None
    """Parameters that affect response generation"""

    global_config: Optional[GlobalConfig] = None
    """Parameters that affect the agent's overall RAG workflow"""

    reformulation_config: Optional[ReformulationConfig] = None
    """Parameters that affect the agent's query reformulation"""

    retrieval_config: Optional[RetrievalConfig] = None
    """Parameters that affect how the agent retrieves from datastore(s)"""


from .filter_and_rerank_config import FilterAndRerankConfig
