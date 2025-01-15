# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LMUnitCreateParams"]


class LMUnitCreateParams(TypedDict, total=False):
    query: Required[str]
    """The prompt to which the model responds"""

    response: Required[str]
    """The model response to evaluate"""

    unit_test: Required[str]
    """A natural language statement or question against which to evaluate the response"""
