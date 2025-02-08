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
    `guideline`, `prompt`, `reference`, and `knowledge`.

    - `knowledge` (`list[str]`): Retrieved knowledge used to generate the reference
      answer. `knowledge` is a list of retrieved text chunks.

    - `reference` (`str`): The gold-standard answer to the prompt.

    - `guideline` (`str`): Guidelines for model output.

    - `prompt` (`str`): Question for the model to respond to.

    Example:

    ```json
    [
      {
        "guideline": "The answer should be accurate.",
        "prompt": "What was last quarter's revenue?",
        "reference": "According to recent reports, the Q3 revenue was $1.2 million, a 0.1 million increase from Q2.",
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

    Local path to the test data file. The test file should follow the same format as
    the training data file.
    """
