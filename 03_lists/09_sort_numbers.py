elements = list(map(int,input().split()))
elements.sort()
print(" <= ".join(str(item) for item in elements))