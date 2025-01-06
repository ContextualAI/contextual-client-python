# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CreateApplicationOutput"]


class CreateApplicationOutput(BaseModel):
    application_id: str
    """ID of the application"""

    datastore_ids: List[str]
    """IDs of the datastores associated with the application.

    If no datastore was provided as part of the request, this is a singleton list
    containing the ID of the automatically created datastore.
    """
