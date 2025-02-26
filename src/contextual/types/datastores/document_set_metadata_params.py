# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

__all__ = ["DocumentSetMetadataParams"]


class DocumentSetMetadataParams(TypedDict, total=False):
    datastore_id: Required[str]
    """Datastore ID of the datastore from which to retrieve the document"""

    custom_metadata: Dict[str, Union[bool, float, str]]
