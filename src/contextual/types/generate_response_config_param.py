# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GenerateResponseConfigParam"]


class GenerateResponseConfigParam(TypedDict, total=False):
    avoid_commentary: bool
    """
    Flag to indicate whether the model should avoid providing additional commentary
    in responses. Commentary is conversational in nature and does not contain
    verifiable claims; therefore, commentary is not strictly grounded in available
    context. However, commentary may provide useful context which improves the
    helpfulness of responses.
    """

    calculate_groundedness: bool
    """This parameter controls generation of groundedness scores."""

    frequency_penalty: float
    """
    This parameter adjusts how the model treats repeated tokens during text
    generation.
    """

    max_new_tokens: int
    """The maximum number of tokens the model can generate in a response."""

    seed: int
    """
    This parameter controls the randomness of how the model selects the next tokens
    during text generation.
    """

    temperature: float
    """The sampling temperature, which affects the randomness in the response."""

    top_p: float
    """
    A parameter for nucleus sampling, an alternative to `temperature` which also
    affects the randomness of the response.
    """
