import os
import sqlite3
from datetime import datetime, timezone
from uuid import uuid4
import httpx

ASAAS_BASE_URL = os.getenv("ASAAS_BASE_URL", "https://api.asaas.com/v3")
PACKAGES = {
    "starter": {"credits": 100, "price": 5.00, "label": "100 consultas"},
    "pro": {"credits": 500, "price": 20.00, "label": "500 consultas"},
    "scale": {"credits": 1000, "price": 35.00, "label": "1.000 consultas"},
}
DB_PATH = os.getenv("DATABASE_PATH", "paid_issue_finder.db")

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("CREATE TABLE IF NOT EXISTS accounts (api_key TEXT PRIMARY KEY, email TEXT NOT NULL, credits INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS payments (payment_id TEXT PRIMARY KEY, api_key TEXT NOT NULL, package_id TEXT NOT NULL, credits INTEGER NOT NULL, amount REAL NOT NULL, status TEXT NOT NULL, processed_at TEXT)")
    conn.commit()
    return conn

def get_or_create_account(email: str):
    conn = db()
    row = conn.execute("SELECT * FROM accounts WHERE email = ?", (email,)).fetchone()
    if row:
        conn.close()
        return dict(row)
    key = "pif_" + uuid4().hex
    conn.execute("INSERT INTO accounts(api_key,email,credits,created_at) VALUES(?,?,0,?)", (key, email, datetime.now(timezone.utc).isoformat()))
    conn.commit()
    row = conn.execute("SELECT * FROM accounts WHERE api_key = ?", (key,)).fetchone()
    conn.close()
    return dict(row)

def get_account(api_key: str):
    conn = db()
    row = conn.execute("SELECT * FROM accounts WHERE api_key = ?", (api_key,)).fetchone()
    conn.close()
    return dict(row) if row else None

def consume_credit(api_key: str):
    conn = db()
    row = conn.execute("SELECT credits FROM accounts WHERE api_key = ?", (api_key,)).fetchone()
    if not row or row["credits"] < 1:
        conn.close()
        return False
    conn.execute("UPDATE accounts SET credits = credits - 1 WHERE api_key = ? AND credits > 0", (api_key,))
    conn.commit()
    conn.close()
    return True

async def create_payment(email: str, package_id: str):
    package = PACKAGES[package_id]
    api_key = os.getenv("ASAAS_API_KEY")
    if not api_key:
        raise RuntimeError("ASAAS_API_KEY is not configured")
    account = get_or_create_account(email)
    headers = {"access_token": api_key, "Content-Type": "application/json"}
    async with httpx.AsyncClient(timeout=20) as client:
        customer = await client.post(ASAAS_BASE_URL + "/customers", json={"name": "Paid Issue Finder", "email": email}, headers=headers)
        if customer.status_code in (200, 201):
            customer_id = customer.json()["id"]
        else:
            search = await client.get(ASAAS_BASE_URL + "/customers", params={"email": email}, headers=headers)
            search.raise_for_status()
            data = search.json().get("data", [])
            if not data:
                raise RuntimeError("Could not create or find Asaas customer")
            customer_id = data[0]["id"]
        charge = {
            "customer": customer_id,
            "billingType": "PIX",
            "value": package["price"],
            "dueDate": datetime.now(timezone.utc).date().isoformat(),
            "description": f"Paid Issue Finder — {package['label']}",
            "externalReference": f"{account['api_key']}:{package_id}",
        }
        response = await client.post(ASAAS_BASE_URL + "/payments", json=charge, headers=headers)
        response.raise_for_status()
        return response.json()

def process_webhook(event: dict, webhook_token: str | None):
    expected = os.getenv("ASAAS_WEBHOOK_TOKEN")
    if expected and webhook_token != expected:
        raise PermissionError("Invalid webhook token")
    event_name = event.get("event")
    payment = event.get("payment") or {}
    payment_id = payment.get("id")
    if event_name not in {"PAYMENT_RECEIVED", "PAYMENT_CONFIRMED"} or not payment_id:
        return False
    external = payment.get("externalReference", "")
    if ":" not in external:
        return False
    api_key, package_id = external.rsplit(":", 1)
    package = PACKAGES.get(package_id)
    if not package:
        return False
    conn = db()
    existing = conn.execute("SELECT payment_id FROM payments WHERE payment_id = ?", (payment_id,)).fetchone()
    if existing:
        conn.close()
        return True
    conn.execute("INSERT INTO payments(payment_id,api_key,package_id,credits,amount,status,processed_at) VALUES(?,?,?,?,?,?,?)",
                 (payment_id, api_key, package_id, package["credits"], package["price"], event_name, datetime.now(timezone.utc).isoformat()))
    conn.execute("UPDATE accounts SET credits = credits + ? WHERE api_key = ?", (package["credits"], api_key))
    conn.commit()
    conn.close()
    return True
