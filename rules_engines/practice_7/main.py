# main.py

from rules_engine import RulesEngine, load_rules_from_yaml

if __name__ == "__main__":
    print("Loading rules from YAML file...")
    rules = load_rules_from_yaml("rules.yaml")
    credit_watch_list = ["joseph", "carla", "maria"]

    my_rules_engine = RulesEngine(rules, credit_watch_list)

    # for rule in my_rules_engine.rules:
    #     print(f"Initialized Rule: {rule.name}")
    #     print(f"Rule Action: {rule.action}")
    #     print(f"Rule Condition: {rule.condition}")
    #     print("-" * 40)

    input_data = {"utilization": 0.4, "customer_age": 10, "customer_name": "kevin"}
    result = my_rules_engine.run(input_data.copy())
    print("Final Result:", result)