# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .unstructured_datastore_config_model_param import UnstructuredDatastoreConfigModelParam

__all__ = ["DatastoreUpdateParams"]


class DatastoreUpdateParams(TypedDict, total=False):
    configuration: UnstructuredDatastoreConfigModelParam
    """Configuration of the datastore.

    If not provided, current configuration is retained.
    """

    name: str
    """Name of the datastore"""
