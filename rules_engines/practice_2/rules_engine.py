# rules_engine.py (updated)

import yaml
import logging

class Rule:
    def __init__(self, name, type="condition", condition=None, action=None, message=None, function=None):
        self.name = name
        self.type = type
        self.condition = condition
        self.action = action
        self.message = message
        self.function = function

    def evaluate(self, context, custom_funcs=None):
        locals_copy = context.copy()
        safe_globals = {}

        def evaluate_expr(expr):
            return eval(expr, safe_globals, locals_copy)

        def execute_code(code):
            exec(code, safe_globals, locals_copy)

        # Dispatch by rule type
        if self.type == "condition":
            if self.condition and evaluate_expr(self.condition):
                if self.action:
                    execute_code(self.action)

        elif self.type == "assert":
            if not evaluate_expr(self.condition):
                raise ValueError(self.message or f"Assertion failed: {self.name}")

        elif self.type == "transform":
            execute_code(self.action)

        elif self.type == "route":
            if evaluate_expr(self.condition):
                execute_code(self.action)

        elif self.type == "score":
            execute_code(self.action)

        elif self.type == "log":
            msg = self.message.format(**locals_copy)
            logging.info(f"[RULE LOG] {self.name}: {msg}")

        elif self.type == "custom":
            if custom_funcs and self.function in custom_funcs:
                custom_funcs[self.function](locals_copy)

        context.update(locals_copy)
        return context

class RulesEngine:
    def __init__(self, rules, custom_funcs=None):
        self.rules = [Rule(**rule) for rule in rules]
        self.custom_funcs = custom_funcs or {}

    def run(self, context):
        for rule in self.rules:
            context = rule.evaluate(context, custom_funcs=self.custom_funcs)
        return context

def load_rules_from_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)["rules"]
