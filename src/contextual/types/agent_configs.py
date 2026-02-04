# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .acl_config import ACLConfig
from .global_config import GlobalConfig
from .retrieval_config import RetrievalConfig
from .translation_config import TranslationConfig
from .reformulation_config import ReformulationConfig
from .generate_response_config import GenerateResponseConfig

__all__ = ["AgentConfigs"]


class AgentConfigs(BaseModel):
    """Response to configs for different components"""

    acl_config: Optional[ACLConfig] = None
    """Parameters that affect the agent's ACL workflow"""

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

    translation_config: Optional[TranslationConfig] = None
    """Parameters that affect the agent's translation workflow"""


from .filter_and_rerank_config import FilterAndRerankConfig
