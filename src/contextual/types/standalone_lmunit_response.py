# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["StandaloneLmunitResponse"]


class StandaloneLmunitResponse(BaseModel):
    score: float
    """The response is scored on a continuous scale from 1 to 5 on the unit test.

    The discrete scores 1, 2, 3, 4, and 5 roughly correspond to "Strongly fails,"
    "Fails," "Neutral," "Passes," and "Strongly passes," respectively.
    """
