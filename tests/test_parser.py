from pathlib import Path

import pytest

from gendiff.parser import parse_file

TEST_DATA_DIR = Path(__file__).parent / 'test_data'

EXPECTED_DATA = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False,
}


@pytest.mark.parametrize('extension', ['json', 'yml'])
def test_parse_file(extension):
    file_path = TEST_DATA_DIR / f'file1.{extension}'

    assert parse_file(file_path) == EXPECTED_DATA
