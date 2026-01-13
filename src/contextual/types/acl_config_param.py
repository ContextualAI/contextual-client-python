# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ACLConfigParam"]


class ACLConfigParam(TypedDict, total=False):
    """Captures ACL configurations for an Agent"""

    acl_active: bool
    """Whether to enable ACL."""

    acl_yaml: str
    """The YAML file to use for ACL."""
