# main.py

from rules_engine import RulesEngine, load_rules_from_yaml

if __name__ == "__main__":
    rules = load_rules_from_yaml("rules.yaml")
    engine = RulesEngine(rules)

    # Example1
    input_data = {"age": 30, "income": 70000}
    result = engine.run(input_data)
    print("Final Result:", result)

    # Example2
    input_data = {"age": 17, "income": 120000}
    result = engine.run(input_data)
    print("Final Result:", result)

    # Example3
    input_data = {"age": 16, "income": 50000}
    result = engine.run(input_data)
    print("Final Result:", result)