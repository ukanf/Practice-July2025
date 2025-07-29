# main.py
import csv
from rules_engine import RulesEngine, load_rules_from_yaml

def read_invoices_csv(file_path):
    input_data_list = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert numeric fields if needed
            for key, value in row.items():
                try:
                    row[key] = float(value)
                except ValueError:
                    pass
            input_data_list.append(row)
    return input_data_list

if __name__ == "__main__":
    # print("Loading rules from YAML file...")
    rules = load_rules_from_yaml("rules.yaml")
    # credit_watch_list = ["joseph", "carla", "maria"]
    # blacklisted_vendors = ["vendor1", "vendor2", "vendor3"]
    # load cvs and use as input_data

    my_rules_engine = RulesEngine(rules)

    invoice_data_list = read_invoices_csv("invoices.csv")

    for input_data in invoice_data_list:
        result = my_rules_engine.run(input_data.copy())
        print("Input:", input_data)
        print("-" * 40)
