# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncDatastoresPage",
    "AsyncDatastoresPage",
    "SyncDocumentsPage",
    "AsyncDocumentsPage",
    "SyncUsersPage",
    "AsyncUsersPage",
    "SyncPage",
    "AsyncPage",
]

_T = TypeVar("_T")


class SyncDatastoresPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
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


class AsyncDatastoresPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
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


class SyncDocumentsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
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


class AsyncDocumentsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
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


class SyncUsersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    users: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        users = self.users
        if not users:
            return []
        return users

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncUsersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    users: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        users = self.users
        if not users:
            return []
        return users

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    agents: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        agents = self.agents
        if not agents:
            return []
        return agents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    agents: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        agents = self.agents
        if not agents:
            return []
        return agents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
