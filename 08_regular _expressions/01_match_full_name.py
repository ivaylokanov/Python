import re
text = input()
regex = re.compile(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b")

for match in regex.finditer(text):
    print(match.group(), end=' ')
