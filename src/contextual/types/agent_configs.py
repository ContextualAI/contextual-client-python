# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .global_config import GlobalConfig
from .retrieval_config import RetrievalConfig
from .filter_and_rerank_config import FilterAndRerankConfig
from .generate_response_config import GenerateResponseConfig

__all__ = ["AgentConfigs"]


class AgentConfigs(BaseModel):
    filter_and_rerank_config: Optional[FilterAndRerankConfig] = None
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: Optional[GenerateResponseConfig] = None
    """Parameters that affect response generation"""

    global_config: Optional[GlobalConfig] = None
    """Parameters that affect the agent's overall RAG workflow"""

    retrieval_config: Optional[RetrievalConfig] = None
    """Parameters that affect how the agent retrieves from datastore(s)"""
