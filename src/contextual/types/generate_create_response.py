# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["GenerateCreateResponse"]


class GenerateCreateResponse(BaseModel):
    response: str
    """The model's response to the last user message."""
