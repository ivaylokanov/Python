import collections

input_line = input()
dict_ref = {}
while input_line != "Over":
    splited_line = input_line.split(" : ")
    if splited_line[1].isnumeric():
        dict_ref[splited_line[0]] = splited_line[1]
    else:
        dict_ref[splited_line[1]] = splited_line[0]
    input_line = input()
sorted_dict_ref = collections.OrderedDict(sorted(dict_ref.items()))
[print(f"{key} -> {value}") for key, value in sorted_dict_ref.items()]
