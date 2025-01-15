# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["TuneCreateParams"]


class TuneCreateParams(TypedDict, total=False):
    training_file: Required[FileTypes]
    """Local path to the training data file.

    The file should be in JSON array format, where each element of the array is a
    JSON object represents a single training example. The four required fields are
    `guideline`, `prompt`, `response`, and `knowledge`.

    - `knowledge` field should be an array of strings, each string representing a
      piece of knowledge that the model should use to generate the response.

    - `response` field should be the model's response to the prompt.

    - `guideline` field should be a description of the expected response.

    - `prompt` field should be a question or statement that the model should respond
      to.

    Example:

    ```json
    [
      {
        "guideline": "The response should be accurate.",
        "prompt": "What was last quarter's revenue?",
        "response": "According to recent reports, the Q3 revenue was $1.2 million, a 0.1 million increase from Q2.",
        "knowledge": [
            "Quarterly report: Q3 revenue was $1.2 million.",
            "Quarterly report: Q2 revenue was $1.1 million.",
            ...
        ],
      },
      ...
    ]
    ```
    """

    model_id: str
    """ID of an existing model to tune.

    Defaults to the agent's default model if not specified.
    """

    test_file: FileTypes
    """Optional.

    Local path to the test data file. The file should follow the same format as the
    training data file.
    """
