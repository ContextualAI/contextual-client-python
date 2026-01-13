# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .acl_config_param import ACLConfigParam
from .global_config_param import GlobalConfigParam
from .retrieval_config_param import RetrievalConfigParam
from .translation_config_param import TranslationConfigParam
from .reformulation_config_param import ReformulationConfigParam
from .generate_response_config_param import GenerateResponseConfigParam

__all__ = ["AgentConfigsParam"]


class AgentConfigsParam(TypedDict, total=False):
    """Response to configs for different components"""

    acl_config: ACLConfigParam
    """Parameters that affect the agent's ACL workflow"""

    filter_and_rerank_config: "FilterAndRerankConfigParam"
    """Parameters that affect filtering and reranking of retrieved knowledge"""

    generate_response_config: GenerateResponseConfigParam
    """Parameters that affect response generation"""

    global_config: GlobalConfigParam
    """Parameters that affect the agent's overall RAG workflow"""

    reformulation_config: ReformulationConfigParam
    """Parameters that affect the agent's query reformulation"""

    retrieval_config: RetrievalConfigParam
    """Parameters that affect how the agent retrieves from datastore(s)"""

    translation_config: TranslationConfigParam
    """Parameters that affect the agent's translation workflow"""


from .filter_and_rerank_config_param import FilterAndRerankConfigParam
