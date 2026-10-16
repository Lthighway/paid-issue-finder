import tempfile
import unittest
from pathlib import Path
from treasure_hunter.core import Store,record
from treasure_hunter.chains import stellar_liquidity
from treasure_hunter.bounties import refresh_known

class TrackingTests(unittest.TestCase):
    def test_no_bids_does_not_confirm_reward(self):
        class C:
            def get(self,url):return {'bids':[]}
        r=record('x','recompensa','stellar','token');r['asset']='USD:GISSUER';stellar_liquidity(C(),[r]);self.assertEqual(r['liquidity'],'SEM OFERTAS DE COMPRA XLM');self.assertEqual(r['status'],'POTENCIAL')
    def test_market_failure_unknown(self):
        class C:
            def get(self,url):raise RuntimeError('offline')
        r=record('x','recompensa','stellar','token');r['asset']='USD:GISSUER';stellar_liquidity(C(),[r]);self.assertEqual(r['liquidity'],'INDISPONÍVEL');self.assertIsNone(r['value_usd'])
    def test_known_bounty_closure(self):
        class C:
            def get(self,url):return {'state':'closed'}
        with tempfile.TemporaryDirectory() as p:
            s=Store(Path(p)/'db');r=record('github:owner/repo:1','bounty','externa','Task',source='https://github.com/owner/repo/issues/1');s.save({'checked_at':'2026-01-01','items':[r]});rows=list(refresh_known(C(),s,[]));s.db.close()
        self.assertEqual(rows[0]['status'],'NÃO ELEGÍVEL');self.assertIsNone(rows[0]['received'])
