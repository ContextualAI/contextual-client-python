# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChunkUpdateContentParams"]


class ChunkUpdateContentParams(TypedDict, total=False):
    datastore_id: Required[str]
    """Datastore ID of the datastore containing the chunk"""

    content: Required[str]
    """The new content text for the chunk"""
