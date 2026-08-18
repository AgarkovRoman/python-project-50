REPLACER = ' '
SPACES_COUNT = 4


def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            indent = REPLACER * (SPACES_COUNT * (depth + 1))
            lines.append(f'{indent}{key}: {format_value(val, depth + 1)}')
        brace_indent = REPLACER * (SPACES_COUNT * depth)
        return '\n'.join(['{', *lines, f'{brace_indent}}}'])
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff, depth=0):
    lines = ['{']
    current_indent = REPLACER * (SPACES_COUNT * depth + 2)
    for node in diff:
        key = node['key']
        node_type = node['type']
        if node_type == 'nested':
            value = format_stylish(node['children'], depth + 1)
            lines.append(f'{current_indent}  {key}: {value}')
        elif node_type == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{current_indent}+ {key}: {value}')
        elif node_type == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{current_indent}- {key}: {value}')
        elif node_type == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{current_indent}  {key}: {value}')
        else:
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(f'{current_indent}- {key}: {old_value}')
            lines.append(f'{current_indent}+ {key}: {new_value}')
    brace_indent = REPLACER * (SPACES_COUNT * depth)
    lines.append(f'{brace_indent}}}')
    return '\n'.join(lines)
