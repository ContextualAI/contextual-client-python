# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["InviteUsersResponse"]


class InviteUsersResponse(BaseModel):
    error_details: Dict[str, str]
    """
    Details of the errors occurred while inviting users, where keys are the emails
    and values are the error messages
    """

    invited_user_emails: List[str]
    """List of emails of the invited users"""
