# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RetrievalConfig"]


class RetrievalConfig(BaseModel):
    lexical_alpha: Optional[float] = None
    """The weight of lexical search during retrieval.

    Must sum to 1 with semantic_alpha.
    """

    semantic_alpha: Optional[float] = None
    """The weight of semantic search during retrieval.

    Must sum to 1 with lexical_alpha.
    """

    top_k_retrieved_chunks: Optional[int] = None
    """The maximum number of retrieved chunks from the datastore."""
