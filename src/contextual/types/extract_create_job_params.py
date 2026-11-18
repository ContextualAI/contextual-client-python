# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExtractCreateJobParams"]


class ExtractCreateJobParams(TypedDict, total=False):
    document_id: Required[str]
    """ID of the document to extract from"""

    schema_id: Required[str]
    """ID of the schema to use for extraction"""

    config: object
    """Configuration options for the extraction process"""

    stream: bool
    """
    Whether to stream the results as they become available. If true, the response will be a stream of JSON objects.
    """
