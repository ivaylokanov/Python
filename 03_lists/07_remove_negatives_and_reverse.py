elements = list(map(int, input().split()))
elements.reverse()
positive_elements = [item for item in elements if item >= 0]
if len(positive_elements)>0:
    [print(item, end=' ') for item in positive_elements]
else:
    print('empty')
