import json


def parse_file(file_path):
    with open(file_path) as f:
        return json.load(f)
