# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvaluationRetrieveParams"]


class EvaluationRetrieveParams(TypedDict, total=False):
    agent_id: Required[str]
    """Agent ID associated with the evaluation dataset"""

    batch_size: int
    """Batch size for processing"""

    version: str
    """Version number of the evaluation dataset to retrieve.

    Defaults to the latest version if not specified.
    """
