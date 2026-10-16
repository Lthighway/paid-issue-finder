from datetime import datetime, timezone
from urllib.parse import urlencode
from .core import record, units

NETWORKS={
 'ethereum':(1,'ETH','https://ethereum-rpc.publicnode.com','https://eth.blockscout.com'),
 'base':(8453,'ETH','https://mainnet.base.org','https://base.blockscout.com'),
 'arbitrum':(42161,'ETH','https://arb1.arbitrum.io/rpc','https://arbitrum.blockscout.com'),
 'optimism':(10,'ETH','https://mainnet.optimism.io','https://optimism.blockscout.com'),
 'polygon':(137,'POL','https://polygon-bor-rpc.publicnode.com','https://polygon.blockscout.com'),
 'bnb':(56,'BNB','https://bsc-rpc.publicnode.com',None),
}

def fail(key,category,network,title,error,**kw):
    return record(key,category,network,title,'INDISPONÍVEL',detail=str(error)[:240],**kw)

def predicate(p,at):
    if p=={'unconditional':True}:return True
    if 'abs_before' in p or 'absBefore' in p:
        return at<datetime.fromisoformat(p.get('abs_before',p.get('absBefore')).replace('Z','+00:00'))
    if 'not' in p:
        x=predicate(p['not'],at);return None if x is None else not x
    for k in ('and','or'):
        if k in p:
            vals=[predicate(x,at) for x in p[k]]
            if k=='and':return False if False in vals else None if None in vals else all(vals)
            return True if True in vals else None if None in vals else any(vals)
    return None

def token_status(token):
    name=(token.get('name','') or '')+' '+(token.get('symbol','') or '')
    if token.get('is_scam') or any(s in name.lower() for s in ('https://','http://','www.','claim at','visit ')):
        return 'SUSPEITO'
    return 'POTENCIAL'

def evm(c,a,n):
    chain,symbol,rpc,explorer=NETWORKS[n]; prefix=f'{n}:{a.lower()}'
    try:
        if int(c.rpc(rpc,'eth_chainId',[]),16)!=chain:raise ValueError('Chain ID incorreto')
        block=c.rpc(rpc,'eth_blockNumber',[])
        balance=c.rpc(rpc,'eth_getBalance',[a,block]); count=c.rpc(rpc,'eth_getTransactionCount',[a,block])
        r=record(prefix+':native','saldo',n,'Saldo nativo','CONFIRMADO',wallet=a,source=rpc,block=block,transactions_sent=int(count,16))
        r.update(amount=units(int(balance,16),18),asset=symbol);yield r
    except Exception as e:yield fail(prefix+':native','saldo',n,'Saldo nativo',e,wallet=a,source=rpc)
    if not explorer:
        yield fail(prefix+':index','cobertura',n,'Tokens e histórico indexado','Sem indexador gratuito configurado; RPC não enumera todos os tokens',wallet=a)
        return
    for kind,path in [('historico','transactions'),('token','tokens')]:
        url=explorer+'/api/v2/addresses/'+a+'/'+path
        try:
            data=c.get(url); entries=data['items']; pages=1
            while data.get('next_page_params') and pages<3:
                data=c.get(url+'?'+urlencode(data['next_page_params']));entries.extend(data['items']);pages+=1
            truncated=bool(data.get('next_page_params'))
            if kind=='historico':
                history=[{k:x.get(k) for k in ('hash','timestamp','status','value','from','to')} for x in entries]
                last=entries[0].get('timestamp') if entries else None
                dormant=None
                if last:
                    dormant=(datetime.now(timezone.utc)-datetime.fromisoformat(last.replace('Z','+00:00'))).days>=180
                yield record(prefix+':history',kind,n,'Transações recentes','CONFIRMADO',wallet=a,source=url,history=history,count=len(entries),truncated=truncated,possibly_forgotten=dormant,detail='Inatividade >=180 dias é indício; não prova esquecimento. Histórico limitado a 3 páginas.')
            else:
                for item in entries:
                    t=item['token'];contract=t.get('address_hash') or t.get('address');d=t.get('decimals')
                    r=record(prefix+':token:'+str(contract),'token',n,t.get('symbol') or str(contract),token_status(t),wallet=a,source=url,contract=contract,balance_verified=True,liquidity='NÃO VERIFICADA',detail='Posse indexada não comprova liquidez nem recompensa. Metadados do token não são fonte oficial.')
                    r.update(amount=units(item['value'],d) if d is not None else str(item['value']),asset=t.get('symbol') or contract)
                    yield r
                yield record(prefix+':tokens_coverage','cobertura',n,'Cobertura de tokens','CONFIRMADO',wallet=a,source=url,count=len(entries),truncated=truncated,detail='Máximo 3 páginas; truncamento explícito.')
        except Exception as e:yield fail(prefix+':'+kind,kind,n,'Consulta '+kind,e,wallet=a,source=url)

