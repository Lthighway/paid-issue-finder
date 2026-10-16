"""Safe payment-route recommendations. This module never transfers funds."""
import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config" / "payouts.json"

def recommend(network=None, supports_crypto=False, supports_paypal=False,
              provider_pays_fees=False, config_path=CONFIG_PATH):
    cfg = json.loads(Path(config_path).read_text(encoding="utf-8"))
    if cfg["spending_limit"] != "0" or cfg["automatic_claims"] or cfg["automatic_transfers"]:
        raise ValueError("Unsafe payout settings")
    if not provider_pays_fees:
        return {"status": "BLOCKED", "reason": "Zero owner cost not verified"}
    if supports_crypto and network in cfg["crypto"]:
        return {"status": "SETUP_REQUIRED", "method": "crypto",
                "destination": cfg["crypto"][network],
                "reason": "Register destination with legitimate payer"}
    if supports_paypal:
        return {"status": "SETUP_REQUIRED", "method": "paypal",
                "destination": cfg["paypal"]["email"],
                "reason": "Register PayPal with legitimate payer"}
    return {"status": "UNAVAILABLE", "reason": "No compatible verified payout route"}
