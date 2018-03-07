import re

detailed_fish = input()
regex = re.compile("(?P<tail>[>]*<)(?P<body>[(]+)(?P<status>[-'x])>")


def tail_description(size):
    if size > 5:
        print(f"  Tail type: Long ({size*2} cm)")
    elif 1 < size <= 5:
        print(f"  Tail type: Medium ({size*2} cm)")
    elif size == 1:
        print(f"  Tail type: Short ({size*2} cm)")
    else:
        print(f"  Tail type: None")


def body_description(size):
    if size > 10:
        print(f"  Body type: Long ({size*2} cm)")
    elif 5 < size <= 10:
        print(f"  Body type: Medium ({size*2} cm)")
    else:
        print(f"  Body type: Short ({size*2} cm)")


def status(shape):
    if shape == "'":
        print(f"  Status: Awake")
    elif shape == "-":
        print(f"  Status: Asleep")
    else:
        print(f"  Status: Dead")


matches = regex.finditer(detailed_fish)
if not regex.findall(detailed_fish):
    print("No fish found.")
    exit()
for index, match in enumerate(matches):
    tail_size = len(match.group("tail")) - 1
    body_size = len(match.group("body"))
    shape_status = match.group("status")
    print(f'Fish {index+1}: {match.group()}')
    tail_description(tail_size)
    body_description(body_size)
    status(shape_status)
