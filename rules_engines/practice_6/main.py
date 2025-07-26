# main.py

from rules_engine import RulesEngine, load_rules_from_yaml

if __name__ == "__main__":
    print("Loading rules from YAML file...")
    rules = load_rules_from_yaml("rules.yaml")
    # for rule in rules:
    #     print(f"Rule Name: {rule['name']}")
    #     print(f"Condition: {rule['condition']}")
    #     print(f"Action: {rule['action']}")
    #     print("-" * 40)

    my_rules_engine = RulesEngine(rules)

    for rule in my_rules_engine.rules:
        print(f"Initialized Rule: {rule.name}")
        print(f"Rule Action: {rule.action}")
        print(f"Rule Condition: {rule.condition}")
        print("-" * 40)

    result = my_rules_engine.run({"age": 30, "income": 70000})
    print("Final Result:", result)