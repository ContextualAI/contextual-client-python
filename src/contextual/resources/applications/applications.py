# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from ...types import application_list_params, application_create_params, application_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .tune.tune import (
    TuneResource,
    AsyncTuneResource,
    TuneResourceWithRawResponse,
    AsyncTuneResourceWithRawResponse,
    TuneResourceWithStreamingResponse,
    AsyncTuneResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncApplicationsListResponse, AsyncApplicationsListResponse
from ..._base_client import AsyncPaginator, make_request_options
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .evaluate.evaluate import (
    EvaluateResource,
    AsyncEvaluateResource,
    EvaluateResourceWithRawResponse,
    AsyncEvaluateResourceWithRawResponse,
    EvaluateResourceWithStreamingResponse,
    AsyncEvaluateResourceWithStreamingResponse,
)
from ...types.application_list_response import ApplicationListResponse
from ...types.create_application_output import CreateApplicationOutput

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def evaluate(self) -> EvaluateResource:
        return EvaluateResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def tune(self) -> TuneResource:
        return TuneResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateApplicationOutput:
        """
        Create a new `Application` with a specific configuration.

        An `Application` queries over a `Datastore` to retrieve relevant data on which
        generations are grounded.

        Retrieval and generation parameters are defined in the provided `Application`
        configuration.

        If no `datastore_id` is provided in the configuration, this API automatically
        creates a datastore and configures the application to use the newly created
        datastore.

        Args:
          name: Name of the application

          datastore_ids: The IDs of the datastore associated with the application. Provide at most one
              datastore. Leave empty to automatically create a new datastore.

          description: Description of the application

          suggested_queries: These queries will show up as suggestions when users load the app. We recommend
              including common queries that users will ask, as well as complex queries so
              users understand the types of complex queries the system can handle.

          system_prompt: Instructions that your RAG system references when generating responses. Note
              that we do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/applications",
            body=maybe_transform(
                {
                    "name": name,
                    "datastore_ids": datastore_ids,
                    "description": description,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateApplicationOutput,
        )

    def update(
        self,
        application_id: str,
        *,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        llm_model_id: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modify a given `Application` to utilize the provided configuration.

        Fields not included in the request body will not be modified.

        Args:
          application_id: Application ID of the application to edit

          datastore_ids: IDs of the datastore to associate with the application.

          llm_model_id: Optional model ID of a tuned model to use for generation. Model must have been
              tuned on this application; tuned models cannot be used across applications. Uses
              default model if none is specified. Set to `default` to deactivate the tuned
              model and use the default model.

          suggested_queries: These queries will show up as suggestions when users load the app. We recommend
              including common queries that users will ask, as well as complex queries so
              users understand the types of complex queries the system can handle.

          system_prompt: Instructions that your RAG system references when generating responses. Note
              that we do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._put(
            f"/applications/{application_id}",
            body=maybe_transform(
                {
                    "datastore_ids": datastore_ids,
                    "llm_model_id": llm_model_id,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                application_update_params.ApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncApplicationsListResponse[ApplicationListResponse]:
        """
        Retrieve a list of all `Applications`.

        Args:
          cursor: Cursor from the previous call to list applications, used to retrieve the next
              set of results

          limit: Maximum number of applications to return

          search: Search text to filter applications by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/applications",
            page=SyncApplicationsListResponse[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "search": search,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    def delete(
        self,
        application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given `Application`.

        This is an irreversible operation.

        Note: `Datastores` which are associated with the `Application` will not be
        deleted, even if no other `Application` is using them. To delete a `Datastore`,
        use the `DELETE /datastores/{datastore_id}` API.

        Args:
          application_id: Application ID of the application to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._delete(
            f"/applications/{application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResource:
        return AsyncEvaluateResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def tune(self) -> AsyncTuneResource:
        return AsyncTuneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sunrise-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateApplicationOutput:
        """
        Create a new `Application` with a specific configuration.

        An `Application` queries over a `Datastore` to retrieve relevant data on which
        generations are grounded.

        Retrieval and generation parameters are defined in the provided `Application`
        configuration.

        If no `datastore_id` is provided in the configuration, this API automatically
        creates a datastore and configures the application to use the newly created
        datastore.

        Args:
          name: Name of the application

          datastore_ids: The IDs of the datastore associated with the application. Provide at most one
              datastore. Leave empty to automatically create a new datastore.

          description: Description of the application

          suggested_queries: These queries will show up as suggestions when users load the app. We recommend
              including common queries that users will ask, as well as complex queries so
              users understand the types of complex queries the system can handle.

          system_prompt: Instructions that your RAG system references when generating responses. Note
              that we do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/applications",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "datastore_ids": datastore_ids,
                    "description": description,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateApplicationOutput,
        )

    async def update(
        self,
        application_id: str,
        *,
        datastore_ids: List[str] | NotGiven = NOT_GIVEN,
        llm_model_id: str | NotGiven = NOT_GIVEN,
        suggested_queries: List[str] | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modify a given `Application` to utilize the provided configuration.

        Fields not included in the request body will not be modified.

        Args:
          application_id: Application ID of the application to edit

          datastore_ids: IDs of the datastore to associate with the application.

          llm_model_id: Optional model ID of a tuned model to use for generation. Model must have been
              tuned on this application; tuned models cannot be used across applications. Uses
              default model if none is specified. Set to `default` to deactivate the tuned
              model and use the default model.

          suggested_queries: These queries will show up as suggestions when users load the app. We recommend
              including common queries that users will ask, as well as complex queries so
              users understand the types of complex queries the system can handle.

          system_prompt: Instructions that your RAG system references when generating responses. Note
              that we do not guarantee that the system will follow these instructions exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._put(
            f"/applications/{application_id}",
            body=await async_maybe_transform(
                {
                    "datastore_ids": datastore_ids,
                    "llm_model_id": llm_model_id,
                    "suggested_queries": suggested_queries,
                    "system_prompt": system_prompt,
                },
                application_update_params.ApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ApplicationListResponse, AsyncApplicationsListResponse[ApplicationListResponse]]:
        """
        Retrieve a list of all `Applications`.

        Args:
          cursor: Cursor from the previous call to list applications, used to retrieve the next
              set of results

          limit: Maximum number of applications to return

          search: Search text to filter applications by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/applications",
            page=AsyncApplicationsListResponse[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "search": search,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    async def delete(
        self,
        application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete a given `Application`.

        This is an irreversible operation.

        Note: `Datastores` which are associated with the `Application` will not be
        deleted, even if no other `Application` is using them. To delete a `Datastore`,
        use the `DELETE /datastores/{datastore_id}` API.

        Args:
          application_id: Application ID of the application to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._delete(
            f"/applications/{application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_raw_response_wrapper(
            applications.create,
        )
        self.update = to_raw_response_wrapper(
            applications.update,
        )
        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.delete = to_raw_response_wrapper(
            applications.delete,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._applications.metadata)

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._applications.query)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self._applications.evaluate)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._applications.datasets)

    @cached_property
    def tune(self) -> TuneResourceWithRawResponse:
        return TuneResourceWithRawResponse(self._applications.tune)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_raw_response_wrapper(
            applications.create,
        )
        self.update = async_to_raw_response_wrapper(
            applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            applications.delete,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._applications.metadata)

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._applications.query)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self._applications.evaluate)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._applications.datasets)

    @cached_property
    def tune(self) -> AsyncTuneResourceWithRawResponse:
        return AsyncTuneResourceWithRawResponse(self._applications.tune)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_streamed_response_wrapper(
            applications.create,
        )
        self.update = to_streamed_response_wrapper(
            applications.update,
        )
        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            applications.delete,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._applications.metadata)

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._applications.query)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self._applications.evaluate)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._applications.datasets)

    @cached_property
    def tune(self) -> TuneResourceWithStreamingResponse:
        return TuneResourceWithStreamingResponse(self._applications.tune)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_streamed_response_wrapper(
            applications.create,
        )
        self.update = async_to_streamed_response_wrapper(
            applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            applications.delete,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._applications.metadata)

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._applications.query)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self._applications.evaluate)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._applications.datasets)

    @cached_property
    def tune(self) -> AsyncTuneResourceWithStreamingResponse:
        return AsyncTuneResourceWithStreamingResponse(self._applications.tune)
