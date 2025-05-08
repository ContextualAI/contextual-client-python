# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GenerateResponseConfig"]


class GenerateResponseConfig(BaseModel):
    avoid_commentary: Optional[bool] = None
    """
    Flag to indicate whether the model should avoid providing additional commentary
    in responses. Commentary is conversational in nature and does not contain
    verifiable claims; therefore, commentary is not strictly grounded in available
    context. However, commentary may provide useful context which improves the
    helpfulness of responses.
    """

    calculate_groundedness: Optional[bool] = None
    """This parameter controls generation of groundedness scores."""

    frequency_penalty: Optional[float] = None
    """
    This parameter adjusts how the model treats repeated tokens during text
    generation.
    """

    max_new_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate in a response."""

    seed: Optional[int] = None
    """
    This parameter controls the randomness of how the model selects the next tokens
    during text generation.
    """

    temperature: Optional[float] = None
    """The sampling temperature, which affects the randomness in the response."""

    top_p: Optional[float] = None
    """
    A parameter for nucleus sampling, an alternative to `temperature` which also
    affects the randomness of the response.
    """
