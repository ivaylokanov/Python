elements = input().split()
last_element = elements.pop()
elements.insert(0, last_element)
[print(item, end=' ') for item in elements]
