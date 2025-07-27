# rules_engine.py

import yaml
from actions import ACTION_MAP

class RulesEngine:
    def __init__(self, rules, credit_watch_list=None):
        self.rules = []
        self.credit_watch_list = credit_watch_list or []
        for rule in rules:
            if rule['action'] not in ACTION_MAP:
                raise ValueError(f"Action '{rule['action']}' not found in ACTION_MAP")
            action_func = ACTION_MAP[rule['action']]
            rule_obj = Rule(rule['name'], rule['condition'], action_func)
            self.rules.append(rule_obj)

    def run(self, context):
        # init context with credit_watch_list
        context["credit_watch_list"] = self.credit_watch_list
        context["decision"] = "Pending"

        # always refer if customer is in credit watch list
        if context.get('customer_name') in self.credit_watch_list:
            # temporarily just 4 for testing
            context = self.rules[4].evaluate(context)
            return context
        
        for rule in self.rules:
            context = rule.evaluate(context)
        return context

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
            context = self.action(context)

        return context

# YAML Parsing
def load_rules_from_yaml(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        # data is an array of rule dictionaries
        return data["rules"]
