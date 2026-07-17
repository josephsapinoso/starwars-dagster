"""Unit tests for SWAPIResource — the only component that touches the network."""

import pytest
import requests

from starwars_dagster.resources import swapi_resource as swapi_module
from starwars_dagster.resources.swapi_resource import SWAPIResource


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

    monkeypatch.setattr(swapi_module.requests, "get", fake_get)


def test_plain_list_response_is_returned_as_is(monkeypatch):
    records = [{"name": "Luke Skywalker"}]
    calls = []
    _patch_get(monkeypatch, _StubResponse(records), calls)

    assert SWAPIResource().fetch("people") == records


def test_results_wrapped_response_is_unwrapped(monkeypatch):
    records = [{"name": "Luke Skywalker"}]
    calls = []
    _patch_get(monkeypatch, _StubResponse({"results": records}), calls)

    assert SWAPIResource().fetch("people") == records


def test_http_errors_raise_instead_of_returning_garbage(monkeypatch):
    calls = []
    _patch_get(monkeypatch, _StubResponse({"detail": "not found"}, status_code=500), calls)

    with pytest.raises(requests.HTTPError):
        SWAPIResource().fetch("people")


def test_configured_timeout_is_passed_to_requests(monkeypatch):
    calls = []
    _patch_get(monkeypatch, _StubResponse([]), calls)

    SWAPIResource(timeout_seconds=7).fetch("films")

    assert calls[0]["timeout"] == 7
    assert calls[0]["url"] == "https://swapi.info/api/films/"
