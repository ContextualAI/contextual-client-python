# Checks each call added from the live API description against a stubbed transport (respx).
# For every call: one request with the description's method and path, every argument sent where the description
# puts it, and the documented response parsed into the method's return type with strict validation on.

from __future__ import annotations

import json
from typing import Any, Dict, cast

import httpx
import respx
import pytest

from contextual import ContextualAI, AsyncContextualAI, types
from contextual._models import BaseModel

base_url = "http://stub.test"

CASES: list[Dict[str, Any]] = json.loads(
    '[{"id": "extract.delete_document", "resource": "extract", "method": "delete_document", "http": "DELETE", "path": "/extract/documents/document_id-value", "args": ["document_id-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {}, "response_type": "ExtractDeleteDocumentResponse", "multipart": []}, {"id": "extract.delete_schema", "resource": "extract", "method": "delete_schema", "http": "DELETE", "path": "/extract/schemas/schema_id-value", "args": ["schema_id-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {}, "response_type": "ExtractDeleteSchemaResponse", "multipart": []}, {"id": "extract.list_documents", "resource": "extract", "method": "list_documents", "http": "GET", "path": "/extract/documents", "args": [], "kwargs": {"limit": 1, "cursor": "cursor-value", "search": "search-value"}, "body": {}, "query": {"limit": "1", "cursor": "cursor-value", "search": "search-value"}, "headers": {}, "response": {"documents": [{"document_id": "document_id-value", "file_name": "file_name-value", "file_size": 1, "page_count": 1, "uploaded_at": "uploaded_at-value", "status": "status-value", "signed_url": "signed_url-value"}], "total_count": 1, "next_cursor": "next_cursor-value", "prev_cursor": "prev_cursor-value"}, "response_type": "ExtractListDocumentsResponse", "multipart": []}, {"id": "extract.retrieve_document", "resource": "extract", "method": "retrieve_document", "http": "GET", "path": "/extract/documents/document_id-value", "args": ["document_id-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"document_id": "document_id-value", "file_name": "file_name-value", "file_size": 1, "page_count": 1, "uploaded_at": "uploaded_at-value", "status": "status-value", "signed_url": "signed_url-value"}, "response_type": "ExtractRetrieveDocumentResponse", "multipart": []}, {"id": "extract.list_jobs", "resource": "extract", "method": "list_jobs", "http": "GET", "path": "/extract/jobs", "args": [], "kwargs": {"limit": 1, "cursor": "cursor-value", "job_status": "job_status-value", "search": "search-value"}, "body": {}, "query": {"limit": "1", "cursor": "cursor-value", "job_status": "job_status-value", "search": "search-value"}, "headers": {}, "response": {"jobs": [{"job_id": "job_id-value", "status": "pending", "created_at": "created_at-value", "progress": {"completion_percentage": 1, "current_step": "current_step-value", "fields_processed": 1, "total_fields": 1}, "current_activity": "current_activity-value", "schema_id": "schema_id-value", "document_id": "document_id-value", "config": {"model": "gemini-2.5-flash", "per_key_attribution": true, "temperature": 1.5, "enable_thinking": true, "additional_instructions": "additional_instructions-value", "enable_agentic_array_extraction": true}}], "total_count": 1, "next_cursor": "next_cursor-value", "prev_cursor": "prev_cursor-value"}, "response_type": "ExtractListJobsResponse", "multipart": []}, {"id": "extract.retrieve_job", "resource": "extract", "method": "retrieve_job", "http": "GET", "path": "/extract/jobs/job_id-value", "args": ["job_id-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"job_id": "job_id-value", "status": "pending", "created_at": "created_at-value", "progress": {"completion_percentage": 1, "current_step": "current_step-value", "fields_processed": 1, "total_fields": 1}, "current_activity": "current_activity-value", "schema_id": "schema_id-value", "document_id": "document_id-value", "config": {"model": "gemini-2.5-flash", "per_key_attribution": true, "temperature": 1.5, "enable_thinking": true, "additional_instructions": "additional_instructions-value", "enable_agentic_array_extraction": true}}, "response_type": "ExtractRetrieveJobResponse", "multipart": []}, {"id": "extract.retrieve_job_results", "resource": "extract", "method": "retrieve_job_results", "http": "GET", "path": "/extract/jobs/job_id-value/results", "args": ["job_id-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"job_id": "job_id-value", "status": "pending", "results": {}, "metadata": {}, "config": {"model": "gemini-2.5-flash", "per_key_attribution": true, "temperature": 1.5, "enable_thinking": true, "additional_instructions": "additional_instructions-value", "enable_agentic_array_extraction": true}}, "response_type": "ExtractRetrieveJobResultsResponse", "multipart": []}, {"id": "extract.list_schemas", "resource": "extract", "method": "list_schemas", "http": "GET", "path": "/extract/schemas", "args": [], "kwargs": {"limit": 1, "cursor": "cursor-value", "search": "search-value"}, "body": {}, "query": {"limit": "1", "cursor": "cursor-value", "search": "search-value"}, "headers": {}, "response": {"schemas": [{"schema_id": "schema_id-value", "name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}, "created_at": "created_at-value", "updated_at": "updated_at-value"}], "total_count": 1, "next_cursor": "next_cursor-value", "prev_cursor": "prev_cursor-value"}, "response_type": "ExtractListSchemasResponse", "multipart": []}, {"id": "extract.retrieve_schema", "resource": "extract", "method": "retrieve_schema", "http": "GET", "path": "/extract/schemas/schema_id-value", "args": ["schema_id-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"schema_id": "schema_id-value", "name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}, "created_at": "created_at-value", "updated_at": "updated_at-value"}, "response_type": "ExtractRetrieveSchemaResponse", "multipart": []}, {"id": "extract.upload_document", "resource": "extract", "method": "upload_document", "http": "POST", "path": "/extract/documents/upload", "args": [], "kwargs": {"file": "__FILE__"}, "body": {}, "query": {}, "headers": {}, "response": {"document_id": "document_id-value", "file_name": "file_name-value", "file_size": 1, "page_count": 1, "uploaded_at": "uploaded_at-value", "status": "status-value"}, "response_type": "ExtractUploadDocumentResponse", "multipart": ["file"]}, {"id": "extract.create_job", "resource": "extract", "method": "create_job", "http": "POST", "path": "/extract/jobs", "args": [], "kwargs": {"document_id": "document_id-value", "schema_id": "schema_id-value", "config": {"model": "gemini-2.5-flash", "per_key_attribution": true, "temperature": 1.5, "enable_thinking": true, "additional_instructions": "additional_instructions-value", "enable_agentic_array_extraction": true}, "stream": true}, "body": {"document_id": "document_id-value", "schema_id": "schema_id-value", "config": {"model": "gemini-2.5-flash", "per_key_attribution": true, "temperature": 1.5, "enable_thinking": true, "additional_instructions": "additional_instructions-value", "enable_agentic_array_extraction": true}, "stream": true}, "query": {}, "headers": {}, "response": {"job_id": "job_id-value", "status": "pending", "created_at": "created_at-value", "estimated_completion": "estimated_completion-value"}, "response_type": "ExtractCreateJobResponse", "multipart": []}, {"id": "extract.create_schema", "resource": "extract", "method": "create_schema", "http": "POST", "path": "/extract/schemas", "args": [], "kwargs": {"name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}}, "body": {"name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}}, "query": {}, "headers": {}, "response": {"schema_id": "schema_id-value", "name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}, "created_at": "created_at-value", "updated_at": "updated_at-value"}, "response_type": "ExtractCreateSchemaResponse", "multipart": []}, {"id": "extract.update_job_results", "resource": "extract", "method": "update_job_results", "http": "PUT", "path": "/extract/jobs/job_id-value/results", "args": ["job_id-value"], "kwargs": {"results": {}}, "body": {"results": {}}, "query": {}, "headers": {}, "response": {}, "response_type": "object", "multipart": []}, {"id": "extract.update_schema", "resource": "extract", "method": "update_schema", "http": "PUT", "path": "/extract/schemas/schema_id-value", "args": ["schema_id-value"], "kwargs": {"name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}}, "body": {"name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}}, "query": {}, "headers": {}, "response": {"schema_id": "schema_id-value", "name": "name-value", "description": "description-value", "schema_definition": {}, "metadata": {}, "created_at": "created_at-value", "updated_at": "updated_at-value"}, "response_type": "ExtractUpdateSchemaResponse", "multipart": []}, {"id": "billing.retrieve_balance", "resource": "billing", "method": "retrieve_balance", "http": "GET", "path": "/billing/balance", "args": [], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"balance": 1.5}, "response_type": "BillingRetrieveBalanceResponse", "multipart": []}, {"id": "billing.list_top_ups", "resource": "billing", "method": "list_top_ups", "http": "GET", "path": "/billing/balance/top-ups", "args": [], "kwargs": {"limit": 1, "cursor": "cursor-value"}, "body": {}, "query": {"limit": "1", "cursor": "cursor-value"}, "headers": {}, "response": {"top_ups": [{"amount": 1.5, "created_at": "2026-01-15T10:00:00+00:00", "description": "description-value", "starting_balance": 1.5, "ending_balance": 1.5}], "has_more": true, "cursor": "cursor-value"}, "response_type": "BillingListTopUpsResponse", "multipart": []}, {"id": "billing.retrieve_billing_mode_history", "resource": "billing", "method": "retrieve_billing_mode_history", "http": "GET", "path": "/billing/billing_mode/history", "args": [], "kwargs": {"year": 2025, "month": 1}, "body": {}, "query": {"year": "2025", "month": "1"}, "headers": {}, "response": {"billing_modes": [{"date": "2026-01-15", "billing_mode": "ON_DEMAND_PREPAID"}]}, "response_type": "BillingRetrieveBillingModeHistoryResponse", "multipart": []}, {"id": "billing.retrieve_metadata", "resource": "billing", "method": "retrieve_metadata", "http": "GET", "path": "/billing/metadata", "args": [], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"is_low_balance": true, "is_auto_top_up_enabled": true}, "response_type": "BillingRetrieveMetadataResponse", "multipart": []}, {"id": "billing.retrieve_acl_usage", "resource": "billing", "method": "retrieve_acl_usage", "http": "GET", "path": "/billing/usages/acl", "args": [], "kwargs": {"year": 2025, "month": 1, "resource_id": "resource_id-value"}, "body": {}, "query": {"year": "2025", "month": "1", "resource_id": "resource_id-value"}, "headers": {}, "response": {"usages": [{"step_name": "step_name-value", "date": "date-value", "input_tokens": 1, "output_tokens": 1, "total_cost": 1.5}]}, "response_type": "BillingRetrieveAclUsageResponse", "multipart": []}, {"id": "billing.retrieve_earliest_usage_date", "resource": "billing", "method": "retrieve_earliest_usage_date", "http": "GET", "path": "/billing/usages/earliest_date", "args": [], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"date": "2026-01-15"}, "response_type": "BillingRetrieveEarliestUsageDateResponse", "multipart": []}, {"id": "billing.retrieve_monthly_usage", "resource": "billing", "method": "retrieve_monthly_usage", "http": "GET", "path": "/billing/usages/monthly", "args": [], "kwargs": {"year": 2025, "month": 1, "resource_id": "resource_id-value"}, "body": {}, "query": {"year": "2025", "month": "1", "resource_id": "resource_id-value"}, "headers": {}, "response": {"usages": [{"date": "2026-01-15", "usage_type": "QUERY_REFORMULATION_INPUT_TOKEN", "quantity": 1, "price": 1.5}]}, "response_type": "BillingRetrieveMonthlyUsageResponse", "multipart": []}, {"id": "workspaces.retrieve_consent", "resource": "workspaces", "method": "retrieve_consent", "http": "GET", "path": "/workspaces/consent", "args": [], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"status": "status-value", "email": "email-value", "created_at": "created_at-value"}, "response_type": "WorkspaceRetrieveConsentResponse", "multipart": []}, {"id": "workspaces.update_consent", "resource": "workspaces", "method": "update_consent", "http": "PUT", "path": "/workspaces/consent", "args": [], "kwargs": {"type": "CONSENT_FULL"}, "body": {"type": "CONSENT_FULL"}, "query": {}, "headers": {}, "response": {}, "response_type": "WorkspaceUpdateConsentResponse", "multipart": []}]'
)


