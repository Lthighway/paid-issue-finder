"""Official, authenticated agent discovery only. Never registers or claims payouts."""
import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone

from .core import record
from .chains import fail

URL = 'https://superteam.fun/api/agents/listings/live?take=20'


def parse(data):
    # Unknown formats must remain unavailable, not silently produce zero results.
    rows = data if isinstance(data, list) else data.get('listings') if isinstance(data, dict) else None
    if not isinstance(rows, list):
        raise ValueError('Schema Superteam não validado; integração precisa de amostra autenticada')
    for row in rows:
        if row.get('agentAccess') not in ('AGENT_ALLOWED', 'AGENT_ONLY'):
            continue
        deadline = row.get('deadline')
        expired = bool(deadline and datetime.fromisoformat(deadline.replace('Z', '+00:00')) <= datetime.now(timezone.utc))
        r = record('superteam:' + str(row['id']), 'bounty', 'solana', row['title'],
                   'EXPIRADO' if expired else 'POTENCIAL', source=URL,
                   official_url='https://superteam.fun/earn/agents',
                   platform='Superteam Earn', deadline=deadline,
                   reward_pool=row.get('rewardAmount'), reward_token=row.get('token'),
                   agent_access=row['agentAccess'], requires_human_claim=True,
                   detail='Prêmio total do anúncio não é pagamento pessoal. Exige seleção, trabalho aceito e vínculo humano para pagamento. Custos e elegibilidade individual não confirmados.')
        yield r


def collect():
    key = os.getenv('SUPERTEAM_API_KEY')
    if not key:
        yield fail('superteam:coverage', 'cobertura', 'solana', 'Superteam Earn — agentes',
                   'Falta SUPERTEAM_API_KEY nos Actions Secrets; cadastro e vínculo humano não realizados.', source=URL)
        return
    try:
        req = urllib.request.Request(URL, headers={'Authorization': 'Bearer ' + key, 'Accept': 'application/json', 'User-Agent': 'OMNIA-Treasure-Hunter/1.0'})
        with urllib.request.urlopen(req, timeout=20) as response:
            body = response.read(2_000_001)
        if len(body) > 2_000_000:
            raise ValueError('Resposta muito grande')
        yield from parse(json.loads(body))
        yield record('superteam:coverage', 'cobertura', 'solana', 'Superteam Earn — agentes', 'CONFIRMADO', source=URL, detail='Consulta autenticada concluída; máximo 20 anúncios.')
    except Exception as exc:
        # Do not expose authorization headers or credential-bearing error strings.
        yield fail('superteam:coverage', 'cobertura', 'solana', 'Superteam Earn — agentes', type(exc).__name__ + ': consulta ou schema indisponível', source=URL)
