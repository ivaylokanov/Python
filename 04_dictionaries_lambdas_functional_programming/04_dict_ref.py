input_line = input()
dict_ref = {}
while input_line != "end":
    splited_line = input_line.split(" = ")
    if splited_line[1].isnumeric():
        dict_ref[splited_line[0]] = splited_line[1]
    else:
        if splited_line[1] in dict_ref.keys():
            dict_ref[splited_line[0]] = dict_ref[splited_line[1]]
        else:
            break
    input_line = input()
[print(f"{key} === {value}") for key, value in dict_ref.items()]
