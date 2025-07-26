# rules_engine.py

import yaml

class RulesEngine:
    def __init__(self, rules):
        self.rules = []
        for rule in rules:
            action_func = ACTION_MAP[rule['action']]
            rule_obj = Rule(rule['name'], rule['condition'], action_func)
            self.rules.append(rule_obj)

    def run(self, context):
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


# Define your action functions
def action_flag_rich_minor(context):
    context['flag'] = 'suspicious'
    context['note'] = 'Minor with high income'
    return context

def action_reject_minor(context):
    context['eligible'] = False
    context['message'] = 'Rejected due to age'
    return context

def action_approve_adult_with_income(context):
    context['eligible'] = True
    context['message'] = 'Approved based on age and income'
    return context

# Map action names to functions
ACTION_MAP = {
    'action_flag_rich_minor': action_flag_rich_minor,
    'action_reject_minor': action_reject_minor,
    'action_approve_adult_with_income': action_approve_adult_with_income,
}
