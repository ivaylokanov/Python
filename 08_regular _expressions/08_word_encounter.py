import re
commander = input()
result = []
while True:
    text = input()
    if text == "end":
        break
    regex_checker = re.compile(r"^[A-Z].*[.?!]$")
    if regex_checker.findall(text):
        regex = re.compile("\w*(?:\w*["+f"{commander[0]}"+"]\w*){"+f"{commander[1]}"+"}")
        matches = regex.finditer(text)
        for match in matches:
            result.append(match.group())
print(*result, sep=', ')
