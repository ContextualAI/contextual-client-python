# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GenerateCreateParams", "ExtraBody", "Message"]


class GenerateCreateParams(TypedDict, total=False):
    api_extra_body: Required[Annotated[ExtraBody, PropertyInfo(alias="extra_body")]]
    """Extra parameters to be passed to Contextual's GLM"""

    messages: Required[Iterable[Message]]
    """List of messages in the conversation so far.

    The last message must be from the user.
    """

    model: Required[str]
    """The version of the Contextual's GLM to use. Currently, we just have "v1"."""


class ExtraBody(TypedDict, total=False):
    knowledge: Required[List[str]]
    """The knowledge sources the model can use when generating a response."""

    system_prompt: str
    """Instructions that the model follows when generating responses.

    Note that we do not guarantee that the model follows these instructions exactly.
    """


class Message(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "system", "assistant"]]
    """Role of the sender"""
