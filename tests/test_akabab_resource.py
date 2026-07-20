"""Unit tests for AkababResource — the second network-touching component."""

import pytest
import requests

from starwars_dagster.resources import akabab_resource as akabab_module
from starwars_dagster.resources.akabab_resource import AkababResource


class _StubResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload


def _patch_get(monkeypatch, response, calls):
    def fake_get(url, **kwargs):
        calls.append({"url": url, **kwargs})
        return response

    monkeypatch.setattr(akabab_module.requests, "get", fake_get)


def test_list_response_is_returned_as_is(monkeypatch):
    records = [{"id": 1, "name": "Luke Skywalker"}]
    calls = []
    _patch_get(monkeypatch, _StubResponse(records), calls)

    assert AkababResource().fetch("all") == records


def test_non_list_payload_raises_instead_of_coercing(monkeypatch):
    # /id/1.json returns a single object; the pipeline only consumes list
    # endpoints, and a silent wrap would hide an upstream contract break.
    calls = []
    _patch_get(monkeypatch, _StubResponse({"id": 1, "name": "Luke Skywalker"}), calls)

    with pytest.raises(ValueError, match="JSON array"):
        AkababResource().fetch("all")


def test_http_errors_raise_instead_of_returning_garbage(monkeypatch):
    calls = []
    _patch_get(monkeypatch, _StubResponse({"detail": "not found"}, status_code=500), calls)

    with pytest.raises(requests.HTTPError):
        AkababResource().fetch("all")


def test_configured_timeout_and_json_suffix_url(monkeypatch):
    calls = []
    _patch_get(monkeypatch, _StubResponse([]), calls)

    AkababResource(timeout_seconds=7).fetch("all")

    assert calls[0]["timeout"] == 7
    assert calls[0]["url"] == "https://akabab.github.io/starwars-api/api/all.json"
