# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RetrievalConfigParam"]


class RetrievalConfigParam(TypedDict, total=False):
    lexical_alpha: float
    """The weight of lexical search during retrieval.

    Must sum to 1 with semantic_alpha.
    """

    semantic_alpha: float
    """The weight of semantic search during retrieval.

    Must sum to 1 with lexical_alpha.
    """

    top_k_retrieved_chunks: int
    """The maximum number of retrieved chunks from the datastore."""
