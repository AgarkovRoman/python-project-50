import argparse
import json


def parse_file(file_path):
    with open(file_path) as f:
        return json.load(f)


def build_parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output',
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    parse_file(args.first_file)
    parse_file(args.second_file)
