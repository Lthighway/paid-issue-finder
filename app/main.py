import os
import asyncio
from typing import Optional
from urllib.parse import urlparse
from fastapi import FastAPI, Header, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from .billing import PACKAGES, create_payment, get_account, consume_credit, process_webhook
import httpx
import re

app = FastAPI(title="Paid Issue Finder", version="0.5.0")
GITHUB_API = "https://api.github.com/search/issues"
MAX_REASONABLE_BOUNTY_USD = 100000
SOURCE_URL_RE = re.compile(r"https?://github\.com/([^/\s)]+)/([^/\s)]+)/issues/(\d+)")


class IssueResult(BaseModel):
    title: str
    url: str
    repository: str
    number: int
    labels: list[str]
    bounty_usd: Optional[float] = None
    confidence: str
    suspicious: bool
    score: float


class SearchResponse(BaseModel):
    query: str
    charged_brl: float
    remaining_credits: Optional[int]
    results: list[IssueResult]


class CheckoutRequest(BaseModel):
    email: str
    package_id: str


def extract_bounty(text: str) -> Optional[float]:
    patterns = [
        r"\$\s?([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)",
        r"(?:USD|US\$)\s?([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)",
        r"([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)\s*(?:USD|dollars?)",
    ]
    values = []
    for pattern in patterns:
        for match in re.findall(pattern, text, flags=re.I):
            try:
                value = float(match.replace(",", ""))
                if 0 < value <= MAX_REASONABLE_BOUNTY_USD:
                    values.append(value)
            except ValueError:
                pass
    return max(values) if values else None


def assess_bounty(issue: dict, bounty: Optional[float]) -> tuple[str, bool]:
    text = ((issue.get("title") or "") + " " + (issue.get("body") or "")).lower()
    labels = " ".join(x.get("name", "") for x in issue.get("labels", [])).lower()
    suspicious_terms = ("pppdud", "take your money back", "follow my", "backflip", "gazillion", "value: 0.00", "approximately 0 usd")
    suspicious = any(term in text for term in suspicious_terms)
    has_bounty_label = any(k in labels for k in ("bounty", "reward", "paid"))
    if bounty and has_bounty_label and not suspicious:
        return "high", False
    if bounty and not suspicious:
        return "medium", False
    if bounty:
        return "low", True
    return "none", suspicious


def score_issue(issue: dict, bounty: Optional[float], confidence: str) -> float:
    score = min(bounty / 100.0, 50.0) if bounty else 0.0
    score += {"high": 10, "medium": 5}.get(confidence, 0)
    score += min((issue.get("comments") or 0) / 10.0, 5)
    return round(score, 2)


def source_issue_ref(issue: dict):
    body = issue.get("body") or ""
    match = SOURCE_URL_RE.search(body)
    if not match:
        return None
    owner, repo, number = match.groups()
    return owner, repo, number, match.group(0).rstrip("., ")


async def canonicalize_candidate(issue: dict, client, headers: dict):
    """Return the original open issue for a mirror; skip closed/unverifiable candidates."""
    source = source_issue_ref(issue)
    if not source:
        return issue if issue.get("state", "open") == "open" else None

    owner, repo, number, source_url = source
    response = await client.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{number}",
        headers=headers,
    )
    if response.status_code != 200:
        return None
    original = response.json()
    if original.get("state") != "open" or original.get("pull_request"):
        return None

    original["repository_url"] = f"https://api.github.com/repos/{owner}/{repo}"
    original["_discovered_url"] = issue.get("html_url") or issue.get("url")
    original["_source_url"] = original.get("html_url") or source_url
    return original


async def verify_candidates(items: list[dict]) -> list[dict]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = "Bearer " + token

    semaphore = asyncio.Semaphore(5)
    async with httpx.AsyncClient(timeout=15) as client:
        async def verify_one(item):
            async with semaphore:
                try:
                    return await canonicalize_candidate(item, client, headers)
                except (httpx.HTTPError, ValueError):
                    return None

        checked = await asyncio.gather(*(verify_one(item) for item in items))
    unique = []
    seen = set()
    for issue in checked:
        if not issue:
            continue
        key = (issue.get("repository_url", ""), issue.get("number"))
        if key in seen:
            continue
        seen.add(key)
        unique.append(issue)
    return unique


