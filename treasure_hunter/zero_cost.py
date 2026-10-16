"""Financial execution stays disabled until a real no-cost payout route exists."""


def assess(row):
    category = row['category']
    if category == 'saldo':
        reason = 'Patrimônio existente, não renda nova.'
    elif category == 'bounty':
        reason = 'Exige trabalho aceito e pagamento do patrocinador; não há crédito liberado.'
    elif category in ('recompensa', 'recuperacao'):
        reason = 'Sem comprovação de todas as taxas e reservas pagas por terceiro; claim automático desativado.'
    else:
        reason = 'Registro informativo; não constitui pagamento.'
    return {
        'owner_spending_limit': '0',
        'automatic_payout_enabled': False,
        'zero_cost_verified': False,
        'blocker': reason,
        'income_received': None,
    }


def annotate(items):
    for item in items:
        item['payout_assessment'] = assess(item)


def submitted_report(issue):
    body = (issue.get('body') or '').lower()
    return ('we identified' in body and 'vulnerability' in body and 'severity' in body) or 'bounty-submission' in body
