resulting_dictionary = {}
range_number = int(input())
list_lines = []
for i in range(range_number):
    line = input()
    list_lines.append(''.join(sorted(line)))
for row in list_lines:
    for ch in row:
        for row in range(range_number):
            print('TO-DO')

print(list_lines)

