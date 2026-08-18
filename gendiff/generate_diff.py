from gendiff.parser import parse_file
from gendiff.stylish import build_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    return build_stylish(data1, data2)
