import os
import unittest
from unittest.mock import patch
from treasure_hunter.zero_cost import assess, submitted_report
from treasure_hunter.superteam import parse, collect


class ZeroCostTests(unittest.TestCase):
    def test_confirmed_balance_is_not_income(self):
        a=assess({'category':'saldo','status':'CONFIRMADO','amount':'40'})
        self.assertFalse(a['automatic_payout_enabled'])
        self.assertIsNone(a['income_received'])

    def test_confirmed_claim_does_not_mean_zero_fee(self):
        self.assertFalse(assess({'category':'recompensa','status':'CONFIRMADO'})['zero_cost_verified'])

    def test_existing_report_is_not_new_work(self):
        self.assertTrue(submitted_report({'body':'Severity: Medium. We identified a vulnerability.'}))
        self.assertFalse(submitted_report({'body':'Fix this issue for a $450 bounty.'}))

    def test_missing_key_has_no_network_call(self):
        with patch.dict(os.environ,{},clear=True), patch('urllib.request.urlopen') as request:
            self.assertEqual(list(collect())[0]['status'],'INDISPONÍVEL')
            request.assert_not_called()

    def test_human_only_skipped(self):
        self.assertEqual(list(parse([{'agentAccess':'HUMAN_ONLY'}])),[])

    def test_schema_mismatch(self):
        with self.assertRaises(ValueError):list(parse({'unexpected':[]}))

    def test_reward_pool_not_income(self):
        r=list(parse([{'agentAccess':'AGENT_ALLOWED','id':'1','title':'Test','rewardAmount':1000,'token':'USDC'}]))[0]
        self.assertEqual(r['status'],'POTENCIAL')
        self.assertEqual(r['reward_pool'],1000)
        self.assertIsNone(r['amount'])
        self.assertIsNone(r['received'])
