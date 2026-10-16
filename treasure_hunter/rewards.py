from datetime import datetime,timezone
from .core import record,units
from .chains import NETWORKS,fail

def merkl(c,a,n):
    chain=NETWORKS[n][0]; url=f'https://api.merkl.xyz/v4/users/{a.lower()}/rewards?chainId={chain}'
    prefix=f'merkl:{n}:{a.lower()}'
    try:
        data=c.get(url)
        if not isinstance(data,list):raise ValueError('Schema Merkl inesperado')
        count=0
        for group in data:
            if group['chain']['id']!=chain:raise ValueError('Resposta de outra rede')
            for reward in group['rewards']:
                t=reward['token'];unclaimed=int(reward['amount'])-int(reward['claimed'])
                if unclaimed<0:raise ValueError('amount menor que claimed')
                proofs=reward.get('proofs',[])
                # The distributor is official evidence, but an unvalidated proof is not onchain confirmation.
                status='POTENCIAL' if unclaimed else 'NÃO ELEGÍVEL'
                if str(t.get('type','')).upper()=='POINT':status='NÃO ELEGÍVEL'
                r=record(prefix+':'+t['address'],'recompensa',n,'Merkl: '+t.get('symbol',t['address']),status,wallet=a,source=url,official_url='https://app.merkl.xyz/',proofs=proofs,onchain_verified=False,deadline=None,pending_raw=reward.get('pending'),detail='API oficial de distribuição; confirmar root, prova, valor já reivindicado e prazo on-chain antes de CONFIRMADO. Pending e pontos não são dinheiro disponível.')
                r.update(amount=units(unclaimed,t['decimals']),asset=t.get('symbol') or t['address']);count+=1;yield r
        yield record(prefix+':coverage','cobertura',n,'Merkl: consulta por endereço','CONFIRMADO',wallet=a,source=url,count=count,detail='Consulta bem-sucedida; lista vazia não exclui outros programas.')
    except Exception as e:yield fail(prefix+':coverage','cobertura',n,'Merkl: consulta por endereço',e,wallet=a,source=url)

def campaigns(c):
    url='https://api.merkl.xyz/v4/opportunities?items=20&page=0'
    try:
        data=c.get(url)
        if not isinstance(data,list):raise ValueError('Schema de campanhas inesperado')
        for x in data:
            yield record('campaign:merkl:'+str(x['id']),'campanha',str(x.get('chainId','multirrede')),x.get('name','Programa Merkl'),'POTENCIAL',source=url,official_url='https://app.merkl.xyz/',deadline=None,detail='Programa público, sem elegibilidade demonstrada para estas carteiras. APR/TVL não são recompensa pessoal.')
        yield record('campaign:coverage','cobertura','multirrede','Catálogo Merkl','CONFIRMADO',source=url,count=len(data),truncated=len(data)==20)
    except Exception as e:yield fail('campaign:coverage','cobertura','multirrede','Catálogo Merkl',e,source=url)

def recoveries(c,wallets,registry):
    # A registry is deliberately explicit: arbitrary third-party lists never establish entitlement.
    if not registry:
        yield fail('recoveries:coverage','recuperacao','multirrede','Restituições e compensações','Nenhum programa com verificador oficial cadastrado; cobertura não implementada para incidentes arbitrários.')
    for p in registry:
        deadline=p.get('deadline'); expired=deadline and datetime.fromisoformat(deadline.replace('Z','+00:00'))<datetime.now(timezone.utc)
        for w in wallets:
            if w['network']!=p['wallet_network']:continue
            key='recovery:'+p['id']+':'+w['address'];url=p['official_url']
            if expired:yield record(key,'recuperacao',p['wallet_network'],p['name'],'EXPIRADO',source=url,deadline=deadline,wallet=w['address']);continue
            if p.get('adapter')=='aave_merkle':
                yield aave_recovery(c,w['address'],p);continue
            yield fail(key,'recuperacao',p['wallet_network'],p['name'],'Programa cadastrado sem adaptador específico validado; link não demonstra elegibilidade.',source=url,deadline=deadline,wallet=w['address'])

def aave_recovery(c,a,p):
    from .merkle import verify_aave_claim,selector
    key='recovery:'+p['id']+':'+a;url=p['data_url']
    try:
        d=c.get(url)
        if d['merkleRoot'].lower()!=p['expected_root'].lower():raise ValueError('Root diverge do programa revisado')
        if not isinstance(d['claims'],dict) or not d['claims']:raise ValueError('Lista de claims inválida')
        claim=next((v for k,v in d['claims'].items() if k.lower()==a.lower()),None)
        r=record(key,'recuperacao','ethereum',p['name'],'NÃO ELEGÍVEL' if claim is None else 'POTENCIAL',wallet=a,source=url,official_url=p['official_url'],deadline=p.get('deadline'),detail='Endereço ausente da lista oficial desta distribuição.' if claim is None else 'Prova validada; consulta do distribuidor necessária para disponibilidade atual.')
        if claim:
            if not verify_aave_claim(a,claim,d['merkleRoot']):r.update(status='SUSPEITO',detail='Prova Merkle inválida');return r
            r.update(amount=units(claim['amountInWei'],p['decimals']),asset=p['symbol'],proof_valid=True,proof=claim['proof'])
            if p.get('distributor'):
                rpc=NETWORKS['ethereum'][2]
                if int(c.rpc(rpc,'eth_chainId',[]),16)!=1:raise ValueError('Chain ID incorreto')
                block=c.rpc(rpc,'eth_blockNumber',[]);did=p['distribution_id']
                raw=c.rpc(rpc,'eth_call',[{'to':p['distributor'],'data':'0x'+selector('getDistribution(uint256)')+f'{did:064x}'},block])
                if len(raw)!=130 or '0x'+raw[-64:]!=d['merkleRoot'].lower():raise ValueError('Root on-chain divergente')
                claimed=c.rpc(rpc,'eth_call',[{'to':p['distributor'],'data':'0x'+selector('isClaimed(uint256,uint256)')+f"{claim['index']:064x}{did:064x}"},block])
                if int(claimed,16) not in (0,1):raise ValueError('Resposta bool inválida')
                r.update(status='NÃO ELEGÍVEL' if int(claimed,16) else 'CONFIRMADO',onchain_verified=True,block=block,detail='Prova, root e isClaimed verificados no mesmo bloco. Gas e liquidez não avaliados; pagamento não executado.')
        return r
    except Exception as e:return fail(key,'recuperacao','ethereum',p['name'],e,wallet=a,source=url)
