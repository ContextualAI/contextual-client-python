# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["HTMLConfiguration"]


class HTMLConfiguration(BaseModel):
    """Configuration for HTML document ingestion settings."""

    max_chunk_length_tokens: Optional[int] = None
    """Target maximum length of text tokens chunks for chunking.

    Chunk length may exceed this value in some edge cases.
    """
