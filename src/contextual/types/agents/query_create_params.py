# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["QueryCreateParams", "Message", "DocumentsFilters", "DocumentsFiltersBaseMetadataFilter", "StructuredOutput"]


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
        Literal["equals", "containsany", "exists", "startswith", "gt", "gte", "lt", "lte", "notequals", "between"]
    ]
    """Operator to be used for the filter."""

    value: Union[str, float, bool, List[Union[str, float, bool]], None]
    """The value to be searched for in the field.

    In case of exists operator, it is not needed.
    """


DocumentsFilters: TypeAlias = Union[DocumentsFiltersBaseMetadataFilter, "CompositeMetadataFilterParam"]


class StructuredOutput(TypedDict, total=False):
    json_schema: Required[object]
    """The output json structure."""

    type: Literal["JSON"]
    """Type of the structured output. The default is JSON"""


from ..datastores.composite_metadata_filter_param import CompositeMetadataFilterParam
