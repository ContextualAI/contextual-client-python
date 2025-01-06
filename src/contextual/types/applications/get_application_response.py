# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GetApplicationResponse"]


class GetApplicationResponse(BaseModel):
    datastore_ids: List[str]
    """The IDs of the datastore associated with the application"""

    name: str
    """Name of the application"""

    description: Optional[str] = None
    """Description of the application"""

    llm_model_id: Optional[str] = None
    """Optional model ID of a tuned model to use for generation.

    Model must have been tuned on this application; tuned models cannot be used
    across applications. Uses default model if none is specified. Set to `default`
    to deactivate the tuned model and use the default model.
    """

    suggested_queries: Optional[List[str]] = None
    """These queries will show up as suggestions when users load the app.

    We recommend including common queries that users will ask, as well as complex
    queries so users understand the types of complex queries the system can handle.
    """

    system_prompt: Optional[str] = None
    """Instructions that your RAG system references when generating responses.

    Note that we do not guarantee that the system will follow these instructions
    exactly.
    """
