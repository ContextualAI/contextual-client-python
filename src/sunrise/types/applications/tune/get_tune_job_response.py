# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["GetTuneJobResponse"]


class GetTuneJobResponse(BaseModel):
    job_status: str
    """Status of the tune job"""

    evaluation_results: Optional[Dict[str, float]] = None
    """
    Evaluation results of the tuned model, represented as an object mapping metric
    names (strings) to their scores (floats). Omitted if the tuning job failed or is
    still in progress.
    """

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """ID of the trained model.

    Omitted if the tuning job failed or is still in progress.
    """
