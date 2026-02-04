# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DatastoreParseConfiguration"]


class DatastoreParseConfiguration(BaseModel):
    """Configuration for data extraction settings from documents at datastore level.

    Controls settings for document parsing. Includes those from `/parse` API along with some extra ingestion-only ones.
    """

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
