from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

sys.dont_write_bytecode = True

from kb_lib import ROOT, atomic_write_text, load_datasets, public_http_url_issues  # noqa: E402


URL_PATTERN = re.compile(r"https?://[^\s<>\"'）)\]】]+")
TRAILING = ".,;:!?，。；：！？、"


class SafeRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001, ANN201
        issues = public_http_url_issues(newurl, resolve_dns=True)
        if issues:
            raise URLError(f"blocked redirect target: {','.join(issues)}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def url_fingerprint(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def safe_open(request: Request, timeout: float):  # noqa: ANN201
    issues = public_http_url_issues(request.full_url, resolve_dns=True)
    if issues:
        raise URLError(f"blocked URL: {','.join(issues)}")
    return build_opener(SafeRedirectHandler()).open(request, timeout=timeout)


def collect_urls() -> list[str]:
    values: set[str] = set()
    records, failures = load_datasets()
    if failures:
        raise RuntimeError("cannot check links while a dataset record is unparsable")
    for record in records:
        text = record.path.read_text(encoding="utf-8")
        values.update(match.rstrip(TRAILING) for match in URL_PATTERN.findall(text))
    return sorted(values, key=str.casefold)


def check(url: str, timeout: float) -> dict[str, object]:
    issues = public_http_url_issues(url, resolve_dns=False)
    if issues:
        return {"url_fingerprint": url_fingerprint(url), "result": "blocked", "issues": issues}
    # urllib needs an ASCII request target, even when the recorded URL contains Chinese text.
    # Preserve URL separators and existing percent escapes on both request paths.
    parts = urlsplit(url)
    request_url = parts._replace(
        path=quote(parts.path, safe="/%:@!$&'()*+,;="),
        query=quote(parts.query, safe="/%?:@!$&'()*+,;="),
    ).geturl()
    request = Request(request_url, method="HEAD", headers={"User-Agent": "econ-dataknowhow-link-check/1.0"})
    try:
        with safe_open(request, timeout=timeout) as response:
            return {"url": url, "status": response.status, "final_url": response.geturl(), "result": "ok"}
    except HTTPError as exc:
        if exc.code != 405:
            return {"url": url, "status": exc.code, "result": "http-error", "error": str(exc.reason)}
        fallback = Request(
            request_url,
            method="GET",
            headers={"User-Agent": "econ-dataknowhow-link-check/1.0", "Range": "bytes=0-1024"},
        )
        try:
            with safe_open(fallback, timeout=timeout) as response:
                return {"url": url, "status": response.status, "final_url": response.geturl(), "result": "ok"}
        except HTTPError as fallback_exc:
            return {"url": url, "status": fallback_exc.code, "result": "http-error", "error": str(fallback_exc.reason)}
        except (URLError, TimeoutError, OSError) as fallback_exc:
            return {"url": url, "result": "error", "error_type": type(fallback_exc).__name__, "error": str(fallback_exc)}
    except (URLError, TimeoutError, OSError) as exc:
        return {"url": url, "result": "error", "error_type": type(exc).__name__, "error": str(exc)}


def build_summary(results: list[dict[str, object]], available_count: int) -> str:
    failures = [item for item in results if item.get("result") != "ok"]
    lines = [
        "## External link freshness",
        "",
        f"Checked **{len(results)} of {available_count}** unique URLs; **{len(failures)}** need review.",
        "",
        "This is a bounded network diagnostic. Access restrictions and temporary connection errors need review "
        "before changing a data record.",
    ]
    if failures:
        lines.extend(["", "| URL | HTTP status | Result | Detail |", "| --- | --- | --- | --- |"])
        for item in failures:
            url = str(item.get("url", "")).replace("|", "%7C")
            label = f"<{url}>" if url else f"Blocked URL ({item.get('url_fingerprint', '')})"
            detail = item.get("error") or item.get("error_type") or ", ".join(item.get("issues", []))
            detail = str(detail).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {label} | {item.get('status', '—')} | {item['result']} | {detail} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Best-effort external link freshness check; never edits canonical records.")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--max-urls", type=int, default=150)
    parser.add_argument("--output", type=Path, default=ROOT / "ledgers" / "link-check.json")
    parser.add_argument("--summary", type=Path, help="also write a readable Markdown report, e.g. GITHUB_STEP_SUMMARY")
    parser.add_argument("--strict", action="store_true", help="return non-zero when any checked URL is not successful")
    args = parser.parse_args()
    urls = collect_urls()
    results = [check(url, args.timeout) for url in urls[: max(args.max_urls, 0)]]
    payload = {
        "schema_version": 1,
        "checked_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "available_count": len(urls),
        "checked_count": len(results),
        "results": results,
    }
    atomic_write_text(args.output, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    if args.summary:
        atomic_write_text(args.summary, build_summary(results, len(urls)))
    failures = sum(1 for item in results if item.get("result") != "ok")
    print(f"checked={len(results)} failures={failures} output={args.output}")
    return 1 if args.strict and failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
