# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .global_config_param import GlobalConfigParam
from .retrieval_config_param import RetrievalConfigParam
from .filter_and_rerank_config_param import FilterAndRerankConfigParam
from .generate_response_config_param import GenerateResponseConfigParam

__all__ = ["AgentConfigsParam"]


class AgentConfigsParam(TypedDict, total=False):
    filter_and_rerank_config: FilterAndRerankConfigParam
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: GenerateResponseConfigParam
    """Parameters that affect response generation"""

    global_config: GlobalConfigParam
    """Parameters that affect the agent's overall RAG workflow"""

    retrieval_config: RetrievalConfigParam
    """Parameters that affect how the agent retrieves from datastore(s)"""
