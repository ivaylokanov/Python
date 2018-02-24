import re
line = input()
finded_matches = ''
regex = r"(<\w+>)"
matches = re.finditer(regex, line)

for matchNum, match in enumerate(matches):
    finded_matches = match.group()
    diamond_calculation = 0
    for ch in finded_matches:
        if ch.isdigit():
            diamond_calculation += int(ch)
    print(f'Found {diamond_calculation} carat diamond')
if finded_matches == '':
    print('Better luck next time')

