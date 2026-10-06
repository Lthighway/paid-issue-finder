import os
import re
from typing import Optional
import httpx
from fastapi import FastAPI, Header, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Paid Issue Finder", version="0.2.0")
GITHUB_API = "https://api.github.com/search/issues"
PRICE_USD_CENTS = 5
MAX_REASONABLE_BOUNTY_USD = 100000

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
                value = float(match.replace(",", ""))
                if 0 < value <= MAX_REASONABLE_BOUNTY_USD:
                    values.append(value)
            except ValueError:
                pass
    return max(values) if values else None

def assess_bounty(issue: dict, bounty: Optional[float]) -> tuple[str, bool]:
    text = ((issue.get("title") or "") + " " + (issue.get("body") or "")).lower()
    labels = " ".join(x.get("name", "") for x in issue.get("labels", [])).lower()
    suspicious_terms = (
        "pppdud", "take your money back", "follow my", "backflip",
        "gazillion", "money before", "value: 0.00", "approximately 0 usd"
    )
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
    score = 0.0
    if bounty:
        score += min(bounty / 100.0, 50.0)
    if confidence == "high":
        score += 10
    elif confidence == "medium":
        score += 5
    score += min((issue.get("comments") or 0) / 10.0, 5)
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
<style>body{font-family:system-ui;max-width:900px;margin:40px auto;padding:0 20px}input{width:70%;padding:12px}button{padding:12px 18px}</style>
</head><body><h1>Paid Issue Finder</h1>
<p>Find GitHub issues with monetary bounties and rank opportunities.</p>
<form action="/search" method="get"><input name="q" value="bounty language:Python state:open" placeholder="bounty language:Python"><button>Search — $0.05</button></form>
<p>Price per query: US$0.05. Results include confidence and suspicious-signal detection.</p>
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
        bounty = extract_bounty((issue.get("title") or "") + " " + (issue.get("body") or ""))
        confidence, suspicious = assess_bounty(issue, bounty)
        repo = issue.get("repository_url", "").split("/repos/")[-1]
        results.append(IssueResult(
            title=issue.get("title", ""),
            url=issue.get("html_url", ""),
            repository=repo,
            number=issue.get("number", 0),
            labels=[x.get("name", "") for x in issue.get("labels", [])],
            bounty_usd=bounty,
            confidence=confidence,
            suspicious=suspicious,
            score=score_issue(issue, bounty, confidence),
        ))
    results.sort(key=lambda x: (x.confidence != "none", not x.suspicious, x.score), reverse=True)
    return SearchResponse(query=q, charged_usd=PRICE_USD_CENTS / 100, results=results)
