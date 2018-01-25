elements = map(int, input().split())
odd_elements = enumerate(elements)
[print(f'Index {index} -> {element}') for index, element in odd_elements if index % 2 != 0 and element % 2 != 0]
