elements = list(map(int, input().split()))
square_elements = [item for item in elements if (item > 0) and (item ** (1 / 2) == int(item ** (1 / 2)))]
square_elements.sort(reverse=True)
print(" ".join(str(item) for item in square_elements))
