# Paid Issue Finder

Find GitHub issues that appear to contain monetary bounties and rank opportunities.

## Pricing

- 100 queries — US$5
- 500 queries — US$20
- 1,000 queries — US$35
- Search consumption: 1 credit per query
- Target unit price: US$0.05/query

## Payment flow

Customer -> /billing/checkout -> Asaas PIX charge -> payment -> Asaas webhook -> credit ledger -> search.

The application uses Asaas for the first payment integration. Asaas supports Pix and cards and provides Webhooks for payment status updates.

## Environment

GITHUB_TOKEN is optional but recommended for GitHub API rate limits.

ASAAS_API_KEY and ASAAS_WEBHOOK_TOKEN are secrets and must never be committed.

Use the Asaas sandbox URL during development:
https://api-sandbox.asaas.com/v3

## API

Create a package payment:

POST /billing/checkout

JSON:
{"email":"you@example.com","package_id":"starter"}

The response contains the Asaas invoice URL.

After payment is confirmed by the webhook, the account receives its credits.

Check balance:

GET /billing/balance

Header:
X-API-Key: pif_...

Search:

GET /search?q=bounty%20language:Python%20state:open

Header:
X-API-Key: pif_...

When payment is enabled, one credit is consumed per successful search.

Webhook:

POST /webhooks/asaas

The endpoint validates the asaas-access-token header and stores payment IDs to prevent duplicate credit allocation.

## Run

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Windows PowerShell:

python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

## Production checklist

1. Create/verify an Asaas production account.
2. Create production API credentials.
3. Deploy this container behind HTTPS.
4. Set ASAAS_API_KEY and ASAAS_WEBHOOK_TOKEN as server secrets.
5. Configure an Asaas webhook for payment events pointing to /webhooks/asaas.
6. Test the complete credit flow in sandbox.
7. Add rate limiting, abuse protection and terms/privacy pages.
8. Only then advertise the service publicly.

License: MIT
