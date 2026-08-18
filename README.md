# Gendiff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/AgarkovRoman/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AgarkovRoman/python-project-50/actions)
[![Python CI](https://github.com/AgarkovRoman/python-project-50/actions/workflows/check.yml/badge.svg)](https://github.com/AgarkovRoman/python-project-50/actions)

«Gendiff» compares two configuration files and shows the difference
between them.

## Requirements

* Python >= 3.12
* [uv](https://docs.astral.sh/uv/)

## Installation

```bash
git clone git@github.com:AgarkovRoman/python-project-50.git
cd python-project-50
make install
make build
make package-install
```

## Usage

```bash
gendiff first_file.json second_file.json
```

As a library:

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```

## Demo

[![asciicast](https://asciinema.org/a/v7Spes9XFErGwFxy.svg)](https://asciinema.org/a/v7Spes9XFErGwFxy)
