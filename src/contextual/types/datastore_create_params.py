# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "DatastoreCreateParams",
    "Configuration",
    "ConfigurationChunking",
    "ConfigurationHTMLConfig",
    "ConfigurationParsing",
]


class DatastoreCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the datastore"""

    configuration: Configuration
    """Configuration of the datastore. If not provided, default configuration is used."""


class ConfigurationChunking(TypedDict, total=False):
    chunking_mode: Literal["hierarchy_depth", "hierarchy_heading", "static_length", "page_level"]
    """Chunking mode to use.

    Options are: `hierarchy_depth`, `hierarchy_heading`, `static_length`,
    `page_level`. `hierarchy_depth` groups chunks of the same hierarchy level or
    below, additionally merging or splitting based on length constraints.
    `hierarchy_heading` splits chunks at every heading in the document hierarchy,
    additionally merging or splitting based on length constraints. `static_length`
    creates chunks of a fixed length. `page_level` creates chunks that cannot run
    over page boundaries.
    """

    enable_hierarchy_based_contextualization: bool
    """Whether to enable section-based contextualization for chunking"""

    max_chunk_length_tokens: int
    """Target maximum length of text tokens chunks for chunking.

    Chunk length may exceed this value in some edge cases.
    """

    min_chunk_length_tokens: int
    """Target minimum length of chunks in tokens.

    Must be at least 384 tokens less than `max_chunk_length_tokens`. Chunk length
    may be shorter than this value in some edge cases. Ignored if `chunking_mode` is
    `page_level`.
    """


class ConfigurationHTMLConfig(TypedDict, total=False):
    max_chunk_length_tokens: int
    """Target maximum length of text tokens chunks for chunking.

    Chunk length may exceed this value in some edge cases.
    """


class ConfigurationParsing(TypedDict, total=False):
    enable_split_tables: bool
    """
    Whether to enable table splitting, which splits large tables into smaller tables
    with at most `max_split_table_cells` cells each. In each split table, the table
    headers are reproduced as the first row(s). This is useful for preserving
    context when tables are too large to fit into one chunk.
    """

    figure_caption_mode: Literal["default", "custom", "ignore"]
    """Mode for figure captioning.

    Options are `default`, `custom`, or `ignore`. Set to `ignore` to disable figure
    captioning. Set to `default` to use the default figure prompt, which generates a
    detailed caption for each figure. Set to `custom` to use a custom prompt.
    """

    figure_captioning_prompt: str
    """Prompt to use for generating image captions.

    Must be non-empty if `figure_caption_mode` is `custom`. Otherwise, must be null.
    """

    max_split_table_cells: int
    """Maximum number of cells for split tables.

    Ignored if `enable_split_tables` is False.
    """


class Configuration(TypedDict, total=False):
    chunking: ConfigurationChunking
    """Configuration for document chunking"""

    html_config: ConfigurationHTMLConfig
    """Configuration for HTML Extraction"""

    parsing: ConfigurationParsing
    """Configuration for document parsing"""
