# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "QueryCreateParams",
    "Message",
    "DocumentsFilters",
    "DocumentsFiltersBaseMetadataFilter",
    "DocumentsFiltersCompositeMetadataFilterInput",
    "DocumentsFiltersCompositeMetadataFilterInputFilter",
    "DocumentsFiltersCompositeMetadataFilterInputFilterBaseMetadataFilter",
    "OverrideConfiguration",
    "StructuredOutput",
]


class QueryCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Messages sent so far in the conversation, ending in the latest user message.

    Add multiple objects to provide conversation history. Last message in the list
    must be a `user`-sent message (i.e. `role` equals `"user"`).
    """

    include_retrieval_content_text: bool
    """Set to `true` to include the text of the retrieved contents in the response.

    If `false`, only metadata about the retrieved contents will be included, not
    content text. This parameter is ignored if `retrievals_only` is `true`, in which
    case `content_text` will always be returned. Content text and other metadata can
    also be fetched separately using the
    `/agents/{agent_id}/query/{message_id}/retrieval/info` endpoint.
    """

    retrievals_only: bool
    """
    Set to `true` to fetch retrieval content and metadata, and then skip generation
    of the response.
    """

    conversation_id: str
    """An optional alternative to providing message history in the `messages` field.

    If provided, all messages in the `messages` list prior to the latest user-sent
    query will be ignored.
    """

    documents_filters: DocumentsFilters
    """
    Defines an Optional custom metadata filter, which can be a list of filters or
    nested filters. The expected input is a nested JSON object that can represent a
    single filter or a composite (logical) combination of filters.

    Unnested Example:

    ```json
    {
      "operator": "AND",
      "filters": [{ "field": "status", "operator": "equals", "value": "active" }]
    }
    ```

    Nested example:

    ```json
    {
      "operator": "AND",
      "filters": [
        { "field": "status", "operator": "equals", "value": "active" },
        {
          "operator": "OR",
          "filters": [
            {
              "field": "category",
              "operator": "containsany",
              "value": ["policy", "HR"]
            },
            { "field": "tags", "operator": "exists" }
          ]
        }
      ]
    }
    ```
    """

    llm_model_id: str
    """Model ID of the specific fine-tuned or aligned LLM model to use.

    Defaults to base model if not specified.
    """

    override_configuration: OverrideConfiguration
    """
    This will modify select configuration parameters for the agent during the
    response generation.
    """

    stream: bool
    """Set to `true` to receive a streamed response"""

    structured_output: StructuredOutput
    """Custom output structure format."""


class Message(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "system", "assistant", "knowledge"]]
    """Role of the sender"""


class DocumentsFiltersBaseMetadataFilter(TypedDict, total=False):
    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal[
            "equals",
            "containsany",
            "exists",
            "startswith",
            "gt",
            "gte",
            "lt",
            "lte",
            "notequals",
            "between",
            "wildcard",
        ]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


class DocumentsFiltersCompositeMetadataFilterInputFilterBaseMetadataFilter(TypedDict, total=False):
    field: Required[str]
    """Field name to search for in the metadata"""

    operator: Required[
        Literal[
            "equals",
            "containsany",
            "exists",
            "startswith",
            "gt",
            "gte",
            "lt",
            "lte",
            "notequals",
            "between",
            "wildcard",
        ]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


DocumentsFiltersCompositeMetadataFilterInputFilter: TypeAlias = Union[
    DocumentsFiltersCompositeMetadataFilterInputFilterBaseMetadataFilter, object
]


class DocumentsFiltersCompositeMetadataFilterInput(TypedDict, total=False):
    filters: Required[Iterable[DocumentsFiltersCompositeMetadataFilterInputFilter]]
    """Filters added to the query for filtering docs"""

    operator: Optional[Literal["AND", "OR", "AND_NOT"]]
    """Composite operator to be used to combine filters"""


DocumentsFilters: TypeAlias = Union[DocumentsFiltersBaseMetadataFilter, DocumentsFiltersCompositeMetadataFilterInput]


class OverrideConfiguration(TypedDict, total=False):
    enable_filter: bool
    """Override the filter_retrievals for the query.

    This will override the filter_retrievals for the agent during evaluation.
    """

    enable_rerank: bool
    """Override the rerank_retrievals for the agent during evaluation."""

    filter_model: str
    """Override the filter_model for the query.

    This will override the filter_model for the agent during evaluation.
    """

    filter_prompt: str
    """Override the filter prompt for the agent during evaluation."""

    lexical_alpha: float
    """Override the lexical_alpha for the agent during evaluation."""

    max_new_tokens: int
    """Override the max new tokens for the agent during evaluation."""

    model: str
    """Override the model for the agent during evaluation."""

    rerank_instructions: str
    """Override the rerank_instructions for the agent during evaluation."""

    reranker: str
    """Override the reranker for the agent during evaluation."""

    reranker_score_filter_threshold: float
    """Override the reranker_score_filter_threshold for the agent during evaluation."""

    semantic_alpha: float
    """Override the semantic_alpha for the agent during evaluation."""

    system_prompt: str
    """Override the system prompt for the agent during evaluation."""

    temperature: float
    """Override the temperature for the query.

    This will override the temperature for the agent during evaluation.
    """

    top_k_reranked_chunks: int
    """Override the rerank_top_k for the query.

    This will override the rerank_top_k for the agent during evaluation.
    """

    top_k_retrieved_chunks: int
    """Override the top_k for the query.

    This will override the top_k for the agent during evaluation.
    """

    top_p: float
    """Override the top_p for the query.

    This will override the top_p for the agent during evaluation.
    """


class StructuredOutput(TypedDict, total=False):
    json_schema: Required[object]
    """The output json structure."""

    type: Literal["JSON"]
    """Type of the structured output. The default is JSON"""
