# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import FileTypes

__all__ = ["TuneCreateParams"]


class TuneCreateParams(TypedDict, total=False):
    test_dataset_name: Optional[str]
    """Optional.

    `Dataset` to use for testing model checkpoints, created through the
    `/datasets/evaluate` API.
    """

    test_file: Optional[FileTypes]
    """Optional.

    Local path to the test data file. The test file should follow the same format as
    the training data file.
    """

    train_dataset_name: Optional[str]
    """`Dataset` to use for training, created through the `/datasets/tune` API.

    Either `train_dataset_name` or `training_file` must be provided, but not both.
    """

    training_file: Optional[FileTypes]
    """Local path to the training data file.

    The file should be in JSON array format, where each element of the array is a
    JSON object represents a single training example. The four required fields are
    `guideline`, `prompt`, `reference`, and `knowledge`.

    - `knowledge` (`list[str]`): Retrieved knowledge used to generate the reference
      answer. `knowledge` is a list of retrieved text chunks.

    - `reference` (`str`): The gold-standard answer to the prompt.

    - `guideline` (`str`): Guidelines for model output. If you do not have special
      guidelines for the model's output, you can use the `System Prompt` defined in
      your Agent configuration as the `guideline`.

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
