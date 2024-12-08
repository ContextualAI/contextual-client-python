# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sunrise import Sunrise, AsyncSunrise
from tests.utils import assert_matches_type
from sunrise.types.applications import QueryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feedback(self, client: Sunrise) -> None:
        query = client.applications.query.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_method_feedback_with_all_params(self, client: Sunrise) -> None:
        query = client.applications.query.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: Sunrise) -> None:
        response = client.applications.query.with_raw_response.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: Sunrise) -> None:
        with client.applications.query.with_streaming_response.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(object, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: Sunrise) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.query.with_raw_response.feedback(
                application_id="",
                feedback="thumbs_up",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_start(self, client: Sunrise) -> None:
        query = client.applications.query.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Sunrise) -> None:
        query = client.applications.query.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model_id="model_id",
            stream=True,
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Sunrise) -> None:
        response = client.applications.query.with_raw_response.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Sunrise) -> None:
        with client.applications.query.with_streaming_response.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Sunrise) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.query.with_raw_response.start(
                application_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "user",
                    }
                ],
            )


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feedback(self, async_client: AsyncSunrise) -> None:
        query = await async_client.applications.query.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_method_feedback_with_all_params(self, async_client: AsyncSunrise) -> None:
        query = await async_client.applications.query.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncSunrise) -> None:
        response = await async_client.applications.query.with_raw_response.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncSunrise) -> None:
        async with async_client.applications.query.with_streaming_response.feedback(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback="thumbs_up",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(object, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncSunrise) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.query.with_raw_response.feedback(
                application_id="",
                feedback="thumbs_up",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_start(self, async_client: AsyncSunrise) -> None:
        query = await async_client.applications.query.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncSunrise) -> None:
        query = await async_client.applications.query.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model_id="model_id",
            stream=True,
        )
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncSunrise) -> None:
        response = await async_client.applications.query.with_raw_response.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncSunrise) -> None:
        async with async_client.applications.query.with_streaming_response.start(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncSunrise) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.query.with_raw_response.start(
                application_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "user",
                    }
                ],
            )