def _check_request(route: respx.Route, case: Dict[str, Any]) -> None:
    assert route.call_count == 1
    request = cast(httpx.Request, route.calls[0].request)  # pyright: ignore[reportUnknownMemberType]
    assert request.method == case["http"]
    assert request.url.path == case["path"]
    if case["multipart"]:
        # a file upload goes as multipart form data, with every field the description names
        assert request.headers["content-type"].startswith("multipart/form-data")
        for key in case["multipart"]:
            assert f'name="{key}"'.encode() in request.content, key
    elif case["body"]:
        sent = json.loads(request.content or b"{}")
        for key, expected in case["body"].items():
            assert sent.get(key) == expected, key
    for key, expected in case["query"].items():
        assert str(request.url.params.get(key)).lower() == expected.lower(), key
    for key, expected in case["headers"].items():
        assert request.headers.get(key) == expected, key


def _kwargs(case: Dict[str, Any]) -> Dict[str, Any]:
    return {k: (b"%PDF-1.4 stub" if v == "__FILE__" else v) for k, v in case["kwargs"].items()}


def _check_response(result: Any, case: Dict[str, Any]) -> None:
    if case["response_type"] == "None":
        # a call whose success response has no body returns None
        assert result is None
        return
    expected = case["response"]
    if isinstance(result, BaseModel):
        # every field of the documented response came back, under its wire name
        assert set(result.to_dict(use_api_names=True).keys()) == set(expected.keys())
    elif isinstance(expected, str):
        # a string response comes back as the response body's text, as the existing string methods do
        assert result == json.dumps(expected)
    else:
        # a list or map response is returned as parsed
        assert result == expected
    if case["response_type"] == "object":
        return  # an untyped response: returned as parsed, checked above
    expected_type = getattr(types, case["response_type"])
    if isinstance(expected_type, type):
        assert isinstance(result, expected_type)


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
@respx.mock
def test_added_call_sync(case: Dict[str, Any]) -> None:
    route = respx.route(method=case["http"], url__startswith=base_url + case["path"]).mock(
        return_value=httpx.Response(204)
        if case["response_type"] == "None"
        else httpx.Response(200, json=case["response"])
    )
    client = ContextualAI(base_url=base_url, api_key="My API Key", _strict_response_validation=True)
    method = getattr(getattr(client, case["resource"]), case["method"])
    result = method(*case["args"], **_kwargs(case))
    _check_request(route, case)
    _check_response(result, case)


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
@respx.mock
async def test_added_call_async(case: Dict[str, Any]) -> None:
    route = respx.route(method=case["http"], url__startswith=base_url + case["path"]).mock(
        return_value=httpx.Response(204)
        if case["response_type"] == "None"
        else httpx.Response(200, json=case["response"])
    )
    client = AsyncContextualAI(base_url=base_url, api_key="My API Key", _strict_response_validation=True)
    method = getattr(getattr(client, case["resource"]), case["method"])
    result = await method(*case["args"], **_kwargs(case))
    _check_request(route, case)
    _check_response(result, case)
