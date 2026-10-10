import pytest

from app import billing


def make_account(tmp_path, monkeypatch):
    monkeypatch.setattr(billing, "DB_PATH", str(tmp_path / "test.db"))
    return billing.get_or_create_account("customer@example.com")


def event_for(account, payment_id="pay_123", value=5.00, package_id="starter"):
    return {
        "event": "PAYMENT_RECEIVED",
        "payment": {
            "id": payment_id,
            "externalReference": f"{account['api_key']}:{package_id}",
            "value": value,
        },
    }


def test_webhook_requires_configured_secret(tmp_path, monkeypatch):
    make_account(tmp_path, monkeypatch)
    monkeypatch.delenv("ASAAS_WEBHOOK_TOKEN", raising=False)
    with pytest.raises(PermissionError):
        billing.process_webhook({"event": "PAYMENT_RECEIVED", "payment": {"id": "p"}}, None)


def test_valid_payment_adds_credits_once(tmp_path, monkeypatch):
    account = make_account(tmp_path, monkeypatch)
    monkeypatch.setenv("ASAAS_WEBHOOK_TOKEN", "a" * 40)
    event = event_for(account)

    assert billing.process_webhook(event, "a" * 40) is True
    assert billing.get_account(account["api_key"])["credits"] == 100

    # Asaas may retry webhook delivery; duplicate events must not double-credit.
    assert billing.process_webhook(event, "a" * 40) is True
    assert billing.get_account(account["api_key"])["credits"] == 100


def test_mismatched_payment_amount_does_not_grant_credits(tmp_path, monkeypatch):
    account = make_account(tmp_path, monkeypatch)
    monkeypatch.setenv("ASAAS_WEBHOOK_TOKEN", "b" * 40)

    assert billing.process_webhook(event_for(account, value=500.00), "b" * 40) is False
    assert billing.get_account(account["api_key"])["credits"] == 0


def test_unknown_account_does_not_receive_credits(tmp_path, monkeypatch):
    monkeypatch.setenv("ASAAS_WEBHOOK_TOKEN", "c" * 40)
    event = {
        "event": "PAYMENT_RECEIVED",
        "payment": {
            "id": "pay_unknown",
            "externalReference": "pif_unknown:starter",
            "value": 5.00,
        },
    }

    assert billing.process_webhook(event, "c" * 40) is False
