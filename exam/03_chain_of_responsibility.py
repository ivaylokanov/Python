import re

number_of_lines = int(input())
robots_cain = []
robots_line = []
flag = 0
flag_manager = 0
manager = ''
regex = re.compile(r"([\d]+[A-Z][a-z]+([A-Z]|\d)(\2)+)")
for i in range(number_of_lines):
    line = input()
    matches = regex.finditer(line)
    for match in matches:
        robots_line.append(match.group(1))
        if line[-2:len(line)] == "!!":
            flag_manager = 1
            manager = match.group(1)
    if len(robots_line)>2:
        first_robot = robots_line[0]
        second_robot = robots_line[-1]
        robots_line = []
        robots_line.append(first_robot)
        robots_line.append(second_robot)
    if len(robots_cain) == 0:
        robots_cain = robots_cain + robots_line
    else:
        if robots_cain[-1] == robots_line[0]:
            robots_cain = robots_cain + robots_line[1:len(robots_line)]
        else:
            print("Broke the chain!")
            flag = 1
            break
    robots_line = []
if flag !=1:
    if flag_manager ==0:
        print("Did not find the manager!")
    else:
        print(f"Found the manager!: {manager}")
print("Chain: ", end='')
print("->".join(str(item) for item in robots_cain))

