# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryFeedbackParams"]


class QueryFeedbackParams(TypedDict, total=False):
    feedback: Required[Literal["thumbs_up", "thumbs_down", "flagged", "removed"]]
    """Feedback to provide on the message.

    Set to "removed" to undo previously provided feedback.
    """

    message_id: Required[str]
    """ID of the message to provide feedback on."""

    content_id: str
    """Content ID to provide feedback on, if feedback is on retrieval.

    Set to None for generation feedback.
    """

    explanation: str
    """Optional explanation for the feedback."""
