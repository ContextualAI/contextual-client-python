# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HTMLConfigurationParam"]


class HTMLConfigurationParam(TypedDict, total=False):
    """Configuration for HTML document ingestion settings."""

    max_chunk_length_tokens: int
    """Target maximum length of text tokens chunks for chunking.

    Chunk length may exceed this value in some edge cases.
    """
