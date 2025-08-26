# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "DatastoreMetadata",
    "Configuration",
    "ConfigurationChunking",
    "ConfigurationHTMLConfig",
    "ConfigurationParsing",
    "DatastoreUsages",
]


class ConfigurationChunking(BaseModel):
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


class ConfigurationHTMLConfig(BaseModel):
    max_chunk_length_tokens: Optional[int] = None
    """Target maximum length of text tokens chunks for chunking.

    Chunk length may exceed this value in some edge cases.
    """


class ConfigurationParsing(BaseModel):
    enable_split_tables: Optional[bool] = None
    """
    Whether to enable table splitting, which splits large tables into smaller tables
    with at most `max_split_table_cells` cells each. In each split table, the table
    headers are reproduced as the first row(s). This is useful for preserving
    context when tables are too large to fit into one chunk.
    """

    figure_caption_mode: Optional[Literal["default", "custom", "ignore"]] = None
    """Mode for figure captioning.

    Options are `default`, `custom`, or `ignore`. Set to `ignore` to disable figure
    captioning. Set to `default` to use the default figure prompt, which generates a
    detailed caption for each figure. Set to `custom` to use a custom prompt.
    """

    figure_captioning_prompt: Optional[str] = None
    """Prompt to use for generating image captions.

    Must be non-empty if `figure_caption_mode` is `custom`. Otherwise, must be null.
    """

    max_split_table_cells: Optional[int] = None
    """Maximum number of cells for split tables.

    Ignored if `enable_split_tables` is False.
    """


class Configuration(BaseModel):
    chunking: Optional[ConfigurationChunking] = None
    """Configuration for document chunking"""

    html_config: Optional[ConfigurationHTMLConfig] = None
    """Configuration for HTML Extraction"""

    parsing: Optional[ConfigurationParsing] = None
    """Configuration for document parsing"""


class DatastoreUsages(BaseModel):
    size_gb: float
    """Actual size of the datastore in GB"""


class DatastoreMetadata(BaseModel):
    agent_ids: List[str]
    """List of agents using this datastore"""

    created_at: datetime
    """Timestamp of when the datastore was created"""

    name: str
    """Name of the datastore"""

    configuration: Optional[Configuration] = None
    """Configuration of the datastore. Not set if default configuration is in use."""

    datastore_type: Optional[Literal["UNSTRUCTURED"]] = None
    """Type of the datastore"""

    datastore_usages: Optional[DatastoreUsages] = None
    """Datastore usage"""
