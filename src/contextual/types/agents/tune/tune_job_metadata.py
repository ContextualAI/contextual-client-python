# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._compat import PYDANTIC_V2, ConfigDict
from ...._models import BaseModel

__all__ = ["TuneJobMetadata"]


class TuneJobMetadata(BaseModel):
    id: str
    """ID of the tune job"""

    job_status: str
    """Status of the tune job"""

    evaluation_metadata: Optional[object] = None
    """Metadata about the model evaluation, including status and results if completed."""

    model_id: Optional[str] = None
    """ID of the tuned model.

    Omitted if the tuning job failed or is still in progress.
    """

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())
