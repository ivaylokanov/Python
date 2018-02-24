text = input().lower()
find_substring = input().lower()
counter = 0
index = 0

while True:
    if text.find(find_substring, index) == -1:
        break
    else:
        counter += 1
        index = text.find(find_substring, index) + 1
print(counter)
