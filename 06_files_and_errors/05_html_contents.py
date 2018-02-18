line = input()

while line != "exit":
    splited_line = line.split()
    tag = splited_line[0]
    content = splited_line[1]
    if tag == "title":
        open('./Resources/Title.txt', 'w').write(f"    <{tag}>{content}</{tag}>\n")
    else:
        open('./Resources/Body.txt', 'a').write(f"    <{tag}>{content}</{tag}>\n")
    line = input()
with open("./Resources/index.html", "a") as output_file:
    output_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
    output_file.write(open('./Resources/Title.txt', 'r').read())
    output_file.write("</head>\n<body>\n")
    output_file.write(open('./Resources/Body.txt', 'r').read())
    output_file.write("</body>\n</html>")
