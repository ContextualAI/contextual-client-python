# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["TuneCreateParams"]


class TuneCreateParams(TypedDict, total=False):
    hyperparams_learning_rate: Annotated[float, PropertyInfo(alias="hyperparams[learning_rate]")]
    """Controls how quickly the model adapts to the training data.

    Must be greater than 0 and less than or equal to 0.1.
    """

    hyperparams_lora_alpha: Annotated[Literal[8, 16, 32, 64, 128], PropertyInfo(alias="hyperparams[lora_alpha]")]
    """Scaling factor that controls the magnitude of LoRA updates.

    Higher values lead to stronger adaptation effects. The effective learning
    strength is determined by the ratio of lora_alpha/lora_rank. Must be one of: 8,
    16, 32, 64 or 128
    """

    hyperparams_lora_dropout: Annotated[float, PropertyInfo(alias="hyperparams[lora_dropout]")]
    """
    LoRA dropout randomly disables connections during training to prevent
    overfitting and improve generalization when fine-tuning language models with
    Low-Rank Adaptation. Must be between 0 and 1 (exclusive).
    """

    hyperparams_lora_rank: Annotated[Literal[8, 16, 32, 64], PropertyInfo(alias="hyperparams[lora_rank]")]
    """Controls the capacity of the LoRA adapters. Must be one of: 8, 16, 32, or 64."""

    hyperparams_num_epochs: Annotated[int, PropertyInfo(alias="hyperparams[num_epochs]")]
    """Number of complete passes through the training dataset."""

    hyperparams_warmup_ratio: Annotated[float, PropertyInfo(alias="hyperparams[warmup_ratio]")]
    """Fraction of training steps used for learning rate warmup.

    Must be between 0 and 1 (exclusive).
    """

    metadata_file: FileTypes
    """Optional. Metadata file to use for synthetic data pipeline."""

    sdp_only: bool
    """Runs the SDP pipeline only if set to True."""

    synth_data: bool
    """Optional. Whether to generate synthetic data for training"""

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