def bitcoin(c,a):
    url='https://mempool.space/api/address/'+a
    try:
        d=c.get(url);s=d['chain_stats'];m=d['mempool_stats']
        r=record('bitcoin:'+a+':native','saldo','bitcoin','Saldo BTC confirmado','CONFIRMADO',wallet=a,source=url,unconfirmed_sats=m['funded_txo_sum']-m['spent_txo_sum'],transactions=s['tx_count'])
        r.update(amount=units(s['funded_txo_sum']-s['spent_txo_sum'],8),asset='BTC');yield r
    except Exception as e:yield fail('bitcoin:'+a+':native','saldo','bitcoin','Saldo BTC',e,wallet=a,source=url)
    try:
        tx=c.get(url+'/txs')
        yield record('bitcoin:'+a+':history','historico','bitcoin','Transações BTC','CONFIRMADO',wallet=a,source=url+'/txs',history=tx,count=len(tx),truncated=len(tx)>=25,detail='Últimas 25 transações; Ordinals/Runes não indexados.')
    except Exception as e:yield fail('bitcoin:'+a+':history','historico','bitcoin','Histórico BTC',e,wallet=a)

def solana(c,a):
    rpc='https://api.mainnet-beta.solana.com';prefix='solana:'+a
    for kind in ('native','history','tokens','tokens2022'):
        try:
            if kind=='native':
                d=c.rpc(rpc,'getBalance',[a,{'commitment':'finalized'}]);r=record(prefix+':native','saldo','solana','Saldo SOL','CONFIRMADO',wallet=a,source=rpc,slot=d['context']['slot']);r.update(amount=units(d['value'],9),asset='SOL');yield r
            elif kind=='history':
                d=c.rpc(rpc,'getSignaturesForAddress',[a,{'limit':100,'commitment':'finalized'}])
                yield record(prefix+':history','historico','solana','Transações SOL','CONFIRMADO',wallet=a,source=rpc,history=d,count=len(d),truncated=len(d)==100)
            else:
                program='TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA' if kind=='tokens' else 'TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb'
                d=c.rpc(rpc,'getTokenAccountsByOwner',[a,{'programId':program},{'encoding':'jsonParsed','commitment':'finalized'}])
                for x in d['value']:
                    info=x['account']['data']['parsed']['info'];t=info['tokenAmount']
                    r=record(prefix+':'+x['pubkey'],'token','solana',info['mint'],wallet=a,source=rpc,balance_verified=True,liquidity='NÃO VERIFICADA');r.update(amount=units(t['amount'],t['decimals']),asset=info['mint']);yield r
                yield record(prefix+':'+kind,'cobertura','solana',kind,'CONFIRMADO',wallet=a,source=rpc,count=len(d['value']))
        except Exception as e:yield fail(prefix+':'+kind,'saldo' if kind=='native' else 'cobertura','solana',kind,e,wallet=a,source=rpc)

