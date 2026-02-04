# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TemplateListResponse"]


class TemplateListResponse(BaseModel):
    templates: Optional[List[str]] = None
    """List of available templates."""