async def github_search(q: str, topn: int) -> list[dict]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(GITHUB_API, params={"q": q, "per_page": min(topn, 100)}, headers=headers)
    if response.status_code != 200:
        raise HTTPException(response.status_code, "GitHub search failed: " + response.text[:300])
    return response.json().get("items", [])


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
async def home():
    return """<!doctype html><html><head><meta charset="utf-8"><title>Paid Issue Finder</title></head>
<body style="font-family:system-ui;max-width:900px;margin:40px auto;padding:20px">
<h1>Paid Issue Finder</h1><p>Find and rank GitHub issues with monetary bounties.</p>
<h2>Credit packages</h2><ul><li>100 queries — R$ 5,00</li><li>500 queries — R$ 25,00</li><li>1,000 queries — R$ 50,00</li></ul>
<form action="/search" method="get"><input name="q" style="width:70%;padding:12px" value="bounty language:Python state:open"><button>Search</button></form>
<p>Amounts detected by the finder are estimates, not guarantees of payment. Verify the original issue and reward terms.</p>
</body></html>"""


@app.post("/billing/checkout")
async def billing_checkout(data: CheckoutRequest):
    if data.package_id not in PACKAGES:
        raise HTTPException(400, "Unknown package")
    try:
        payment = await create_payment(data.email, data.package_id)
    except RuntimeError as exc:
        raise HTTPException(503, str(exc))
    return {
        "package": PACKAGES[data.package_id],
        "currency": "BRL",
        "payment_id": payment.get("id"),
        "invoice_url": payment.get("invoiceUrl"),
        "status": payment.get("status"),
    }


@app.get("/billing/balance")
async def billing_balance(x_api_key: Optional[str] = Header(default=None)):
    if not x_api_key:
        raise HTTPException(401, "X-API-Key required")
    account = get_account(x_api_key)
    if not account:
        raise HTTPException(401, "Invalid API key")
    return {"credits": account["credits"], "price_per_query_brl": 0.05}


@app.post("/webhooks/asaas")
async def asaas_webhook(request: Request):
    token = request.headers.get("asaas-access-token")
    try:
        processed = process_webhook(await request.json(), token)
    except PermissionError as exc:
        raise HTTPException(401, str(exc))
    return {"received": True, "processed": processed}


@app.get("/search", response_model=SearchResponse)
async def search(
    q: str = Query(..., min_length=2, max_length=500),
    topn: int = Query(20, ge=1, le=100),
    x_api_key: Optional[str] = Header(default=None),
):
    require_payment = os.getenv("REQUIRE_PAYMENT", "true").lower() == "true"
    account = None
    if require_payment:
        if not x_api_key:
            raise HTTPException(402, "Payment required. Buy credits and provide X-API-Key.")
        account = get_account(x_api_key)
        if not account or account["credits"] < 1:
            raise HTTPException(402, "Insufficient credits.")

    items = await github_search(q, topn)
    items = await verify_candidates(items)
    remaining = None
    if require_payment:
        if not consume_credit(x_api_key):
            raise HTTPException(402, "Insufficient credits.")
        remaining = account["credits"] - 1

    results = []
    for issue in items:
        bounty = extract_bounty((issue.get("title") or "") + " " + (issue.get("body") or ""))
        confidence, suspicious = assess_bounty(issue, bounty)
        repo = issue.get("repository_url", "").split("/repos/")[-1]
        results.append(IssueResult(
            title=issue.get("title", ""), url=issue.get("html_url", ""),
            repository=repo, number=issue.get("number", 0),
            labels=[x.get("name", "") for x in issue.get("labels", [])],
            bounty_usd=bounty, confidence=confidence, suspicious=suspicious,
            score=score_issue(issue, bounty, confidence),
        ))
    results.sort(key=lambda x: (x.confidence != "none", not x.suspicious, x.score), reverse=True)
    return SearchResponse(query=q, charged_brl=0.05, remaining_credits=remaining, results=results)
