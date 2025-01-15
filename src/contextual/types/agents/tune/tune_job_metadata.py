# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._compat import PYDANTIC_V2, ConfigDict
from ...._models import BaseModel

__all__ = ["TuneJobMetadata"]


class TuneJobMetadata(BaseModel):
    job_status: str
    """Status of the tune job.

    There are four possible statuses: 'failed', 'pending', 'processing',
    'completed'.
    """

    evaluation_results: Optional[Dict[str, float]] = None
    """
    Evaluation results of the tuned model, represented as a dictionary mapping
    metric names (strings) to their scores (floats). Omitted if the tuning job
    failed or is still in progress.
    """

    model_id: Optional[str] = None
    """ID of the trained model.

    Omitted if the tuning job failed or is still in progress.
    """

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())
