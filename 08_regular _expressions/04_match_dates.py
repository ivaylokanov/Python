import re

text = input()
regex = re.compile(r"(?P<day>\d{2})([-./])(?P<month>\w{3})\2(?P<year>\d{4})")
matches = regex.finditer(text)

for match in matches:
    groups = match.groupdict(match)
    day = groups['day']
    month = groups['month']
    year = groups['year']
    print(f'Day: {day}, Month: {month}, Year: {year}')
