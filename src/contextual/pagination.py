# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncDatastoresListPagination",
    "AsyncDatastoresListPagination",
    "SyncDatastoresDocumentsListPagination",
    "AsyncDatastoresDocumentsListPagination",
    "SyncApplicationsListPagination",
    "AsyncApplicationsListPagination",
]

_T = TypeVar("_T")


class SyncDatastoresListPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    datastores: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        datastores = self.datastores
        if not datastores:
            return []
        return datastores

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncDatastoresListPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    datastores: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        datastores = self.datastores
        if not datastores:
            return []
        return datastores

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncDatastoresDocumentsListPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncDatastoresDocumentsListPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncApplicationsListPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    applications: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        applications = self.applications
        if not applications:
            return []
        return applications

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncApplicationsListPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    applications: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        applications = self.applications
        if not applications:
            return []
        return applications

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
