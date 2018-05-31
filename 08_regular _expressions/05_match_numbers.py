import re

text = input()
regex = re.compile(r"([\d]+[A-Z][a-z]+([A-Z]|\d)(\2)+)")
[print(match.group(), end=' ') for match in regex.finditer(text)]
