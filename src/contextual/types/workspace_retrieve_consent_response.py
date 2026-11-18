# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WorkspaceRetrieveConsentResponse"]


class WorkspaceRetrieveConsentResponse(BaseModel):
    """Response for the endpoint that retrieves the consent status for the workspace."""

    created_at: Optional[str] = None
    """The timestamp when the consent was granted or revoked"""

    email: Optional[str] = None
    """The email of the user who granted or revoked the consent"""

    status: str
    """The current consent status in `ConsentType`."""
