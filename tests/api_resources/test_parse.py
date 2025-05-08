# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from contextual import ContextualAI, AsyncContextualAI
from tests.utils import assert_matches_type
from contextual.types import (
    ParseJobsResponse,
    ParseCreateResponse,
    ParseJobStatusResponse,
    ParseJobResultsResponse,
)
from contextual._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ContextualAI) -> None:
        parse = client.parse.create(
            raw_file=b"raw file contents",
        )
        assert_matches_type(ParseCreateResponse, parse, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ContextualAI) -> None:
        parse = client.parse.create(
            raw_file=b"raw file contents",
            enable_document_hierarchy=True,
            enable_split_tables=True,
            figure_caption_mode="concise",
            max_split_table_cells=0,
            page_range="page_range",
            parse_mode="standard",
        )
        assert_matches_type(ParseCreateResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ContextualAI) -> None:
        response = client.parse.with_raw_response.create(
            raw_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseCreateResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ContextualAI) -> None:
        with client.parse.with_streaming_response.create(
            raw_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseCreateResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_job_results(self, client: ContextualAI) -> None:
        parse = client.parse.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

    @parametrize
    def test_method_job_results_with_all_params(self, client: ContextualAI) -> None:
        parse = client.parse.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            output_types=["markdown-document"],
        )
        assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_job_results(self, client: ContextualAI) -> None:
        response = client.parse.with_raw_response.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_job_results(self, client: ContextualAI) -> None:
        with client.parse.with_streaming_response.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_job_results(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parse.with_raw_response.job_results(
                job_id="",
            )

    @parametrize
    def test_method_job_status(self, client: ContextualAI) -> None:
        parse = client.parse.job_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParseJobStatusResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_job_status(self, client: ContextualAI) -> None:
        response = client.parse.with_raw_response.job_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseJobStatusResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_job_status(self, client: ContextualAI) -> None:
        with client.parse.with_streaming_response.job_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseJobStatusResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_job_status(self, client: ContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parse.with_raw_response.job_status(
                "",
            )

    @parametrize
    def test_method_jobs(self, client: ContextualAI) -> None:
        parse = client.parse.jobs()
        assert_matches_type(ParseJobsResponse, parse, path=["response"])

    @parametrize
    def test_method_jobs_with_all_params(self, client: ContextualAI) -> None:
        parse = client.parse.jobs(
            uploaded_after=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ParseJobsResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_jobs(self, client: ContextualAI) -> None:
        response = client.parse.with_raw_response.jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseJobsResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_jobs(self, client: ContextualAI) -> None:
        with client.parse.with_streaming_response.jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseJobsResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.create(
            raw_file=b"raw file contents",
        )
        assert_matches_type(ParseCreateResponse, parse, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.create(
            raw_file=b"raw file contents",
            enable_document_hierarchy=True,
            enable_split_tables=True,
            figure_caption_mode="concise",
            max_split_table_cells=0,
            page_range="page_range",
            parse_mode="standard",
        )
        assert_matches_type(ParseCreateResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.parse.with_raw_response.create(
            raw_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseCreateResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextualAI) -> None:
        async with async_client.parse.with_streaming_response.create(
            raw_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseCreateResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_job_results(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

    @parametrize
    async def test_method_job_results_with_all_params(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            output_types=["markdown-document"],
        )
        assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_job_results(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.parse.with_raw_response.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_job_results(self, async_client: AsyncContextualAI) -> None:
        async with async_client.parse.with_streaming_response.job_results(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseJobResultsResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_job_results(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parse.with_raw_response.job_results(
                job_id="",
            )

    @parametrize
    async def test_method_job_status(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.job_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParseJobStatusResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_job_status(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.parse.with_raw_response.job_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseJobStatusResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_job_status(self, async_client: AsyncContextualAI) -> None:
        async with async_client.parse.with_streaming_response.job_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseJobStatusResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_job_status(self, async_client: AsyncContextualAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parse.with_raw_response.job_status(
                "",
            )

    @parametrize
    async def test_method_jobs(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.jobs()
        assert_matches_type(ParseJobsResponse, parse, path=["response"])

    @parametrize
    async def test_method_jobs_with_all_params(self, async_client: AsyncContextualAI) -> None:
        parse = await async_client.parse.jobs(
            uploaded_after=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ParseJobsResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_jobs(self, async_client: AsyncContextualAI) -> None:
        response = await async_client.parse.with_raw_response.jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseJobsResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_jobs(self, async_client: AsyncContextualAI) -> None:
        async with async_client.parse.with_streaming_response.jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseJobsResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True
