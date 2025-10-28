# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QueryFeedbackResponse"]


class QueryFeedbackResponse(BaseModel):
    feedback_id: str
    """ID of the submitted or updated feedback."""
