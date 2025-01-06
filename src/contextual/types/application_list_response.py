# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ApplicationListResponse"]


class ApplicationListResponse(BaseModel):
    id: str
    """ID of the application"""

    description: str
    """Description of the application"""

    name: str
    """Name of the application"""
