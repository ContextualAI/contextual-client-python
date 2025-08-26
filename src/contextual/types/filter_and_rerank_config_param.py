# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypeAlias, TypedDict

from .datastores.base_metadata_filter_param import BaseMetadataFilterParam

__all__ = ["FilterAndRerankConfigParam", "DefaultMetadataFilters"]

DefaultMetadataFilters: TypeAlias = Union[BaseMetadataFilterParam, "CompositeMetadataFilterParam"]


class FilterAndRerankConfigParam(TypedDict, total=False):
    default_metadata_filters: DefaultMetadataFilters
    """
    Optional metadata filter which is applied while retrieving from every datastore
    linked to this agent.
    """

    per_datastore_metadata_filters: Dict[str, "CompositeMetadataFilterParam"]
    """Defines an optional custom metadata filter per datastore ID.

    Each entry in the dictionary should have a datastore UUID as the key, and the
    value should be a metadata filter definition. The filter will be applied in
    addition to filter(s) specified in `default_metadata_filters` and in the
    `documents_filters` field in the `/query` request during retrieval.
    """

    rerank_instructions: str
    """Instructions that the reranker references when ranking retrievals.

    Note that we do not guarantee that the reranker will follow these instructions
    exactly. Examples: "Prioritize internal sales documents over market analysis
    reports. More recent documents should be weighted higher. Enterprise portal
    content supersedes distributor communications." and "Emphasize forecasts from
    top-tier investment banks. Recent analysis should take precedence. Disregard
    aggregator sites and favor detailed research notes over news summaries."
    """

    reranker_score_filter_threshold: float
    """
    If the reranker relevance score associated with a chunk is below this threshold,
    then the chunk will be filtered out and not used for generation. Scores are
    between 0 and 1, with scores closer to 1 being more relevant. Set the value to 0
    to disable the reranker score filtering.
    """

    top_k_reranked_chunks: int
    """The number of highest ranked chunks after reranking to be used"""


from .datastores.composite_metadata_filter_param import CompositeMetadataFilterParam
