# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ListEvaluationResponse", "EvaluationRound"]


class EvaluationRound(BaseModel):
    id: str
    """ID of the evaluation round"""

    created_at: datetime
    """Timestamp indicating when the evaluation round was created"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Status of the evaluation round"""

    user_email: str
    """Email of the user who launched the evaluation round"""


class ListEvaluationResponse(BaseModel):
    evaluation_rounds: List[EvaluationRound]
    """List of evaluation results"""
