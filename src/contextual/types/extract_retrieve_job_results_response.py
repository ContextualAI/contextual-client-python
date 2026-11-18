# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractRetrieveJobResultsResponse", "ConfigExtractConfig"]


class ConfigExtractConfig(BaseModel):
    """
    Configuration for structured extraction. Most settings have sensible defaults, but you can customize them for your specific use case.
    """

    additional_instructions: Optional[str] = None
    """
    Additional instructions to the model. This is a string that will be appended to the prompt. It is useful for providing additional context or instructions to the model.
    """

    enable_agentic_array_extraction: Optional[bool] = None
    """
    If True, will use agentic array extraction to extract the array of objects when possible. Requires isolate_arrays=True in splitter_config. One can also enable agentic array extraction for specific arrays by setting agenticArrayExtractionMaxItemsPerTurn > 0 for the array in the JSON schema.
    """

    enable_thinking: Optional[bool] = None
    """Enable reasoning which can improve accuracy but increases processing time and cost."""

    model: Optional[Literal["gemini-2.5-flash", "gemini-2.5-pro", "gemini-3-pro-preview", "gemini-3-flash-preview"]] = (
        None
    )
    """
    Base model for extraction. 'gemini-2.5-flash' is faster and cheaper, while 'gemini-2.5-pro' is more accurate and expensive.
    """

    per_key_attribution: Optional[bool] = None
    """
    Set to include attributions for each extracted field including reasoning, confidence scores, and page numbers. This option increases processing time and cost.
    """

    temperature: Optional[float] = None
    """
    Sampling temperature (0.0-2.0). Lower values make output more deterministic and consistent, higher values vary more. Leave as None for model defaults.
    """


class ExtractRetrieveJobResultsResponse(BaseModel):
    """
    Response model for job results.

    The results field contains extracted data conforming to the provided JSON Schema. When per_key_attribution is enabled in ExtractConfig, primitive fields in results will be wrapped with AttributionInfo structures containing the extracted_value along with reasoning, confidence, and page location metadata.
    """

    config: Optional[ConfigExtractConfig] = None
    """Configuration used for the extraction job (model, temperature, etc.)"""

    job_id: str
    """Unique ID of the extraction job"""

    metadata: Dict[str, object]
    """
    Metadata about the extraction process. May include has_attributions boolean flag indicating if attribution data is present in results.
    """

    results: Dict[str, object]
    """
    Extracted results conforming to the provided JSON Schema. When per_key_attribution is enabled, primitive values are wrapped with AttributionInfo containing extracted_value, reasoning, confidence, and location fields.
    """

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Current status of the job"""
