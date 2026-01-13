# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BaseMetadataFilterParam"]


class BaseMetadataFilterParam(TypedDict, total=False):
    """Defines a custom metadata filter.

    The expected input is a dict which can have different operators, fields and values. For example:

        {"field": "title", "operator": "startswith", "value": "hr-"}

    Use **lowercase** for `value` when not using `equals` operator. For document_id and date_created the query is built using direct query without nesting.
    """

    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal[
            "equals",
            "containsany",
            "exists",
            "startswith",
            "gt",
            "gte",
            "lt",
            "lte",
            "notequals",
            "between",
            "wildcard",
        ]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, SequenceNotStr[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """
