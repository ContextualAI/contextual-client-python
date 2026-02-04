# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ACLConfig"]


class ACLConfig(BaseModel):
    """Captures ACL configurations for an Agent"""

    acl_active: Optional[bool] = None
    """Whether to enable ACL."""

    acl_yaml: Optional[str] = None
    """The YAML file to use for ACL."""
