# main.py

from rules_engine import RulesEngine, load_rules_from_yaml

if __name__ == "__main__":
    print("Loading rules from YAML file...")
    rules = load_rules_from_yaml("rules.yaml")

    my_rules_engine = RulesEngine(rules)

    # for rule in my_rules_engine.rules:
    #     print(f"Initialized Rule: {rule.name}")
    #     print(f"Rule Action: {rule.action}")
    #     print(f"Rule Condition: {rule.condition}")
    #     print("-" * 40)

    input_data = {"age": 66, "income": 70000}
    result = my_rules_engine.run(input_data.copy())
    print("Final Result:", result)