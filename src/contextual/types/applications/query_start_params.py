# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryStartParams", "Message"]


class QueryStartParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Message objects in the conversation"""

    conversation_id: str
    """Conversation ID.

    An optional alternative to providing message history in the `messages` field. If
    provided, history in the `messages` field will be ignored.
    """

    model_id: str
    """Model ID of the specific fine-tuned or aligned model to use.

    Defaults to base model if not specified.
    """

    stream: bool
    """Set to `true` to receive a streamed response"""


class Message(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "system", "assistant"]]
    """Role of sender"""
