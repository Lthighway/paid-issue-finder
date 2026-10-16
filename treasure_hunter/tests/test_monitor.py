import json
import tempfile
import unittest
from datetime import datetime,timezone
from pathlib import Path
from unittest.mock import patch
from treasure_hunter.core import Store,Client,record,units
from treasure_hunter.validation import validate
from treasure_hunter.chains import predicate,token_status,evm,stellar
from treasure_hunter.rewards import merkl
from treasure_hunter.notify import deliver
from treasure_hunter.render import render

A='0xB70401fC0F2922e10728bD70856C8E68e1CcC27c'
class Fake:
    def __init__(self,data=None,error=False):self.data=data;self.error=error
    def get(self,*a,**k):
        if self.error:raise RuntimeError('offline')
        return self.data
    def rpc(self,*a,**k):raise RuntimeError('offline')

class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.path=Path(self.temp.name);self.store=Store(self.path/'state.sqlite')
    def tearDown(self):self.store.db.close();self.temp.cleanup()
    def result(self,r,at='2026-01-01T00:00:00+00:00'):return {'checked_at':at,'items':[r],'wallets':[]}
    def test_wallets(self):
        for w in json.loads(Path('treasure_hunter/config/wallets.json').read_text()):self.assertTrue(validate(w['network'],w['address'])[0])
    def test_bad_checksums(self):
        for net,a in [('bitcoin','bc1qvtuhezyjkvrwgxcsvhrnc2k7r8vzr3mewus6mq'),('stellar','GBOVZNBRN3GZJTVFEDFPZMASDGQJFPL4VNFCQNVSFOUX25MG2B2FJIWA'),('evm','0x123'),('solana','0OOIl')]:self.assertFalse(validate(net,a)[0])
    def test_decimal_precision(self):self.assertEqual(units('123456789123456789',18),'0.123456789123456789')
    def test_persistence_across_processes(self):
        r=record('x','recompensa','stellar','reward','CONFIRMADO');r['amount']='3'
        self.assertEqual(len(self.store.save(self.result(r))),1)
        other=Store(self.path/'state.sqlite')
        self.assertEqual(other.save(self.result(r,'2026-01-02T00:00:00Z')),[]);other.db.close()
    def test_amount_change(self):
        r=record('x','recompensa','stellar','reward');self.store.save(self.result(r));r['amount']='1';self.assertEqual(len(self.store.save(self.result(r))),1)
    def test_no_alert_on_evidence_change(self):
        r=record('x','recompensa','stellar','reward');self.store.save(self.result(r));r['evidence']=[{'sha256':'new'}];r['checked_at']='later';self.assertEqual(self.store.save(self.result(r)),[])
    def test_notifications_dedupe(self):
        self.store.save(self.result(record('x','recompensa','stellar','reward')));sent=[]
        deliver(self.store,lambda c,m:sent.append(m),['telegram']);deliver(self.store,lambda c,m:sent.append(m),['telegram']);self.assertEqual(len(sent),1)
    def test_delivery_failure_retry(self):
        self.store.save(self.result(record('x','recompensa','stellar','reward')))
        def bad(*a):raise RuntimeError('secret-token')
        with patch('builtins.print') as log:
            self.assertEqual(deliver(self.store,bad,['telegram'])['errors'],1);self.assertNotIn('secret-token',str(log.call_args))
        self.assertEqual(deliver(self.store,lambda *a:None,['telegram'])['sent'],1)
    def test_partial_channels(self):
        self.store.save(self.result(record('x','recompensa','stellar','reward')))
        def sender(c,m):
            if c=='email':raise RuntimeError()
        deliver(self.store,sender,['telegram','email']);self.assertEqual(deliver(self.store,lambda *a:None,['telegram','email'])['sent'],1)
    def test_rpc_write_forbidden(self):
        with self.assertRaises(ValueError):Client(self.store).rpc('https://example.com','eth_sendRawTransaction',[])
    def test_rpc_error_not_zero(self):
        rows=list(evm(Fake(error=True),A,'ethereum'));self.assertTrue(all(r['status']=='INDISPONÍVEL' for r in rows));self.assertTrue(all(r['amount'] is None for r in rows))
    def test_merkl_schema_failure(self):self.assertEqual(list(merkl(Fake({}),A,'base'))[0]['status'],'INDISPONÍVEL')
    def test_merkl_no_false_confirmation(self):
        data=[{'chain':{'id':1},'rewards':[{'token':{'address':A,'decimals':18,'symbol':'X'},'amount':'2000000000000000000','claimed':'1000000000000000000','proofs':['0x123']}]}]
        r=list(merkl(Fake(data),A,'ethereum'))[0];self.assertEqual(r['amount'],'1');self.assertEqual(r['status'],'POTENCIAL')
    def test_pending_not_counted(self):
        data=[{'chain':{'id':1},'rewards':[{'token':{'address':A,'decimals':18},'amount':'0','claimed':'0','pending':'999'}]}]
        self.assertEqual(list(merkl(Fake(data),A,'ethereum'))[0]['status'],'NÃO ELEGÍVEL')
    def test_predicate(self):
        at=datetime(2026,1,1,tzinfo=timezone.utc)
        self.assertTrue(predicate({'unconditional':True},at));self.assertFalse(predicate({'abs_before':'2025-01-01T00:00:00Z'},at));self.assertIsNone(predicate({'rel_before':'60'},at));self.assertTrue(predicate({'not':{'abs_before':'2025-01-01T00:00:00Z'}},at))
    def test_spam(self):self.assertEqual(token_status({'symbol':'https://claim.scam'}),'SUSPEITO')
    def test_unknown_token_not_cash(self):self.assertEqual(token_status({'symbol':'USDT'}),'POTENCIAL')
    def test_dashboard_escapes_data(self):
        r=record('x','bounty','external','</script><script>alert(1)</script>');render(self.result(r),self.path)
        self.assertNotIn('</script><script>alert(1)',(self.path/'index.html').read_text())
        self.assertEqual(json.loads((self.path/'results.json').read_text())['items'][0]['title'],r['title'])
    def test_no_channels_no_delivery(self):
        self.store.save(self.result(record('x','recompensa','stellar','reward')));self.assertFalse(deliver(self.store,lambda *a:self.fail(),[])['configured'])

if __name__=='__main__':unittest.main()
