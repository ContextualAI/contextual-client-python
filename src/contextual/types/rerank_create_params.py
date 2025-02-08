# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RerankCreateParams"]


class RerankCreateParams(TypedDict, total=False):
    documents: Required[List[str]]
    """The texts to be reranked according to their relevance to the query"""

    model: Required[str]
    """The version of the reranker to use. Currently, we just have "v1"."""

    query: Required[str]
    """The string against which documents will be ranked for relevance"""

    top_n: int
    """The number of top-ranked results to return"""
