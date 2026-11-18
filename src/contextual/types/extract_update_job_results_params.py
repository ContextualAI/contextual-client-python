# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ExtractUpdateJobResultsParams"]


class ExtractUpdateJobResultsParams(TypedDict, total=False):
    results: Required[Dict[str, object]]
    """Extracted results conforming to the provided JSON Schema."""
