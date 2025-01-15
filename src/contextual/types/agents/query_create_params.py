# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryCreateParams", "Message"]


class QueryCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Messages sent so far in the conversation, ending in the latest user message.

    Add multiple objects to provide conversation history. Last message in the list
    must be a `user`-sent message (i.e. `role` equals `"user"`).
    """

    retrievals_only: bool
    """Set to `true` to skip generation of the response."""

    conversation_id: str
    """An optional alternative to providing message history in the `messages` field.

    If provided, all messages in the `messages` list prior to the latest user-sent
    query will be ignored.
    """

    llm_model_id: str
    """Model ID of the specific fine-tuned or aligned LLM model to use.

    Defaults to base model if not specified.
    """

    stream: bool
    """Set to `true` to receive a streamed response"""


class Message(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "system", "assistant"]]
    """Role of sender"""
