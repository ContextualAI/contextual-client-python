# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .global_config_param import GlobalConfigParam
from .retrieval_config_param import RetrievalConfigParam
from .generate_response_config_param import GenerateResponseConfigParam

__all__ = ["AgentConfigsParam", "ACLConfig", "ReformulationConfig", "TranslationConfig"]


class ACLConfig(TypedDict, total=False):
    acl_active: bool
    """Whether to enable ACL."""

    acl_yaml: str
    """The YAML file to use for ACL."""


class ReformulationConfig(TypedDict, total=False):
    enable_query_decomposition: bool
    """Whether to enable query decomposition."""

    enable_query_expansion: bool
    """Whether to enable query expansion."""

    query_decomposition_prompt: str
    """The prompt to use for query decomposition."""

    query_expansion_prompt: str
    """The prompt to use for query expansion."""


class TranslationConfig(TypedDict, total=False):
    translate_confidence: float
    """The confidence threshold for translation."""

    translate_needed: bool
    """Whether to enable translation for the agent's responses."""


class AgentConfigsParam(TypedDict, total=False):
    acl_config: ACLConfig
    """Parameters that affect the agent's ACL workflow"""

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

    translation_config: TranslationConfig
    """Parameters that affect the agent's translation workflow"""


from .filter_and_rerank_config_param import FilterAndRerankConfigParam
