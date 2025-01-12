# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._compat import PYDANTIC_V2, ConfigDict
from ...._models import BaseModel

__all__ = ["ModelListResponse", "Model"]


class Model(BaseModel):
    application_id: str
    """ID of the associated application"""

    created_at: datetime
    """Timestamp indicating when the model was created"""

    job_id: str
    """ID of the tuning job that produced the model"""

    model_id: str
    """ID of the registered model"""

    task_type: Literal["tune", "align"]
    """Type of specialization task that produced the model"""

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ModelListResponse(BaseModel):
    has_more: bool
    """Whether there are more models to retrieve"""

    models: List[Model]
    """List of registered models for the application"""

    total: int
    """Total number of models associated with the application"""

    next_after: Optional[str] = None
    """Identifier of the last model from the current request, used for pagination"""
