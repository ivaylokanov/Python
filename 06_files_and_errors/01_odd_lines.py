counter = 0;
with open("./Resources/01. Odd Lines/Input.txt", 'r') as lines:
    read_line = None
    while read_line != "":
        read_line = lines.readline()
        counter += 1
        if counter % 2 == 0:
            with open("./Resources/01. Odd Lines/Output.txt", 'a') as odd_lines:
                odd_lines.write(read_line)
print(odd_lines)
