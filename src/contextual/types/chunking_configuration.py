# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChunkingConfiguration"]


class ChunkingConfiguration(BaseModel):
    """Configuration for document chunking settings."""

    chunking_mode: Optional[Literal["hierarchy_depth", "hierarchy_heading", "static_length", "page_level"]] = None
    """Chunking mode to use.

    Options are: `hierarchy_depth`, `hierarchy_heading`, `static_length`,
    `page_level`. `hierarchy_depth` groups chunks of the same hierarchy level or
    below, additionally merging or splitting based on length constraints.
    `hierarchy_heading` splits chunks at every heading in the document hierarchy,
    additionally merging or splitting based on length constraints. `static_length`
    creates chunks of a fixed length. `page_level` creates chunks that cannot run
    over page boundaries.
    """

    enable_hierarchy_based_contextualization: Optional[bool] = None
    """Whether to enable section-based contextualization for chunking"""

    max_chunk_length_tokens: Optional[int] = None
    """Target maximum length of text tokens chunks for chunking.

    Chunk length may exceed this value in some edge cases.
    """

    min_chunk_length_tokens: Optional[int] = None
    """Target minimum length of chunks in tokens.

    Must be at least 384 tokens less than `max_chunk_length_tokens`. Chunk length
    may be shorter than this value in some edge cases. Ignored if `chunking_mode` is
    `page_level`.
    """
