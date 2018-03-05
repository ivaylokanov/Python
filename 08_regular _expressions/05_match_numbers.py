import re

text = input()
regex = re.compile(r"(^|(?<=\s))-?\d+\.?\d*\b")
[print(match.group(), end=' ') for match in regex.finditer(text)]
