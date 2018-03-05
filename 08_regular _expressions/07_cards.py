import re

text = input()
regex = re.compile(r"(?:[23456789AKQJ]{1}|10)[S|H|D|C]{1}")
[print(match.group(), end=' ') for match in regex.finditer(text)]