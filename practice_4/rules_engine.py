


class Rule:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action
# condition takes single input/state and returns boolean
# action only be called if condition returns true - called with the same state of the condition and returns whatever makes sense for that action

# interprets a set of rules applying them to some state/context
class RulesEngine:
    def __init__(self, rules):
        self.rules = rules
        
    def run(self, state):
        for rule in self.rules:
            if rule.condition(state):
                return rule.action(state)
        return None