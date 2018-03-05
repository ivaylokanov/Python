import re

text = input()
regex = re.compile(r'\b[ox0-9A-F]+\b')
[print(match.group(), end=' ') for match in regex.finditer(text)]
