#Python script to read a JSON file and pretty-print its contents.

import json

def pretty_print_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=2))

# Example usage:
json_file_path = "example.json"
pretty_print_json(json_file_path)
