# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkspaceUpdateConsentParams"]


class WorkspaceUpdateConsentParams(TypedDict, total=False):
    type: Required[Literal["CONSENT_FULL", "CONSENT_SUPPORT", "REVOKE", "UNKNOWN"]]
    """The new consent status"""
