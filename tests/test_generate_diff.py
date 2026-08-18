from pathlib import Path

from gendiff import generate_diff

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def read_test_data(filename):
    return (TEST_DATA_DIR / filename).read_text()


def test_generate_diff_flat_json():
    file_path1 = TEST_DATA_DIR / 'file1.json'
    file_path2 = TEST_DATA_DIR / 'file2.json'
    expected = read_test_data('flat_stylish_expected.txt')

    assert generate_diff(file_path1, file_path2) == expected
