from gendiff.formatters.stylish import format_stylish

FORMATTERS = {
    'stylish': format_stylish,
}


def format_diff(diff, format_name='stylish'):
    formatter = FORMATTERS[format_name]
    return formatter(diff)
