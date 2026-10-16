import json
import unittest
from pathlib import Path
from treasure_hunter.merkle import verify_aave_claim
from treasure_hunter.rewards import aave_recovery

class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.d=json.loads(Path(__file__).with_name('aave_fixture.json').read_text());self.a=next(iter(self.d['claims']));self.claim=self.d['claims'][self.a]
    def test_official_vector(self):self.assertTrue(verify_aave_claim(self.a,self.claim,self.d['merkleRoot']))
    def test_tampering(self):
        c={**self.claim,'amountInWei':'1'};self.assertFalse(verify_aave_claim(self.a,c,self.d['merkleRoot']))
    def test_absent_address_negative(self):
        data=self.d
        class C:
            def get(self,url):return data
        p={'id':'test','data_url':'https://official.test/data','expected_root':data['merkleRoot'],'name':'Test','official_url':'https://official.test'}
        self.assertEqual(aave_recovery(C(),'0x'+'11'*20,p)['status'],'NÃO ELEGÍVEL')

class OnchainTests(RecoveryTests):
    def test_onchain_claim_status(self):
        data=self.d
        class C:
            def get(self,url):return data
            def rpc(self,url,method,params):
                if method=='eth_chainId':return '0x1'
                if method=='eth_blockNumber':return '0x123'
                if len(params[0]['data'])==74:return '0x'+'0'*64+data['merkleRoot'][2:]
                return '0x'+'0'*64
        p={'id':'test','data_url':'https://official.test/data','expected_root':data['merkleRoot'],'name':'Test','official_url':'https://official.test','distributor':'0x'+'22'*20,'distribution_id':2,'decimals':6,'symbol':'USDT'}
        self.assertEqual(aave_recovery(C(),self.a,p)['status'],'CONFIRMADO')
