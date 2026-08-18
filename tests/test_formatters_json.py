import json

from gendiff.diff import build_diff
from gendiff.formatters.json import format_json


def test_format_json_round_trip():
    data1 = {'a': 1, 'b': {'c': 2}, 'removed': True}
    data2 = {'a': 2, 'b': {'c': 2}, 'added': False}

    diff = build_diff(data1, data2)

    assert json.loads(format_json(diff)) == diff
