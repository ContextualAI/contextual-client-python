# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["DocumentIngestParams"]


class DocumentIngestParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to ingest."""

    metadata: str
    """Metadata request in JSON format.

    `custom_metadata` is a flat dictionary containing one or more key-value pairs,
    where each value must be a primitive type (`str`, `bool`, `float`, or `int`).
    The default maximum metadata fields that can be used is 15, contact support if
    more is needed.The combined size of the metadata must not exceed **2 KB** when
    encoded as JSON.The strings with date format must stay in date format or be
    avoided if not in date format.The `custom_metadata.url` field is automatically
    included in returned attributions during query time, if provided.

    **Example Request Body:**

    ```json
    {
      "custom_metadata": {
        "topic": "science",
        "difficulty": 3
      }
    }
    ```
    """
