# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .query_response import QueryResponse

__all__ = ["QueryFormFillingResponse"]


class QueryFormFillingResponse(BaseModel):
    responses: List[QueryResponse]
    """Attributions for the response"""
