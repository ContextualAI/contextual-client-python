# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ApplicationCreateParams"]


class ApplicationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the application"""

    datastore_ids: List[str]
    """The IDs of the datastore associated with the application.

    Provide at most one datastore. Leave empty to automatically create a new
    datastore.
    """

    description: str
    """Description of the application"""

    suggested_queries: List[str]
    """These queries will show up as suggestions when users load the app.

    We recommend including common queries that users will ask, as well as complex
    queries so users understand the types of complex queries the system can handle.
    """

    system_prompt: str
    """Instructions that your RAG system references when generating responses.

    Note that we do not guarantee that the system will follow these instructions
    exactly.
    """
