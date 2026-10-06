# Paid Issue Finder

A small API/web service that discovers GitHub issues that appear to contain monetary bounties and ranks them as opportunities.

## Product model

- Search price: US$0.05 per query
- Data source: GitHub Issues Search API
- Ranking: detected bounty amount, bounty/reward labels and discussion activity
- API-first design so a payment provider can be swapped without rewriting the search engine

## Current MVP

- FastAPI service
- Browser search page
- GitHub issue search integration
- USD bounty extraction from issue title/body
- Opportunity scoring
- Docker deployment
- Payment enforcement boundary

## Run locally

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Windows PowerShell:

    python -m venv .venv
    .\\.venv\\Scripts\\Activate.ps1
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Open http://127.0.0.1:8000.

## API

GET /search?q=bounty%20language:Python%20state:open

The response includes the detected bounty, issue URL, labels and opportunity score.

## Monetization

The intended unit price is US$0.05/query.

Setting a price in application code does not itself collect money. Before public monetization, connect a payment/credit provider and make the provider authorize or debit one query before calling /search. The REQUIRE_PAYMENT switch intentionally prevents pretending payment has already been implemented.

Recommended production flow:

1. User buys credits.
2. Payment provider confirms payment.
3. API issues credits/API key.
4. Each successful search consumes 1 credit.
5. API returns remaining balance.
6. Add rate limits and abuse protection.

## Roadmap

- Payment provider integration
- User accounts/API keys
- Credit ledger
- Better bounty detection for major bounty platforms and custom formats
- Filters for minimum bounty, language, repository stars and activity
- Opportunity history and alerts
- Public landing page
- Analytics

## License

MIT
