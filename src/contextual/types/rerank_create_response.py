# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RerankCreateResponse", "Result"]


class Result(BaseModel):
    index: int
    """Index of the document in the input list, starting with 0"""

    relevance_score: float
    """
    Relevance scores assess how likely a document is to have information that is
    helpful to answer the query. Our model outputs the scores in a wide range, and
    we normalize scores to a 0-1 scale and truncate the response to 8 decimal
    places. Our reranker is designed for RAG, so its purpose is to check whether a
    document has information that is helpful to answer the query. A reranker that is
    designed for direct Q&A (Question & Answer) would behave differently.
    """


class RerankCreateResponse(BaseModel):
    results: List[Result]
    """
    The ranked list of documents containing the index of the document and the
    relevance score, sorted by relevance score.
    """
