import hashlib
import json
import os
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal

STATUSES=('CONFIRMADO','POTENCIAL','NÃO ELEGÍVEL','EXPIRADO','SUSPEITO','INDISPONÍVEL')
def now():return datetime.now(timezone.utc).isoformat()
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def units(raw,decimals):return str(Decimal(str(raw))/(Decimal(10)**int(decimals)))
def record(key,category,network,title,status='POTENCIAL',**kw):
    assert status in STATUSES
    return dict(id=key,category=category,network=network,title=title,status=status,amount=None,asset=None,value_usd=None,received=None,**kw)

class Store:
    def __init__(self,path):
        self.db=sqlite3.connect(path)
        self.db.executescript('''
        CREATE TABLE IF NOT EXISTS cache(key TEXT PRIMARY KEY, ts REAL, body TEXT);
        CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY, at TEXT, payload TEXT);
        CREATE TABLE IF NOT EXISTS observations(id TEXT PRIMARY KEY, fingerprint TEXT, payload TEXT, last_seen TEXT);
        CREATE TABLE IF NOT EXISTS outbox(id TEXT PRIMARY KEY, payload TEXT, channels TEXT DEFAULT '[]', sent INTEGER DEFAULT 0);
        ''')
    def save(self,result):
        changes=[]
        for r in result['items']:
            # Observation timestamps, raw response hashes and price fluctuations do not create alerts.
            stable={k:v for k,v in r.items() if k not in ('checked_at','evidence','value_usd','history','last_seen','raw')}
            fp=digest(stable)
            old=self.db.execute('SELECT fingerprint FROM observations WHERE id=?',(r['id'],)).fetchone()
            if old is None or old[0]!=fp:
                changes.append(r)
                self.db.execute('INSERT OR REPLACE INTO outbox(id,payload) VALUES(?,?)',(r['id'],json.dumps(r)))
            self.db.execute('INSERT OR REPLACE INTO observations VALUES(?,?,?,?)',(r['id'],fp,json.dumps(r),result['checked_at']))
        self.db.execute('INSERT INTO runs(at,payload) VALUES(?,?)',(result['checked_at'],json.dumps(result)))
        self.db.execute('DELETE FROM cache WHERE ts < ?',(time.time()-86400,))
        self.db.commit()
        return changes
    def history(self):
        return [dict(at=a,items=len(json.loads(p)['items']),errors=sum(x['status']=='INDISPONÍVEL' for x in json.loads(p)['items'])) for a,p in self.db.execute('SELECT at,payload FROM runs ORDER BY id DESC LIMIT 120')]

class Client:
    def __init__(self,store,timeout=12,ttl=300):self.store=store;self.timeout=timeout;self.ttl=ttl;self.last=0;self.evidence=[]
    def get(self,url,payload=None):
        if not url.startswith('https://'):raise ValueError('Apenas HTTPS')
        key=digest([url,payload]); t=time.time()
        row=self.store.db.execute('SELECT ts,body FROM cache WHERE key=?',(key,)).fetchone()
        if row and t-row[0]<self.ttl:
            body=row[1]; observed=datetime.fromtimestamp(row[0],timezone.utc).isoformat()
        else:
            for attempt in range(3):
                time.sleep(max(0,0.35-(time.monotonic()-self.last)))
                headers={'User-Agent':'OMNIA-Treasure-Hunter/1.0','Accept':'application/json'}
                if urllib.parse.urlparse(url).netloc=='api.github.com' and os.getenv('GH_TOKEN'):
                    headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
                if payload is not None:headers['Content-Type']='application/json'
                req=urllib.request.Request(url, data=None if payload is None else json.dumps(payload).encode(),headers=headers)
                self.last=time.monotonic()
                try:
                    with urllib.request.urlopen(req,timeout=self.timeout) as r: body=r.read(8_000_001).decode()
                    if len(body)>8_000_000:raise ValueError('Resposta excede limite')
                    break
                except urllib.error.HTTPError as e:
                    if e.code not in (429,500,502,503,504) or attempt==2:raise RuntimeError(f'HTTP {e.code} em {urllib.parse.urlparse(url).netloc}') from None
                    retry=e.headers.get('Retry-After','')
                    delay=float(retry) if retry.isdigit() else 2**attempt
                    if delay>30:raise RuntimeError('Rate limit: tentar na próxima execução') from None
                    time.sleep(delay)
                except (TimeoutError,urllib.error.URLError):
                    if attempt==2:raise RuntimeError('Timeout/rede indisponível') from None
                    time.sleep(2**attempt)
            observed=now()
            parsed=json.loads(body)
            if isinstance(parsed,dict) and parsed.get('error'):raise ValueError('Erro RPC: '+str(parsed['error'])[:200])
            self.store.db.execute('INSERT OR REPLACE INTO cache VALUES(?,?,?)',(key,time.time(),body));self.store.db.commit()
        data=json.loads(body)
        self.evidence.append(dict(url=url,observed_at=observed,sha256=hashlib.sha256(body.encode()).hexdigest(),cached=bool(row and t-row[0]<self.ttl)))
        return data
    def rpc(self,url,method,params):
        if method not in {'eth_chainId','eth_blockNumber','eth_getBalance','eth_getTransactionCount','eth_call','getBalance','getSignaturesForAddress','getTokenAccountsByOwner'}:raise ValueError('RPC de escrita proibido')
        return self.get(url,dict(jsonrpc='2.0',id=1,method=method,params=params))['result']
