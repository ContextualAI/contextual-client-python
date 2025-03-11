# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RerankCreateParams"]


class RerankCreateParams(TypedDict, total=False):
    documents: Required[List[str]]
    """
    The texts to be reranked according to their relevance to the query and the
    optional instruction
    """

    model: Required[str]
    """The version of the reranker to use.

    Currently, we just have "ctxl-rerank-en-v1-instruct".
    """

    query: Required[str]
    """The string against which documents will be ranked for relevance"""

    instruction: str
    """Instructions that the reranker references when ranking retrievals.

    We evaluated the model on instructions for recency, document type, source, and
    metadata, and it can generalize to other instructions as well. Note that we do
    not guarantee that the reranker will follow these instructions exactly.
    Examples: "Prioritize internal sales documents over market analysis reports.
    More recent documents should be weighted higher. Enterprise portal content
    supersedes distributor communications." and "Emphasize forecasts from top-tier
    investment banks. Recent analysis should take precedence. Disregard aggregator
    sites and favor detailed research notes over news summaries."
    """

    metadata: List[str]
    """Metadata for documents being passed to the reranker.

    Must be the same length as the documents list. If a document does not have
    metadata, add an empty string.
    """

    top_n: int
    """The number of top-ranked results to return"""
