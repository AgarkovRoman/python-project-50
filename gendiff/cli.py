import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser


def main():
    parser = build_parser()
    parser.parse_args()
