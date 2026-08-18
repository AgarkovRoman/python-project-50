def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def build_stylish(data1, data2):
    keys = sorted(set(data1) | set(data2))
    lines = []
    for key in keys:
        if key not in data2:
            lines.append(f'  - {key}: {format_value(data1[key])}')
        elif key not in data1:
            lines.append(f'  + {key}: {format_value(data2[key])}')
        elif data1[key] == data2[key]:
            lines.append(f'    {key}: {format_value(data1[key])}')
        else:
            lines.append(f'  - {key}: {format_value(data1[key])}')
            lines.append(f'  + {key}: {format_value(data2[key])}')
    return '\n'.join(['{', *lines, '}'])
