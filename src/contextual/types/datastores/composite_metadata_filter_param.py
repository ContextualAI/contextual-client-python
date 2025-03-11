# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict, TypeAliasType

from ..._utils import PropertyInfo
from ..._compat import PYDANTIC_V2

__all__ = ["CompositeMetadataFilterParam", "Filter", "FilterBaseMetadataFilter"]


class FilterBaseMetadataFilter(TypedDict, total=False):
    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal["equals", "containsany", "exists", "startswith", "gt", "gte", "lt", "lte", "notequals", "between"]
    ]
    """Operator to be used for the filter."""

    value: Annotated[
        Union[
            str,
            Union[str, datetime],
            float,
            bool,
            Iterable[object],
            Iterable[object],
            Iterable[object],
            Iterable[object],
            Iterable[object],
        ],
        PropertyInfo(format="iso8601"),
    ]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


if TYPE_CHECKING or PYDANTIC_V2:
    Filter = TypeAliasType("Filter", Union[FilterBaseMetadataFilter, "CompositeMetadataFilterParam"])
else:
    Filter: TypeAlias = Union[FilterBaseMetadataFilter, "CompositeMetadataFilterParam"]


class CompositeMetadataFilterParam(TypedDict, total=False):
    filters: Required[Iterable[Filter]]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]]
    """Composite operator to be used to combine filters"""
