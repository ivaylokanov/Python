import re
text = input()
regex = re.compile(r"[+]359([ -])2\1[\d+]{3}\1[\d+]{4}\b")

for match in regex.finditer(text):
    print(match.group(), end=' ')
