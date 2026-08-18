import json
from pathlib import Path

import yaml

PARSERS = {
    '.json': json.load,
    '.yml': yaml.safe_load,
    '.yaml': yaml.safe_load,
}


def parse_file(file_path):
    extension = Path(file_path).suffix
    parse = PARSERS[extension]
    with open(file_path) as f:
        return parse(f)
