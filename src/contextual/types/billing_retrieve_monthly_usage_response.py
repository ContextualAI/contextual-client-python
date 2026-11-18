# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingRetrieveMonthlyUsageResponse", "Usage"]


class Usage(BaseModel):
    date: datetime.date
    """Date of the usage"""

    price: float
    """Price per unit"""

    quantity: int
    """Usage quantity"""

    usage_type: Literal[
        "QUERY_REFORMULATION_INPUT_TOKEN",
        "QUERY_REFORMULATION_OUTPUT_TOKEN",
        "QUERY_EXPANSION_INPUT_TOKEN",
        "QUERY_EXPANSION_OUTPUT_TOKEN",
        "QUERY_FILTER_TOKEN",
        "QUERY_RETRIEVAL_TOKEN",
        "QUERY_RERANK_TOKEN",
        "QUERY_GENERATION_INPUT_TOKEN",
        "QUERY_GENERATION_OUTPUT_TOKEN",
        "QUERY_CONTEXTUALIZATION_TOKEN",
        "QUERY_GROUNDEDNESS_TOKEN",
        "QUERY_PLANNING_INPUT_TOKEN",
        "QUERY_PLANNING_OUTPUT_TOKEN",
        "QUERY_TRANSLATION_INPUT_TOKEN",
        "QUERY_TRANSLATION_OUTPUT_TOKEN",
        "QUERY_REQUEST",
        "TUNE_REQUEST",
        "EVAL_REQUEST",
        "INGEST_BASIC_PAGE",
        "INGEST_STANDARD_PAGE",
        "INGEST_V3_STANDARD_PAGE",
        "INGEST_V3_ADVANCED_PAGE",
        "INGEST_V3_PREMIUM_PAGE",
        "PARSE_BASIC_PAGE",
        "PARSE_STANDARD_PAGE",
        "RERANK_TOKEN",
        "RERANK_V2_MINI_TOKEN",
        "RERANK_V2_TOKEN",
        "GENERATE_INPUT_TOKEN",
        "GENERATE_OUTPUT_TOKEN",
        "LMUNIT_TOKEN",
        "ACL_COST",
        "STRUCTURED_EXTRACTION_COST",
        "STRUCTURED_EXTRACTION_INPUT_TOKENS",
        "STRUCTURED_EXTRACTION_OUTPUT_TOKENS",
        "STRUCTURED_EXTRACTION_CACHED_TOKENS",
        "STRUCTURED_EXTRACTION_REASONING_TOKENS",
    ]
    """Type of usage"""


class BillingRetrieveMonthlyUsageResponse(BaseModel):
    """Response to GET /billing/usage/monthly request"""

    usages: List[Usage]
    """List of daily usages"""
