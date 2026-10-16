import json
from treasure_hunter.payout_routes import recommend

def test_no_verified_free_route():
    result = recommend(network="solana", supports_crypto=True)
    assert result["status"] == "BLOCKED"

def test_free_crypto_route_requires_payer_setup():
    result = recommend(network="solana", supports_crypto=True, provider_pays_fees=True)
    assert result["status"] == "SETUP_REQUIRED"
    assert result["method"] == "crypto"

def test_free_paypal_route_requires_payer_setup():
    result = recommend(supports_paypal=True, provider_pays_fees=True)
    assert result["status"] == "SETUP_REQUIRED"
    assert result["method"] == "paypal"

def test_no_transfer_or_claim_enabled():
    from treasure_hunter.payout_routes import CONFIG_PATH
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    assert cfg["spending_limit"] == "0"
    assert cfg["automatic_claims"] is False
    assert cfg["automatic_transfers"] is False
