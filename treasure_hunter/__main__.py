import argparse
import json
from pathlib import Path
from .core import Client,Store,now,record
from .validation import validate
from . import chains,rewards,bounties
from .render import render
from .notify import deliver

ROOT=Path(__file__).parent

def main():
    p=argparse.ArgumentParser();p.add_argument('command',choices=['scan','notify','wallet']);p.add_argument('--state',default='treasure-state');p.add_argument('--config',default=str(ROOT/'config/wallets.json'));p.add_argument('--no-bounties',action='store_true');p.add_argument('--action',choices=['add','remove','list'],default='list');p.add_argument('--network');p.add_argument('--address');args=p.parse_args()
    wallets=json.loads(Path(args.config).read_text())
    if args.command=='wallet':
        if args.action=='list':print(json.dumps(wallets,indent=2));return
        if not args.network or not args.address:p.error('--network e --address obrigatórios')
        w={'network':args.network,'address':args.address}
        if args.action=='add':
            valid,reason=validate(args.network,args.address)
            if not valid:p.error(reason)
            if w not in wallets:wallets.append(w)
        else:wallets=[x for x in wallets if x!=w]
        Path(args.config).write_text(json.dumps(wallets,indent=2)+'\n');return
    state=Path(args.state);state.mkdir(parents=True,exist_ok=True);store=Store(state/'monitor.sqlite')
    if args.command=='notify':print(json.dumps(deliver(store)));return
    client=Client(store);items=[]
    def collect(generator):
        for r in generator:
            r['checked_at']=now();r['evidence']=[e for e in client.evidence if e['url']==r.get('source')][-1:];items.append(r)
            print(json.dumps({'event':'observation','id':r['id'],'status':r['status']},ensure_ascii=False),flush=True)
    for w in wallets:
        network,a=w['network'],w['address'];valid,reason=validate(network,a)
        if not valid:
            items.append(record(network+':'+a+':invalid','configuracao',network,'Endereço inválido','INDISPONÍVEL',wallet=a,detail=reason));continue
        if network=='evm':
            for n in chains.NETWORKS:collect(chains.evm(client,a,n));collect(rewards.merkl(client,a,n))
        else:collect(getattr(chains,network)(client,a))
    collect(rewards.campaigns(client))
    collect(rewards.recoveries(client,wallets,json.loads((ROOT/'config/recoveries.json').read_text())))
    if not args.no_bounties:collect(bounties.collect(client))
    result={'schema_version':1,'checked_at':now(),'wallets':wallets,'items':items,'notifications':'Configuráveis; verificar etapa notify','received_total':None}
    changes=store.save(result);result['changes']=len(changes);result['history']=store.history();render(result,state)
    (state/'evidence.json').write_text(json.dumps(client.evidence,indent=2))
    print(json.dumps({'event':'complete','items':len(items),'changes':len(changes),'report':str(state/'REPORT.md')}))

if __name__=='__main__':main()
