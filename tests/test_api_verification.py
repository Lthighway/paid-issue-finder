import asyncio

from app.main import canonicalize_candidate, source_issue_ref


class FakeResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


class FakeClient:
    def __init__(self, response):
        self.response = response
        self.calls = []

    async def get(self, url, headers=None):
        self.calls.append((url, headers))
        return self.response


def mirror():
    return {
        "title": "Aggregator says reward $999999999",
        "body": "Original: https://github.com/example/project/issues/42",
        "html_url": "https://github.com/aggregator/feed/issues/9",
        "state": "open",
    }


def test_api_extracts_original_issue_reference():
    assert source_issue_ref(mirror()) == (
        "example", "project", "42", "https://github.com/example/project/issues/42"
    )


def test_api_uses_original_issue_not_mirror_text():
    client = FakeClient(FakeResponse(200, {
        "number": 42,
        "title": "Fix actual regression",
        "body": "Reward: $125",
        "state": "open",
        "html_url": "https://github.com/example/project/issues/42",
        "labels": [{"name": "bounty"}],
    }))
    result = asyncio.run(canonicalize_candidate(mirror(), client, {}))

    assert result["title"] == "Fix actual regression"
    assert result["repository_url"] == "https://api.github.com/repos/example/project"
    assert result["_discovered_url"] == "https://github.com/aggregator/feed/issues/9"
    assert client.calls[0][0] == "https://api.github.com/repos/example/project/issues/42"


def test_api_skips_closed_or_unverifiable_mirrors():
    closed = FakeClient(FakeResponse(200, {"state": "closed"}))
    assert asyncio.run(canonicalize_candidate(mirror(), closed, {})) is None

    missing = FakeClient(FakeResponse(404, {}))
    assert asyncio.run(canonicalize_candidate(mirror(), missing, {})) is None


def test_api_keeps_direct_open_issue_and_skips_closed_issue():
    direct = {"number": 5, "state": "open", "body": "Reward: $50"}
    closed = {"number": 6, "state": "closed", "body": "Reward: $50"}
    client = FakeClient(FakeResponse(500, {}))

    assert asyncio.run(canonicalize_candidate(direct, client, {})) is direct
    assert asyncio.run(canonicalize_candidate(closed, client, {})) is None



def test_api_prefers_original_outside_mirror_repository():
    issue = {
        "title": "Repeated mirror",
        "body": (
            "Copy: https://github.com/aggregator/feed/issues/8\n"
            "Original source: https://github.com/example/project/issues/42"
        ),
        "html_url": "https://github.com/aggregator/feed/issues/9",
        "state": "open",
    }
    assert source_issue_ref(issue) == (
        "example", "project", "42", "https://github.com/example/project/issues/42"
    )


def test_api_skips_unverified_bounty_before_fetch():
    issue = {
        "title": "Archived duplicate",
        "body": "Lifecycle: `unavailable`",
        "labels": [{"name": "verification-unavailable"}],
        "html_url": "https://github.com/aggregator/feed/issues/9",
        "state": "open",
    }
    client = FakeClient(FakeResponse(200, {}))
    assert asyncio.run(canonicalize_candidate(issue, client, {})) is None
    assert client.calls == []


def test_api_does_not_parse_usdc_as_usd():
    from app.main import extract_bounty
    assert extract_bounty("Solver reward: 0.90 USDC; funding: 1.00 USDC") is None
    assert extract_bounty("Bounty: $200 USD") == 200
