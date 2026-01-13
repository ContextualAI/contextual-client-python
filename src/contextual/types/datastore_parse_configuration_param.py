# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DatastoreParseConfigurationParam"]


class DatastoreParseConfigurationParam(TypedDict, total=False):
    """Configuration for data extraction settings from documents at datastore level.

    Controls settings for document parsing. Includes those from `/parse` API along with some extra ingestion-only ones.
    """

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
