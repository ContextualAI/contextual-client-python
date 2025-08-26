# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DocumentMetadata", "CustomMetadataConfig"]


class CustomMetadataConfig(BaseModel):
    filterable: Optional[bool] = None
    """Whether to use in filtering. Defaults to True"""

    in_chunks: Optional[bool] = None
    """Whether to add in chunks.

    Defaults to True. The maximum amount of characters per metadata field that can
    be added to the prompt or rerank is 400. The maximum amount of metadata fields
    that can be added for prompt or retrieval is 10. Contact support@contextual.ai
    to request quota increases.
    """

    returned_in_response: Optional[bool] = None
    """Whether to add in response. Defaults to False"""


class DocumentMetadata(BaseModel):
    id: str
    """ID of the document that was ingested"""

    created_at: str
    """Timestamp of when the document was created in ISO format."""

    name: str
    """User specified name of the document"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Status of this document's ingestion job"""

    custom_metadata: Optional[Dict[str, Union[bool, float, str]]] = None
    """
    Custom metadata for the document, provided by the user at ingestion time.Must be
    a JSON-serializable dictionary with string keys and simple primitive values
    (str, int, float, bool). The total size must not exceed 2 KB.The strings with
    date format must stay in date format or be avodied if not in date format.The
    'custom_metadata.url' field is automatically included in returned attributions
    during query time, if provided.The default maximum metadata fields that can be
    used is 15, contact support if more is needed.
    """

    custom_metadata_config: Optional[Dict[str, CustomMetadataConfig]] = None
    """
    A dictionary mapping metadata field names to the configuration to use for each
    field.

            - If a metadata field is not present in the dictionary, the default configuration will be used.

            - If the dictionary is not provided, metadata will be added in chunks but will not be retrievable.


            Limits: - Maximum characters per metadata field (for prompt or rerank): 400

            - Maximum number of metadata fields (for prompt or retrieval): 10


            Contact support@contextual.ai to request quota increases.
    """

    has_access: Optional[bool] = None
    """Whether the user has access to this document."""

    ingestion_config: Optional[object] = None
    """Ingestion configuration for the document when the document was ingested.

    It may be different from the current datastore configuration.
    """

    updated_at: Optional[str] = None
    """Timestamp of when the document was modified in ISO format."""
