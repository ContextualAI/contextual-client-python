# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TranslationConfig"]


class TranslationConfig(BaseModel):
    """Captures Translation configurations for an Agent"""

    translate_confidence: Optional[float] = None
    """The confidence threshold for translation."""

    translate_needed: Optional[bool] = None
    """Whether to enable translation for the agent's responses."""
