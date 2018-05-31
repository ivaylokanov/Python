first_line = input().split(" ")
second_line = input().split(" ")

state_list = list(map(int, first_line))
command_list = list(map(int, second_line))

for item in command_list:
    manipulated_list = []
    if item % 2 == 0:
        for element in state_list:
            if element % 2 == 0:
                manipulated_list.append(element * abs(item))
            else:
                manipulated_list.append(element)
    else:
        if item % 2 != 0:
            for element in state_list:
                if element % 2 != 0:
                    manipulated_list.append(element // abs(item))
                else:
                    manipulated_list.append(element)
    state_list = manipulated_list
    manipulated_list = []
    if item >= 0:
        for element in state_list:
            if element > 0:
                manipulated_list.append(element + item)
            else:
                manipulated_list.append(element)
    else:
        if item < 0:
            for element in state_list:
                if element < 0:
                    manipulated_list.append(element + item)
                else:
                    manipulated_list.append(element)
    state_list = manipulated_list
print(manipulated_list)
