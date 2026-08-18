from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def read_test_data(filename):
    return (TEST_DATA_DIR / filename).read_text()


@pytest.mark.parametrize('extension', ['json', 'yml'])
def test_generate_diff_flat(extension):
    file_path1 = TEST_DATA_DIR / f'file1.{extension}'
    file_path2 = TEST_DATA_DIR / f'file2.{extension}'
    expected = read_test_data('flat_stylish_expected.txt')

    assert generate_diff(file_path1, file_path2) == expected
