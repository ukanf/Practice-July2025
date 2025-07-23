# rules_engine.py

import yaml

# Rule Logic Design
class Rule:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def evaluate(self, context):
        # Controlled eval environment for safety
        safe_globals = {}
        safe_locals = context.copy()

        if eval(self.condition, safe_globals, safe_locals):
            exec(self.action, safe_globals, safe_locals)
            context.update(safe_locals)

        return context

class RulesEngine:
    def __init__(self, rules):
        # each item in rules is a dictionary with keys 'name', 'condition', and 'action'
        # if not isinstance(rules, list):
        #     raise ValueError("Rules must be a list of dictionaries")
        # if not all(isinstance(rule, dict) for rule in rules):
        #     raise ValueError("Each rule must be a dictionary")
        # if not all('name' in rule and 'condition' in rule and 'action' in rule for rule in rules):
        #     raise ValueError("Each rule must contain 'name', 'condition', and 'action' keys")
        self.rules = [Rule(rule['name'], rule['condition'], rule['action']) for rule in rules]

    def run(self, context):
        for rule in self.rules:
            context = rule.evaluate(context)
        return context

# YAML Parsing
def load_rules_from_yaml(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        # data is an array of rule dictionaries
        return data["rules"]
