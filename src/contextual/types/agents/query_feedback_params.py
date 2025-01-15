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
    """ID of the message on which to provide feedback."""

    content_id: str
    """ID of the content on which to provide feedback, if feedback is on retrieval.

    Do not set (or set to null) while providing generation feedback.
    """

    explanation: str
    """Optional explanation for the feedback."""
