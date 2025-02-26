# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateCreateParams", "Message"]


class GenerateCreateParams(TypedDict, total=False):
    knowledge: Required[List[str]]
    """The knowledge sources the model can use when generating a response."""

    messages: Required[Iterable[Message]]
    """List of messages in the conversation so far.

    The last message must be from the user.
    """

    model: Required[str]
    """The version of the Contextual's GLM to use. Currently, we just have "v1"."""

    avoid_commentary: bool
    """
    Flag to indicate whether the model should avoid providing additional commentary
    in responses. Commentary is conversational in nature and does not contain
    verifiable claims; therefore, commentary is not strictly grounded in available
    context. However, commentary may provide useful context which improves the
    helpfulness of responses.
    """

    system_prompt: str
    """Instructions that the model follows when generating responses.

    Note that we do not guarantee that the model follows these instructions exactly.
    """


class Message(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "system", "assistant", "knowledge"]]
    """Role of the sender"""
