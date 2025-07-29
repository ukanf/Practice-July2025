# test_rules_engine.py

import unittest
from rules_engine import RulesEngine, load_rules_from_yaml

class TestAdvancedRulesEngine(unittest.TestCase):

    def setUp(self):
        rules = load_rules_from_yaml("rules.yaml")
        self.engine = RulesEngine(rules)

    def test_fail_paid_status(self):
        input_data = {'invoice_number': "''", 'issue_date': '2024-07-24', 'due_date': '2024-08-23', 'vendor_name': 'Global Shipping LLC', 'vendor_id': 'VS-009', 'total_amount': 1750.5, 'currency': 'USD', 'status': 'overdue', 'line_items': 2.0}
        result = self.engine.run(input_data.copy())
        self.assertNotIn('paid_status', result)

    def test_valid_paid_status(self):
        input_data = {'invoice_number': "''", 'issue_date': '2024-07-24', 'due_date': '2024-08-23', 'vendor_name': 'Global Shipping LLC', 'vendor_id': 'VS-009', 'total_amount': 1750.5, 'currency': 'USD', 'status': 'paid', 'line_items': 2.0}
        result = self.engine.run(input_data.copy())
        self.assertEqual(result['paid_status'], 'Valid')

if __name__ == "__main__":
    unittest.main()
