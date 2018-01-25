elements = map(int, input().split())
count_odd_elements = [abs(item) for item in elements if item % 2 != 0]
print(count_odd_elements.__len__())