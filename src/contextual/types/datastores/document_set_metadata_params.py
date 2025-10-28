# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DocumentSetMetadataParams", "CustomMetadataConfig"]


class DocumentSetMetadataParams(TypedDict, total=False):
    datastore_id: Required[str]
    """Datastore ID of the datastore from which to retrieve the document"""

    custom_metadata: Dict[str, Union[bool, float, str, Iterable[float]]]
    """
    Custom metadata for the document, provided by the user at ingestion time.Must be
    a JSON-serializable dictionary with string keys and simple primitive values
    (str, int, float, bool). The total size must not exceed 2 KB.The strings with
    date format must stay in date format or be avodied if not in date format.The
    'custom_metadata.url' field is automatically included in returned attributions
    during query time, if provided.The default maximum metadata fields that can be
    used is 15, contact support if more is needed.
    """

    custom_metadata_config: Dict[str, CustomMetadataConfig]
    """
    A dictionary mapping metadata field names to the configuration to use for each
    field. If a metadata field is not present in the dictionary, the default
    configuration will be used. If the dictionary is not provided, metadata will be
    added in context for rerank and generation but will not be returned back to the
    user in retrievals in query API. Limits: - Maximum characters per metadata field
    (for prompt or rerank): **400** - Maximum number of metadata fields (for prompt
    or retrieval): **10** Contact support@contextual.ai to request quota increases.
    """


class CustomMetadataConfig(TypedDict, total=False):
    filterable: bool
    """Whether to use in filtering. Defaults to True"""

    in_chunks: bool
    """Whether to add in chunks.

    Defaults to True. The maximum amount of characters per metadata field that can
    be added to the prompt or rerank is 400. The maximum amount of metadata fields
    that can be added for prompt or retrieval is 10. Contact support@contextual.ai
    to request quota increases.
    """

    returned_in_response: bool
    """Whether to add in response. Defaults to False"""
