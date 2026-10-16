import html
import json
from pathlib import Path

def render(result,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    (out/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    def clean(x):return str(x if x is not None else '—').replace('|','/').replace('\n',' ')
    lines=['# OMNIA Treasure Hunter','',f"Verificação: {result['checked_at']}",'','Saldo ≠ valor anunciado ≠ recompensa elegível ≠ dinheiro recebido. Não somamos moedas diferentes.','', '## Resultados','', '| Rede | Categoria | Resultado | Status | Quantidade | Ativo | Fonte |','|---|---|---|---|---|---|---|']
    for r in result['items']:
        lines.append('| '+' | '.join(clean(r.get(k)) for k in ('network','category','title','status','amount','asset','source'))+' |')
    lines+=['','## Evidências e limitações','']
    for r in result['items']:
        if r.get('detail'):lines.append(f"- **{clean(r['title'])} ({r['network']})**: {clean(r['detail'])}")
    lines+=['','## Operação','',f"Mudanças nesta execução: {result.get('changes',0)}",'Histórico: SQLite e branch treasure-data. Fontes com erro não equivalem a saldo zero.','Notificações exigem Secrets. Nenhuma assinatura, transferência ou aprovação é executada.']
    (out/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    template=Path(__file__).with_name('dashboard.html').read_text()
    payload=json.dumps(result,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    (out/'index.html').write_text(template.replace('__PAYLOAD__',payload),encoding='utf-8')
