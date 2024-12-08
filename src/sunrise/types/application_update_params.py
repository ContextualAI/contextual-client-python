# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["ApplicationUpdateParams"]


class ApplicationUpdateParams(TypedDict, total=False):
    datastore_ids: List[str]
    """IDs of the datastore to associate with the application."""

    llm_model_id: str
    """Optional model ID of a tuned model to use for generation.

    Model must have been tuned on this application; tuned models cannot be used
    across applications. Uses default model if none is specified. Set to `default`
    to deactivate the tuned model and use the default model.
    """

    system_prompt: str
    """Instructions that your RAG system references when generating responses.

    Note that we do not guarantee that the system will follow these instructions
    exactly.
    """
