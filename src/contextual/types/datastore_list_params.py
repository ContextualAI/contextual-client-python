# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DatastoreListParams"]


class DatastoreListParams(TypedDict, total=False):
    application_id: str
    """ID of the application used to filter datastores.

    If provided, only datastores linked to this application will be returned.
    """

    cursor: str
    """
    Cursor from the previous call to list datastores, used to retrieve the next set
    of results
    """

    limit: int
    """Maximum number of datastores to return"""
