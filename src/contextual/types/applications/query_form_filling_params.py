# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["QueryFormFillingParams", "Query"]


class QueryFormFillingParams(TypedDict, total=False):
    queries: Required[Iterable[Query]]
    """Queries used to fill the form"""

    scope_metadata: Required[str]
    """Scope of the form filling.

    This is the metadata that is used to determine the form filling strategy
    """


class Query(TypedDict, total=False):
    field: Required[str]

    instructions: Required[str]
