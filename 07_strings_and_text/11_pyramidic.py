import operator
resulting_dictionary = {}
range_number = int(input())
find_index = 0
list_lines = []
for i in range(range_number):
    line = input()
    list_lines.append(''.join(sorted(line)))
for j in range(range_number):
    for ch in list_lines[j]:
        counter = 0
        find_index +=1
        for m in range(j,range_number-1):
            surched_str = ch * ((find_index)*2+1)
            if list_lines[m+1].find(surched_str) != -1:
                    counter +=1
                    find_index +=1
            else:
                find_index = 0
                break

        if ch in resulting_dictionary:
            if resulting_dictionary[ch] <= counter:
                resulting_dictionary[ch] = counter
        else:
            resulting_dictionary[ch] = counter

pyramid_value = (max(resulting_dictionary.items(), key=operator.itemgetter(1))[0])
pyramid_shape = resulting_dictionary[pyramid_value]
if pyramid_shape > 0:
    for i in range(pyramid_shape+2):
        print(pyramid_value * (i*2-1))
