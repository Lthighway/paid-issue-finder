import os
import re
from typing import Optional
import httpx
from fastapi import FastAPI, Header, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Paid Issue Finder", version="0.1.0")
GITHUB_API = "https://api.github.com/search/issues"
PRICE_USD_CENTS = 5

class IssueResult(BaseModel):
    title: str
    url: str
    repository: str
    number: int
    labels: list[str]
    bounty_usd: Optional[float] = None
    score: float

class SearchResponse(BaseModel):
    query: str
    charged_usd: float
    results: list[IssueResult]

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
                values.append(float(match.replace(",", "")))
            except ValueError:
                pass
    return max(values) if values else None

def score_issue(issue: dict, bounty: Optional[float]) -> float:
    score = 0.0
    if bounty:
        score += min(bounty / 100.0, 50.0)
    labels = " ".join(x.get("name", "") for x in issue.get("labels", [])).lower()
    if any(k in labels for k in ("bounty", "reward", "paid", "help wanted", "good first issue")):
        score += 10
    score += min(issue.get("comments", 0) / 10.0, 5)
    return round(score, 2)

async def github_search(q: str, topn: int) -> list[dict]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    params = {"q": q, "per_page": min(topn, 100)}
    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(GITHUB_API, params=params, headers=headers)
    if response.status_code != 200:
        raise HTTPException(response.status_code, "GitHub search failed: " + response.text[:300])
    return response.json().get("items", [])

@app.get("/", response_class=HTMLResponse)
async def home():
    return """<!doctype html>
<html><head><meta charset="utf-8"><title>Paid Issue Finder</title>
<style>body{font-family:system-ui;max-width:900px;margin:40px auto;padding:0 20px}input{width:70%;padding:12px}button{padding:12px 18px}li{margin:14px 0}</style>
</head><body><h1>Paid Issue Finder</h1>
<p>Find GitHub issues with monetary bounties and rank the best opportunities.</p>
<form action="/search" method="get"><input name="q" value="bounty language:Python state:open" placeholder="bounty language:Python"><button>Search — $0.05</button></form>
<p>Price per query: US$0.05. Payment enforcement is a replaceable layer and must be configured before public monetization.</p>
</body></html>"""

@app.get("/search", response_model=SearchResponse)
async def search(
    q: str = Query(..., min_length=2, max_length=500),
    topn: int = Query(20, ge=1, le=100),
    x_api_key: Optional[str] = Header(default=None),
):
    require_payment = os.getenv("REQUIRE_PAYMENT", "false").lower() == "true"
    if require_payment and not x_api_key:
        raise HTTPException(402, "Payment required. Supply a valid API key/credit.")
    items = await github_search(q, topn)
    results = []
    for issue in items:
        body = issue.get("body") or ""
        text = issue.get("title", "") + " " + body
        bounty = extract_bounty(text)
        repo = issue.get("repository_url", "").split("/repos/")[-1]
        results.append(IssueResult(
            title=issue.get("title", ""),
            url=issue.get("html_url", ""),
            repository=repo,
            number=issue.get("number", 0),
            labels=[x.get("name", "") for x in issue.get("labels", [])],
            bounty_usd=bounty,
            score=score_issue(issue, bounty),
        ))
    results.sort(key=lambda x: (x.bounty_usd or 0, x.score), reverse=True)
    return SearchResponse(query=q, charged_usd=PRICE_USD_CENTS / 100, results=results)