def stellar(c,a):
    base='https://horizon.stellar.org';prefix='stellar:'+a
    for kind,path in [('account','/accounts/'+a),('history','/accounts/'+a+'/transactions?order=desc&limit=100'),('claims','/claimable_balances?claimant='+a+'&limit=200')]:
        url=base+path
        try:
            d=c.get(url)
            if kind=='account':
                for b in d['balances']:
                    native=b['asset_type']=='native';asset='XLM' if native else b.get('asset_code','POOL')+':'+b.get('asset_issuer',b.get('liquidity_pool_id',''))
                    r=record(prefix+':'+asset,'saldo' if native else 'token','stellar',asset,'CONFIRMADO' if native else 'POTENCIAL',wallet=a,source=url,balance_verified=True,liquidity='NATIVO' if native else 'NÃO VERIFICADA',detail='Saldo total; reserva mínima e passivos não descontados.');r.update(amount=b['balance'],asset=asset);yield r
            elif kind=='history':
                rows=d['_embedded']['records'];yield record(prefix+':history','historico','stellar','Transações XLM','CONFIRMADO',wallet=a,source=url,count=len(rows),truncated=len(rows)==100,history=[{k:x.get(k) for k in ('hash','created_at','successful')} for x in rows])
            else:
                rows=d['_embedded']['records']
                for x in rows:
                    p=next(y['predicate'] for y in x['claimants'] if y['destination']==a)
                    eligible=predicate(p,datetime.now(timezone.utc));native=x['asset']=='native'
                    status=('CONFIRMADO' if native else 'POTENCIAL') if eligible else 'NÃO ELEGÍVEL' if eligible is False else 'INDISPONÍVEL'
                    r=record(prefix+':claim:'+x['id'],'recompensa','stellar','Claimable balance',status,wallet=a,source=base+'/claimable_balances/'+x['id'],predicate=p,eligibility_verified=eligible,deadline=None,detail='Direito técnico de reivindicação; origem e liquidez de ativos não nativos não verificadas. Nenhuma transação executada.');r.update(amount=x['amount'],asset='XLM' if native else x['asset']);yield r
                yield record(prefix+':claims','cobertura','stellar','Claimable balances consultados','CONFIRMADO',wallet=a,source=url,count=len(rows),truncated=len(rows)==200)
        except Exception as e:yield fail(prefix+':'+kind,'cobertura','stellar',kind,e,wallet=a,source=url)

def stellar_liquidity(c,items):
    """Inspect order books without following issuer URLs or trusting token names."""
    books={}
    for r in items:
        if r['network']!='stellar' or r['category'] not in ('token','recompensa') or not r.get('asset') or r['asset']=='XLM':continue
        asset=r['asset']
        if ':' not in asset:continue
        code,issuer=asset.split(':',1)
        if asset not in books:
            url='https://horizon.stellar.org/order_book?'+urlencode({'selling_asset_type':'credit_alphanum4' if len(code)<=4 else 'credit_alphanum12','selling_asset_code':code,'selling_asset_issuer':issuer,'buying_asset_type':'native','limit':20})
            try:
                d=c.get(url)
                books[asset]={'status':'OFERTAS XLM PRESENTES' if d['bids'] else 'SEM OFERTAS DE COMPRA XLM','bid_levels':len(d['bids']),'source':url,'checked_at':datetime.now(timezone.utc).isoformat()}
            except Exception as e:books[asset]={'status':'INDISPONÍVEL','error':str(e)[:180],'source':url}
        r['market_check']=books[asset]
        r['liquidity']=books[asset]['status']
        r['detail']=r.get('detail','')+' Token de emissor terceiro. Livro XLM não prova resgate, legitimidade, profundidade suficiente ou execução; nenhuma cotação foi convertida em dinheiro recebido.'
        if code in ('BTC','XRP','XLMWRAPPED','Kaspa','TRUMPSOL'):
            r['risk_flags']=['Nome remete a ativo de outra rede; lastro e emissor não verificados']
