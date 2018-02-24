manipulated_string = input()
while True:
    line = input()
    if line == "end":
        break
    command_element = line.split(' ')
    command = command_element[0]
    first_condition = int(command_element[1])
    if command == 'Right':
        for i in range(first_condition):
            manipulated_string = manipulated_string[-1] + manipulated_string[0:len(manipulated_string)-1]
    elif command == 'Left':
        for i in range(first_condition):
            manipulated_string = manipulated_string[1:len(manipulated_string)] + manipulated_string[0]
    elif command == 'Delete':
        second_condition = int(command_element[2])
        manipulated_string = manipulated_string.replace(manipulated_string[first_condition:second_condition+1], '')
    elif command == 'Insert':
        second_condition = command_element[2]
        if first_condition == 0:
            manipulated_string = second_condition + manipulated_string
        else:
            manipulated_string = manipulated_string[0:first_condition] + second_condition + manipulated_string[(first_condition+1):len(manipulated_string)]
    else:
        print(f'Unsolved command: {command}')

print(manipulated_string)