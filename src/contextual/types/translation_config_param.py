# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranslationConfigParam"]


class TranslationConfigParam(TypedDict, total=False):
    """Captures Translation configurations for an Agent"""

    translate_confidence: float
    """The confidence threshold for translation."""

    translate_needed: bool
    """Whether to enable translation for the agent's responses."""
