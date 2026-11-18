# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    ExtractListJobsResponse,
    ExtractCreateJobResponse,
    ExtractListSchemasResponse,
    ExtractRetrieveJobResponse,
    ExtractCreateSchemaResponse,
    ExtractDeleteSchemaResponse,
    ExtractUpdateSchemaResponse,
    ExtractListDocumentsResponse,
    ExtractDeleteDocumentResponse,
    ExtractRetrieveSchemaResponse,
    ExtractUploadDocumentResponse,
    ExtractRetrieveDocumentResponse,
    ExtractRetrieveJobResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_document(self, client: ContextualAI) -> None:
        extract = client.extract.delete_document(
            "document_id",
        )
        assert_matches_type(ExtractDeleteDocumentResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_delete_document(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.delete_document(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractDeleteDocumentResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_delete_document(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.delete_document(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractDeleteDocumentResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_document(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.extract.with_raw_response.delete_document(
                "",
            )

    @parametrize
    def test_method_delete_schema(self, client: ContextualAI) -> None:
        extract = client.extract.delete_schema(
            "schema_id",
        )
        assert_matches_type(ExtractDeleteSchemaResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_delete_schema(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.delete_schema(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractDeleteSchemaResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_delete_schema(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.delete_schema(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractDeleteSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_schema(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.extract.with_raw_response.delete_schema(
                "",
            )

    @parametrize
    def test_method_list_documents(self, client: ContextualAI) -> None:
        extract = client.extract.list_documents()
        assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

    @parametrize
    def test_method_list_documents_with_all_params(self, client: ContextualAI) -> None:
        extract = client.extract.list_documents(
            limit=1,
            cursor="cursor",
            search="search",
        )
        assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_list_documents(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.list_documents()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_list_documents(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.list_documents() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_document(self, client: ContextualAI) -> None:
        extract = client.extract.retrieve_document(
            "document_id",
        )
        assert_matches_type(ExtractRetrieveDocumentResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_document(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.retrieve_document(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractRetrieveDocumentResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_document(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.retrieve_document(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractRetrieveDocumentResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_document(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.extract.with_raw_response.retrieve_document(
                "",
            )

    @parametrize
    def test_method_list_jobs(self, client: ContextualAI) -> None:
        extract = client.extract.list_jobs()
        assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

    @parametrize
    def test_method_list_jobs_with_all_params(self, client: ContextualAI) -> None:
        extract = client.extract.list_jobs(
            limit=1,
            cursor="cursor",
            job_status="job_status",
            search="search",
        )
        assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_list_jobs(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.list_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_list_jobs(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.list_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_job(self, client: ContextualAI) -> None:
        extract = client.extract.retrieve_job(
            "job_id",
        )
        assert_matches_type(ExtractRetrieveJobResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_job(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractRetrieveJobResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_job(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractRetrieveJobResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_job(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.with_raw_response.retrieve_job(
                "",
            )

    @parametrize
    def test_method_retrieve_job_results(self, client: ContextualAI) -> None:
        extract = client.extract.retrieve_job_results(
            "job_id",
        )
        assert_matches_type(ExtractRetrieveJobResultsResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_job_results(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.retrieve_job_results(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractRetrieveJobResultsResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_job_results(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.retrieve_job_results(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractRetrieveJobResultsResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_job_results(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.with_raw_response.retrieve_job_results(
                "",
            )

    @parametrize
    def test_method_list_schemas(self, client: ContextualAI) -> None:
        extract = client.extract.list_schemas()
        assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

    @parametrize
    def test_method_list_schemas_with_all_params(self, client: ContextualAI) -> None:
        extract = client.extract.list_schemas(
            limit=1,
            cursor="cursor",
            search="search",
        )
        assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_list_schemas(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.list_schemas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_list_schemas(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.list_schemas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_schema(self, client: ContextualAI) -> None:
        extract = client.extract.retrieve_schema(
            "schema_id",
        )
        assert_matches_type(ExtractRetrieveSchemaResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_schema(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.retrieve_schema(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractRetrieveSchemaResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_schema(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.retrieve_schema(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractRetrieveSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_schema(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.extract.with_raw_response.retrieve_schema(
                "",
            )

    @parametrize
    def test_method_upload_document(self, client: ContextualAI) -> None:
        extract = client.extract.upload_document(
            file=b"raw file contents",
        )
        assert_matches_type(ExtractUploadDocumentResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_upload_document(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.upload_document(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractUploadDocumentResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_upload_document(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.upload_document(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractUploadDocumentResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_job(self, client: ContextualAI) -> None:
        extract = client.extract.create_job(
            document_id="document_id",
            schema_id="schema_id",
        )
        assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

    @parametrize
    def test_method_create_job_with_all_params(self, client: ContextualAI) -> None:
        extract = client.extract.create_job(
            document_id="document_id",
            schema_id="schema_id",
            config={},
            stream=True,
        )
        assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_create_job(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.create_job(
            document_id="document_id",
            schema_id="schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_create_job(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.create_job(
            document_id="document_id",
            schema_id="schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_schema(self, client: ContextualAI) -> None:
        extract = client.extract.create_schema(
            name="name",
            schema_definition={},
        )
        assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

    @parametrize
    def test_method_create_schema_with_all_params(self, client: ContextualAI) -> None:
        extract = client.extract.create_schema(
            name="name",
            description="description",
            schema_definition={},
            metadata={},
        )
        assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_create_schema(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.create_schema(
            name="name",
            schema_definition={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_create_schema(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.create_schema(
            name="name",
            schema_definition={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_job_results(self, client: ContextualAI) -> None:
        extract = client.extract.update_job_results(
            "job_id",
            results={},
        )
        assert_matches_type(object, extract, path=["response"])

    @parametrize
    def test_raw_response_update_job_results(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.update_job_results(
            "job_id",
            results={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(object, extract, path=["response"])

    @parametrize
    def test_streaming_response_update_job_results(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.update_job_results(
            "job_id",
            results={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(object, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_job_results(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.with_raw_response.update_job_results(
                "",
                results={},
            )

    @parametrize
    def test_method_update_schema(self, client: ContextualAI) -> None:
        extract = client.extract.update_schema(
            "schema_id",
        )
        assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

    @parametrize
    def test_method_update_schema_with_all_params(self, client: ContextualAI) -> None:
        extract = client.extract.update_schema(
            "schema_id",
            name="name",
            description="description",
            schema_definition={},
            metadata={},
        )
        assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_update_schema(self, client: ContextualAI) -> None:
        response = client.extract.with_raw_response.update_schema(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_update_schema(self, client: ContextualAI) -> None:
        with client.extract.with_streaming_response.update_schema(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_schema(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.extract.with_raw_response.update_schema(
                "",
            )


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete_document(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.delete_document(
            "document_id",
        )
        assert_matches_type(ExtractDeleteDocumentResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_delete_document(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.delete_document(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractDeleteDocumentResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_delete_document(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.delete_document(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractDeleteDocumentResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_document(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.extract.with_raw_response.delete_document(
                "",
            )

    @parametrize
    async def test_method_delete_schema(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.delete_schema(
            "schema_id",
        )
        assert_matches_type(ExtractDeleteSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_delete_schema(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.delete_schema(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractDeleteSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_delete_schema(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.delete_schema(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractDeleteSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_schema(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.extract.with_raw_response.delete_schema(
                "",
            )

    @parametrize
    async def test_method_list_documents(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.list_documents()
        assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

    @parametrize
    async def test_method_list_documents_with_all_params(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.list_documents(
            limit=1,
            cursor="cursor",
            search="search",
        )
        assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_list_documents(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.list_documents()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_list_documents(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.list_documents() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractListDocumentsResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_document(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.retrieve_document(
            "document_id",
        )
        assert_matches_type(ExtractRetrieveDocumentResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_document(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.retrieve_document(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractRetrieveDocumentResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_document(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.retrieve_document(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractRetrieveDocumentResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_document(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.extract.with_raw_response.retrieve_document(
                "",
            )

    @parametrize
    async def test_method_list_jobs(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.list_jobs()
        assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

    @parametrize
    async def test_method_list_jobs_with_all_params(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.list_jobs(
            limit=1,
            cursor="cursor",
            job_status="job_status",
            search="search",
        )
        assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_list_jobs(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.list_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_list_jobs(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.list_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractListJobsResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_job(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.retrieve_job(
            "job_id",
        )
        assert_matches_type(ExtractRetrieveJobResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_job(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractRetrieveJobResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_job(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractRetrieveJobResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_job(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.with_raw_response.retrieve_job(
                "",
            )

    @parametrize
    async def test_method_retrieve_job_results(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.retrieve_job_results(
            "job_id",
        )
        assert_matches_type(ExtractRetrieveJobResultsResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_job_results(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.retrieve_job_results(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractRetrieveJobResultsResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_job_results(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.retrieve_job_results(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractRetrieveJobResultsResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_job_results(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.with_raw_response.retrieve_job_results(
                "",
            )

    @parametrize
    async def test_method_list_schemas(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.list_schemas()
        assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

    @parametrize
    async def test_method_list_schemas_with_all_params(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.list_schemas(
            limit=1,
            cursor="cursor",
            search="search",
        )
        assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_list_schemas(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.list_schemas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_list_schemas(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.list_schemas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractListSchemasResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_schema(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.retrieve_schema(
            "schema_id",
        )
        assert_matches_type(ExtractRetrieveSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_schema(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.retrieve_schema(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractRetrieveSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_schema(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.retrieve_schema(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractRetrieveSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_schema(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.extract.with_raw_response.retrieve_schema(
                "",
            )

    @parametrize
    async def test_method_upload_document(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.upload_document(
            file=b"raw file contents",
        )
        assert_matches_type(ExtractUploadDocumentResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_upload_document(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.upload_document(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractUploadDocumentResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_upload_document(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.upload_document(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractUploadDocumentResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_job(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.create_job(
            document_id="document_id",
            schema_id="schema_id",
        )
        assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

    @parametrize
    async def test_method_create_job_with_all_params(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.create_job(
            document_id="document_id",
            schema_id="schema_id",
            config={},
            stream=True,
        )
        assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_create_job(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.create_job(
            document_id="document_id",
            schema_id="schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_create_job(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.create_job(
            document_id="document_id",
            schema_id="schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractCreateJobResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_schema(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.create_schema(
            name="name",
            schema_definition={},
        )
        assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_method_create_schema_with_all_params(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.create_schema(
            name="name",
            description="description",
            schema_definition={},
            metadata={},
        )
        assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_create_schema(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.create_schema(
            name="name",
            schema_definition={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_create_schema(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.create_schema(
            name="name",
            schema_definition={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractCreateSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_job_results(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.update_job_results(
            "job_id",
            results={},
        )
        assert_matches_type(object, extract, path=["response"])

    @parametrize
    async def test_raw_response_update_job_results(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.update_job_results(
            "job_id",
            results={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(object, extract, path=["response"])

    @parametrize
    async def test_streaming_response_update_job_results(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.update_job_results(
            "job_id",
            results={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(object, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_job_results(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.with_raw_response.update_job_results(
                "",
                results={},
            )

    @parametrize
    async def test_method_update_schema(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.update_schema(
            "schema_id",
        )
        assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_method_update_schema_with_all_params(self, async_client: AsyncContextualAI) -> None:
        extract = await async_client.extract.update_schema(
            "schema_id",
            name="name",
            description="description",
            schema_definition={},
            metadata={},
        )
        assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_update_schema(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.extract.with_raw_response.update_schema(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_update_schema(self, async_client: AsyncContextualAI) -> None:
        async with async_client.extract.with_streaming_response.update_schema(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractUpdateSchemaResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_schema(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.extract.with_raw_response.update_schema(
                "",
            )
