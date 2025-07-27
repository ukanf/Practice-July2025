# test_rules_engine.py

import unittest
from rules_engine import RulesEngine, load_rules_from_yaml

class TestAdvancedRulesEngine(unittest.TestCase):

    def setUp(self):
        rules = load_rules_from_yaml("rules.yaml")
        credit_watch_list = ["joseph"]
        self.engine = RulesEngine(rules, credit_watch_list)

    def test_approve_newcustomer_lowutilization(self):
        input_data = {"utilization": 0.4, "customer_age": 100, "customer_name": "kevin"}
        result = self.engine.run(input_data.copy())
        self.assertEqual(result['decision'], 'Approve')

    def test_refer_newcustomer_highutilization(self):
        input_data = {"utilization": 0.9, "customer_age": 100, "customer_name": "kevin"}
        result = self.engine.run(input_data.copy())
        self.assertEqual(result['decision'], 'Refer')

    def test_decline_highutilization(self):
        input_data = {"utilization": 1.1, "customer_age": 200, "customer_name": "kevin"}
        result = self.engine.run(input_data.copy())
        self.assertEqual(result['decision'], 'Decline')
    
    def test_always_refer_customer_in_watchlist(self):
        input_data = {"utilization": 0.5, "customer_age": 50, "customer_name": "joseph"}
        result = self.engine.run(input_data.copy())
        self.assertEqual(result['decision'], 'Refer')

if __name__ == "__main__":
    unittest.main()
