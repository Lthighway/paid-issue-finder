from urllib.parse import urlencode
from scripts.analyze_issues import analyze_issue
from scripts import run_finder
from .core import record
from .chains import fail
from .zero_cost import submitted_report

def collect(c,limit=12):
    url='https://api.github.com/search/issues?'+urlencode({'q':'is:issue is:open bounty','sort':'updated','per_page':limit})
    # Reuse canonicalization and competition evaluation, replacing only the gh transport.
    original=run_finder.gh_json
    run_finder.gh_json=lambda args:c.get('https://api.github.com/'+args[0])
    try:
        data=c.get(url);seen=set()
        for candidate in data['items']:
            try:
                issue=run_finder.canonicalize_issue(candidate)
                if not issue:continue
                repo=run_finder.issue_repo(issue);number=issue['number'];key=f'github:{repo}:{number}'
                if key in seen:continue
                seen.add(key)
                if submitted_report(issue):
                    yield fail(key,'bounty','externa',issue['title'],'Relatório de vulnerabilidade já submetido por terceiro; não demonstra oferta disponível ao proprietário.',source=issue['html_url'])
                    continue
                meta=c.get('https://api.github.com/repos/'+repo)
                if meta.get('archived'):continue
                issue['author']=issue.get('user');issue['updatedAt']=issue.get('updated_at')
                history=run_finder.repo_history(repo,number);analysis=analyze_issue(issue,meta,history)
                if not analysis:continue
                status='SUSPEITO' if analysis['verdict']=='AVOID' else 'POTENCIAL'
                body=issue.get('body') or '';platform='Algora/GitHub' if 'algora.io' in body else 'GitHub'
                complexity='ALTA (heurística)' if any(k in (issue['title']+' '+body).lower() for k in ('architecture','migration','refactor','security')) else 'NÃO DETERMINADA'
                r=record(key,'bounty','externa',issue['title'],status,source=issue['html_url'],platform=platform,deadline=None,competition=analysis['competition'],complexity=complexity,payer_reputation={'stars':meta.get('stargazers_count'),'payment_history_verified':False},completion_probability=None,payment_probability=None,analysis=analysis,detail='Valor extraído do texto, sujeito a contexto. Probabilidades sem base calibrada: não estimáveis. Issue aberta não garante vaga nem pagamento.')
                r.update(announced_value=analysis['value'],announced_currency='USD',value_usd=analysis['value']);yield r
            except Exception as e:yield fail('github:issue:'+str(candidate.get('id')),'bounty','externa','Falha ao verificar issue',e,source=candidate.get('html_url'))
        yield record('github:coverage','cobertura','externa','Pesquisa GitHub/Algora','CONFIRMADO',source=url,count=len(data['items']),truncated=data.get('total_count',0)>limit,detail='Algora detectada em issues públicas; não cobre catálogo completo ou API autenticada. Máximo 12 candidatos por execução.')
    except Exception as e:yield fail('github:coverage','cobertura','externa','Pesquisa de bounties',e,source=url)
    finally:run_finder.gh_json=original

def refresh_known(c,store,current):
    """Recheck tracked issues missing from the bounded discovery window."""
    seen={x['id'] for x in current}
    known=store.db.execute("SELECT payload FROM observations WHERE id LIKE 'github:%' ORDER BY last_seen DESC LIMIT 30").fetchall()
    import json
    for payload, in known:
        previous=json.loads(payload)
        if previous['category']!='bounty' or previous['id'] in seen:continue
        parts=previous['id'].split(':')
        if len(parts)!=3:continue
        _,repo,number=parts
        try:
            issue=c.get(f'https://api.github.com/repos/{repo}/issues/{number}')
            if submitted_report(issue):
                yield fail(previous['id'],'bounty','externa',previous['title'],'Relatório já submetido por terceiro; recompensa disponível não demonstrada.',source=previous.get('source'))
                continue
            r=dict(previous);r.pop('evidence',None);r.pop('checked_at',None)
            if issue['state']!='open':r.update(status='NÃO ELEGÍVEL',detail='Issue encerrada na fonte original; não demonstra pagamento ao proprietário.')
            else:
                # A live issue can still have a withdrawn/changed bounty: re-evaluate the text.
                meta=c.get('https://api.github.com/repos/'+repo)
                analysis=analyze_issue(issue,meta,{})
                if not analysis or meta.get('archived'):r.update(status='INDISPONÍVEL',detail='Bounty não reconfirmada no texto atual ou repositório arquivado.')
                else:r.update(status='SUSPEITO' if analysis['verdict']=='AVOID' else 'POTENCIAL',announced_value=analysis['value'],value_usd=analysis['value'],analysis=analysis,competition='UNKNOWN',detail='Issue continua aberta; valor reavaliado. Concorrência não reavaliada fora da janela de descoberta.')
            yield r
        except Exception as e:yield fail(previous['id'],'bounty','externa',previous['title'],e,source=previous.get('source'))
