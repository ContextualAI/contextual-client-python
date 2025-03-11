# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["DocumentIngestParams"]


class DocumentIngestParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to ingest."""

    metadata: str
    """Metadata in `JSON` format.

    Metadata should be passed as a nested dictionary structure where:

    - The **metadata type** `custom_metadata` is mapped to a dictionary. - The
      **dictionary keys** represent metadata attributes. - The **values** can be of
      type `str`, `bool`, `float`, or `int`.

    **Example Metadata JSON:**

    ```json
    {
      "metadata": {
        "custom_metadata": {
          "customKey1": "value3",
          "_filterKey": "filterValue3"
        }
      }
    }
    ```
    """
