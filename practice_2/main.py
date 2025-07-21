from rules_engine import RulesEngine, load_rules_from_yaml
from custom_rules import check_vip

custom_funcs = {
    "check_vip": check_vip
}

rules = load_rules_from_yaml("rules.yaml")
engine = RulesEngine(rules, custom_funcs=custom_funcs)
result = engine.run({"age": 25, "income": 150000, "vip_code": "X123"})
