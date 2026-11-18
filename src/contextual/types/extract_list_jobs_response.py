# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractListJobsResponse", "JobProgress", "JobConfigExtractConfig", "Job"]


class JobProgress(BaseModel):
    """Progress information for an extraction job."""

    completion_percentage: int
    """Overall progress percentage (0-100)"""

    current_step: str
    """Current processing stage or step description"""

    fields_processed: Optional[int] = None
    """Number of schema fields that have been processed"""

    total_fields: Optional[int] = None
    """Total number of schema fields to process"""


class JobConfigExtractConfig(BaseModel):
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


class Job(BaseModel):
    """
    Response model for job status.

    Returns basic job status and progress.
    """

    config: Optional[JobConfigExtractConfig] = None
    """Configuration used for the extraction job (model, temperature, etc.)"""

    created_at: str
    """Timestamp when the job was created"""

    current_activity: str
    """Current activity being performed"""

    document_id: str
    """ID of the document used for the extraction"""

    job_id: str
    """Unique ID of the extraction job"""

    progress: JobProgress
    """Progress information for an extraction job."""

    schema_id: str
    """ID of the schema used for the extraction"""

    status: Literal["pending", "processing", "retrying", "completed", "failed", "cancelled"]
    """Current status of the job"""


class ExtractListJobsResponse(BaseModel):
    """Response model for job listing."""

    jobs: List[Job]
    """List of jobs"""

    next_cursor: Optional[str] = None
    """Next cursor to continue pagination. Omitted if there are no more jobs to retrieve."""

    prev_cursor: Optional[str] = None
    """Previous cursor to go back in pagination. Omitted if this is the first page."""

    total_count: int
    """Total number of jobs"""
