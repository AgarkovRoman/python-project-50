import argparse

from gendiff.generate_diff import generate_diff


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
    print(generate_diff(args.first_file, args.second_file, args.format))
