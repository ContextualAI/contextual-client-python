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
    """The version of the Contextual's GLM to use.

    Currently, we just have "ctxl-rerank-en-v1-instruct".
    """

    avoid_commentary: bool
    """
    Flag to indicate whether the model should avoid providing additional commentary
    in responses. Commentary is conversational in nature and does not contain
    verifiable claims; therefore, commentary is not strictly grounded in available
    context. However, commentary may provide useful context which improves the
    helpfulness of responses.
    """

    max_new_tokens: int
    """The maximum number of tokens that the model can generate in the response."""

    system_prompt: str
    """Instructions that the model follows when generating responses.

    Note that we do not guarantee that the model follows these instructions exactly.
    """

    temperature: float
    """The sampling temperature, which affects the randomness in the response.

    Note that higher temperature values can reduce groundedness.
    """

    top_p: float
    """
    A parameter for nucleus sampling, an alternative to temperature which also
    affects the randomness of the response. Note that higher top_p values can reduce
    groundedness.
    """


class Message(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "assistant"]]
    """Role of the sender"""
