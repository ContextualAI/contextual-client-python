# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual._utils import parse_datetime
from contextual.pagination import SyncDocumentsPage, AsyncDocumentsPage
from contextual.types.datastores import (
    DocumentMetadata,
    IngestionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ContextualAI) -> None:
        document = client.datastores.documents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncDocumentsPage[DocumentMetadata], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ContextualAI) -> None:
        document = client.datastores.documents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            ingestion_job_status=["pending"],
            limit=1,
            uploaded_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            uploaded_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncDocumentsPage[DocumentMetadata], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ContextualAI) -> None:
        response = client.datastores.documents.with_raw_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncDocumentsPage[DocumentMetadata], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ContextualAI) -> None:
        with client.datastores.documents.with_streaming_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncDocumentsPage[DocumentMetadata], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.documents.with_raw_response.list(
                datastore_id="",
            )

    @parametrize
    def test_method_delete(self, client: ContextualAI) -> None:
        document = client.datastores.documents.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, document, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ContextualAI) -> None:
        response = client.datastores.documents.with_raw_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(object, document, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ContextualAI) -> None:
        with client.datastores.documents.with_streaming_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.documents.with_raw_response.delete(
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.datastores.documents.with_raw_response.delete(
                document_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_ingest(self, client: ContextualAI) -> None:
        document = client.datastores.documents.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(IngestionResponse, document, path=["response"])

    @parametrize
    def test_method_ingest_with_all_params(self, client: ContextualAI) -> None:
        document = client.datastores.documents.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
            metadata='{"field1": "value1", "field2": "value2"}}',
        )
        assert_matches_type(IngestionResponse, document, path=["response"])

    @parametrize
    def test_raw_response_ingest(self, client: ContextualAI) -> None:
        response = client.datastores.documents.with_raw_response.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(IngestionResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_ingest(self, client: ContextualAI) -> None:
        with client.datastores.documents.with_streaming_response.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(IngestionResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_ingest(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.documents.with_raw_response.ingest(
                datastore_id="",
                file=b"raw file contents",
            )

    @parametrize
    def test_method_metadata(self, client: ContextualAI) -> None:
        document = client.datastores.documents.metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    def test_raw_response_metadata(self, client: ContextualAI) -> None:
        response = client.datastores.documents.with_raw_response.metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    def test_streaming_response_metadata(self, client: ContextualAI) -> None:
        with client.datastores.documents.with_streaming_response.metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentMetadata, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.documents.with_raw_response.metadata(
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.datastores.documents.with_raw_response.metadata(
                document_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_set_metadata(self, client: ContextualAI) -> None:
        document = client.datastores.documents.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    def test_method_set_metadata_with_all_params(self, client: ContextualAI) -> None:
        document = client.datastores.documents.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": True},
        )
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    def test_raw_response_set_metadata(self, client: ContextualAI) -> None:
        response = client.datastores.documents.with_raw_response.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    def test_streaming_response_set_metadata(self, client: ContextualAI) -> None:
        with client.datastores.documents.with_streaming_response.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentMetadata, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_metadata(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            client.datastores.documents.with_raw_response.set_metadata(
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.datastores.documents.with_raw_response.set_metadata(
                document_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncDocumentsPage[DocumentMetadata], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            ingestion_job_status=["pending"],
            limit=1,
            uploaded_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            uploaded_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncDocumentsPage[DocumentMetadata], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.documents.with_raw_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncDocumentsPage[DocumentMetadata], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.documents.with_streaming_response.list(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncDocumentsPage[DocumentMetadata], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.list(
                datastore_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, document, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.documents.with_raw_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(object, document, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.documents.with_streaming_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.delete(
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.delete(
                document_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_ingest(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(IngestionResponse, document, path=["response"])

    @parametrize
    async def test_method_ingest_with_all_params(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
            metadata='{"field1": "value1", "field2": "value2"}}',
        )
        assert_matches_type(IngestionResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.documents.with_raw_response.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(IngestionResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.documents.with_streaming_response.ingest(
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(IngestionResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_ingest(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.ingest(
                datastore_id="",
                file=b"raw file contents",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.documents.with_raw_response.metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.documents.with_streaming_response.metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentMetadata, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.metadata(
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.metadata(
                document_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_set_metadata(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    async def test_method_set_metadata_with_all_params(self, async_client: AsyncContextualAI) -> None:
        document = await async_client.datastores.documents.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": True},
        )
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    async def test_raw_response_set_metadata(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.datastores.documents.with_raw_response.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentMetadata, document, path=["response"])

    @parametrize
    async def test_streaming_response_set_metadata(self, async_client: AsyncContextualAI) -> None:
        async with async_client.datastores.documents.with_streaming_response.set_metadata(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentMetadata, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_metadata(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datastore_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.set_metadata(
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                datastore_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.datastores.documents.with_raw_response.set_metadata(
                document_id="",
                datastore_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
