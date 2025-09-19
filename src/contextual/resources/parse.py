# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import parse_jobs_params, parse_create_params, parse_job_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.parse_jobs_response import ParseJobsResponse
from ..types.parse_create_response import ParseCreateResponse
from ..types.parse_job_status_response import ParseJobStatusResponse
from ..types.parse_job_results_response import ParseJobResultsResponse

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        raw_file: FileTypes,
        enable_document_hierarchy: bool | Omit = omit,
        enable_split_tables: bool | Omit = omit,
        figure_caption_mode: Literal["concise", "detailed"] | Omit = omit,
        max_split_table_cells: int | Omit = omit,
        page_range: str | Omit = omit,
        parse_mode: Literal["basic", "standard"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseCreateResponse:
        """Parse a file into a structured Markdown and/or JSON.

        Files must be less than
        100MB and 400 pages. We use LibreOffice to convert DOC(X) and PPT(X) files to
        PDF, which may affect page count.

        See our [blog post](https://contextual.ai/blog/document-parser-for-rag) and
        [code examples](https://github.com/ContextualAI/examples/blob/main/03-standalone-api/04-parse/parse.ipynb).
        Email [parse-feedback@contextual.ai](mailto:parse-feedback@contextual.ai) with
        any feedback or questions.

        Args:
          raw_file: The file to be parsed. The file type must be PDF, DOC / DOCX, PPT / PPTX.

          enable_document_hierarchy: Adds a table of contents to the output with the structure of the entire parsed
              document. This feature is in beta. Controls parsing heading levels (e.g. H1, H2,
              H3) at higher quality. Not permitted in `basic` parsing_mode, or if page_range
              is not continuous and/or does not start from page zero.

          enable_split_tables: Controls whether tables are split into multiple tables by row with the headers
              propagated. Use for improving LLM comprehension of very large tables. Not
              permitted in `basic` parsing_mode.

          figure_caption_mode: Controls how thorough figure captions are. `concise` is short and minimizes
              chances of hallucinations. `detailed` is more thorough and can include
              commentary; this mode is in beta. Not permitted in `basic` parsing_mode.

          max_split_table_cells: Threshold number of table cells beyond which large tables are split if
              `enable_split_tables` is True. Must be null if `enable_split_tables` is False.

          page_range: Optional string representing page range to be parsed. Format: comma-separated
              indexes (0-based, e.g. `0,1,2,5,6`), or ranges inclusive of both ends (e.g.
              `0-2,5,6`)

          parse_mode: The settings to use for parsing. `basic` is for simple, text-only documents.
              `standard` is for complex documents with images, complex hierarchy, and/or no
              natively encoded textual data (e.g. for scanned documents).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "raw_file": raw_file,
                "enable_document_hierarchy": enable_document_hierarchy,
                "enable_split_tables": enable_split_tables,
                "figure_caption_mode": figure_caption_mode,
                "max_split_table_cells": max_split_table_cells,
                "page_range": page_range,
                "parse_mode": parse_mode,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["raw_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/parse",
            body=maybe_transform(body, parse_create_params.ParseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseCreateResponse,
        )

    def job_results(
        self,
        job_id: str,
        *,
        output_types: List[Literal["markdown-document", "markdown-per-page", "blocks-per-page"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseJobResultsResponse:
        """
        Get the results of a parse job.

        Parse job results are retained for up to 30 days after job creation. Fetching
        results for a parse job that is older than 30 days will return a 404 error.

        Args:
          job_id: Unique ID of the parse job

          output_types: The desired output format(s) of the parsed file. Must be `markdown-document`,
              `markdown-per-page`, and/or `blocks-per-page`. Specify multiple values to get
              multiple formats in the response. `markdown-document` parses the whole document
              into a single concatenated markdown output. `markdown-per-page` provides
              markdown output per page. `blocks-per-page` provides a structured JSON
              representation of the content blocks on each page, sorted by reading order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/parse/jobs/{job_id}/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"output_types": output_types}, parse_job_results_params.ParseJobResultsParams),
            ),
            cast_to=ParseJobResultsResponse,
        )

    def job_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseJobStatusResponse:
        """
        Get the status of a parse job.

        Parse job results are retained for up to 30 days after job creation. Fetching a
        status for a parse job that is older than 30 days will return a 404 error.

        Args:
          job_id: Unique ID of the parse job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/parse/jobs/{job_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseJobStatusResponse,
        )

    def jobs(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        uploaded_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseJobsResponse:
        """
        Get list of parse jobs, sorted from most recent to oldest.

        Returns all jobs from the last 30 days, or since the optional `uploaded_after`
        timestamp.

        Args:
          cursor: Cursor from the previous call to list parse jobs, used to retrieve the next set
              of results

          limit: Maximum number of parse jobs to return

          uploaded_after: Filters to only documents uploaded to `/parse` at or after specified UTC
              timestamp. If not provided, or if the provided timestamp is before the maximum
              parse job retention period (30 days), the maximum retention period will be used
              instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/parse/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "uploaded_after": uploaded_after,
                    },
                    parse_jobs_params.ParseJobsParams,
                ),
            ),
            cast_to=ParseJobsResponse,
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        raw_file: FileTypes,
        enable_document_hierarchy: bool | Omit = omit,
        enable_split_tables: bool | Omit = omit,
        figure_caption_mode: Literal["concise", "detailed"] | Omit = omit,
        max_split_table_cells: int | Omit = omit,
        page_range: str | Omit = omit,
        parse_mode: Literal["basic", "standard"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseCreateResponse:
        """Parse a file into a structured Markdown and/or JSON.

        Files must be less than
        100MB and 400 pages. We use LibreOffice to convert DOC(X) and PPT(X) files to
        PDF, which may affect page count.

        See our [blog post](https://contextual.ai/blog/document-parser-for-rag) and
        [code examples](https://github.com/ContextualAI/examples/blob/main/03-standalone-api/04-parse/parse.ipynb).
        Email [parse-feedback@contextual.ai](mailto:parse-feedback@contextual.ai) with
        any feedback or questions.

        Args:
          raw_file: The file to be parsed. The file type must be PDF, DOC / DOCX, PPT / PPTX.

          enable_document_hierarchy: Adds a table of contents to the output with the structure of the entire parsed
              document. This feature is in beta. Controls parsing heading levels (e.g. H1, H2,
              H3) at higher quality. Not permitted in `basic` parsing_mode, or if page_range
              is not continuous and/or does not start from page zero.

          enable_split_tables: Controls whether tables are split into multiple tables by row with the headers
              propagated. Use for improving LLM comprehension of very large tables. Not
              permitted in `basic` parsing_mode.

          figure_caption_mode: Controls how thorough figure captions are. `concise` is short and minimizes
              chances of hallucinations. `detailed` is more thorough and can include
              commentary; this mode is in beta. Not permitted in `basic` parsing_mode.

          max_split_table_cells: Threshold number of table cells beyond which large tables are split if
              `enable_split_tables` is True. Must be null if `enable_split_tables` is False.

          page_range: Optional string representing page range to be parsed. Format: comma-separated
              indexes (0-based, e.g. `0,1,2,5,6`), or ranges inclusive of both ends (e.g.
              `0-2,5,6`)

          parse_mode: The settings to use for parsing. `basic` is for simple, text-only documents.
              `standard` is for complex documents with images, complex hierarchy, and/or no
              natively encoded textual data (e.g. for scanned documents).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "raw_file": raw_file,
                "enable_document_hierarchy": enable_document_hierarchy,
                "enable_split_tables": enable_split_tables,
                "figure_caption_mode": figure_caption_mode,
                "max_split_table_cells": max_split_table_cells,
                "page_range": page_range,
                "parse_mode": parse_mode,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["raw_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/parse",
            body=await async_maybe_transform(body, parse_create_params.ParseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseCreateResponse,
        )

    async def job_results(
        self,
        job_id: str,
        *,
        output_types: List[Literal["markdown-document", "markdown-per-page", "blocks-per-page"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseJobResultsResponse:
        """
        Get the results of a parse job.

        Parse job results are retained for up to 30 days after job creation. Fetching
        results for a parse job that is older than 30 days will return a 404 error.

        Args:
          job_id: Unique ID of the parse job

          output_types: The desired output format(s) of the parsed file. Must be `markdown-document`,
              `markdown-per-page`, and/or `blocks-per-page`. Specify multiple values to get
              multiple formats in the response. `markdown-document` parses the whole document
              into a single concatenated markdown output. `markdown-per-page` provides
              markdown output per page. `blocks-per-page` provides a structured JSON
              representation of the content blocks on each page, sorted by reading order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/parse/jobs/{job_id}/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"output_types": output_types}, parse_job_results_params.ParseJobResultsParams
                ),
            ),
            cast_to=ParseJobResultsResponse,
        )

    async def job_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseJobStatusResponse:
        """
        Get the status of a parse job.

        Parse job results are retained for up to 30 days after job creation. Fetching a
        status for a parse job that is older than 30 days will return a 404 error.

        Args:
          job_id: Unique ID of the parse job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/parse/jobs/{job_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseJobStatusResponse,
        )

    async def jobs(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        uploaded_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseJobsResponse:
        """
        Get list of parse jobs, sorted from most recent to oldest.

        Returns all jobs from the last 30 days, or since the optional `uploaded_after`
        timestamp.

        Args:
          cursor: Cursor from the previous call to list parse jobs, used to retrieve the next set
              of results

          limit: Maximum number of parse jobs to return

          uploaded_after: Filters to only documents uploaded to `/parse` at or after specified UTC
              timestamp. If not provided, or if the provided timestamp is before the maximum
              parse job retention period (30 days), the maximum retention period will be used
              instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/parse/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "uploaded_after": uploaded_after,
                    },
                    parse_jobs_params.ParseJobsParams,
                ),
            ),
            cast_to=ParseJobsResponse,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create = to_raw_response_wrapper(
            parse.create,
        )
        self.job_results = to_raw_response_wrapper(
            parse.job_results,
        )
        self.job_status = to_raw_response_wrapper(
            parse.job_status,
        )
        self.jobs = to_raw_response_wrapper(
            parse.jobs,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create = async_to_raw_response_wrapper(
            parse.create,
        )
        self.job_results = async_to_raw_response_wrapper(
            parse.job_results,
        )
        self.job_status = async_to_raw_response_wrapper(
            parse.job_status,
        )
        self.jobs = async_to_raw_response_wrapper(
            parse.jobs,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create = to_streamed_response_wrapper(
            parse.create,
        )
        self.job_results = to_streamed_response_wrapper(
            parse.job_results,
        )
        self.job_status = to_streamed_response_wrapper(
            parse.job_status,
        )
        self.jobs = to_streamed_response_wrapper(
            parse.jobs,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create = async_to_streamed_response_wrapper(
            parse.create,
        )
        self.job_results = async_to_streamed_response_wrapper(
            parse.job_results,
        )
        self.job_status = async_to_streamed_response_wrapper(
            parse.job_status,
        )
        self.jobs = async_to_streamed_response_wrapper(
            parse.jobs,
        )
