# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V1
from ..._models import BaseModel
from .base_metadata_filter import BaseMetadataFilter

__all__ = ["CompositeMetadataFilter", "Filter"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Filter = TypeAliasType("Filter", Union[BaseMetadataFilter, "CompositeMetadataFilter"])
else:
    Filter: TypeAlias = Union[BaseMetadataFilter, "CompositeMetadataFilter"]


class CompositeMetadataFilter(BaseModel):
    filters: List[Filter]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]] = None
    """Composite operator to be used to combine filters"""
