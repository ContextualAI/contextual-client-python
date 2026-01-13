# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .unstructured_datastore_config_model_param import UnstructuredDatastoreConfigModelParam

__all__ = ["DatastoreCreateParams"]


class DatastoreCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the datastore"""

    configuration: UnstructuredDatastoreConfigModelParam
    """Configuration of the datastore. If not provided, default configuration is used."""
