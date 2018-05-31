import operator
from collections import OrderedDict

base = {}
counter = 0
while True:
    line = input()
    if line == "end":
        break
    course = line.split(" - ")[0]
    lectures_elements = line.split(" - ")[1].split(", ")

    if course not in base:
        base[course] = {}

    for item in lectures_elements:
        lecture = item.split(":")[0]
        participants = int(item.split(":")[1])
        if lecture not in base[course]:
            base[course][lecture] = participants
        else:
            base[course][lecture] = base[course][lecture] + participants

    base = OrderedDict(sorted(base[course].items(), key=lambda x: sum(x)))

for key, internal_base in base:
    if counter == 0:
        print(f"Most popular: {key} ({sum(internal_base.values())} participants)")
    counter += 1
    if counter == len(base):
        print(f"Least popular: {key} ({sum(internal_base.values())} participants)")

for key, internal_base in base:
    print(f"{key} ({sum(internal_base.values())} participants):")

    internal_base1 = OrderedDict(sorted(internal_base.items(), key=lambda x: x[1], reverse=True))

    [print(f"--{k} -> {v}") for k, v in internal_base1.items()]
