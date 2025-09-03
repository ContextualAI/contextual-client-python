# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["RerankCreateParams"]


class RerankCreateParams(TypedDict, total=False):
    documents: Required[SequenceNotStr[str]]
    """
    The texts to be reranked according to their relevance to the query and the
    optional instruction
    """

    model: Required[str]
    """The version of the reranker to use.

    Currently, we have: "ctxl-rerank-v2-instruct-multilingual",
    "ctxl-rerank-v2-instruct-multilingual-mini", "ctxl-rerank-v1-instruct".
    """

    query: Required[str]
    """The string against which documents will be ranked for relevance"""

    instruction: str
    """
    Instructions that the reranker references when ranking documents, after
    considering relevance. We evaluated the model on instructions for recency,
    document type, source, and metadata, and it can generalize to other instructions
    as well. For instructions related to recency and timeframe, specify the
    timeframe (e.g., instead of saying "this year") because the reranker doesn't
    know the current date. Example: "Prioritize internal sales documents over market
    analysis reports. More recent documents should be weighted higher. Enterprise
    portal content supersedes distributor communications."
    """

    metadata: SequenceNotStr[str]
    """Metadata for documents being passed to the reranker.

    Must be the same length as the documents list. If a document does not have
    metadata, add an empty string.
    """

    top_n: int
    """The number of top-ranked results to return"""
