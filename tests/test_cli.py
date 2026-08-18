from pathlib import Path

from gendiff.cli import build_parser, main

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def test_build_parser_defaults():
    parser = build_parser()
    args = parser.parse_args(['file1.json', 'file2.json'])

    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'stylish'


def test_build_parser_format_option():
    parser = build_parser()
    args = parser.parse_args(
        ['file1.json', 'file2.json', '--format', 'json'],
    )

    assert args.format == 'json'


def test_main_prints_diff(monkeypatch, capsys):
    file_path1 = str(TEST_DATA_DIR / 'file1.json')
    file_path2 = str(TEST_DATA_DIR / 'file2.json')
    monkeypatch.setattr('sys.argv', ['gendiff', file_path1, file_path2])
    expected = (TEST_DATA_DIR / 'flat_stylish_expected.txt').read_text()

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()
