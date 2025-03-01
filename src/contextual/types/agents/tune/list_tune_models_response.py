# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ...._compat import PYDANTIC_V2, ConfigDict
from ...._models import BaseModel

__all__ = ["ListTuneModelsResponse", "Model"]


class Model(BaseModel):
    application_id: str
    """ID of the associated agent"""

    created_at: datetime
    """Timestamp indicating when the model was created"""

    job_id: str
    """ID of the tuning job that produced the model"""

    model_id: str
    """ID of the registered model"""

    state: Literal["active", "inactive", "pending"]
    """State of the model"""

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ListTuneModelsResponse(BaseModel):
    models: List[Model]
    """List of registered models for the agent"""

    total_count: int
    """Total number of models associated with the agent"""
