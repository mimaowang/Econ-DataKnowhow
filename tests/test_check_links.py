from __future__ import annotations

import json
import sys
from contextlib import nullcontext
from types import SimpleNamespace
from urllib.error import HTTPError, URLError

import pytest

import check_links
from check_links import check


def test_link_checker_blocks_private_and_script_targets_without_network() -> None:
    private = check("http://127.0.0.1/latest/meta-data", timeout=0.01)
    script = check("javascript:alert(1)", timeout=0.01)
    assert private["result"] == "blocked"
    assert "non-public-ip" in private["issues"]
    assert script["result"] == "blocked"
    assert "non-http-scheme" in script["issues"]
    assert "url" not in private
    assert "url" not in script


@pytest.mark.parametrize("fallback", [False, True])
def test_unicode_url_is_encoded_for_head_and_get(monkeypatch, fallback) -> None:
    url = "https://books.google.com/books/about/%E4%B8%AD国农村经济.html?id=123&title=统计"
    calls = []

    def fake_open(request, timeout):
        calls.append(request)
        request.full_url.encode("ascii")  # Matches urllib's HTTP request-target requirement.
        if fallback and request.get_method() == "HEAD":
            raise HTTPError(request.full_url, 405, "Method Not Allowed", {}, None)
        return nullcontext(SimpleNamespace(status=200, geturl=lambda: request.full_url))

    monkeypatch.setattr(check_links, "safe_open", fake_open)
    result = check(url, timeout=0.01)

    assert result["result"] == "ok"
    assert result["url"] == url
    assert "%E4%B8%AD%E5%9B%BD" in result["final_url"]
    assert "title=%E7%BB%9F%E8%AE%A1" in result["final_url"]
    assert "%25E4" not in result["final_url"]
    assert [request.get_method() for request in calls] == (["HEAD", "GET"] if fallback else ["HEAD"])


def test_get_fallback_reports_its_own_http_status(monkeypatch) -> None:
    def fake_open(request, timeout):
        status = 405 if request.get_method() == "HEAD" else 403
        raise HTTPError(request.full_url, status, "request denied", {}, None)

    monkeypatch.setattr(check_links, "safe_open", fake_open)
    result = check("https://example.org/", timeout=0.01)
    assert result["result"] == "http-error"
    assert result["status"] == 403


@pytest.mark.parametrize("strict, expected_exit", [(False, 0), (True, 1)])
def test_cli_finishes_and_reports_network_findings(monkeypatch, tmp_path, strict, expected_exit) -> None:
    urls = ["https://example.org/ok", "https://example.org/denied", "https://example.org/timeout", "https://example.org/later"]
    output = tmp_path / "links.json"
    summary = tmp_path / "summary.md"
    arguments = ["check_links.py", "--max-urls", "3", "--output", str(output), "--summary", str(summary)]
    if strict:
        arguments.append("--strict")

    def fake_open(request, timeout):
        if request.full_url.endswith("/denied"):
            raise HTTPError(request.full_url, 403, "Forbidden", {}, None)
        if request.full_url.endswith("/timeout"):
            raise URLError("timed out")
        return nullcontext(SimpleNamespace(status=200, geturl=lambda: request.full_url))

    monkeypatch.setattr(sys, "argv", arguments)
    monkeypatch.setattr(check_links, "collect_urls", lambda: urls)
    monkeypatch.setattr(check_links, "safe_open", fake_open)

    assert check_links.main() == expected_exit
    report = json.loads(output.read_text(encoding="utf-8"))
    assert report["available_count"] == 4
    assert report["checked_count"] == 3
    assert [item["result"] for item in report["results"]] == ["ok", "http-error", "error"]
    markdown = summary.read_text(encoding="utf-8")
    assert "**3 of 4**" in markdown
    assert "**2** need review" in markdown
    assert "https://example.org/denied" in markdown
    assert "403" in markdown
    assert "https://example.org/timeout" in markdown
    assert "timed out" in markdown


def test_unexpected_checker_error_is_not_hidden(monkeypatch, tmp_path) -> None:
    def broken_check(url, timeout):
        raise RuntimeError("unexpected checker error")

    monkeypatch.setattr(sys, "argv", ["check_links.py", "--output", str(tmp_path / "links.json")])
    monkeypatch.setattr(check_links, "collect_urls", lambda: ["https://example.org/"])
    monkeypatch.setattr(check_links, "check", broken_check)
    with pytest.raises(RuntimeError, match="unexpected checker error"):
        check_links.main()
