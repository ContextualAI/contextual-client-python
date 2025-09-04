# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from ..._compat import PYDANTIC_V1
from .base_metadata_filter_param import BaseMetadataFilterParam

__all__ = ["CompositeMetadataFilterParam", "Filter"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Filter = TypeAliasType("Filter", Union[BaseMetadataFilterParam, "CompositeMetadataFilterParam"])
else:
    Filter: TypeAlias = Union[BaseMetadataFilterParam, "CompositeMetadataFilterParam"]


class CompositeMetadataFilterParam(TypedDict, total=False):
    filters: Required[Iterable[Filter]]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]]
    """Composite operator to be used to combine filters"""
