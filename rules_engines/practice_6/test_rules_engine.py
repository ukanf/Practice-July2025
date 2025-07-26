# test_rules_engine.py

import unittest
from rules_engine import RulesEngine, load_rules_from_yaml

class TestAdvancedRulesEngine(unittest.TestCase):

    def setUp(self):
        rules = load_rules_from_yaml("rules.yaml")
        self.engine = RulesEngine(rules)

    def test_approved_adult(self):
        input_data = {"age": 25, "income": 60000}
        result = self.engine.run(input_data.copy())
        self.assertTrue(result.get("eligible"))
        self.assertEqual(result.get("message"), "Approved based on age and income")
        self.assertEqual(result.get("flag"), None)

    def test_rejected_older_adult(self):
        input_data = {"age": 75, "income": 600000}
        result = self.engine.run(input_data.copy())
        self.assertFalse(result.get("eligible"))
        self.assertEqual(result.get("message"), "Rejected due to age")
        self.assertEqual(result.get("flag"), None)

    def test_rejected_minor(self):
        input_data = {"age": 15, "income": 1000}
        result = self.engine.run(input_data.copy())
        self.assertFalse(result.get("eligible"))
        self.assertEqual(result.get("message"), "Rejected due to age")
        self.assertEqual(result.get("flag"), None)

    def test_suspicious_minor(self):
        input_data = {"age": 17, "income": 120000}
        result = self.engine.run(input_data.copy())
        self.assertEqual(result.get("flag"), "suspicious")
        self.assertEqual(result.get("note"), "Minor with high income")

if __name__ == "__main__":
    unittest.main()
