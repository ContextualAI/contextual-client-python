# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ContentListResponse", "DocumentContentEntry", "StructuredContentEntry"]


class DocumentContentEntry(BaseModel):
    content_id: str
    """ID of the content"""

    page_number: int
    """Page number of the content"""

    content_type: Optional[Literal["unstructured"]] = None


class StructuredContentEntry(BaseModel):
    content_id: str
    """ID of the content"""

    table_name: str
    """Name of the table"""

    content_type: Optional[Literal["structured"]] = None

    schema_: Optional[str] = FieldInfo(alias="schema", default=None)
    """Name of the schema of the table"""


ContentListResponse: TypeAlias = Annotated[
    Union[DocumentContentEntry, StructuredContentEntry], PropertyInfo(discriminator="content_type")
]
